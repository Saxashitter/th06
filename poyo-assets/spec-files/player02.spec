entry {
    path: "data/player02/player02.png",
    path_2: "data/player02/player02_a.png",
    has_data: false,
    rt_width: 128,
    rt_height: 128,
    rt_format: FORMAT_ARGB_4444,
    sprites: {
        idle: {x: 0.0, y: 0.0, w: 40.0, h: 49.0},
        gun: {x: 40.0, y: 49.0, w: 40.0, h: 49.0},
        swing1: {x: 40.0, y: 0.0, w: 40.0, h: 49.0},
        swing2: {x: 80.0, y: 0.0, w: 40.0, h: 49.0},
        swing3: {x: 0.0, y: 49.0, w: 40.0, h: 49.0},
        bullet: {x: 80.0, y: 49.0, w: 4.0, h: 7.0, id: 64},
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

script 0 idle_anim {
    loop {
        ins_1(idle);
+2:
    }
}


script 1 shoot_anim {
    ins_1(gun);
+35:
    loop {
        ins_1(idle);
+2:
    }
}


script 2 swing_anim {
    ins_1(swing1);
+3:
    ins_1(swing2);
+3:
    ins_1(swing3);
+9:
    loop {
        ins_1(idle);
+2:
    }
}


script 3 script3 {
    ins_1(idle);
}


script 4 script4 {
    ins_7();
    ins_1(idle);
}


script 64 script5 {
    // ins_10(0.0, 0.0, 0.1);
    // ins_2(1.5, 1.5);
    // ins_3(0x80);
    ins_1(bullet);
    ins_31(true);
+10000: // 10000
    ins_15();
}


script 65 script6 {
    ins_10(0.0, 0.0, -0.15);
    ins_2(1.5, 1.5);
    ins_3(0x60);
    ins_1(bullet);
    ins_31(true);
+10000: // 10000
    ins_15();
}


script 66 script7 {
    ins_3(0xa0);
    ins_1(bullet);
    ins_26(1);
    ins_31(true);
+10000: // 10000
    ins_15();
}


script 96 script8 {
    ins_13();
    ins_2(1.5, 1.5);
    ins_1(bullet);
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
    ins_1(bullet);
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
    ins_1(bullet);
    ins_26(1);
    ins_30(0.1, 6.0, 20);
    ins_31(true);
+20: // 20
    ins_15();
}


script 128 script11 {
    ins_10(0.0, 0.0, 0.1);
    loop {
        ins_1(bullet);
+10000: // 10000
    }
}


script 129 script12 {
    ins_10(0.0, 0.0, -0.1);
    loop {
        ins_1(bullet);
+10000: // 10000
    }
}


script 130 script13 {
    ins_10(0.0, 0.0, 0.1);
    loop {
        ins_1(bullet);
+10000: // 10000
    }
}


script 131 script14 {
    ins_10(0.0, 0.0, -0.1);
    loop {
        ins_1(bullet);
+10000: // 10000
    }
}


script 132 script15 {
    ins_1(bullet);
    ins_15();
}


script 133 script16 {
    ins_1(bullet);
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
    ins_1(bullet);
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
    ins_1(bullet);
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
    ins_1(bullet);
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
    ins_1(bullet);
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
    ins_1(bullet);
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
    ins_1(bullet);
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
    ins_1(bullet);
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
