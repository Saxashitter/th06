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
    ins_1(sprite0);
    ins_17(768.0, 368.0, 0.0);
    ins_24();

// animation that tweens in once a difficulty is selected or returning from shot select
interrupt[7]:
    ins_12(0xff, 15);
    ins_2(1.0, 1.0);
    ins_19(448.0, 368.0, 0.0, 30);
+30: // 30
    ins_21();

// animation that plays once the character is selected (moving right)
interrupt[10]:
    ins_2(0.0, 1.0);
    ins_17(576.0, 368.0, 0.0);
    ins_30(1.0, 1.0, 10);
    ins_18(448.0, 368.0, 0.0, 10);
+10: // 40
    ins_21();

// animation that plays once the character is selected (pressing left)
interrupt[9]:
    ins_2(0.0, 1.0);
    ins_17(320.0, 368.0, 0.0);
    ins_30(1.0, 1.0, 10);
    ins_18(448.0, 368.0, 0.0, 10);
+10: // 50
    ins_21();

// animation that plays once the character is deselected (pressing left)
interrupt[12]:
    ins_17(448.0, 368.0, 0.0);
    ins_2(1.0, 1.0);
    ins_30(0.0, 1.0, 10);
    ins_18(576.0, 368.0, 0.0, 10);
+10: // 60
    ins_24();

// animation that plays once the character is deselected (moving right)
interrupt[11]:
    ins_2(1.0, 1.0);
    ins_17(448.0, 368.0, 0.0);
    ins_30(0.0, 1.0, 10);
    ins_18(320.0, 368.0, 0.0, 10);
+10: // 70
    ins_24();

// the character returns to the right side of the screen (returning to difficulty select)
interrupt[18]:
interrupt[6]:
    ins_19(768.0, 368.0, 0.0, 30);
+30: // 100
    ins_24();

// transitioning to shot select
interrupt[13]:
interrupt[19]:
    ins_19(320.0, 368.0, 0.0, 15);
    ins_12(0x80, 15);
+30: // 130
    ins_21();
}
