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
    ins_1(sprite0);
    ins_17(-32.0, 336.0, 0.0);
    ins_24();

interrupt[1]:
    ins_17(-32.0, 336.0, 0.0);
    ins_19(96.0, 336.0, 0.0, 30);
    ins_12(0xff, 30);
+30: // 30
    ins_21();

interrupt[2]:
    ins_19(-32.0, 336.0, 0.0, 30);
+30: // 60
    ins_21();

interrupt[3]:
    ins_12(0xff, 16);
    ins_19(96.0, 336.0, 0.0, 16);
+30: // 90
    ins_21();

interrupt[4]:
    ins_12(0x80, 16);
    ins_19(80.0, 352.0, 0.0, 16);
+30: // 120
    ins_21();

interrupt[5]:
    ins_19(-32.0, 336.0, 0.0, 30);
+30: // 150
    ins_0();
}


script 1 script1 {
    ins_1(sprite0);
    ins_3(0xe0);
    ins_17(-32.0, 272.0, 0.0);
    ins_19(160.0, 272.0, 0.0, 30);
+90: // 90
    ins_12(0x0, 30);
    ins_11(0.06666667, 0.06666667);
+30: // 120
    ins_0();
}


script 2 script2 {
    ins_1(sprite0);
    ins_17(480.0, 336.0, 0.0);
    ins_24();

interrupt[1]:
    ins_17(480.0, 336.0, 0.0);
    ins_19(352.0, 336.0, 0.0, 30);
    ins_12(0xff, 30);
+30: // 30
    ins_21();

interrupt[2]:
    ins_19(480.0, 336.0, 0.0, 30);
+30: // 60
    ins_21();

interrupt[3]:
    ins_12(0xff, 16);
    ins_19(352.0, 336.0, 0.0, 30);
+30: // 90
    ins_21();

interrupt[4]:
    ins_12(0x80, 16);
    ins_19(368.0, 352.0, 0.0, 30);
+30: // 120
    ins_21();

interrupt[5]:
    ins_19(480.0, 336.0, 0.0, 30);
+30: // 150
    ins_0();
}


script 3 script3 {
    ins_1(sprite0);
    ins_3(0xe0);
    ins_17(480.0, 240.0, 0.0);
    ins_19(320.0, 240.0, 0.0, 30);
+90: // 90
    ins_12(0x0, 30);
    ins_11(0.06666667, 0.06666667);
+30: // 120
    ins_0();
}
