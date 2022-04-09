init python:

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

init:

    # Create such a character.
     define girl = Character("Girl", callback=speaker("girl"))

     # Composite things together to make a character with blinking eyes and
     # lip-flap.
     image girl normal = LiveComposite(
        (359, 927),
        (0, 0), "base.png",
        (0, 0), WhileSpeaking("girl", "girl mouth normal", "mouth_closed.png"),
        )

     image girl mouth normal:
        "mouth_speak1.png"
        .2
        "mouth_speak2.png"
        .2
        repeat

# The game starts here.
label start:
    scene black
    show girl normal

    "Not speaking."

    girl "Now I'm speaking. Blah blah blah blah blah blah blah."

    "Not speaking any more."

    girl "Now I'm speaking once again. Blah blah blah blah blah blah blah."
