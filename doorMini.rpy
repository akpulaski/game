#Code for door interactions, will be updated once we know where in the script we need to include it. 
# NEED: Gui images for the door and door bell. Hand mouse 


screen door:
    modal True 
    
    imagebutton: 
        idle "door.jpeg"
        xpos .2
        action(Jump("knockKnock"))
    
    imagebutton: 
        xpos .7
        ypos .4
        action(Jump("dingDong"))
        hover "pressed.png"
        idle "unpressed.png"
        

label knockKnock: 
    $ default_mouse =  "hand"
    "Knock knock"
    return

label dingDong: 
    $ default_mouse =  "hand"
    "Ding dong"
    return
