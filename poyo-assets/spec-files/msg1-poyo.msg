#pragma mapfile "C:/DevTools/TouhouMaps-main/th06.msgm"

meta {table: {0: {script: "script0"}, 1: {script: "script1"}}}


script script0 {
    portrait_anm_script(LeftPortrait, 0);
    portrait_anm_sprite(LeftPortrait, 5);
    anm_interrupt(LeftPortrait, 1);
+60: // 60
    text_dialogue(PaleBlue, TopLine, "Damnit, these things almost");
    text_dialogue(PaleBlue, BottomLine, "got me.");
    wait(200);
+1: // 61
    portrait_anm_sprite(LeftPortrait, 4);
    text_dialogue(PaleBlue, TopLine, "I swear, if that girl doesn't");
    text_dialogue(PaleBlue, BottomLine, "keep her promise and take me home...");
    wait(300);
    ecl_resume();
+63: // 124
    portrait_anm_script(RightPortrait, 0);
    portrait_anm_sprite(RightPortrait, 2);
    anm_interrupt(RightPortrait, 1);
    anm_interrupt(LeftPortrait, 4);
    text_dialogue(PaleRed, TopLine, "Not if I have anything");
    text_dialogue(PaleRed, BottomLine, "to say about it!");
    wait(300);
+1: // 125
    portrait_anm_sprite(LeftPortrait, 0);
    portrait_anm_sprite(RightPortrait, 0);
    anm_interrupt(LeftPortrait, 3);
    anm_interrupt(RightPortrait, 4);
    text_dialogue(PaleBlue, TopLine, "...I'm sorry, who are you?");
    wait(200);
+1: // 126
    portrait_anm_sprite(LeftPortrait, 5);
    text_dialogue(PaleBlue, TopLine, "No offense, but you look as strong");
    text_dialogue(PaleBlue, BottomLine, "as a man on his death bed.");
    wait(300);
+8: // 134
    portrait_anm_sprite(RightPortrait, 3);
    anm_interrupt(LeftPortrait, 4);
    anm_interrupt(RightPortrait, 3);
    text_intro(PaleRed, TopLine, "Rumia");
    text_intro(PaleRed, BottomLine, "Youkai of Night");
    text_dialogue(PaleRed, TopLine, "Didn't we meet a few minutes ago?");
    msg_flag_wait_skippable(false);
    wait(30);
    msg_flag_wait_skippable(true);
    wait(300);
+1: // 135
    portrait_anm_sprite(LeftPortrait, 4);
    portrait_anm_sprite(RightPortrait, 0);
    anm_interrupt(LeftPortrait, 3);
    anm_interrupt(RightPortrait, 4);
    text_dialogue(PaleBlue, TopLine, "A couple minutes ago, I was fighting");
    text_dialogue(PaleBlue, BottomLine, "against midgets in the dark.");
    wait(200);
+1: // 136
    portrait_anm_sprite(LeftPortrait, 0);
    text_dialogue(PaleBlue, TopLine, "I still can't see that well...");
    wait(300);
+1: // 137
    portrait_anm_sprite(LeftPortrait, 0);
    portrait_anm_sprite(RightPortrait, 1);
    anm_interrupt(LeftPortrait, 4);
    anm_interrupt(RightPortrait, 3);
    text_dialogue(PaleRed, TopLine, "That must happen everytime you");
    text_dialogue(PaleRed, BottomLine, "go to work out here, right?");
    wait(300);
+1: // 138
    portrait_anm_sprite(LeftPortrait, 0);
    anm_interrupt(LeftPortrait, 3);
    anm_interrupt(RightPortrait, 4);
    text_dialogue(PaleBlue, TopLine, "I'm not from here.");
    wait(200);
+1: // 139
    text_dialogue(PaleBlue, TopLine, "Some woman kidnapped me so");
    text_dialogue(PaleBlue, BottomLine, "she didn't have to work.");
    wait(200);
+1: // 140
    portrait_anm_sprite(LeftPortrait, 4);
    text_dialogue(PaleBlue, TopLine, "I don't wanna be here.");
    wait(300);
+1: // 141
    portrait_anm_sprite(LeftPortrait, 0);
    portrait_anm_sprite(RightPortrait, 2);
    anm_interrupt(LeftPortrait, 4);
    anm_interrupt(RightPortrait, 3);
    text_dialogue(PaleRed, TopLine, "Is that so~？");
    wait(300);
+1: // 142
    portrait_anm_sprite(RightPortrait, 1);
    text_dialogue(PaleRed, TopLine, "Hopefully, she won't mind");
    text_dialogue(PaleRed, BottomLine, "if you become my dinner!");
    music(Music1);
    wait(300);
+1: // 143
    anm_interrupt(LeftPortrait, 3);
    anm_interrupt(RightPortrait, 4);
    text_dialogue(PaleBlue, TopLine, "Surprisingly, she didn't eat me");
    text_dialogue(PaleBlue, BottomLine, "before you came along.");
    wait(500);
    anm_interrupt(LeftPortrait, 5);
    anm_interrupt(RightPortrait, 5);
    msg_flag_wait_skippable(false);
+30: // 173
    msg_delete();
    msg_flag_wait_skippable(true);
}


script script1 {
    portrait_anm_script(LeftPortrait, 0);
    portrait_anm_sprite(LeftPortrait, 1);
    anm_interrupt(LeftPortrait, 1);
+60: // 60
    text_dialogue(PaleBlue, TopLine, "And it wasn't like I'd let you");
    text_dialogue(PaleBlue, BottomLine, "either, numbnuts.");
    wait(900);
    msg_flag_wait_skippable(false);
+60: // 120
    stage_results();
    music_fade_out();
+60: // 180
    wait(1200);
    stage_end();
    msg_halt();
}
