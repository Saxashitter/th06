entry {
    path: "data/player00/player00.png",
    path_2: "data/player00/player00_a.png",
    has_data: false,
    rt_width: 256,
    rt_height: 256,
    rt_format: FORMAT_ARGB_4444,
    sprites: {
        sprite0: {x: 1.0, y: 1.0, w: 31.0, h: 47.0},
        sprite1: {x: 33.0, y: 1.0, w: 31.0, h: 47.0},
        sprite2: {x: 65.0, y: 1.0, w: 31.0, h: 47.0},
        sprite3: {x: 97.0, y: 1.0, w: 31.0, h: 47.0},
        sprite4: {x: 1.0, y: 49.0, w: 31.0, h: 47.0},
        sprite5: {x: 33.0, y: 49.0, w: 31.0, h: 47.0},
        sprite6: {x: 65.0, y: 49.0, w: 31.0, h: 47.0},
        sprite7: {x: 97.0, y: 49.0, w: 31.0, h: 47.0},
        sprite8: {x: 129.0, y: 49.0, w: 31.0, h: 47.0},
        sprite9: {x: 161.0, y: 49.0, w: 31.0, h: 47.0},
        sprite10: {x: 193.0, y: 49.0, w: 31.0, h: 47.0},
        sprite11: {x: 1.0, y: 49.0, w: 31.0, h: 47.0},
        sprite12: {x: 33.0, y: 49.0, w: 31.0, h: 47.0},
        sprite13: {x: 65.0, y: 49.0, w: 31.0, h: 47.0},
        sprite14: {x: 97.0, y: 49.0, w: 31.0, h: 47.0},
        sprite15: {x: 129.0, y: 49.0, w: 31.0, h: 47.0},
        sprite16: {x: 161.0, y: 49.0, w: 31.0, h: 47.0},
        sprite17: {x: 193.0, y: 49.0, w: 31.0, h: 47.0},
        sprite64: {x: 129.0, y: 1.0, w: 14.0, h: 14.0, id: 64},
        sprite65: {x: 144.0, y: 1.0, w: 14.0, h: 14.0},
        sprite66: {x: 160.0, y: 0.0, w: 16.0, h: 16.0},
        sprite67: {x: 176.0, y: 0.0, w: 16.0, h: 16.0},
        sprite68: {x: 193.0, y: 1.0, w: 14.0, h: 46.0},
        sprite128: {x: 128.0, y: 16.0, w: 16.0, h: 16.0, id: 128},
        sprite129: {x: 144.0, y: 16.0, w: 16.0, h: 16.0},
        sprite130: {x: 128.0, y: 32.0, w: 16.0, h: 16.0},
        sprite131: {x: 1.0, y: 97.0, w: 62.0, h: 62.0},
        sprite132: {x: 65.0, y: 97.0, w: 62.0, h: 62.0},
    },
}


script 0 script0 {
    loop {
        ins_1(sprite0);
+8: // 8
        ins_1(sprite1);
+8: // 16
        ins_1(sprite2);
+8: // 24
        ins_1(sprite3);
+8: // 32
    }
}


script 1 script1 {
    ins_1(sprite4);
+3: // 3
    ins_1(sprite5);
+3: // 6
    ins_1(sprite6);
+8: // 14
    loop {
        ins_1(sprite7);
+8: // 22
        ins_1(sprite8);
+8: // 30
        ins_1(sprite9);
+8: // 38
        ins_1(sprite10);
+8: // 46
    }
}


script 2 script2 {
    ins_1(sprite7);
+3: // 3
    ins_1(sprite6);
+3: // 6
    ins_1(sprite5);
+3: // 9
    ins_1(sprite4);
+8: // 17
    loop {
        ins_1(sprite0);
+8: // 25
        ins_1(sprite1);
+8: // 33
        ins_1(sprite2);
+8: // 41
        ins_1(sprite3);
+8: // 49
    }
}


script 3 script3 {
    ins_7();
    ins_1(sprite4);
+3: // 3
    ins_1(sprite5);
+3: // 6
    ins_1(sprite6);
+8: // 14
    loop {
        ins_1(sprite7);
+8: // 22
        ins_1(sprite8);
+8: // 30
        ins_1(sprite9);
+8: // 38
        ins_1(sprite10);
+8: // 46
    }
}


script 4 script4 {
    ins_7();
    ins_1(sprite7);
+3: // 3
    ins_1(sprite6);
+3: // 6
    ins_1(sprite5);
+3: // 9
    ins_1(sprite4);
+8: // 17
    loop {
        ins_1(sprite0);
+8: // 25
        ins_1(sprite1);
+8: // 33
        ins_1(sprite2);
+8: // 41
        ins_1(sprite3);
+8: // 49
    }
}


