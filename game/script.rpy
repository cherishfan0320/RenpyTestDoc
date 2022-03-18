

label start:
    "test"
    show screen test_text_trans
    "test"
    return

screen test_text_trans:
    text "add skill" at add_skill

transform add_skill:
    animation
    xcenter 0.6
    ycenter 0.5
    linear 5.0 yalign 0.2
    # repeat
