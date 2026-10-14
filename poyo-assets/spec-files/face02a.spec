entry {
    path: "data/face/face02a.png",
    path_2: "data/face/face02a_a.png",
    has_data: false,
    rt_width: 256,
    rt_height: 256,
    sprites: {
        sprite0: {x: 0.0, y: 0.0, w: 128.0, h: 256.0},
        sprite1: {x: 128.0, y: 0.0, w: 128.0, h: 256.0},
    },
}


script 0 script0 {
    sprite_set(sprite0);
    move_position(-32.0, 336.0, 0.0);
    anm_halt_invisible();

interrupt[1]:
    move_position(-32.0, 336.0, 0.0);
    move_position_interp_decelerate_slow(96.0, 336.0, 0.0, 30);
    alpha_interp_linear(0xff, 30);
+30: // 30
    anm_halt();

interrupt[2]:
    move_position_interp_decelerate_slow(-32.0, 336.0, 0.0, 30);
+30: // 60
    anm_halt();

interrupt[3]:
    alpha_interp_linear(0xff, 16);
    move_position_interp_decelerate_slow(96.0, 336.0, 0.0, 16);
+30: // 90
    anm_halt();

interrupt[4]:
    alpha_interp_linear(0x80, 16);
    move_position_interp_decelerate_slow(80.0, 352.0, 0.0, 16);
+30: // 120
    anm_halt();

interrupt[5]:
    move_position_interp_decelerate_slow(-32.0, 336.0, 0.0, 30);
+30: // 150
    anm_delete();
}


script 1 script1 {
    sprite_set(sprite0);
    alpha(0xe0);
    move_position(-32.0, 272.0, 0.0);
    move_position_interp_decelerate_slow(160.0, 272.0, 0.0, 30);
+90: // 90
    alpha_interp_linear(0x0, 30);
    scale_speed(0.06666667, 0.06666667);
+30: // 120
    anm_delete();
}


script 2 script2 {
    sprite_set(sprite0);
    move_position(480.0, 336.0, 0.0);
    anm_halt_invisible();

interrupt[1]:
    move_position(480.0, 336.0, 0.0);
    move_position_interp_decelerate_slow(352.0, 336.0, 0.0, 30);
    alpha_interp_linear(0xff, 30);
+30: // 30
    anm_halt();

interrupt[2]:
    move_position_interp_decelerate_slow(480.0, 336.0, 0.0, 30);
+30: // 60
    anm_halt();

interrupt[3]:
    alpha_interp_linear(0xff, 16);
    move_position_interp_decelerate_slow(352.0, 336.0, 0.0, 30);
+30: // 90
    anm_halt();

interrupt[4]:
    alpha_interp_linear(0x80, 16);
    move_position_interp_decelerate_slow(368.0, 352.0, 0.0, 30);
+30: // 120
    anm_halt();

interrupt[5]:
    move_position_interp_decelerate_slow(480.0, 336.0, 0.0, 30);
+30: // 150
    anm_delete();
}


script 3 script3 {
    sprite_set(sprite0);
    alpha(0xe0);
    move_position(480.0, 240.0, 0.0);
    move_position_interp_decelerate_slow(320.0, 240.0, 0.0, 30);
+90: // 90
    alpha_interp_linear(0x0, 30);
    scale_speed(0.06666667, 0.06666667);
+30: // 120
    anm_delete();
}
