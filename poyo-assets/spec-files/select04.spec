entry {
    path: "data/title/select04.png",
    path_2: "data/title/select04_a.png",
    has_data: false,
    rt_width: 256,
    rt_height: 256,
    rt_format: FORMAT_ARGB_4444,
    sprites: {
        sprite0: {x: 0.0, y: 0.0, w: 256.0, h: 48.0},
        sprite1: {x: 0.0, y: 48.0, w: 256.0, h: 48.0},
        sprite2: {x: 0.0, y: 96.0, w: 256.0, h: 48.0},
        sprite3: {x: 0.0, y: 144.0, w: 256.0, h: 48.0},
        sprite4: {x: 0.0, y: 96.0, w: 256.0, h: 48.0},
        sprite5: {x: 0.0, y: 144.0, w: 256.0, h: 48.0},
    },
}


script 0 script0 {
    sprite_set(sprite0);
    move_position(640.0, 208.0, 0.0);
    anchor_top_left();
    anm_halt_invisible();

interrupt[13]:
    move_position_interp_decelerate_slow(368.0, 208.0, 0.0, 30);
+30: // 30
    anm_halt();

interrupt[-1]:
    move_position_interp_decelerate_slow(640.0, 208.0, 0.0, 30);
+30: // 60
    anm_halt_invisible();
}


script 1 script1 {
    sprite_set(sprite1);
    move_position(640.0, 256.0, 0.0);
    anchor_top_left();
    anm_halt_invisible();

interrupt[13]:
    move_position_interp_decelerate_slow(368.0, 256.0, 0.0, 30);
+30: // 30
    anm_halt();

interrupt[-1]:
    move_position_interp_decelerate_slow(640.0, 256.0, 0.0, 30);
+30: // 60
    anm_halt_invisible();
}


script 2 script2 {
    sprite_set(sprite2);
    move_position(640.0, 208.0, 0.0);
    anchor_top_left();
    anm_halt_invisible();

interrupt[13]:
    move_position_interp_decelerate_slow(368.0, 208.0, 0.0, 30);
+30: // 30
    anm_halt();

interrupt[-1]:
    move_position_interp_decelerate_slow(640.0, 208.0, 0.0, 30);
+30: // 60
    anm_halt_invisible();
}


script 3 script3 {
    sprite_set(sprite3);
    move_position(640.0, 256.0, 0.0);
    anchor_top_left();
    anm_halt_invisible();

interrupt[13]:
    move_position_interp_decelerate_slow(368.0, 256.0, 0.0, 30);
+30: // 30
    anm_halt();

interrupt[-1]:
    move_position_interp_decelerate_slow(640.0, 256.0, 0.0, 30);
+30: // 60
    anm_halt_invisible();
}

script 4 script4 {
    sprite_set(sprite4);
    move_position(640.0, 256.0, 0.0);
    anchor_top_left();
    anm_halt_invisible();

interrupt[13]:
    move_position_interp_decelerate_slow(368.0, 256.0, 0.0, 30);
+30: // 30
    anm_halt();

interrupt[-1]:
    move_position_interp_decelerate_slow(640.0, 256.0, 0.0, 30);
+30: // 60
    anm_halt_invisible();
}

script 5 script5 {
    sprite_set(sprite5);
    move_position(640.0, 256.0, 0.0);
    anchor_top_left();
    anm_halt_invisible();

interrupt[13]:
    move_position_interp_decelerate_slow(368.0, 256.0, 0.0, 30);
+30: // 30
    anm_halt();

interrupt[-1]:
    move_position_interp_decelerate_slow(640.0, 256.0, 0.0, 30);
+30: // 60
    anm_halt_invisible();
}
