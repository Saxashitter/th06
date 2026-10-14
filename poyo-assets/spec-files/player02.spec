entry {
    path: "data/playerpoyo.png",
    path_2: "data/playerpoyo_a.png",
    has_data: false,
    rt_width: 512,
    rt_height: 512,
    rt_format: FORMAT_ARGB_4444,
    sprites: {
        idle1: {x: 0.0, y: 0.0, w: 64.0, h: 96.0},
        idle2: {x: 66.0, y: 0.0, w: 64.0, h: 96.0},
        idle3: {x: 132.0, y: 0.0, w: 64.0, h: 96.0},
        swing1: {x: 198.0, y: 0.0, w: 64.0, h: 96.0},
        swing2: {x: 264.0, y: 0.0, w: 64.0, h: 96.0},
        swing3: {x: 330.0, y: 0.0, w: 64.0, h: 96.0},
        right1: {x: 396.0, y: 0.0, w: 64.0, h: 96.0},
        right2: {x: 0.0, y: 98.0, w: 64.0, h: 96.0},
        right3: {x: 66.0, y: 98.0, w: 64.0, h: 96.0},
        left1: {x: 132.0, y: 98.0, w: 64.0, h: 96.0},
        left2: {x: 198.0, y: 98.0, w: 64.0, h: 96.0},
        left3: {x: 264.0, y: 98.0, w: 64.0, h: 96.0},
        bullet: {x: 357.0, y: 138.0, w: 10.0, h: 24.0, id: 64},

        sprite6: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite7: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite8: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite9: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite10: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite64: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite65: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite66: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite67: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite68: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite128: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite129: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite130: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite131: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        sprite132: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
    },
}

// idle
script 0 script0 {
    loop {
        sprite_set(idle1);
+8:
        sprite_set(idle2);
+8:
        sprite_set(idle3);
+8:
    }
}


script 1 script1 {
    loop {
        sprite_set(left1);
+8: // 8
        sprite_set(left2);
+8: // 8
        sprite_set(left3);
    }
}


script 2 script2 {
    loop {
        sprite_set(right1);
+8: // 25
        sprite_set(right2);
+8:
        sprite_set(right3);
    }
}

script 3 script3 {
    sprite_set(swing1);
+4:
    sprite_set(swing2);
+4:
    sprite_set(swing3);
+15:
    loop {
        sprite_set(idle1);
+8:
        sprite_set(idle2);
+8:
        sprite_set(idle3);
+8:
    }
}

script 64 script5 {
    sprite_set(bullet);
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
