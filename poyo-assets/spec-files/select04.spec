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
    ins_1(sprite0);
    ins_17(640.0, 208.0, 0.0);
    ins_23();
    ins_24();

interrupt[13]:
    ins_19(368.0, 208.0, 0.0, 30);
+30: // 30
    ins_21();

interrupt[-1]:
    ins_19(640.0, 208.0, 0.0, 30);
+30: // 60
    ins_24();
}


script 1 script1 {
    ins_1(sprite1);
    ins_17(640.0, 256.0, 0.0);
    ins_23();
    ins_24();

interrupt[13]:
    ins_19(368.0, 256.0, 0.0, 30);
+30: // 30
    ins_21();

interrupt[-1]:
    ins_19(640.0, 256.0, 0.0, 30);
+30: // 60
    ins_24();
}


script 2 script2 {
    ins_1(sprite2);
    ins_17(640.0, 208.0, 0.0);
    ins_23();
    ins_24();

interrupt[13]:
    ins_19(368.0, 208.0, 0.0, 30);
+30: // 30
    ins_21();

interrupt[-1]:
    ins_19(640.0, 208.0, 0.0, 30);
+30: // 60
    ins_24();
}


script 3 script3 {
    ins_1(sprite3);
    ins_17(640.0, 256.0, 0.0);
    ins_23();
    ins_24();

interrupt[13]:
    ins_19(368.0, 256.0, 0.0, 30);
+30: // 30
    ins_21();

interrupt[-1]:
    ins_19(640.0, 256.0, 0.0, 30);
+30: // 60
    ins_24();
}

script 4 script4 {
    ins_1(sprite4);
    ins_17(640.0, 256.0, 0.0);
    ins_23();
    ins_24();

interrupt[13]:
    ins_19(368.0, 256.0, 0.0, 30);
+30: // 30
    ins_21();

interrupt[-1]:
    ins_19(640.0, 256.0, 0.0, 30);
+30: // 60
    ins_24();
}

script 5 script5 {
    ins_1(sprite5);
    ins_17(640.0, 256.0, 0.0);
    ins_23();
    ins_24();

interrupt[13]:
    ins_19(368.0, 256.0, 0.0, 30);
+30: // 30
    ins_21();

interrupt[-1]:
    ins_19(640.0, 256.0, 0.0, 30);
+30: // 60
    ins_24();
}