script 64 script5 {
    ins_10(0.0, 0.0, 0.1);
    ins_2(1.5, 1.5);
    ins_3(0x80);
    ins_1(sprite64);
    ins_31(true);
+10000: // 10000
    ins_15();
}


script 65 script6 {
    ins_10(0.0, 0.0, -0.15);
    ins_2(1.5, 1.5);
    ins_3(0x60);
    ins_1(sprite65);
    ins_31(true);
+10000: // 10000
    ins_15();
}


script 66 script7 {
    ins_3(0xa0);
    ins_1(sprite68);
    ins_26(1);
    ins_31(true);
+10000: // 10000
    ins_15();
}


script 96 script8 {
    ins_13();
    ins_2(1.5, 1.5);
    ins_1(sprite66);
    ins_3(0x60);
    ins_12(0x0, 30);
    ins_11(0.023333333, 0.023333333);
    ins_31(true);
+30: // 30
    ins_0();
}


script 97 script9 {
    ins_13();
    ins_2(1.5, 1.5);
    ins_1(sprite67);
    ins_3(0x48);
    ins_12(0x0, 30);
    ins_11(0.023333333, 0.023333333);
    ins_31(true);
+30: // 30
    ins_0();
}


script 98 script10 {
    ins_3(0x40);
    ins_12(0x0, 20);
    ins_13();
    ins_1(sprite68);
    ins_26(1);
    ins_30(0.1, 6.0, 20);
    ins_31(true);
+20: // 20
    ins_15();
}


script 128 script11 {
    ins_10(0.0, 0.0, 0.1);
    loop {
        ins_1(sprite128);
+10000: // 10000
    }
}


script 129 script12 {
    ins_10(0.0, 0.0, -0.1);
    loop {
        ins_1(sprite128);
+10000: // 10000
    }
}


script 130 script13 {
    ins_10(0.0, 0.0, 0.1);
    loop {
        ins_1(sprite129);
+10000: // 10000
    }
}


script 131 script14 {
    ins_10(0.0, 0.0, -0.1);
    loop {
        ins_1(sprite129);
+10000: // 10000
    }
}


script 132 script15 {
    ins_1(sprite130);
    ins_15();
}


script 133 script16 {
    ins_1(sprite131);
    ins_31(true);
    ins_13();
    ins_4(0xff, 0x30, 0x30);
    ins_25(true);
    ins_17(0.0, 0.0, 0.0);
    ins_3(0x80);
    ins_2(0.0, 0.0);
    ins_11(0.05, 0.05);
+30: // 30
    ins_20(16.0, 16.0, 0.0, 10);
+30: // 60
    ins_11(0.0, 0.0);
+10: // 70
    loop {
        ins_20(-16.0, -8.0, 0.0, 10);
+10: // 80
        ins_20(0.0, -16.0, 0.0, 10);
+10: // 90
        ins_20(8.0, 0.0, 0.0, 10);
+10: // 100
        ins_20(-16.0, 16.0, 0.0, 10);
+10: // 110
        ins_20(-8.0, 8.0, 0.0, 10);
    }

interrupt[1]:
    ins_12(0x0, 30);
+10: // 120
    ins_20(-16.0, -8.0, 0.0, 10);
+10: // 130
    ins_20(0.0, -16.0, 0.0, 10);
    ins_0();
}


script 134 script17 {
    ins_1(sprite131);
    ins_31(true);
    ins_13();
    ins_4(0xff, 0xff, 0x30);
    ins_25(true);
    ins_17(0.0, 0.0, 0.0);
    ins_3(0x80);
    ins_2(0.0, 0.0);
+8: // 8
    ins_11(0.05, 0.05);
+30: // 38
    ins_20(-16.0, 16.0, 0.0, 10);
+30: // 68
    ins_11(0.0, 0.0);
+10: // 78
    loop {
        ins_20(-8.0, 8.0, 0.0, 10);
+10: // 88
        ins_20(16.0, -16.0, 0.0, 10);
+10: // 98
        ins_20(-8.0, 8.0, 0.0, 10);
+10: // 108
        ins_20(-16.0, -16.0, 0.0, 10);
+10: // 118
        ins_20(8.0, -8.0, 0.0, 10);
    }

interrupt[1]:
    ins_12(0x0, 30);
+10: // 128
    ins_20(-8.0, 8.0, 0.0, 10);
+10: // 138
    ins_20(16.0, -16.0, 0.0, 10);
    ins_0();
}


