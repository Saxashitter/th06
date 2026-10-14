entry {
    path: "data/title/slpl02b.png",
    path_2: "data/title/slpl02b_a.png",
    has_data: false,
    rt_width: 256,
    rt_height: 256,
    sprites: {sprite0: {x: 0.0, y: 0.0, w: 256.0, h: 224.0}},
}

// everything happens here
script 0 script0 {
    sprite_set(sprite0);
    move_position(768.0, 368.0, 0.0);
    anm_halt_invisible();

// animation that tweens in once a difficulty is selected or returning from shot select
interrupt[7]:
    alpha_interp_linear(0xff, 15);
    scale(1.0, 1.0);
    move_position_interp_decelerate_slow(448.0, 368.0, 0.0, 30);
+30: // 30
    anm_halt();

// animation that plays once the character is selected (moving right)
interrupt[10]:
    scale(0.0, 1.0);
    move_position(576.0, 368.0, 0.0);
    scale_interp_linear(1.0, 1.0, 10);
    move_position_interp_linear(448.0, 368.0, 0.0, 10);
+10: // 40
    anm_halt();

// animation that plays once the character is selected (pressing left)
interrupt[9]:
    scale(0.0, 1.0);
    move_position(320.0, 368.0, 0.0);
    scale_interp_linear(1.0, 1.0, 10);
    move_position_interp_linear(448.0, 368.0, 0.0, 10);
+10: // 50
    anm_halt();

// animation that plays once the character is deselected (pressing left)
interrupt[12]:
    move_position(448.0, 368.0, 0.0);
    scale(1.0, 1.0);
    scale_interp_linear(0.0, 1.0, 10);
    move_position_interp_linear(576.0, 368.0, 0.0, 10);
+10: // 60
    anm_halt_invisible();

// animation that plays once the character is deselected (moving right)
interrupt[11]:
    scale(1.0, 1.0);
    move_position(448.0, 368.0, 0.0);
    scale_interp_linear(0.0, 1.0, 10);
    move_position_interp_linear(320.0, 368.0, 0.0, 10);
+10: // 70
    anm_halt_invisible();

// the character returns to the right side of the screen (returning to difficulty select)
interrupt[18]:
interrupt[6]:
    move_position_interp_decelerate_slow(768.0, 368.0, 0.0, 30);
+30: // 100
    anm_halt_invisible();

// transitioning to shot select
interrupt[13]:
interrupt[19]:
    move_position_interp_decelerate_slow(320.0, 368.0, 0.0, 15);
    alpha_interp_linear(0x80, 15);
+30: // 130
    anm_halt();
}
