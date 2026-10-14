param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("compile", "decompile")]
    [string]$Mode,

    [Parameter(Mandatory = $true)]
    [string]$Source,

    [Parameter(Mandatory = $true)]
    [string]$Output,

    [string]$Wave
)

$ErrorActionPreference = "Stop"

function Read-LoopPoints {
    param([string]$Path)

    $values = @(
        Get-Content -LiteralPath $Path |
            ForEach-Object { ($_ -replace "#.*$", "").Trim() } |
            Where-Object { $_ -ne "" } |
            ForEach-Object { $_ -split "\s+" }
    )

    if ($values.Count -ne 2) {
        throw "Expected exactly two sample positions in $Path (loop start and exclusive loop end)."
    }

    $start = [decimal]0
    $end = [decimal]0
    $style = [System.Globalization.NumberStyles]::AllowDecimalPoint
    $culture = [System.Globalization.CultureInfo]::InvariantCulture
    if (-not [decimal]::TryParse($values[0], $style, $culture, [ref]$start) -or
        -not [decimal]::TryParse($values[1], $style, $culture, [ref]$end)) {
        throw "Loop times in $Path must be non-negative decimal milliseconds."
    }
    if ($start -ge $end) {
        throw "Loop start must be less than loop end in $Path."
    }

    return @($start, $end)
}

try {
    if ($Mode -eq "decompile") {
        $bytes = [System.IO.File]::ReadAllBytes($Source)
        if ($bytes.Length -ne 8) {
            throw "$Source is $($bytes.Length) bytes; expected an 8-byte Touhou position file."
        }

        $startSamples = [System.BitConverter]::ToUInt32($bytes, 0)
        $endSamples = [System.BitConverter]::ToUInt32($bytes, 4)
        if ($startSamples -ge $endSamples) {
            throw "Loop start must be less than loop end in $Source."
        }

        $culture = [System.Globalization.CultureInfo]::InvariantCulture
        $start = ([decimal]$startSamples * 1000 / 44100).ToString("0.######", $culture)
        $end = ([decimal]$endSamples * 1000 / 44100).ToString("0.######", $culture)
        $text = @(
            "# Loop times in milliseconds; decimals are allowed and loop end is exclusive."
            $start
            $end
        )
        [System.IO.File]::WriteAllLines($Output, $text, [System.Text.Encoding]::ASCII)
    } else {
        if ([string]::IsNullOrWhiteSpace($Wave)) {
            throw "A WAV path is required when compiling a position source."
        }

        $points = Read-LoopPoints -Path $Source
        $start = [decimal]$points[0]
        $end = [decimal]$points[1]
        $waveBytes = [System.IO.File]::ReadAllBytes($Wave)

        if ($waveBytes.Length -lt 44 -or
            [System.Text.Encoding]::ASCII.GetString($waveBytes, 0, 4) -ne "RIFF" -or
            [System.Text.Encoding]::ASCII.GetString($waveBytes, 8, 4) -ne "WAVE" -or
            [System.Text.Encoding]::ASCII.GetString($waveBytes, 12, 4) -ne "fmt " -or
            [System.Text.Encoding]::ASCII.GetString($waveBytes, 36, 4) -ne "data") {
            throw "$Wave is not a supported 44-byte-header RIFF/WAVE file."
        }

        $format = [System.BitConverter]::ToUInt16($waveBytes, 20)
        $channels = [System.BitConverter]::ToUInt16($waveBytes, 22)
        $sampleRate = [System.BitConverter]::ToUInt32($waveBytes, 24)
        $blockAlign = [System.BitConverter]::ToUInt16($waveBytes, 32)
        $bitsPerSample = [System.BitConverter]::ToUInt16($waveBytes, 34)
        $dataBytes = [System.BitConverter]::ToUInt32($waveBytes, 40)

        if ($format -ne 1 -or $channels -ne 2 -or $sampleRate -ne 44100 -or
            $blockAlign -ne 4 -or $bitsPerSample -ne 16 -or $dataBytes % 4 -ne 0 -or
            $dataBytes -gt $waveBytes.Length - 44) {
            throw "$Wave must be stereo 44,100 Hz 16-bit PCM with a valid data chunk."
        }

        $sampleCount = [uint32]($dataBytes / 4)
        $startSamples = [decimal]::Round($start * 44100 / 1000, 0, [System.MidpointRounding]::AwayFromZero)
        $endSamples = [decimal]::Round($end * 44100 / 1000, 0, [System.MidpointRounding]::AwayFromZero)
        if ($startSamples -gt [uint32]::MaxValue -or $endSamples -gt [uint32]::MaxValue) {
            throw "Loop times in $Source exceed the maximum supported sample position."
        }
        if ($startSamples -ge $endSamples) {
            throw "Loop start and end in $Source must resolve to different sample frames."
        }
        if ($endSamples -gt $sampleCount) {
            $waveDuration = ([decimal]$sampleCount * 1000 / 44100).ToString("0.###", [System.Globalization.CultureInfo]::InvariantCulture)
            throw "Loop end $end ms in $Source exceeds the WAV duration of $waveDuration ms ($sampleCount sample frames)."
        }

        $bytes = [System.BitConverter]::GetBytes([uint32]$startSamples) +
            [System.BitConverter]::GetBytes([uint32]$endSamples)
        [System.IO.File]::WriteAllBytes($Output, $bytes)
    }
} catch {
    Write-Error $_
    exit 1
}
