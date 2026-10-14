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
        sprite_set(sprite0);
+8: // 8
        sprite_set(sprite1);
+8: // 16
        sprite_set(sprite2);
+8: // 24
        sprite_set(sprite3);
+8: // 32
    }
}


script 1 script1 {
    sprite_set(sprite4);
+3: // 3
    sprite_set(sprite5);
+3: // 6
    sprite_set(sprite6);
+8: // 14
    loop {
        sprite_set(sprite7);
+8: // 22
        sprite_set(sprite8);
+8: // 30
        sprite_set(sprite9);
+8: // 38
        sprite_set(sprite10);
+8: // 46
    }
}


script 2 script2 {
    sprite_set(sprite7);
+3: // 3
    sprite_set(sprite6);
+3: // 6
    sprite_set(sprite5);
+3: // 9
    sprite_set(sprite4);
+8: // 17
    loop {
        sprite_set(sprite0);
+8: // 25
        sprite_set(sprite1);
+8: // 33
        sprite_set(sprite2);
+8: // 41
        sprite_set(sprite3);
+8: // 49
    }
}


script 3 script3 {
    scale_flip_x();
    sprite_set(sprite4);
+3: // 3
    sprite_set(sprite5);
+3: // 6
    sprite_set(sprite6);
+8: // 14
    loop {
        sprite_set(sprite7);
+8: // 22
        sprite_set(sprite8);
+8: // 30
        sprite_set(sprite9);
+8: // 38
        sprite_set(sprite10);
+8: // 46
    }
}


script 4 script4 {
    scale_flip_x();
    sprite_set(sprite7);
+3: // 3
    sprite_set(sprite6);
+3: // 6
    sprite_set(sprite5);
+3: // 9
    sprite_set(sprite4);
+8: // 17
    loop {
        sprite_set(sprite0);
+8: // 25
        sprite_set(sprite1);
+8: // 33
        sprite_set(sprite2);
+8: // 41
        sprite_set(sprite3);
+8: // 49
    }
}


script 64 script5 {
    rotation_speed(0.0, 0.0, 0.1);
    scale(1.5, 1.5);
    alpha(0x80);
    sprite_set(sprite64);
    anm_flag_disable_z_write(true);
+10000: // 10000
    anm_static();
}


script 65 script6 {
    rotation_speed(0.0, 0.0, -0.15);
    scale(1.5, 1.5);
    alpha(0x60);
    sprite_set(sprite65);
    anm_flag_disable_z_write(true);
+10000: // 10000
    anm_static();
}


script 66 script7 {
    alpha(0xa0);
    sprite_set(sprite68);
    __rotate_auto(1);
    anm_flag_disable_z_write(true);
+10000: // 10000
    anm_static();
}


script 96 script8 {
    blend_mode_additive();
    scale(1.5, 1.5);
    sprite_set(sprite66);
    alpha(0x60);
    alpha_interp_linear(0x0, 30);
    scale_speed(0.023333333, 0.023333333);
    anm_flag_disable_z_write(true);
+30: // 30
    anm_delete();
}


script 97 script9 {
    blend_mode_additive();
    scale(1.5, 1.5);
    sprite_set(sprite67);
    alpha(0x48);
    alpha_interp_linear(0x0, 30);
    scale_speed(0.023333333, 0.023333333);
    anm_flag_disable_z_write(true);
+30: // 30
    anm_delete();
}


script 98 script10 {
    alpha(0x40);
    alpha_interp_linear(0x0, 20);
    blend_mode_additive();
    sprite_set(sprite68);
    __rotate_auto(1);
    scale_interp_linear(0.1, 6.0, 20);
    anm_flag_disable_z_write(true);
+20: // 20
    anm_static();
}


script 128 script11 {
    rotation_speed(0.0, 0.0, 0.1);
    loop {
        sprite_set(sprite128);
+10000: // 10000
    }
}


script 129 script12 {
    rotation_speed(0.0, 0.0, -0.1);
    loop {
        sprite_set(sprite128);
+10000: // 10000
    }
}


script 130 script13 {
    rotation_speed(0.0, 0.0, 0.1);
    loop {
        sprite_set(sprite129);
+10000: // 10000
    }
}


