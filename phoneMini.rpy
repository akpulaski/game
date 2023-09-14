default photo_list = []
default person = ""
default x = 500
default y = 200

## this game is needing photos and a camera sound - the images for this game are currently in the folders but will remove once we have assets

define config.mouse = { }
define config.mouse["extra"] = [ ( "images/cursor/skullhand.png", 0, 0) ]
define config.mouse["hand"] = [ ( "images/hand_cursor.png", 0, 0) ]

init python:

    def cell_dragged(drags, drop):

        store.x = drags[0].x
        store.y = drags[0].y

        if not drop:
            return

        return drop.drag_name

screen take_photo():

    add "background_image"

    draggroup:

        # The cellphone.
        drag:
            child "iphonesmall"
            droppable False
            dragged cell_dragged
            xpos x ypos y

        # The targets.
        drag:
            drag_name "one"
            idle_child Solid("#0000", xysize=(50,50))
            # Just trying to see when the drag is droppable:
            selected_idle_child Solid("#0004", xysize=(50,50))
            draggable False
            pos (121, 43)

        drag:
            drag_name "two"
            child Solid("#0000", xysize=(50,50))
            draggable False
            pos (100, 257)

        drag:
            drag_name "three"
            child Solid("#0000", xysize=(50,50))
            draggable False
            pos (592, 217)

        drag:
            drag_name "four"
            child Solid("#0000", xysize=(50,50))
            draggable False
            pos (708, 56)

        drag:
            drag_name "five"
            child Solid("#0000", xysize=(50,50))
            draggable False
            pos (1070, 9)

    hbox:
        yalign 1.0 spacing 10
        for i in photo_list:
            frame:
                add i

    frame:
        align (1.0,1.0)
        has hbox
        textbutton "Take a Photo" action Return("photo")
        textbutton "Continue" action Return("exit")

image white = Solid("#fff")

label start_phone_game:
    scene black with None

    jump taking_photos

label taking_photos:

    $ default_mouse =  "extra"

    call screen take_photo

    $ result = _return

    if result in ["one", "two", "three", "four", "five"]:
        $ person = result
        jump taking_photos

    elif result == "photo":
        if person and person not in photo_list:
            $ photo_list.append(person)
            play sound "audio/Time for Rest.ogg"
            scene white with dissolve

        jump taking_photos

    scene black with None

    $ default_mouse =  "hand"

    $ person = ""

    "Let's keep visiting the neighbors...."

    return