script 135 script18 {
    ins_1(sprite131);
    ins_31(true);
    ins_13();
    ins_4(0x30, 0xff, 0x30);
    ins_25(true);
    ins_17(0.0, 0.0, 0.0);
    ins_3(0x80);
    ins_2(0.0, 0.0);
+8: // 8
    ins_11(0.05, 0.05);
+30: // 38
    ins_20(0.0, -8.0, 0.0, 10);
+30: // 68
    ins_11(0.0, 0.0);
+10: // 78
    loop {
        ins_20(-8.0, 16.0, 0.0, 10);
+10: // 88
        ins_20(8.0, 0.0, 10.0, 0);
+10: // 98
        ins_20(16.0, 16.0, 0.0, 10);
+10: // 108
        ins_20(16.0, 16.0, 0.0, 10);
+10: // 118
        ins_20(0.0, -16.0, 0.0, 10);
    }

interrupt[1]:
    ins_12(0x0, 30);
+10: // 128
    ins_20(-8.0, 16.0, 0.0, 10);
+10: // 138
    ins_20(8.0, 0.0, 10.0, 0);
    ins_0();
}


script 136 script19 {
    ins_1(sprite131);
    ins_31(true);
    ins_13();
    ins_4(0x30, 0x30, 0xff);
    ins_25(true);
    ins_17(0.0, 0.0, 0.0);
    ins_3(0x80);
+24: // 24
    ins_2(0.0, 0.0);
    ins_11(0.05, 0.05);
+30: // 54
    ins_20(0.0, 0.0, 0.0, 30);
+30: // 84
    ins_11(0.0, 0.0);
+10: // 94
    loop {
        ins_20(8.0, -8.0, 0.0, 10);
+10: // 104
        ins_20(-16.0, -8.0, 0.0, 10);
+10: // 114
        ins_20(-8.0, 16.0, 0.0, 10);
+10: // 124
        ins_20(8.0, -16.0, 0.0, 10);
+10: // 134
        ins_20(-8.0, 8.0, 0.0, 10);
    }

interrupt[1]:
    ins_12(0x0, 30);
+10: // 144
    ins_20(8.0, -8.0, 0.0, 10);
+10: // 154
    ins_20(-16.0, -8.0, 0.0, 10);
    ins_0();
}


script 137 script20 {
    ins_1(sprite132);
    ins_31(true);
    ins_13();
    ins_4(0x90, 0x90, 0xff);
    ins_2(3.0, 7.225806);
    ins_3(0x0);
    ins_12(0xff, 60);
+60: // 60
    ins_25(true);
    ins_17(0.0, 0.0, 0.0);
    ins_20(-192.0, 0.0, 0.0, 120);
+60: // 120
    ins_12(0x0, 60);
+60: // 180
    ins_0();
}


script 138 script21 {
    ins_1(sprite132);
    ins_31(true);
    ins_9(0.0, 0.0, -1.5707964);
    ins_13();
    ins_4(0xff, 0x90, 0x90);
    ins_2(3.0, 7.225806);
    ins_3(0x0);
    ins_12(0xff, 60);
+60: // 60
    ins_25(true);
    ins_17(0.0, 0.0, 0.0);
    ins_20(0.0, -320.0, 0.0, 120);
+60: // 120
    ins_12(0x0, 60);
+60: // 180
    ins_0();
}


script 139 script22 {
    ins_1(sprite132);
    ins_31(true);
    ins_9(0.0, 0.0, 3.1415927);
    ins_13();
    ins_4(0x90, 0x90, 0xff);
    ins_2(3.0, 7.225806);
    ins_3(0x0);
    ins_12(0xff, 60);
+60: // 60
    ins_25(true);
    ins_17(0.0, 0.0, 0.0);
    ins_20(192.0, 0.0, 0.0, 120);
+60: // 120
    ins_12(0x0, 60);
+60: // 180
    ins_0();
}


script 140 script23 {
    ins_1(sprite132);
    ins_31(true);
    ins_9(0.0, 0.0, 1.5707964);
    ins_13();
    ins_4(0xff, 0x90, 0x90);
    ins_2(3.0, 7.225806);
    ins_3(0x0);
    ins_12(0xff, 60);
+60: // 60
    ins_25(true);
    ins_17(0.0, 0.0, 0.0);
    ins_20(0.0, 320.0, 0.0, 120);
+60: // 120
    ins_12(0x0, 60);
+60: // 180
    ins_0();
}