script 131 script14 {
    rotation_speed(0.0, 0.0, -0.1);
    loop {
        sprite_set(sprite129);
+10000: // 10000
    }
}


script 132 script15 {
    sprite_set(sprite130);
    anm_static();
}


script 133 script16 {
    sprite_set(sprite131);
    anm_flag_disable_z_write(true);
    blend_mode_additive();
    color(0xff, 0x30, 0x30);
    position_mode(true);
    move_position(0.0, 0.0, 0.0);
    alpha(0x80);
    scale(0.0, 0.0);
    scale_speed(0.05, 0.05);
+30: // 30
    move_position_interp_decelerate_fast(16.0, 16.0, 0.0, 10);
+30: // 60
    scale_speed(0.0, 0.0);
+10: // 70
    loop {
        move_position_interp_decelerate_fast(-16.0, -8.0, 0.0, 10);
+10: // 80
        move_position_interp_decelerate_fast(0.0, -16.0, 0.0, 10);
+10: // 90
        move_position_interp_decelerate_fast(8.0, 0.0, 0.0, 10);
+10: // 100
        move_position_interp_decelerate_fast(-16.0, 16.0, 0.0, 10);
+10: // 110
        move_position_interp_decelerate_fast(-8.0, 8.0, 0.0, 10);
    }

interrupt[1]:
    alpha_interp_linear(0x0, 30);
+10: // 120
    move_position_interp_decelerate_fast(-16.0, -8.0, 0.0, 10);
+10: // 130
    move_position_interp_decelerate_fast(0.0, -16.0, 0.0, 10);
    anm_delete();
}


script 134 script17 {
    sprite_set(sprite131);
    anm_flag_disable_z_write(true);
    blend_mode_additive();
    color(0xff, 0xff, 0x30);
    position_mode(true);
    move_position(0.0, 0.0, 0.0);
    alpha(0x80);
    scale(0.0, 0.0);
+8: // 8
    scale_speed(0.05, 0.05);
+30: // 38
    move_position_interp_decelerate_fast(-16.0, 16.0, 0.0, 10);
+30: // 68
    scale_speed(0.0, 0.0);
+10: // 78
    loop {
        move_position_interp_decelerate_fast(-8.0, 8.0, 0.0, 10);
+10: // 88
        move_position_interp_decelerate_fast(16.0, -16.0, 0.0, 10);
+10: // 98
        move_position_interp_decelerate_fast(-8.0, 8.0, 0.0, 10);
+10: // 108
        move_position_interp_decelerate_fast(-16.0, -16.0, 0.0, 10);
+10: // 118
        move_position_interp_decelerate_fast(8.0, -8.0, 0.0, 10);
    }

interrupt[1]:
    alpha_interp_linear(0x0, 30);
+10: // 128
    move_position_interp_decelerate_fast(-8.0, 8.0, 0.0, 10);
+10: // 138
    move_position_interp_decelerate_fast(16.0, -16.0, 0.0, 10);
    anm_delete();
}


script 135 script18 {
    sprite_set(sprite131);
    anm_flag_disable_z_write(true);
    blend_mode_additive();
    color(0x30, 0xff, 0x30);
    position_mode(true);
    move_position(0.0, 0.0, 0.0);
    alpha(0x80);
    scale(0.0, 0.0);
+8: // 8
    scale_speed(0.05, 0.05);
+30: // 38
    move_position_interp_decelerate_fast(0.0, -8.0, 0.0, 10);
+30: // 68
    scale_speed(0.0, 0.0);
+10: // 78
    loop {
        move_position_interp_decelerate_fast(-8.0, 16.0, 0.0, 10);
+10: // 88
        move_position_interp_decelerate_fast(8.0, 0.0, 10.0, 0);
+10: // 98
        move_position_interp_decelerate_fast(16.0, 16.0, 0.0, 10);
+10: // 108
        move_position_interp_decelerate_fast(16.0, 16.0, 0.0, 10);
+10: // 118
        move_position_interp_decelerate_fast(0.0, -16.0, 0.0, 10);
    }

interrupt[1]:
    alpha_interp_linear(0x0, 30);
+10: // 128
    move_position_interp_decelerate_fast(-8.0, 16.0, 0.0, 10);
+10: // 138
    move_position_interp_decelerate_fast(8.0, 0.0, 10.0, 0);
    anm_delete();
}


