
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# define anita = Character("Anita",color="#ca1f7b")
# define mory = Character("[mory_name]",color="#4F7942")
# define eleanor = Character("Eleanor", color ="#ba55d3")
# define vivian = Character("[vivian_name]",color="#9c0101")
# define void = Character("Void",color="#301934")
# define cafe_waiter = Character("Cafe Waiter",color="#0088A3")
# define allen = Character("Allen",color="#0088A3")

default vivian_name = "???"
default mory_name = "???"
default elleanor_name = "???"

define anita = Character("Anita", namebox_background=AlphaMask(Solid("#ca1f7b"), "gui/namebox.png"))
define mory = Character("[mory_name]", namebox_background=AlphaMask(Solid("#4F7942"), "gui/namebox.png"))
define elleanor = Character("[elleanor_name]", namebox_background=AlphaMask(Solid("#ba55d3"), "gui/namebox.png"))
define vivian = Character("[vivian_name]", namebox_background=AlphaMask(Solid("#9c0101"), "gui/namebox.png"))
define void = Character("Void", namebox_background=AlphaMask(Solid("#301934"), "gui/namebox.png"))
define cafe_waiter = Character("Cafe Waiter", namebox_background=AlphaMask(Solid("#0088A3"), "gui/namebox.png"))
define allen = Character("Allen", namebox_background=AlphaMask(Solid("#0088A3"), "gui/namebox.png"))
define lamlor = Character("Mr.Lamlor", namebox_background=AlphaMask(Solid("#0088A3"), "gui/namebox.png"))
define receptionist = Character("Receptionist", namebox_background=AlphaMask(Solid("#0088A3"), "gui/namebox.png"))
define doctorh = Character("Dr. Hood", namebox_background=AlphaMask(Solid("#0088A3"), "gui/namebox.png"))
define question = Character("????", namebox_background=AlphaMask(Solid("#0088F2"), "gui/namebox.png"))
define mom = Character("Mom", namebox_background=AlphaMask(Solid("#008080"), "gui/namebox.png"))
define young = Character("Young Anita", namebox_background=AlphaMask(Solid("008080"), "gui/namebox.png"))
define dad = Character("Dad", namebox_background=AlphaMask(Solid("#008080"), "gui/namebox.png" ))
define emma = Character("Emma", namebox_background=AlphaMask(Solid("008080"), "gui/namebox.png"))

# The game starts here.

label start:
    #Temporary jump to petting Void 
    menu: 
        "Pet void.": 
            call screen petVoid
            jump start
        "Proceed to main story.": 
            jump scene_101

    # This ends the game.

    return
return
