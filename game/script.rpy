

label start:
    call screen planner_test

screen say:

    drag:
        drag_name "say"
        yalign 1.0

        drag_handle (0, 0, 1.0, 30)

        xalign 0.5

        window id "window":
            # Ensure that the window is smaller than the screen.
            xmaximum 600

            #这俩一起drag了
            has vbox
            text "who"
            text "what"

init python:

    def detective_dragged(drags, drop):

        if not drop:
            return

        store.detective = drags[0].drag_name
        store.city = drop.drag_name

        return True

#### detective example #####
screen send_detective_screen:

    # A map as background.
    add "europe.jpg"

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        # Our detectives.
        drag:
            drag_name "Ivy"
            child "ivy.png"
            droppable False
            dragged detective_dragged
            xpos 100 ypos 100
        drag:
            drag_name "Zack"
            child "zack.png"
            droppable False
            dragged detective_dragged
            xpos 150 ypos 100

        # The cities they can go to.
        drag:
            drag_name "London"
            child "london.png"
            draggable False
            xpos 450 ypos 140
        drag:
            drag_name "Paris"
            draggable False
            child "paris.png"
            xpos 500 ypos 280

label send_detective:
    "We need to investigate! Who should we send, and where should they go?"

    call screen send_detective_screen

    "Okay, we'll send [detective] to [city]."
