init python:

    #This controls when the love-points floater appears.
    show_giselle=False
    show_arthur=False
    show_shino=False

    ## ------------ Love Points Floater ----------------------

    def stats_overlay():

        # --- Giselle's Love Bar -------
        if show_giselle:
            ui.frame(
                xalign = 0.5, #centered
                ypos = 400,) #400 px Down from the Top

            ui.vbox(xalign = 0.5)
            ui.text ("Giselle's Love Points: %d" %giselle_love,
                xalign = 0.5)
            ui.bar(max_love, giselle_love,
                style="my_bar")

            ui.close()

        # --- Arthur's Love Bar -------
        if show_arthur:
            ui.frame(
                xalign = 0.5,
                ypos = 400,)

            ui.vbox()
            ui.text ("Arthur's Love Points: %d" %arthur_love,
                xalign = 0.5)
            ui.bar(max_love, arthur_love,
                style="my_bar")

            ui.close()

        # --- Shino's Love Bar -------
        if show_shino:
            ui.frame(
                xalign = 0.5,
                ypos = 400,)

            ui.vbox()
            ui.text ("Shino's Love Points: %d" %shino_love,
                xalign = 0.5)
            ui.bar(max_love, shino_love,
                style="my_bar")

            ui.close()

    config.overlay_functions.append(stats_overlay)

init -2 python:
    giselle_love=10
    max_love = 150

    arthur_love=10
    max_love = 150

    shino_love =10
    max_love = 150

init -5 python:
    #custom bar
    style.my_bar = Style(style.default)
    style.my_bar.xalign = 0.5
    style.my_bar.xmaximum = 315 # bar width
    style.my_bar.ymaximum = 30 # bar height
    style.my_bar.left_gutter = 5
    style.my_bar.right_gutter = 5

    # I have all my User Interface graphics stored in one file called ui.
    # To access them in my code, I put ui/ in front of all images in that file.

    style.my_bar.left_bar = Frame("ui/bar_full.png", 0, 0)
    style.my_bar.right_bar = Frame("ui/bar_empty.png", 0, 0)
    style.my_bar.hover_left_bar = Frame("ui/bar_hover.png", 0, 0)

    style.my_bar.thumb = "ui/thumb.png"
    style.my_bar.thumb_shadow = None
    style.my_bar.thumb_offset = 5
