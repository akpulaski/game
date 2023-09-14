transform catLoc: 
    xpos .3
    ypos .1


define config.mouse = { }
define config.mouse['pet_cat'] = [ ( "gui/hand.jpeg", 0, 0) ]

screen petVoid: 
    modal True

    imagebutton: 
        idle "void button"
        xpos .35
        ypos .19
        action [Call("petCat2")]
    imagebutton: 
        idle "ear left"
        xpos .378
        ypos .11
        action [Call("petCat")]
    imagebutton: 
        idle "ear right"
        xpos .507
        ypos .11 
    imagebutton: 
        idle "paws"
        xpos .420
        ypos .855
        action [Call("petCat3")]
    imagebutton: 
        idle "tail"
        xpos .589
        ypos .380
        action [Call("petCat3")]

#disliked ears
label petCat: 
    show void angry at catLoc
    "Void didn't seem to like that."
    return
    
#liked, main body, head
label petCat2: 
    show void happy at catLoc
    "Void purrs a bit." 
    return

#very disliked paw, tail
label petCat3: 
    show void startled at catLock 
    "Void really didn't like that."
    return