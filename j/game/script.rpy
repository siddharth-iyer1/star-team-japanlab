# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MC = Character("Main Character")


screen streetView():
    zorder 5
    imagebutton:
        idle "setsuko_dot.png"  # Use a simple test image
        hover "setsuko_dot.png"
        xalign 0.5
        yalign 0.8
        action [ToggleScreen("streetView"), Jump("setsuko_letter")]
    imagebutton:
        idle "movie_dot.png"  # Use a simple test image
        hover "movie_dot.png"
        xalign 0.25
        yalign 0.55
        action [ToggleScreen("streetView"), Jump("two_woman")]
    imagebutton:
        idle "news_dot.png"  # Use a simple test image
        hover "news_dot.png"
        xalign 0.95
        yalign 0.3
        action [ToggleScreen("streetView"), Jump("newspaper")]
    imagebutton:
        idle "radio_dot.png"  # Use a simple test image
        hover "radio_dot.png"
        xalign 0.775
        yalign 0.25
        action [ToggleScreen("streetView"), Jump("magazine")]
    

label setsuko_letter:
    MC "You read a letter from Setsuko, gossiping about a girl from their school who was supposed to be a big star. Unfortunately, she got cast in a few traditional roles and was dunked on by the critics. Setsuko mentions that this girl starred alongside the guy from their film together – someone she’s totally not into."
    menu:
        "Keep Exploring?":
            call screen streetView
        "Done Exploring.":
            return
label magazine:
    MC "You browse through the magazines, noticing a strong emphasis on the modern girl movement. Articles encourage women to make their own decisions and stand out in society."
    menu:
        "Keep Exploring?":
            call screen streetView
        "Done Exploring.":
            return
label two_woman:
    MC "You overhear two young women gasping and clutching their pearls. They seem to be making fun of a friend who’s stuck in a boring, traditional marriage."
    menu:
        "Keep Exploring?":
            call screen streetView
        "Done Exploring.":
            return
label newspaper:
    MC "You glance at the newspaper, which discusses exoticism and the rise of talkies, along with mentions of importations from America and other parts of Asia."
    menu:
        "Keep Exploring?":
            call screen streetView
        "Done Exploring.":
            return

label start:
    scene street bg
    call screen streetView
    return

