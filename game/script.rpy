define s = Character("...")
define slowfade = Fade(1.0,1.0,1.0)

label start:

    $ renpy.pause(1)

    s "WHERE IS MY BODY?"
    s "I CANNOT FIND IT."

    $ renpy.pause(1)

    s "IT WAS {b}THEM{/b}."
    s "{b}THEY{/b} TOOK MY BODY."
    s "WHERE DID THEY TAKE IT?"

    $renpy.pause(1)

    s "THEY CANNOT {b}HAVE{/b} IT."
    s "I WILL TAKE IT {b}BACK{/b}."

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
            $ renpy.pause(1)
            s "THE SHELF IS COVERED IN COINS AND PAPERS."
            s "A DISORGANIZED MESS."
            $ checked_shelf = True
        "Look in the boxes." if not checked_boxes:
            $ renpy.pause(1)
            s "THE BOXES ARE FILLED WITH BOTTLES."
            s "THE BOTTLES ARE FILLED WITH CHEMICALS."
            s "THE CHEMICALS ARE FILLED WITH POISONS."
            $ checked_boxes = True

    $ renpy.pause(1)

    s "MY BODY IS NOT THERE."

    if not (checked_shelf and checked_boxes):
        jump search_storeroom

    $ renpy.pause(1)

    s "MY BODY IS NOT IN THIS ROOM."
    s "WHERE IS MY BODY?"

    menu:
        "Search elsewhere.":
            pass

    scene bg forest
    with slowfade

    $ renpy.pause(1)

    s "OUTSIDE."
    s "I WOULD BE COLD {w}IF I HAD SKIN."
    s "WHERE IS MY BODY?"
    
    default checked_trees = False
    default checked_rocks = False
    default checked_creek = False
    
label search_forest:
    menu:
        "Look behind the trees." if not checked_trees:

            $renpy.pause(1)

            s "THE ROOTS ARE LIKE PETRIFIED TENTACLES, THEIR WRITHING \
            CAUGHT IN TIME."
            s "SOMETHING CAUGHT ON A PROTRUSION."

            $renpy.pause(1)

            s "A SCRAP OF CLOTH FROM A SHIRT."
            s "WAS IT FROM {b}MY{/b} SHIRT?"
            
            $ checked_trees = True

        "Look under the rocks." if not checked_rocks:
            
            $renpy.pause(1)

            s "SMALL LOOSE ROCKS SCATTERED ACROSS THE DIRT."
            s "EASY TO SLIP AND FALL."
            s "WHERE WOULD YOU LAND IF YOU FELL LIKE THAT?"

            $checked_rocks = True

            jump search_forest

        "Look in the creek." if checked_rocks and not checked_creek:

            $renpy.pause(1)

            s "A STEEP BANK COVERED IN LOOSE STONES ABOVE ICY WATERS."
            s "WHAT LIES BENEATH THE SURFACE?"

            $renpy.pause(1)

            s "THE KEY TO A CAR."
            s "IS IT MY CAR?"

            $checked_creek = True

    $ renpy.pause(1)

    s "MY BODY IS NOT THERE."

    if not (checked_trees and checked_creek):
        jump search_forest

    $ renpy.pause(1)

    s "MY BODY IS NOT IN THE FOREST."
    s "WHERE IS MY BODY?"

    menu:
        "Explore the city.":
            pass

    scene bg streets
    with slowfade

    s "QUIET NIGHT. EMPTY STREETS."
    s "I WOULD GO FOR A WALK {w}IF I HAD LEGS."
    s "WHERE IS MY BODY?" 

default checked_shops = False
default checked_alley = False

label search_city:
    menu:
        "Look in the shop windows." if not checked_shops:

            $ renpy.pause(1)

            s "CLOTHES TO COVER THE BODY."
            s "FOOD TO NOURISH THE BODY."
            s "DRINK TO QUENCH THE BODY."

            $ renpy.pause(1)

            s "NOTHING FOR ME."

            $ checked_shops = True

        "Look down the alley." if not checked_alley:

            $ renpy.pause(1)

            s "NARROW AND DARK. TALL BUILDINGS LOOMING ON EITHER SIDE."
            s "NO{b}BODY{/b} WOULD RISK WANDERING A DARK ALLEY AT NIGHT."

            $ checked_alley = True

    $ renpy.pause(1)

    s "MY BODY IS NOT THERE."

    if not (checked_shops and checked_alley):
        jump search_city

    show taker standing at center
    with moveinleft
    
    hide taker
    with moveoutright

    s "WHO WAS THAT?"
    s "WAS THAT {w=1.0}MY {b}BODY{/b}?"

    menu:
        "Follow the figure.":
            pass 

    scene bg lab
    with slowfade

    s "A LABORATORY."
    s "THE THIEF IS INSIDE."
    s "MY {b}BODY{/b} IS INSIDE."
    return
