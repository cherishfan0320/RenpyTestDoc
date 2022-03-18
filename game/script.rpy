

label start:
    $ text_move = 1
    "test"
    call show_one_text_trans
    "test"
    return

label show_one_text_trans:
    # show the text prompt with movement
    show screen test_text_trans
    pause 1
    # dissolve
    $Hide("test_text_trans", transition=Dissolve(1.0))()

screen test_text_trans:
# need to get variable to have the text
    text "add skill" at add_skill

transform add_skill:
    easein 0.5
    xcenter 0.5
    ycenter 0.5
    linear 1.0 yalign 0.3
    # repeat