script 136 script19 {
    sprite_set(sprite131);
    anm_flag_disable_z_write(true);
    blend_mode_additive();
    color(0x30, 0x30, 0xff);
    position_mode(true);
    move_position(0.0, 0.0, 0.0);
    alpha(0x80);
+24: // 24
    scale(0.0, 0.0);
    scale_speed(0.05, 0.05);
+30: // 54
    move_position_interp_decelerate_fast(0.0, 0.0, 0.0, 30);
+30: // 84
    scale_speed(0.0, 0.0);
+10: // 94
    loop {
        move_position_interp_decelerate_fast(8.0, -8.0, 0.0, 10);
+10: // 104
        move_position_interp_decelerate_fast(-16.0, -8.0, 0.0, 10);
+10: // 114
        move_position_interp_decelerate_fast(-8.0, 16.0, 0.0, 10);
+10: // 124
        move_position_interp_decelerate_fast(8.0, -16.0, 0.0, 10);
+10: // 134
        move_position_interp_decelerate_fast(-8.0, 8.0, 0.0, 10);
    }

interrupt[1]:
    alpha_interp_linear(0x0, 30);
+10: // 144
    move_position_interp_decelerate_fast(8.0, -8.0, 0.0, 10);
+10: // 154
    move_position_interp_decelerate_fast(-16.0, -8.0, 0.0, 10);
    anm_delete();
}


script 137 script20 {
    sprite_set(sprite132);
    anm_flag_disable_z_write(true);
    blend_mode_additive();
    color(0x90, 0x90, 0xff);
    scale(3.0, 7.225806);
    alpha(0x0);
    alpha_interp_linear(0xff, 60);
+60: // 60
    position_mode(true);
    move_position(0.0, 0.0, 0.0);
    move_position_interp_decelerate_fast(-192.0, 0.0, 0.0, 120);
+60: // 120
    alpha_interp_linear(0x0, 60);
+60: // 180
    anm_delete();
}


script 138 script21 {
    sprite_set(sprite132);
    anm_flag_disable_z_write(true);
    rotation(0.0, 0.0, -1.5707964);
    blend_mode_additive();
    color(0xff, 0x90, 0x90);
    scale(3.0, 7.225806);
    alpha(0x0);
    alpha_interp_linear(0xff, 60);
+60: // 60
    position_mode(true);
    move_position(0.0, 0.0, 0.0);
    move_position_interp_decelerate_fast(0.0, -320.0, 0.0, 120);
+60: // 120
    alpha_interp_linear(0x0, 60);
+60: // 180
    anm_delete();
}


script 139 script22 {
    sprite_set(sprite132);
    anm_flag_disable_z_write(true);
    rotation(0.0, 0.0, 3.1415927);
    blend_mode_additive();
    color(0x90, 0x90, 0xff);
    scale(3.0, 7.225806);
    alpha(0x0);
    alpha_interp_linear(0xff, 60);
+60: // 60
    position_mode(true);
    move_position(0.0, 0.0, 0.0);
    move_position_interp_decelerate_fast(192.0, 0.0, 0.0, 120);
+60: // 120
    alpha_interp_linear(0x0, 60);
+60: // 180
    anm_delete();
}


script 140 script23 {
    sprite_set(sprite132);
    anm_flag_disable_z_write(true);
    rotation(0.0, 0.0, 1.5707964);
    blend_mode_additive();
    color(0xff, 0x90, 0x90);
    scale(3.0, 7.225806);
    alpha(0x0);
    alpha_interp_linear(0xff, 60);
+60: // 60
    position_mode(true);
    move_position(0.0, 0.0, 0.0);
    move_position_interp_decelerate_fast(0.0, 320.0, 0.0, 120);
+60: // 120
    alpha_interp_linear(0x0, 60);
+60: // 180
    anm_delete();
}
