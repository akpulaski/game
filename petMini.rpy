#mini game for petting the cat. 
# NEED: Void picture, hand icon. 

screen petMini: 
    modal True

    imagebutton: 
        idle "cat"
        xpos .5
        ypos .4 
        action [Call("petCat")]

    
label petCat: 
    show cat at catLoc
    "PET!"