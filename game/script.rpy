# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("...")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    $ renpy.pause(1)

    s "WHERE IS MY BODY?"
    s "I CANNOT FIND IT."

    $ renpy.pause(1)

    s "IT WAS THEM."
    s "THEY TOOK MY BODY."
    s "WHERE DID THEY TAKE IT?"
    s "THEY CANNOT HAVE IT."
    s "I WILL TAKE IT BACK."

    menu:
        "I will help to find your body.":
            pass

    $ renpy.pause(1)

    scene bg storeroom
    with dissolve

    $ renpy.pause(1)

    s "THIS ROOM."
    s "THINGS ARE KEPT HERE."
    s "WAS MY BODY KEPT HERE?"

    default checked_shelf = False
    default checked_boxes = False

label search_storeroom:
    menu:
        "Look on the shelf." if not checked_shelf:
            $ checked_shelf = True
            pass
        "Look in the boxes." if not checked_boxes:
            $ checked_boxes = True
            pass

    $ renpy.pause(1)

    s "MY BODY IS NOT THERE."

    if (not checked_shelf) or (not checked_boxes):
        jump search_storeroom

    s "MY BODY IS NOT IN THIS ROOM."

    menu:
        "Search elsewhere.":
            pass
    # This ends the game.

    return
