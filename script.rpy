# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define anita = Character("Anita",color="#ca1f7b")
define mory = Character("[mory_name]",color="#4F7942")
define eleanor = Character("Eleanor", color ="#ba55d3")
define vivian = Character("[vivian_name]",color="#9c0101")
define void = Character("Void",color="#301934")
define cafe_waiter = Character("Cafe Waiter",color="#0088A3")
define allen = Character("Allen",color="#0088A3")

default vivian_name = " "
default mory_name = " "
# The game starts here.

label start:
    ## we probably need to call scene_101 first - unless that will not exist.
    jump scene_102

    # This ends the game.

    return
