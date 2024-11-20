init python:
    import csv
    import random

    movie_data_fp = "/Users/justinbanh/Documents/GitHub/star-team-japanlab/star team/game/csv files/Movie DB - prewar movies.csv"

    used_movies = []

    class MovieMetaData:

        def __init__(self, id, title, description, role, di):
            self.id = id
            self.title = title
            self.description = description
            self.role = role
            self.di = di

    def get_two_movies_from_era_0():
        movies = []
        with open(movie_data_fp, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Era'] == '0':
                    movies.append(MovieMetaData(row['movieRoleId'], row['title'], row['description'], row['role']))

        return random.sample(movies, 2)

    def get_two_movies_of_type(type):
        # Only valid types allowed
        valid_types = {'trendiness', 'westernization', 'nationalism'}

        # If the type is invalid, return an error
        if type not in valid_types:
            return None, None  # or handle it appropriately

        movies = []
        with open(movie_data_fp, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['type'] == type and row['movieRoleId'] not in used_movies:
                    # Check if `di` is not empty and is either 0 or 1
                    try:
                        di_value = int(row['di'])  # Convert di to integer if possible
                    except ValueError:
                        continue  # Skip rows where di is NaN or invalid
                    if di_value in [0, 1]:  # Only include if di is 0 or 1
                        movies.append(MovieMetaData(row['movieRoleId'], row['title'], row['description'], row['role'], di_value))

        # Separate into two lists based on the `di` value
        movies_with_score_0 = [movie for movie in movies if movie.di == 0]
        movies_with_score_1 = [movie for movie in movies if movie.di == 1]

        # Check if we have movies in both lists before choosing randomly
        if not movies_with_score_0 or not movies_with_score_1:
            return None, None  # Or handle error as needed

        # Randomly select one movie from each list
        movie1 = random.choice(movies_with_score_0) #decrease
        movie2 = random.choice(movies_with_score_1) #increase

        # Add selected movies to the used list
        used_movies.extend([movie1.id, movie2.id])

        return movie1, movie2

    def get_movie_scores(movieRoleId):
        fp = "/Users/justinbanh/Documents/GitHub/star-team-japanlab/star team/game/csv files/Movie DB - movie stats.csv"
        with open(fp, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['movieRoleId'] == movieRoleId:
                    return row['trendiness'], row['westernization'], row['nationalism']

    def what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score):
        if trendiness_score <= 1:
            p_star = "star_p_empty"
        elif 1 <= trendiness_score <= 3:
            p_star = "star_p_one_quarter"
        elif 4 <= trendiness_score <= 7:
            p_star = "star_p_half"
        elif 8 <= trendiness_score <= 12:
            p_star = "star_p_three_quarter"
        elif 13 <= trendiness_score <= 15:
            p_star = "star_p_three_quarter"
        else:
            p_star = "star_p_overflow"

        if westernization_score == 0:
            b_star = "star_b_empty"
        elif 1 <= westernization_score <= 2:
            b_star = "star_b_one_quarter"
        elif westernization_score == 3:
            b_star = "star_b_half"
        elif 4 <= westernization_score <= 7:
            b_star = "star_b_three_quarter"
        elif westernization_score == 8:
            b_star = "star_b_full"
        else:
            b_star = "star_b_overflow"

        if nationalism_score == 0:
            g_star = "star_g_empty"
        # elif nationalism_score <=:
        #     g_star = "star_g_one_quarter"
        elif 1 <= nationalism_score <= 2:
            g_star = "star_g_half"
        elif 2 <= nationalism_score <= 4:
            g_star = "star_g_three_quarter"
        elif nationalism_score == 5:
            g_star = "star_g_full"
        else:
            g_star = "star_g_overflow"

        return p_star, b_star, g_star

    def what_relationship_bar_to_use(relationship_score):
        if relationship_score == 0:
            relationship_bar = "relationship_0"
        elif relationship_score == 1:
            relationship_bar = "relationship_1"
        elif relationship_score == 2:
            relationship_bar = "relationship_2"
        elif relationship_score == 3:
            relationship_bar = "relationship_3"
        elif relationship_score == 4:
            relationship_bar = "relationship_4"
        elif relationship_score == 5:
            relationship_bar = "relationship_5"
        elif relationship_score == 6:
            relationship_bar = "relationship_6"
        elif relationship_score == 7:
            relationship_bar = "relationship_7"
        elif relationship_score == 8:
            relationship_bar = "relationship_8"
        elif relationship_score == 9:
            relationship_bar = "relationship_9"
        elif relationship_score == 10:
            relationship_bar = "relationship_10"
        elif relationship_score == 11:
            relationship_bar = "relationship_11"
        elif relationship_score == 12:
            relationship_bar = "relationship_12"
        elif relationship_score == 13:
            relationship_bar = "relationship_13"
        elif relationship_score == 14:
            relationship_bar = "relationship_14"
        elif relationship_score == 15:
            relationship_bar = "relationship_15"
        else:
            relationship_bar = "unknown_relationship"

        return relationship_bar

init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0
    transform zoomedin:
        zoom 0.20
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0

#Define characters
define mcName = "Assertive Feminine Voice"
define MC = Character("[mcName]", window_background=Frame("images/mc_textbox.png", 25, 25))
define MCWar = Character("[mcName]", window_background=Frame("images/mc_textbox_war.png", 25, 25))
define darkMC = Character("[mcName]")
define prod = Character("Producer",image="producer")
define direct = Character("Director", image="director")
define setsuko = Character("Setsuko",image="setsuko", window_background=Frame("images/setsuko_textbox.png", 25, 25))
define toshiro = Character("Toshiro",image="toshiro", window_background=Frame("images/toshiro_textbox.png", 25, 25))
define kiyo = Character("Kiyo",image="kiyo", window_background=Frame("images/kiyo_textbox.png", 25, 25))
define kazuo = Character("Kazuo", image="kazuo", window_background=Frame("images/kazuo_textbox.png", 25, 25))
define setsukoWar = Character("Setsuko",image="setsukoWar", window_background=Frame("images/setsuko_textbox.png", 25, 25))
define toshiroWar = Character("Toshiro",image="toshiroWar", window_background=Frame("images/toshiro_textbox.png", 25, 25))
define kiyoWar = Character("Kiyo",image="kiyoWar", window_background=Frame("images/kiyo_textbox.png", 25, 25))
define kazuoWar = Character("Kazuo", image="kazuoWar", window_background=Frame("images/kazuo_textbox.png", 25, 25))
define older_actor = Character("Older Actor")
define older_actress = Character("Older Actress")
define manager = Character("Manager")
define crew = Character("Cast and Crew")
define male_actor = Character("Male Actor")

image chap1_movie = Movie(size=(1920, 1080), channel='movie', play="images/chap1.webm")
image intro_movie = Movie(size=(1920, 1080), channel='movie', play="images/intro_movie.webm")

# For Star Power Images
image background_strip = "images/Star Power Background.png"

image star_p_empty = "images/Purple Empty.png"
image star_p_one_quarter = "images/Purple One Quarter.png"
image star_p_half = "images/Purple Half.png"
image star_p_three_quarter = "images/Purple Three Quarter.png"
image star_p_full = "images/Purple Full.png"
image star_p_hover_flash = "images/Purple Hover.png"
image star_p_overflow = "images/Purple Overflow.png"

image star_b_empty = "images/Blue Empty.png"
image star_b_one_quarter = "images/Blue One Quarter.png"
image star_b_half = "images/Blue Half.png"
image star_b_three_quarter = "images/Blue Three Quarter.png"
image star_b_full = "images/Blue Full.png"
image star_b_hover_flash = "images/Blue Hover.png"
image star_b_overflow = "images/Blue Overflow.png"

image star_g_empty = "images/Green Empty.png"
image star_g_one_quarter = "images/Green One Quarter.png"
image star_g_half = "images/Green Half.png"
image star_g_three_quarter = "images/Green Three Quarter.png"
image star_g_full = "images/Green Full.png"
image star_g_hover_flash = "images/Green Hover.png"
image star_g_overflow = "images/Green Overflow.png"

image relationship_0 = "images/0.png"
image relationship_1 = "images/1.png"
image relationship_2 = "images/2.png"
image relationship_3 = "images/3.png"
image relationship_4 = "images/4.png"
image relationship_5 = "images/5.png"
image relationship_6 = "images/6.png"
image relationship_7 = "images/7.png"
image relationship_8 = "images/8.png"
image relationship_9 = "images/9.png"
image relationship_10 = "images/10.png"
image relationship_11 = "images/11.png"
image relationship_12 = "images/12.png"
image relationship_13 = "images/13.png"
image relationship_14 = "images/14.png"
image relationship_15 = "images/15.png"

#Define character sprites
image MC = "MC.png"
image side setsuko = "setsuko.png"
image side toshiro = "toshiro.png"
image side kiyo = "kiyo.png"
image side kazuo = "kazuo.png"
image side producer = "producer.png"
image side setsukoWar = "setsukoWar.png"
image side toshiroWar = "toshiroWar.png"
image side kiyoWar = "kiyoWar.png"
image side kazuoWar = "kazuoWar.png"
image side director = "director.png"
# Define initial scores
default trendiness_score = 0
default westernization_score = 0
default nationalism_score = 0
default relationship_score = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

    bar value time range timer_range xalign 0.5 yalign 0.7 xmaximum 300 at alpha_dissolve

label QTE:
    label QTEmenu:
        $ time = 5
        $ timer_range = 3
        $ timer_jump = 'QTEmenu_slow'
        show screen countdown

        menu:
            "AHHH I HAVE TO PRESS THIS BUTTON IN 5 SECONDS":
                hide screen countdown
                jump start
    label QTEmenu_slow:
        MC "OH NO I DIDNT RESPONT TO THE QTE IN TIME"
        return

label QTE1:
    label QTE1menu:
        $ time = 12.5
        $ timer_range = 12
        $ timer_jump = 'QTE1menu_slow'
        show screen countdown

        menu:
            "(ENCOURAGE) You need to project your voice! Your character will need to be heard over the background noise – the audience won’t only be hearing you.":
                hide screen countdown
                play sound "page turn.mp3" volume 0.5
                $ setsuko_path = "encourage"
                $ relationship_score += 1
                $ trendiness_score += 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
                play sound "page turn.mp3" volume 0.5
                $ renpy.pause(0.5)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                setsuko "You’re right. It might be a bit difficult for me, but I’ll try my best!"
                play sound "page turn.mp3" volume 0.5
                direct "Action!"
                play sound "page turn.mp3" volume 0.5
                setsuko "(shouting) Darling, I made dinner an hour ago, and you still haven’t eaten yet! I work so hard for this family..."
                play sound "page turn.mp3" volume 0.5
                direct "Cut! Splendid job, Wada-san! All that noise gave me a splitting headache… which is exactly what I wanted! Good work today."
                play sound "page turn.mp3" volume 0.5
                setsuko "(bows) Thank you. I will continue to do my best."
                play sound "page turn.mp3" volume 0.5
                jump afterQTE1
            "(REASSURE) You’ll be alright, don’t worry about it. You don’t want the scene to be too overwhelming.":
                hide screen countdown
                jump QTE1menu_slow
    label QTE1menu_slow:
            play sound "page turn.mp3" volume 0.5
            $ setsuko_path = "reassure"
            $ relationship_score -= 1
            $ trendiness_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            setsuko "Are you sure? Okay, I’ll follow your advice."
            play sound "page turn.mp3" volume 0.5
            direct "Action!"
            play sound "page turn.mp3" volume 0.5
            setsuko "(softly) Darling, I made dinner an hour ago, and you still haven’t eaten yet! I work so hard for this family..."
            play sound "page turn.mp3" volume 0.5
            direct "Cut! Wada-san, I said nagging wife, not passive wife! I could barely even hear you over the rest of the noise. We’ll have to dub over your audio in post-production."
            play sound "page turn.mp3" volume 0.5
            setsuko "(bows deeply) I apologize. I’ll try harder next time."
            play sound "page turn.mp3" volume 0.5
            direct "We don’t have any room for trying, Wada-san. You will do better."
            play sound "page turn.mp3" volume 0.5
            jump afterQTE1
        

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


# Screen for star and points
screen star_with_score(star_image, star_image_hover_flash, score, xpos, ypos, zoom, text_size, offset):

    fixed:
        xpos xpos
        ypos ypos

        add star_image zoom zoom  # Adjust zoom to resize the star

        imagebutton:
            idle star_image
            hover star_image_hover_flash
            action Show("info_screen") at zoomedin

        text "[score]":
            xpos 50 * text_size + offset
            ypos 48 * text_size + offset
            xanchor 0.5
            yanchor 0.5
            size (20 * text_size) # Adjust text size as needed
            color "#ffffff"  # Text color

screen industry_relations(image, hover_image, xpos, ypos, zoom, offset):

    fixed:
        xpos xpos
        ypos ypos

        add image zoom zoom  # Adjust zoom to resize the star

        imagebutton:
            idle image
            hover hover_image
            action Show("relationship_screen") at zoomedin

screen star_with_info(star_image, xpos, ypos):
    fixed:
        xpos xpos
        ypos ypos

        # Define the imagebutton with the star image as its idle and hover state
        imagebutton:
            idle star_image
            hover star_image
            action Show("info_screen") at zoomedin  # Replace with desired action

            # Text overlay on top of the imagebutton

screen score_display(p_star, b_star, g_star, ir, p_score, b_score, g_score):

    # Display the background image at the left corner
    # add "background_strip" xpos 0 ypos -80 zoom 0.18

    # Display the stars with scores using the helper screen
    use star_with_score(p_star, "star_p_hover_flash", p_score, xpos=20, ypos=10, zoom=0.2, text_size=1, offset=0)
    use star_with_score(b_star, "star_b_hover_flash", b_score, xpos=120, ypos=10, zoom=0.2, text_size=1, offset=0)
    use star_with_score(g_star, "star_g_hover_flash", g_score, xpos=220, ypos=10, zoom=0.2, text_size=1, offset=0)
    use industry_relations(ir, "industry_relations", xpos=1800, ypos=10, zoom=0.2, offset=0)

screen stats_bar():
    frame:
        background "#333333"
        xalign 0.5
        yalign 0.0
        padding (10, 10, 10, 10)
        hbox:
            spacing 50

            vbox:
                text "trendiness" size 20
                text "[trendiness_score]" size 20

            vbox:
                text "westernization" size 20
                text "[westernization_score]" size 20

            vbox:
                text "Nationalism" size 20
                text "[nationalism_score]" size 20

screen info_screen:
    modal True
    tag info_screen

    # Background frame with layered images
    frame:
        padding (-10, -10)

        # Use a fixed container to layer images and components
        fixed:
            add "starpower_background.png"  # Base background image

            # Display each star with its score in specific positions
            use star_with_score(p_star, "star_p_hover_flash", "Trendy", xpos=130, ypos=100, zoom=1, text_size=3, offset=95)
            use star_with_score(b_star, "star_b_hover_flash", "Westernized", xpos=700, ypos=100, zoom=1, text_size=3, offset=95)
            use star_with_score(g_star, "star_g_hover_flash", "Nationalistic", xpos=1300, ypos=100, zoom=1, text_size=3, offset=105)

            # Text descriptions under each star
            text "This trait reflects how well you adapt to changing social norms, industrial trends, and progressive ideas -– primarily appearing modern and fashionable. Trendiness can be influenced by boldness in dialogue, a consciousness of new film techniques, and an understanding of shifting gender ideas.":
                color "#000000"
                size 28
                xpos 400
                ypos 600
                xanchor 0.5
                xmaximum 425  # Limit the width to fit below the star

            text "This trait highlights how you adapt to the introduction of Western trends and attitudes. In an increasingly interconnected world, you will need to be aware of foreign influences -- whether that be new music trends, clothing styles, or popular makeup. Through either adhering to or defying local standards, responding to Western cultural influences, and more, your choices will define whether you stay true to a traditional Japanese style or dive into a more foreign, Westernized look.":
                color "#000000"
                size 28
                xpos 980
                ypos 600
                xanchor 0.5
                xmaximum 425  # Limit the width to fit below the star

            text "This trait represents your alignment with traditional Japanese values, culture, and governmental ideals. It manifests through adherence to social expectations, pride in the national memory, and awareness of the national sentiment, emphasizing an unifying, Japanese identity and support for your heritage.":
                color "#000000"
                size 28
                xpos 1580
                ypos 600
                xanchor 0.5
                xmaximum 425  # Limit the width to fit below the star

    # Button to close the screen
    textbutton "Close":
        action Hide("info_screen")
        xpos 0.5
        ypos 0.95
        xanchor 0.5
        yanchor 0.5

screen relationship_screen:
    modal True
    tag info_screen

    # Background frame with layered images
    # Display the relationship bar at the top center
    frame:
        background None
        add relationship_bar


    # Button to close the screen
    textbutton "Close":
        action Hide("relationship_screen")
        xpos 0.5
        ypos 0.95
        xanchor 0.5
        yanchor 0.5

define movie_header_font = "fonts/RialtoNF.ttf"

style movie_name_text:
    font movie_header_font
    size 48
    color "#FFFFFF"
    align (0.5, 0.5)

# Custom button style for the "Accept Role" button
style role_button:
    background im.FactorScale("images/Script_Button.png", 0.32)
    size 50
    padding (10, 10)
    xalign 0.5  # Center the text horizontally within the button
    yalign 0.5  # Center the text vertically within the button


screen movie_role_choice(movie1, movie2):
    hbox:
        spacing 200
        align (0.5, 0.35)

        frame:
            background im.FactorScale("images/Movie Script Asset.png", 0.87)
            xsize 400
            ysize 600

            vbox:
                xpos 0.15
                ypos 0.1
                # xmaximum 300
                spacing 20
                text "[movie1['name']]" style "movie_name_text"
                text "Description: [movie1['description']]" size 25 color "#000000"
                text "Role: [movie1['role']]" size 25 color "#000000"

                frame:
                    yfill True
                    background None

                # Button to choose this role
                textbutton "Accept Role" action [SetVariable("chosen_movie", "movie1"), Return()] style "role_button" text_color "#000000" align (0.4, 0.5)

        frame:
            background im.FactorScale("images/Movie Script Asset.png", 0.87)
            xsize 400
            ysize 600

            vbox:
                xpos 0.15
                ypos 0.1
                # xmaximum 300
                spacing 20
                text "[movie2['name']]" style "movie_name_text"
                text "Description: [movie2['description']]" size 25 color "#000000" align (0.5, 0.5)
                text "Role: [movie1['role']]" size 25 color "#000000"

                frame:
                    yfill True
                    background None


                # Button to choose this role
                textbutton "Accept Role" action [SetVariable("chosen_movie", "movie2"), Return()] style "role_button" text_color "#000000" align (0.4, 0.5)

screen relationship_bar(relationship_image):
    # Display the relationship bar at the top center
    frame:
        xpos 0.85
        ypos 0.05
        xanchor 0.5
        yanchor 0
        background None

        add relationship_image zoom 0.3

label setsuko_letter:
    play sound "page turn.mp3" volume 0.5
    MC "You read a letter from Setsuko, gossiping about a girl from their school who was supposed to be a big star. Unfortunately, she got cast in a few traditional roles and was dunked on by the critics. Setsuko mentions that this girl starred alongside the guy from their film together – someone she’s totally not into."
    play sound "page turn.mp3" volume 0.5
    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump officeOne
            return
label magazine:
    play sound "page turn.mp3" volume 0.5
    MC "You browse through the magazines, noticing a strong emphasis on the modern girl movement. Articles encourage women to make their own decisions and stand out in society."
    play sound "page turn.mp3" volume 0.5
    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump officeOne
            return
label two_woman:
    play sound "page turn.mp3" volume 0.5
    MC "You overhear two young women gasping and clutching their pearls. They seem to be making fun of a friend who’s stuck in a boring, traditional marriage."
    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump officeOne
            return
label newspaper:
    play sound "page turn.mp3" volume 0.5
    MC "You glance at the newspaper, which discusses westernization and the rise of talkies, along with mentions of importations from America and other parts of Asia."
    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump officeOne
            return

label start:
    python:
        p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
    python:
        relationship_bar = what_relationship_bar_to_use(relationship_score)

    stop music
    scene solidblack

    darkMC "Who am I?"
    play sound "page turn.mp3" volume 0.5

    darkMC "That’s an interesting question, I suppose."
    play sound "page turn.mp3" volume 0.5

    darkMC "I’m a woman. I was born in Osaka, Japan, in 1915."
    play sound "page turn.mp3" volume 0.5

    darkMC "My favorite color is red, but I rarely get to wear it."
    play sound "page turn.mp3" volume 0.5

    darkMC "But that doesn’t answer your question, does it?"
    play sound "page turn.mp3" volume 0.5

    darkMC "So, tell me – who am I?"
    play sound "page turn.mp3" volume 0.5

    play sound "click reverb.mp3"
    darkMC "Don’t be nervous. This is what I do. I am whoever you want me to be. Just tell me."

    show greysil

    python:
        mcName = renpy.input("Name:", length=16)
        mcName = mcName.strip()
        if not mcName:
            mcName = "Yoshiko"

    scene solidblack

    darkMC "[mcName]. Interesting. Did you know that changing names is a common practice among actresses?"
    play sound "page turn.mp3" volume 0.5
    darkMC "Oh, that’s what I forgot to tell you. I’m an actress, and forgive my arrogance, but quite a good one, too."
    play sound "page turn.mp3" volume 0.5
    darkMC "Now, as an actress, I’ve had quite a number of stories to tell. Whirlwind romances, a wrenching tragedy, a soft, sweet girl appearing only to support the glittering ingenue."
    play sound "page turn.mp3" volume 0.5
    darkMC "There is a glamor to the screen – it all glows in that dark room, the only light amid a backdrop of silence. It is stunning. Captivating."
    play sound "page turn.mp3" volume 0.5
    darkMC "The voices you could picture from the radio suddenly belong to people – to women and men with faces and expressions that seize you by the heart and force it to beat to a rhythm of their own design."
    play sound "page turn.mp3" volume 0.5
    darkMC "Oh yes, it’s a spectacle. All the audience weeps and laughs together. Well, all together in attendance."
    play sound "page turn.mp3" volume 0.5
    darkMC "In that moment, perhaps there is unity. But once the lights return and the world is no longer scripted, what becomes of the characters?"
    play sound "page turn.mp3" volume 0.5
    darkMC "They disappear. They melt back into their original forms – the actors. But even then, the show never stops. For in the day, in the night, between each bite at each meal, the performance goes on. That is what it means to be a star."
    play sound "page turn.mp3" volume 0.5
    darkMC "You cannot rely on the lights of the set to carry you through to the next role. No, you must shine of your own accord. You must never go out. And you must reach far beyond your own space."
    play sound "page turn.mp3" volume 0.5
    darkMC "Would you like to hear how I did it?"

    menu:
        "Yes":
            darkMC "Thank you for indulging me."
            play sound "page turn.mp3" volume 0.5
        "No":
            darkMC "Hm, perhaps another time then."
            return
        "SKIP TO CHAPTER 2":
            jump start2

    darkMC "I hope my story will be an interesting enough exchange..."
    play sound "page turn.mp3" volume 0.5

    show intro_movie

    scene intro 1

    play music "onna keizu no uta.mp3" loop

    darkMC "I’m from Osaka, you already know that.My parents were a perfect sort of couple – father a hardworking government officer, mother a housewife that put all others to shame. Meals were quiet, but never uncomfortable."
    play sound "page turn.mp3" volume 0.5

    scene intro 2

    darkMC "I always loved to sing. I’d put on private performances for myself, singing the same songs I’d heard at the festivals and in school. And at nine, my mother took notice. She enrolled me in music lessons with a strict but kind tutor, Ō Shūka, though she preferred I called her by her Chinese name, Wang Qiuxia."
    play sound "page turn.mp3" volume 0.5

    darkMC "We spent long days together – I often saw her more than my own family. She spoke to me in both Japanese and Mandarin, broken parts of the latter until I could finally hold a conversation in full. I owe much of my career to her and her guidance."
    play sound "page turn.mp3" volume 0.5

    scene intro 3

    darkMC "At the Aoi Matsuri in 1928, I was given the opportunity – no doubt with some strings pulled by Ms. Wang and my parents – to perform on a public stage. It was a night that would change my life."
    play sound "page turn.mp3" volume 0.5

    darkMC "A man in the audience, whether or not his presence was a coincidence, treated my song as an audition and offered me a spot in the Naniwa Conservatoire, a top acting school. Though I kept an air of quiet humility as I accepted, as I signed my first contract, there was not a drop of reservation between my trembling fingers."   
    play sound "page turn.mp3" volume 0.5

    stop music
    play music "typewriter.mp3" loop

    hide intro 3

    window hide

    show chap1_movie zorder 10
    pause
    show studio bg
    hide chap1_movie
    window auto
    show screen score_display(p_star, b_star, g_star, "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    stop music
    play music "crowd-ambience.mp3" loop volume 0.5
    direct "What do you mean she can’t make the shot? What’s her excuse? Doesn’t she understand how big of an opportunity this is?"
    play sound "page turn.mp3" volume 0.5

    prod "Her family sends their regrets, sir, but her doctor doesn’t recommend she leave the hospital until her lungs have cleared."
    play sound "page turn.mp3" volume 0.5

    direct "This is a disaster – we don’t have this space forever. Should we just cut the character?"
    play sound "page turn.mp3" volume 0.5

    prod "It may be too late for that. Why don’t we get one of the younger girls to stand in? She just has to look nice, right?"
    play sound "page turn.mp3" volume 0.5

    direct "(sighs, grumbles) At least let me get a look at them. These girls are here for their voices, not their faces. We don’t need some oni wasting space on the film."
    play sound "page turn.mp3" volume 0.5

    play sound "MC laughing.mp3" volume 1.5
    MC "Hahaha!"
    play sound "page turn.mp3" volume 0.5

    direct "Where did that one come from?"
    play sound "page turn.mp3" volume 0.5

    prod "That would be [mcName], I believe."
    play sound "page turn.mp3" volume 0.5

    direct "What school?"
    play sound "page turn.mp3" volume 0.5

    prod "The Naniwa Conservatoire. Her family is quite well-to-do – I believe she’s been taking lessons since childhood. Would you–"
    play sound "page turn.mp3" volume 0.5

    direct "Get her in costume. I want her back here in five minutes."
    play sound "page turn.mp3" volume 0.5

    prod "Yes, sir."
    play sound "page turn.mp3" volume 0.5

    prod "[mcName]?"
    play sound "page turn.mp3" volume 0.5

    MC "Hm? Oh! Hello, sir."
    play sound "page turn.mp3" volume 0.5

    prod "We are in a bit of an emergency situation. One of our actresses has fallen ill and we need someone to fill in her place. The director has chosen you."
    play sound "page turn.mp3" volume 0.5

    play sound "woman startled gasp.mp3" volume 0.8
    MC "What, me?"
    play sound "page turn.mp3" volume 0.5
    MC "Oh my gosh!" # Visible excitement
    play sound "page turn.mp3" volume 0.5

    # MC's thoughts
    MC "My first role! At sixteen! But that poor actress, I almost feel guilty…"

    menu:
        "I know I’m only an amateur, but I’ll give it my all!":
            play sound "MC laughing.mp3" volume 1.5
            MC "I know I’m only an amateur, but I’ll give it my all!"
            play sound "page turn.mp3" volume 0.5
            $ trendiness_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

        "I’m not sure if I should…":
            MC "I’m not sure if I should…"
            play sound "page turn.mp3" volume 0.5
            $ trendiness_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    prod "No need for stress – it’s a walk-on role."
    play sound "page turn.mp3" volume 0.5

    MC "Oh… ([mcName] is slightly disappointed...)"
    play sound "page turn.mp3" volume 0.5

    prod "That doesn’t mean it’s not important. The director chose you. Let me show you to the costuming room – we need you back here as soon as possible for a run-through."
    play sound "page turn.mp3" volume 0.5

    # Producer exits the frame
    prod "Follow me. (The producer exits the room.)"
    play sound "page turn.mp3" volume 0.5

    # MC left alone
    MC "That was how it began – a total accident. A role so small my name might not even appear in the credits. But that moment…"
    play sound "page turn.mp3" volume 0.5

    MC "The feeling of powder on my cheeks, like hot sand on my skin."
    play sound "page turn.mp3" volume 0.5

    MC "Whether warm from the lights or from the mixture of pride and sheer terror that coursed my body."
    play sound "page turn.mp3" volume 0.5

    MC "I was stiff as a board, I’m sure. Yet that was the first time I felt so alive. So very real."
    play sound "page turn.mp3" volume 0.5

    stop music

 # MC and Producer dialogue

    scene office bg
    play music "tokyo kenbutsu.mp3" loop

    MC "Thank you. It was just a bit part…"
    play sound "page turn.mp3" volume 0.5


    menu:
        "but I’m grateful nonetheless.":
            play sound "page turn.mp3" volume 0.5

            prod "Well, you were outstanding. So much so that…"
            play sound "page turn.mp3" volume 0.5

            $ trendiness_score -= 1
            $ relationship_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)


        "so I’m ready to move on to bigger things.":
            play sound "page turn.mp3" volume 0.5

            prod "Quite a spark you’ve got there. You’re going to need that ambition, because…"
            play sound "page turn.mp3" volume 0.5
            $ trendiness_score += 2
            $ relationship_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)

    $ renpy.pause(0.5)

    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    prod "You’ve been contracted to a new role."
    play sound "page turn.mp3" volume 0.5


    python:
        movie_choices = get_two_movies_of_type("trendiness")

        movie1_title = movie_choices[0].title
        movie1_description = movie_choices[0].description
        movie1_role = movie_choices[0].role

        movie2_title = movie_choices[1].title
        movie2_description = movie_choices[1].description
        movie2_role = movie_choices[1].role

        movie1 = {
            "name": movie1_title,
            "description": movie1_description,
            "role": movie1_role,
        }

        movie2 = {
            "name": movie2_title,
            "description": movie2_description,
            "role": movie2_role,
        }

    call screen movie_role_choice(movie1, movie2)

    if chosen_movie == "movie1":
        play sound "click.mp3" volume 1.5
        "You have chosen the role in [movie1['name']]."
        $ trendiness_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    elif chosen_movie == "movie2":
        play sound "click.mp3" volume 1.5
        "You have chosen the role in [movie2['name']]."
        $ trendiness_score += 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)


    play sound "page turn.mp3" volume 0.5

    $ renpy.pause(0.5)

    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    prod "Here is your script. Rehearsals will start promptly next Tuesday. I’m obligated to tell you to represent us well, though I doubt you’ll have any trouble with that."
    play sound "page turn.mp3" volume 0.5

    MC "Of course."
    play sound "page turn.mp3" volume 0.5

    stop music

    # Setting changes to the movie set
    show studio bg

    play music "crowd-ambience.mp3" loop volume 0.5

    # MC and Setsuko dialogue
    setsuko "Oh, this is just thrilling! I can’t believe we’re here, together, in our first film!"
    play sound "page turn.mp3" volume 0.5

    MC "First… yes."
    play sound "page turn.mp3" volume 0.5

    play sound "hmm.mp3" volume 0.5
    MC "I don’t know if I should tell her it isn’t my first…"
    play sound "page turn.mp3" volume 0.5

    setsuko "I heard that one of the actresses in 'first film name' got kicked out, and they had a random chorus girl take her place! It’s so embarrassing – I don’t know how I’d return to the company. But whoever filled in – what a lucky girl! What I wouldn’t give to have that chance."
    play sound "page turn.mp3" volume 0.5

    MC "(slightly uncomfortable) Wow, that’s quite a story. Where did you hear that?"
    play sound "page turn.mp3" volume 0.5

    setsuko "Where haven’t I heard! It’s all the talk around the academy–"
    play sound "page turn.mp3" volume 0.5

    prod "Ladies, that’s enough chatting. We’re starting soon. [mcName], please save your voice unless you’re going over your lines. Wada, what on earth are you doing in your regular clothes? Go see costumes immediately."
    play sound "page turn.mp3" volume 0.5

    setsuko "(in a whisper) What a killjoy! Oh, but [mcName], I’ll tell you more later!"
    play sound "page turn.mp3" volume 0.5

    # Setsuko hurries off
    play sound "woman startled gasp.mp3" volume 0.8
    MC "(internal) What should I do right now?"
    play sound "page turn.mp3" volume 0.5


    menu:
        "Rehearse alone.":
            play sound "page turn.mp3" volume 0.5
            MC "I’ll just go over my lines quietly."
            play sound "page turn.mp3" volume 0.5
            # End the scene and transition to next part
            jump after_film_scene

        "Find Setsuko.":
            play sound "page turn.mp3" volume 0.5
            $ relationship_score += 1
            python:
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            # Leads to the scene in blue
            jump find_setsuko_scene

label after_film_scene:
    # Insert after film scene logic here
    MC "I rehearsed by myself..."
    stop music
    play music "minato chanson.mp3" loop

    jump explore_scene

label find_setsuko_scene:
    scene studio bg # Replace with the appropriate background
    play music "crowd-ambience.mp3" loop volume 0.5
    MC "Setsuko?"
    play sound "page turn.mp3" volume 0.5
    setsuko "(jumps) [mcName]! What are you doing? I thought you were supposed to be rehearsing!"
    play sound "page turn.mp3" volume 0.5
    MC "I wanted to hear more about…"
    play sound "page turn.mp3" volume 0.5
    menu:
        "the gossip around the academy.":
            play sound "page turn.mp3" volume 0.5
            play sound "mc laughing.mp3" volume 1.5
            setsuko "(smirks conspiratorially) Well, I heard that it was one of our girls who got selected for that fill-in role! No one knows who, exactly, but what a bold move! Imagine volunteering for something like that… I know I’d do it without a second thought, but the older tutors are always telling me I come across way too eager."
            play sound "page turn.mp3" volume 0.5
            setsuko "It’s too ‘modern’ or ‘not ladylike’ or something. But what’s wrong with that? I think that’s what the people like nowadays, anyway!"
            play sound "page turn.mp3" volume 0.5
        "the other actors here.":
            play sound "page turn.mp3" volume 0.5
            setsuko "(smirks conspiratorially) Hm, well I haven’t really spoken to him yet, but I did see this right 'relevant hot guy' talking with the director earlier. I don’t think he’s a big star or anything, but maybe he is! He’s certainly got the looks for it! (she blushes) Not that I’m interested. I’m just saying…"
            play sound "page turn.mp3" volume 0.5
    MC "What’s wrong with being interested?"
    play sound "page turn.mp3" volume 0.5
    setsuko "I don’t want him to think I’m too forward!"
    play sound "page turn.mp3" volume 0.5
    MC "I wonder if people still like shy girls these days…"
    play sound "page turn.mp3" volume 0.5
    setsuko "You’re right! Actually, just last week I saw this magazine headline: 'He’s Your Husband, Not Your Parents’!' These trends change so fast… It feels like just a year ago we were being told to shut up and stick to our homes. But now you see all these modern girls walking around in their heels and their bold colors!"
    play sound "page turn.mp3" volume 0.5
    MC "I don’t know how to keep up with it."
    play sound "page turn.mp3" volume 0.5
    setsuko "I don’t really know either – but I guess you can find out a lot through the news and the things people say on the street. We should both keep our ears sharp! And I’ll let you know if I learn anything really interesting."
    play sound "page turn.mp3" volume 0.5

    stop music
    play music "minato chanson.mp3" loop

    # Transition to the next part of the game
    jump explore_scene

label explore_scene:
    scene street bg
    call screen streetView

label officeOne:
    stop music
    play music "tokyo kenbutsu.mp3" loop
    # Scene change to MC with Producer
    scene office bg  # Replace with the appropriate background

    prod "Five years ago I never would’ve thought I’d be seeing one of my actresses in a talkie. I didn’t even think we’d have talkies by now! I’m proud of you, MC."
    play sound "page turn.mp3" volume 0.5
    MC "Thank you…"
    play sound "page turn.mp3" volume 0.5

    show office bg
    menu:
        "I really didn’t expect things to take off so fast.":
            play sound "page turn.mp3" volume 0.5
            $ trendiness_score -= 1
            $ relationship_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            prod "No need to be humble. You’ve got something special. Even that quack of a director could tell just from a single look."
            play sound "page turn.mp3" volume 0.5


        "But I never really doubted myself.":
            play sound "page turn.mp3" volume 0.5
            $ trendiness_score += 1
            $ relationship_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            prod "There’s that spunk again. Keep that spark – the people like a clever girl."
            play sound "page turn.mp3" volume 0.5

    prod "And on that note, I’ve got some exciting news."
    play sound "page turn.mp3" volume 0.5

    # Producer produces a script
    prod "You’ve got another role!"
    play sound "page turn.mp3" volume 0.5
    # He hands MC the script
    prod "This one is called…"
    play sound "page turn.mp3" volume 0.5

    python:
        movie_choices = get_two_movies_of_type("westernization")

        movie1_title = movie_choices[0].title
        movie1_description = movie_choices[0].description
        movie1_role = movie_choices[0].role

        movie2_title = movie_choices[1].title
        movie2_description = movie_choices[1].description
        movie2_role = movie_choices[1].role

        movie1 = {
            "name": movie1_title,
            "description": movie1_description,
            "role": movie1_role,
        }

        movie2 = {
            "name": movie2_title,
            "description": movie2_description,
            "role": movie2_role,
        }

    call screen movie_role_choice(movie1, movie2)

    if chosen_movie == "movie1":
        "You have chosen the role in [movie1['name']]."
        play sound "page turn.mp3" volume 0.5
        $ westernization_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
        show screen score_display("Purple Empty Idle.png", "Red Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
    elif chosen_movie == "movie2":
        "You have chosen the role in [movie2['name']]."
        play sound "page turn.mp3" volume 0.5
        $ westernization_score += 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
        show screen score_display("Purple Empty Idle.png", "Green Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    $ renpy.pause(0.5)

    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    prod "Shooting starts next week – start looking over your lines. Take a deep breath, you’ll be fine. The last movie did well and the stakes are low, alright? Do your best."
    play sound "page turn.mp3" volume 0.5
    stop music

    # Scene change to the set
    scene studio bg  # Replace with the appropriate background
    play music "crowd-ambience.mp3" loop volume 0.5

    # Kiyo and Tōshiro conversation
    kiyo "Ohh, that was you was it? I thought you were divine, but that girl you were with… What was her name?"
    play sound "page turn.mp3" volume 0.5

    toshiro "Suga… something?"
    play sound "page turn.mp3" volume 0.5

    kiyo "Doesn’t matter. She was so plain. Such a shame! Things probably would’ve gone much smoother if you got someone more lively."
    play sound "page turn.mp3" volume 0.5

    # Kiyo notices MC
    kiyo "Hello you! (she beckons [mcName] over) Don’t be shy – we don’t bite."
    play sound "page turn.mp3" volume 0.5

    MC "(internal) Are you sure…?"
    play sound "page turn.mp3" volume 0.5

    toshiro "Hm. (he looks [mcName] up and down) Your face… Have we met before?"
    play sound "page turn.mp3" volume 0.5

    MC "I believe so. I’m [mcName], I think we did (name of first bucket movie) a year or so ago? I was–"
    play sound "page turn.mp3" volume 0.5
    show studio bg
    toshiro "Impossible. I would’ve remembered a face like yours. (he smirks) But maybe I’ll give that one another watch – join me, make it a reunion?"
    play sound "page turn.mp3" volume 0.5

    menu:
        "I wouldn’t mind reliving some moments.":
            play sound "page turn.mp3" volume 0.5
            toshiro "We’ll talk a little later, then?"
            play sound "page turn.mp3" volume 0.5
            kiyo "(clears throat) I can’t imagine you’d have time, what with your schedule. Weren’t you just saying you have another film lined up right after this?"
            play sound "page turn.mp3" volume 0.5
            toshiro "Films are easy to come by. This is a rare opportunity."
            play sound "page turn.mp3" volume 0.5
            kiyo "(clearly disgruntled) [mcName], where did you get your dress?"
            play sound "page turn.mp3" volume 0.5

        "Only if I can bring my friend, Setsuko. Do you remember her too?" :
            play sound "page turn.mp3" volume 0.5
            python:
                relationship_score += 1
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            toshiro "Um… if you want–"
            play sound "page turn.mp3" volume 0.5
            kiyo "How cute! Maybe I’ll tag along, we can make a night of it. But we ladies might have to do some shopping first. Your dress…"
            play sound "page turn.mp3" volume 0.5

    MC "My dress?"
    play sound "page turn.mp3" volume 0.5
    show studio bg
    kiyo "It’s so quaint. Cute, I suppose – reminds me of that little rural town I visited back as a girl. Which is fine, of course, plenty of girls are still attached to that schoolgirl look. I just think it’s become a bit… outdated, don’t you think?"
    play sound "page turn.mp3" volume 0.5

    # A third person approaches
    kazuo "Hey everyone. (he notices [mcName]) I don’t think we’ve met – this is my first movie, actually. I’m Tachibana Kazuo."
    play sound "page turn.mp3" volume 0.5

    MC "[mcName], it’s nice to meet you."
    play sound "page turn.mp3" volume 0.5
    show studio bg
    toshiro "You need something?"
    play sound "page turn.mp3" volume 0.5

    kazuo "I just thought we might want to do a bit of rehearsal? Run through some lines, or something…"
    play sound "page turn.mp3" volume 0.5

    kiyo "Fantastic idea, Tachibana."
    play sound "page turn.mp3" volume 0.5

    kazuo "Tachibana."
    play sound "page turn.mp3" volume 0.5

    kiyo "Okay. Watanabe-san, do you want to go into the hallway? We can work on that second scene together."
    play sound "page turn.mp3" volume 0.5

    toshiro "Sure. (towards [mcName]) See you later?"
    play sound "page turn.mp3" volume 0.5

    # The two leave, now just Kazuo and MC
    kazuo "So, do you want to do a read-through?"
    play sound "page turn.mp3" volume 0.5

    MC "Oh…"
    play sound "page turn.mp3" volume 0.5

    menu:
        "Actually, I think I’m in that second scene as well.":
            $ relationship_score += 2
            python:
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            jump blue1  # leads to scene in blue

        "That sounds nice.":
            $ relationship_score += 1
            python:
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            jump green1  # leads to scene in green

label blue1:
    kiyo "(in character) Sasuke-san, you can’t possibly be asking me to marry you? Why, I’m only finishing school!"
    play sound "page turn.mp3" volume 0.5
    toshiro "Is it later already?"
    play sound "page turn.mp3" volume 0.5
    kiyo "I don’t think we need another person right now."
    play sound "page turn.mp3" volume 0.5
    toshiro "Relax, it’s not like we were doing anything serious."
    play sound "page turn.mp3" volume 0.5

    menu:
        "You don’t take your work seriously?":
            $ relationship_score -= 1
            $ trendiness_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ toshiro_path = "a"
        "Why don’t you show me something serious, then?":
            $ relationship_score += 1
            $ trendiness_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ toshiro_path = "b"

    if toshiro_path == "a":
        play sound "page turn.mp3" volume 0.5
        toshiro "I take things seriously when they’re worth it. You’re new here, right?"
        play sound "page turn.mp3" volume 0.5
        MC "No, not particularly..."
        play sound "page turn.mp3" volume 0.5
        toshiro "A decent actor is an easy find, these days. Everyone wants to be on screen..."
        play sound "page turn.mp3" volume 0.5
        menu:
            "We’re actors. We’re here to act, isn’t that most important?":
                play sound "page turn.mp3" volume 0.5
                pass
            "...What do you mean? (internal) What am I missing?":
                play sound "page turn.mp3" volume 0.5
                pass

    elif toshiro_path == "b":
        toshiro "(smirks) Sure, next time. Give me a call and we’ll make it a date, alright?"
        play sound "page turn.mp3" volume 0.5
        MC "(rolls eyes)"
        play sound "page turn.mp3" volume 0.5
        kiyo "Oh, please, get a room..."
        play sound "page turn.mp3" volume 0.5
        menu:
            "Finally, something we can agree on.":
                play sound "page turn.mp3" volume 0.5
                pass
            "I wasn’t really interested, anyway...":
                play sound "page turn.mp3" volume 0.5
                pass

    toshiro "There’s more to being an actor than just a script. Anyone can perform lines and call it a day..."
    play sound "page turn.mp3" volume 0.5
    kiyo "We’re special. We have a certain... presence..."
    play sound "page turn.mp3" volume 0.5
    MC "That’s right... At least, I hope I won’t."
    play sound "page turn.mp3" volume 0.5
    jump CH1QTE1

label green1:
    kazuo "(in character) That will be ten sen, please."
    play sound "page turn.mp3" volume 0.5
    MC "(in character) Couldn’t you spare a discount? For a hungry young girl?"
    play sound "page turn.mp3" volume 0.5
    kazuo "No can do, miss. Sorry, but business has to run somehow. (he breaks character and sighs)"
    play sound "page turn.mp3" volume 0.5
    kazuo "I don’t know why he’s being so stingy. It’s just a piece of bread."
    play sound "page turn.mp3" volume 0.5

    menu:
        "Would you?":
            play sound "page turn.mp3" volume 0.5
            $ kazuo_path = "a"
        "Would you for me?":
            play sound "page turn.mp3" volume 0.5
            $ kazuo_path = "b"

    if kazuo_path == "a":
        kazuo "I might… It would depend on whether or not my boss would notice the missing money, I guess..."
        play sound "page turn.mp3" volume 0.5
    elif kazuo_path == "b":
        kazuo "(coughs) I mean, uh. Well, you know–"
        play sound "page turn.mp3" volume 0.5
        MC "It was just a joke."
        play sound "page turn.mp3" volume 0.5

    kazuo "Do you ever think about what you would do if you weren’t an actress?"
    play sound "page turn.mp3" volume 0.5
    menu:
        "Sometimes. Do you?":
            $ relationship_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            pass
        "No. Why, do you?":
            $ relationship_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            pass

    kazuo "I guess I do. I’d really love to be a big star one day..."
    play sound "page turn.mp3" volume 0.5
    menu:
        "You need to fix your attitude or you’ll be in trouble.":
            play sound "page turn.mp3" volume 0.5
            $ trendiness_score += 1
            $ relationship_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

            pass
        "You never know! What would you do if you weren’t an actor?":
            $ relationship_score += 1
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            pass

    kazuo "Is it time already? I got so carried away; we barely did any rehearsing..."
    play sound "page turn.mp3" volume 0.5
    kazuo "But it was nice talking to you. I’ll see you around here, then!"
    play sound "page turn.mp3" volume 0.5
    jump CH1QTE1

label CH1QTE1:
    scene studio bg
    prod "Alright, everybody, get on set! Filming starts in five minutes!"
    play sound "page turn.mp3" volume 0.5
    direct "I expect everyone to bring their best performances today! We have no room for error, and I won’t tolerate any mistakes."
    play sound "page turn.mp3" volume 0.5
    setsuko "Well, this is my scene. After all the countless times I’ve done this, I still can’t help but feel a little nervous."
    play sound "page turn.mp3" volume 0.5

    MC "Is there anything I can do to help?"
    play sound "page turn.mp3" volume 0.5

    setsuko "I’m not sure… I’m still not used to talkies. I can never tell if I’m speaking too quiet or too loud, or if my voice is too high pitched. You don’t think my voice sounds strange, do you? You’re the expert, after all."
    play sound "page turn.mp3" volume 0.5

    jump QTE1menu
    """
    menu:
        "(ENCOURAGE) You need to project your voice! Your character will need to be heard over the background noise – the audience won’t only be hearing you.":
            play sound "page turn.mp3" volume 0.5
            $ setsuko_path = "encourage"
            $ relationship_score += 1
            $ trendiness_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "(REASSURE) You’ll be alright, don’t worry about it. You don’t want the scene to be too overwhelming.":
            play sound "page turn.mp3" volume 0.5
            $ setsuko_path = "reassure"
            $ relationship_score -= 1
            $ trendiness_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
    if setsuko_path == "encourage":
        setsuko "You’re right. It might be a bit difficult for me, but I’ll try my best!"
        play sound "page turn.mp3" volume 0.5
        direct "Action!"
        play sound "page turn.mp3" volume 0.5
        setsuko "(shouting) Darling, I made dinner an hour ago, and you still haven’t eaten yet! I work so hard for this family..."
        play sound "page turn.mp3" volume 0.5
        direct "Cut! Splendid job, Wada-san! All that noise gave me a splitting headache… which is exactly what I wanted! Good work today."
        play sound "page turn.mp3" volume 0.5
        setsuko "(bows) Thank you. I will continue to do my best."
        play sound "page turn.mp3" volume 0.5
    else:
        setsuko "Are you sure? Okay, I’ll follow your advice."
        play sound "page turn.mp3" volume 0.5
        direct "Action!"
        play sound "page turn.mp3" volume 0.5
        setsuko "(softly) Darling, I made dinner an hour ago, and you still haven’t eaten yet! I work so hard for this family..."
        play sound "page turn.mp3" volume 0.5
        direct "Cut! Wada-san, I said nagging wife, not passive wife! I could barely even hear you over the rest of the noise. We’ll have to dub over your audio in post-production."
        play sound "page turn.mp3" volume 0.5
        setsuko "(bows deeply) I apologize. I’ll try harder next time."
        play sound "page turn.mp3" volume 0.5
        direct "We don’t have any room for trying, Wada-san. You will do better."
        play sound "page turn.mp3" volume 0.5 """

label afterQTE1:
    MC "(thinking) Setsuko’s work is done, but mine is just starting. It’s time for me to prepare for my scene."
    play sound "page turn.mp3" volume 0.5

    # Transition to MC’s scene
    direct "Action!"
    play sound "page turn.mp3" volume 0.5

    menu:
        "(ACT COY) I’ll keep my expressions understated. It wouldn’t be proper to overshadow the main character – I don’t want to be too flamboyant.":
            play sound "page turn.mp3" volume 0.5
            $ mc_scene_path = "coy"
            $ trendiness_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

        "(ACT EXPRESSIVE) I’ll make my emotions very clear on my face! Even though I don’t say a lot, I can still show a lot.":
            play sound "page turn.mp3" volume 0.5
            $ mc_scene_path = "expressive"
            $ trendiness_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)


    if mc_scene_path == "coy":
        MC "(in character) Shinjiro, I… I don’t know if I can tell you how I feel…"
        play sound "page turn.mp3" volume 0.5
        direct "Very demure, MC-san… maybe not quite what I expected with your character, but I think it can work. Let’s work on getting our next scene filmed now, okay?"
        play sound "page turn.mp3" volume 0.5
        toshiro "(whispers) Gee, MC… it was hard to tell if you were even in love with me. Really sell it to me next time, alright?"
        play sound "page turn.mp3" volume 0.5
        MC "(rolls eyes)"
        play sound "page turn.mp3" volume 0.5
    else:
        MC "(in character) Shinjiro, I… I don’t know if I can tell you how I feel…"
        play sound "page turn.mp3" volume 0.5
        direct "Well done, MC-san! I almost shed a tear watching you – I’m sure the audiences will, too. I’ll ask the producer about marketing this movie with a warning about needing handkerchiefs."
        play sound "page turn.mp3" volume 0.5
        MC "You flatter me, sir. I’m just doing my job – you’re doing the real hard work."
        play sound "page turn.mp3" volume 0.5
        toshiro "(whispers) Nice one, MC… You really sold your feelings for me. Are you sure they weren’t real?"
        play sound "page turn.mp3" volume 0.5
        MC "(rolls eyes)"
        play sound "page turn.mp3" volume 0.5

    # Transition to the jazz club scene
    MC "Ugh, I really can’t stand the stink of all this smoke."
    play sound "page turn.mp3" volume 0.5
    kiyo "(exhales smoke from her cigarette) That’s too bad, MC-chan, you’ll have to get used to it soon if you want to pull this scene off."
    play sound "page turn.mp3" volume 0.5
    MC "You mean I have to smoke? I never signed up for that!"
    play sound "page turn.mp3" volume 0.5
    toshiro "(laughs) You’re such a little girl, MC-chan! But you’re not supposed to be playing that – you’re a woman now, and a rebellious one at that."
    play sound "page turn.mp3" volume 0.5

    menu:
        "(SWANKY) I need to live it up! The only way I can keep the scene going is by contributing to the lively energy.":
            play sound "page turn.mp3" volume 0.5
            $ westernization_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Green Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ dance_path = "swanky"
        "(CASUAL) I’ll lay low and keep it cool. I’m not a major character in this scene, anyway.":
            play sound "page turn.mp3" volume 0.5
            $ westernization_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Red Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ dance_path = "casual"

    if dance_path == "swanky":
        MC "(snaps fingers and sways with the beat, taking a long draw from the cigarette) (thinking) I can feel the energy of the room!"
        play sound "page turn.mp3" volume 0.5
        direct "Well done, everyone! If the music were any louder, I’m afraid the police wouldn’t be so convinced we were filming a movie!"
        play sound "page turn.mp3" volume 0.5
        direct "Wonderful performance, MC-san! I can see your training in the performing arts serves you well… although I wasn’t aware they taught that kind of dancing!"
        play sound "page turn.mp3" volume 0.5
        MC "(laughs) Thank you, sir!"
        play sound "page turn.mp3" volume 0.5
    else:
        MC "(sways subtly to the beat, keeping in the background) (thinking) I’m just part of the scenery for this one..."
        play sound "page turn.mp3" volume 0.5
        direct "I was expecting to see a little more energy from you, given your dancing background… but I’m sure your performance will suffice."
        play sound "page turn.mp3" volume 0.5
        MC "I understand, sir. I’ll try harder next time."
        play sound "page turn.mp3" volume 0.5

    jump CH1QTE2

label CH1QTE2:
    scene office bg
    prod "Your reputation is growing, MC. I’ve even heard your name on the streets and in town – you’ve attracted some dedicated fans."
    play sound "page turn.mp3" volume 0.5

    menu:
        "Oh, how wonderful! I do owe much of it to you and the studio…":
            $ prod_path = "encourage"
            $ relationship_score += 1
            $ trendiness_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "I’m finally getting some deserved recognition.":
            $ prod_path = "assertive"
            $ relationship_score -= 1
            $ trendiness_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    if prod_path == "encourage":
        prod "Don’t sell yourself short, kid. You’re special, you’ve worked hard to get here. Any other producer would be lucky to have you."
        play sound "page turn.mp3" volume 0.5
    else:
        prod "Don’t be too rash. You got very lucky. Your first role was the gift of that poor girl’s tuberculosis – otherwise you might still be singing in the background at your school."
        play sound "page turn.mp3" volume 0.5

    prod "With that being said, I’ve got something to share."
    play sound "page turn.mp3" volume 0.5
    prod "*a rustling sound* (He produces a script.)"
    play sound "page turn.mp3" volume 0.5
    prod "You’ve got another role! (He hands MC the script) This one is called…"
    play sound "page turn.mp3" volume 0.5

    python:
        movie_choices = get_two_movies_of_type("nationalism")

        movie1_title = movie_choices[0].title
        movie1_description = movie_choices[0].description
        movie1_role = movie_choices[0].role

        movie2_title = movie_choices[1].title
        movie2_description = movie_choices[1].description
        movie2_role = movie_choices[1].role

        movie1 = {
            "name": movie1_title,
            "description": movie1_description,
            "role": movie1_role,
        }

        movie2 = {
            "name": movie2_title,
            "description": movie2_description,
            "role": movie2_role,
        }

    call screen movie_role_choice(movie1, movie2)

    if chosen_movie == "movie1":
        play sound "click.mp3" volume 1.5
        "You have chosen the role in [movie1['name']]."
        $ nationalism_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Red Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    elif chosen_movie == "movie2":
        play sound "click.mp3" volume 1.5
        "You have chosen the role in [movie2['name']]."
        $ nationalism_score += 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    prod "Shooting starts next week – start looking over your lines. You’ve got some experience on your side, not to mention that handful of fans. Still, stay alert and do your best. We’re proud of you, MC. I’m proud of you."
    play sound "page turn.mp3" volume 0.5

    scene studio bg with fade

    setsuko "But sometimes I feel like they’re right. Maybe I wasn’t meant for a career like this…"
    play sound "page turn.mp3" volume 0.5
    kiyo "You’re going to give up, just like that? What’s the point of all this, then?"
    play sound "page turn.mp3" volume 0.5

    setsuko "My aunt did well on the stage…"
    play sound "page turn.mp3" volume 0.5
    kiyo "The stage? This isn’t the centennial. We’re in 1935 – it’s time for bigger things!"
    play sound "page turn.mp3" volume 0.5

    MC "Am I interrupting?"
    play sound "page turn.mp3" volume 0.5

    setsuko "MC! Not at all. I was actually hoping you’d get here soon. You see, I got this letter from my mother and I’m feeling terribly torn–"
    play sound "page turn.mp3" volume 0.5
    kiyo "She got a marriage offer from some random boy back home, and her mom wants her to abandon her whole career for him."
    play sound "page turn.mp3" volume 0.5

    setsuko "That’s not what happened!"
    play sound "page turn.mp3" volume 0.5
    kiyo "Fine, then you explain it."
    play sound "page turn.mp3" volume 0.5

    setsuko "(fiddling with her obi) It’s just that… My last movie – White Orchids in Spring – It didn’t do so well. My producer was really disappointed. He put so much on the line with this movie and if I mess up again, then it’s really over for me."
    play sound "page turn.mp3" volume 0.5
    kiyo "It’s one bad film. You’re a fine enough face, you’ll survive. Just don’t ruin this one."
    play sound "page turn.mp3" volume 0.5

    setsuko "I don’t want to end on such a sad note, though! I’d rather leave for love than… be fired."
    play sound "page turn.mp3" volume 0.5
    kiyo "Ha! Love? Do you even know this boy’s name?"
    play sound "page turn.mp3" volume 0.5
    setsuko "He’s not a boy! And yes, his name is… I don’t know how he pronounces the kanji."
    play sound "page turn.mp3" volume 0.5
    kiyo "Sure, love. [MC], you’re her friend, right? Talk some sense into her."
    play sound "page turn.mp3" volume 0.5

    menu:
        "Kiyo has a point.":
            $ relationship_score += 1
            $ trendiness_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            jump blue2
        "Marriage isn’t so bad…":
            $ relationship_score -= 1
            $ trendiness_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            jump green2
        "I don’t really know…":
            jump QTE2

    

label blue2:
    MC "Look at Tōshiro – he was in that one really awful movie with Midori, from school. You talked about it yourself. He’s still doing just fine. Didn’t he just announce a new production?"
    play sound "page turn.mp3" volume 0.5

    setsuko "But that’s different! Tōshiro’s a man. They’re allowed to mess up. Midori hasn’t been in anything since then."
    play sound "page turn.mp3" volume 0.5

    kiyo "Oh, don’t sell yourself short. Sure, men have the advantage here, but it’s not like that Morioka girl was going to do well, anyway."
    play sound "page turn.mp3" volume 0.5

    setsuko "What are you talking about? She was one of the best in our school!"
    play sound "page turn.mp3" volume 0.5

    kiyo "Mhm, and where is she now?"
    play sound "page turn.mp3" volume 0.5

    setsuko "I’m… not sure."
    play sound "page turn.mp3" volume 0.5

    kiyo "School is just a starting point, Setsuko. You can do all the right things, pass all your tests and sing your little ditties, but no amount of fancy kimonos and matsuri dances will move you forward if you aren’t moving forward."
    play sound "page turn.mp3" volume 0.5

    setsuko "Moving forward?"
    play sound "page turn.mp3" volume 0.5

    kiyo "Changing with the times. Like that dainty schoolgirl act you put on around the director – it’s cute, but it’s so average."
    play sound "page turn.mp3" volume 0.5

    setsuko "What’s wrong with being polite?"
    play sound "page turn.mp3" volume 0.5

    kiyo "Nothing! Ugh, MC, you’ve clearly got a handle on this. Give an example."
    play sound "page turn.mp3" volume 0.5

    menu:
        "You could try changing the way you dress? Looking into those new Western styles?":
            $ example_choice = "dress"
            $ westernization_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Green Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

        "You should be bolder, like one of those modern girls on magazine covers!":
            $ example_choice = "dress"
            $ trendiness_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            $ example_choice = "bold"

    if example_choice == "dress":
        setsuko "How I dress?"
        play sound "page turn.mp3" volume 0.5
        kiyo "Yes, finally someone said it! You’re pretty, but you have that standard kind of pretty. It makes you perfect for those friend roles, and eventually you might start being cast as the shopkeeper or the teacher—but who wants that? If you start to dress like a star, your team might actually start to see you like a star."
        play sound "page turn.mp3" volume 0.5
        setsuko "What do stars dress like?"
        play sound "page turn.mp3" volume 0.5
        kiyo "Look around you! See all those posters? Global stars like Pickford, Hepburn… Follow the trends and watch the scripts come pouring in!"
        play sound "page turn.mp3" volume 0.5
    else:
        setsuko "I don’t want to offend anyone."
        play sound "page turn.mp3" volume 0.5
        kiyo "I’m not telling you to go and flash a thigh or anything! There’s a line between audacious and intriguing. No one wants to see a little wife holed up and taking orders from her man anymore. We want women who are exciting, inspiring, maybe a little naughty when no one’s looking. (she nudges Setsuko) Enough to make your boy back home blush, but not shame your mother and father."
        play sound "page turn.mp3" volume 0.5

    MC "It’s at least worth a try, isn’t it?"
    play sound "page turn.mp3" volume 0.5

    setsuko "I’m just scared… What if my career ends here?"
    play sound "page turn.mp3" volume 0.5

    kiyo "What if, what if! Such a ridiculous thing to be worried about – “what if”. Stop trying to predict the future and just live in the now, girl. Don’t be a coward."
    play sound "page turn.mp3" volume 0.5

    menu:
        "This is your dream, isn’t it?":
            play sound "page turn.mp3" volume 0.5
            $ push_forward = "dream"
        "Don’t accept failure.":
            play sound "page turn.mp3" volume 0.5
            $ push_forward = "failure"
    $ relationship_score += 1
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
    python:
        p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
        relationship_bar = what_relationship_bar_to_use(relationship_score)
    play sound "page turn.mp3" volume 0.5
    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
    play sound "page turn.mp3" volume 0.5

    setsuko "Yes… You’re right. I just have to keep pushing forward! Thank you, girls. *she clearly wants to go in for a hug but stops herself*"
    play sound "page turn.mp3" volume 0.5

    menu:
        "(Hug her)":
            $ hug_setsuko = True
            $ relationship_score += 1
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations", trendiness_score, westernization_score, nationalism_score)
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            play sound "page turn.mp3" volume 0.5
            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
            play sound "page turn.mp3" volume 0.5
        "(Don’t hug her)":
            play sound "page turn.mp3" volume 0.5
            $ hug_setsuko = False

    if hug_setsuko:
        "*Kiyo embraces Setsuko and gives her a kiss on the cheek. From offscreen, a producer calls everyone to set.*"
        play sound "page turn.mp3" volume 0.5
        kiyo "Well, let’s go show them what these three women are made of."
        play sound "page turn.mp3" volume 0.5
    else:
        "(From offscreen, a producer calls everyone to set.)"
        play sound "page turn.mp3" volume 0.5
        kiyo "Well, let’s go show them what these three women are made of."
        play sound "page turn.mp3" volume 0.5

    jump QTE2

label green2:
    scene studio bg
    kiyo "“Not so bad” – how inspirational."

    setsuko "Do you hate marriage, Kiyo?"

    kiyo "Of course not! I’d love to have a handsome man on my arm and a sweet little boy to dress up and show off – oh it would drive my sisters mad! But I’m my own person first. I’m not tossing away an opportunity for the first man who asks."

    setsuko "He’s not the first…"

    kiyo "Even better, then! You’ve got options. Make them wait, focus on your career."

    setsuko "But why would they want me once I fail? No one would want to marry an actress who couldn’t make it…"

    kiyo "There you go again – “I’m going to fail, I’m going to fail.” Stop saying such self-effacing nonsense!"

    setsuko "But I’m not what they want, am I?"

    kiyo "Not right now, certainly. But you can fix that."

    menu:
        "I think Setsuko is fine as she is.":
            $ setsuko_advice = "fine"
        "I don’t think it’s something to be fixed.":
            $ setsuko_advice = "fix"

    kiyo "Really? Then tell me, MC, what do you think she should do?"

    MC "Write your mother back…"
    menu:
        "At least meet with this man – maybe he’s nice?":
            $ mother_advice = "meet"
        "Keep being as you are. You got this role, after all.":
            $ mother_advice = "stay"

    if mother_advice == "meet":
        kiyo "I’m sure he’s lovely. But after all this, you’ll just settle down? Just give up?"
        setsuko "How is marriage giving up?"
        kiyo "You can’t be a wife and a growing star. You need to be desirable, not some kind of role model."
    else:
        kiyo "And “this role” is just a bit part. It’s a step down from the last."
        setsuko "That’s why I’m considering just stopping here!"
        kiyo "And you truly think that’ll make you happy?"
        setsuko "Maybe. Not everyone can strike out on their first try, like you."
        kiyo "Are you suggesting it was just luck for me?"
        setsuko "Of course not!"

        kiyo "I’m not just some rich girl who happened to be nearby when some director had a last minute casting call. I didn’t get here by chance. I had to work for this. And you? You have talent, but that’s all!"

        setsuko "If I have talent, then why am I not getting cast?"

        kiyo "Because you don’t do your research. You play the same girl at home, on screen, in front of the producers – sweet Setsuko with her perfect kimono and gentle voice. Always lets the men speak first, always bows her head… You’re what everyone wants in a bride in the countryside, maybe, but this is the city. This is the silver screen."

    kiyo "(Kiyo looks between MC and Setsuko. A manager comes by.)"

    manager "Kiyo, the director would like to go over the last scene."

    kiyo "Of course." 
    kiyo "(she turns back to Setsuko, briefly) If you keep playing yourself down, you’ll end up in the same situation as that White Orchid business. Except next time, I won’t be helping you."

    menu:
        "What happened with your last film?":
            $ setsuko_last_film = "ask"
        "(stay quiet, let Setsuko be – she’s had enough)":
            $ setsuko_last_film = "quiet"

    if setsuko_last_film == "ask":
        setsuko "The reviews were just… so mean."
        MC "How so?"
        setsuko "They called me plain. Nothing to offer, seen it a million times already. I guess… it’s just like Kiyo was saying. There are hundreds of girls just like me. My screen partner was so angry. He told my team he would never work with me again. I’d never seen my producer look so disappointed. When he called me into his office to give me this role, I really thought he was going to fire me."
        MC "And that’s why you were considering quitting?"
        setsuko "Yes. Especially after my mother’s letter came in. Maybe I’m not the type who can keep Japan interested, right now. I’m too traditional, too ‘perfect.’"
        MC "(laughs) “Too perfect”?"
        setsuko "(flushes) You know what I mean! I’ll never be like you, or like Kiyo. And if that’s not what the studios want, then what more can I do? I don’t know if I can take any more critiques like that…"
        MC "I understand. But at least stay for this movie, okay? I need my best friend."
        setsuko "(Setsuko nods, her eyes a little watery.)"
        setsuko "Oh no, now they’re going to yell at me for smudging my makeup. I’d better go clean up. (she pauses) Thank you, MC. You’ve given me a little hope."
    else:
        setsuko "Well, I’d better go clean up, I suppose. If it’s my last role, I want to look my best, right?" 
        setsuko "(she smiles, but there’s no joy in it) I’ll see you on set, MC."

    jump QTE2
label QTE2:

    MC "(thinking) I can’t believe I’m the lead actress in this movie! There’s no room for error – my reputation could be on the line if I don’t perform well."

    toshiro "(Tōshiro approaches from behind and places his hand on MC’s shoulder. MC jumps.)"

    toshiro "Relax, MC-chan, it’s just me."

    MC "That isn’t very proper of you, Watanabe-san."

    toshiro "I know, I know… but we’re playing fiances in this movie, so maybe it’s alright."

    "([mcName] gently takes his hand off her shoulder.)"

    MC "I’d prefer if you got into character another way, thank you very much – besides, we need to get ready to film."

    toshiro "As you wish… (whispers) feisty, I like it."

    "([mcName] rolls her eyes as Tōshiro leaves.)"

    MC "(thinking) The nerve of that man…"

    "([mcName] straightens out her clothes, a chic French dress from a high-end department store – no doubt a dress Kiyo would envy. It feels foreign, in every sense of the word, but the delicate fabric fills MC with a sense of excitement. She is a star, and she looks like one.)"

    prod "I expect big things from you today, MC-san. I know you won’t disappoint me."

    MC "Thank you, sir, I won’t."

    "([mcName] and the other actors go to their positions on set.)"

    direct "Action!"

    "([mcName]'s character stands alone on the side of the road. In this brief scene, she is meant to call over a car by herself."

    MC "(thinking) I know I’m playing a modern girl, and I need to be bold… but I can’t be too bold. What should I do? Maybe…"

    menu:
        "(MIMIC) I’ll mimic what I saw a character do in a Western movie – audiences will love that!":
            $ mc_choice = "mimic"
        "(REFERENCE) I’ll reference what I saw a character do in a Western movie, but I won’t copy it exactly.":
            $ mc_choice = "reference"

    if mc_choice == "mimic":
        "([mcName] stands with her thumb out in a hitchhiker’s gesture. Then, she stretches out her leg and raises the hem of her skirt over her calf. The director raises an eyebrow. Filming ceases.)"

        direct "Cut!"

        prod "MC-san, please speak with me."

        MC "Is everything alright, sir?"

        prod "That was very Hollywood, MC… you clearly know your stuff. However, we aren’t making that kind of movie – we don’t want our audience to get the wrong idea. Too much skin might attract the wrong kind of attention!"

        MC "I understand."

        direct "Alright everyone, from the top! Get back in your places…"

    elif mc_choice == "reference":
        "([mcName] stands with her thumb out in a hitchhiker’s gesture, looking forward with a confident look in her eyes. The director looks satisfied. Filming ceases.)"

        direct "Cut!"

        prod "Good job, MC-san – very forward, but not too scandalous. Our audience might not be able to handle anything too bold, if you get what I mean."

        MC "I understand. Thank you, sir."

    jump CH1ToshiroTransition

label CH1ToshiroTransition:
    toshiro "Excited for our scene together?"

    MC "(crosses her arms) Shouldn’t we be rehearsing? Besides, it’s not like this will be our first time on screen together."

    toshiro "Just trying to diffuse the tension… (peers over at the script) So, we’re just walking in this scene? Sounds easy enough."

    MC "(thinking) There’s a lot more nuance than meets the eye, depending on how you play it… Now, what should I do?"

    menu:
        "(BE BOLD) I’ll walk in front of him – we may be fiances, but our characters view each other as equals.":
            $ mc_walk_choice = "bold"
        "(BE RESPECTFUL) He is a man, and I am playing his fiancee, so I should walk behind him. That’s the proper thing to do.":
            $ mc_walk_choice = "respectful"

    if mc_walk_choice == "bold":
        "(The actors go to their places.)"

        direct "Action!"

        "(MC’s and Tōshiro’s characters walk forward together, and MC visibly moves to walk in front of him. The director looks surprised, yet pleased. Filming ceases.)"

        direct "Cut!"

        toshiro "That was certainly something, MC-chan."

        MC "I think it fits with the tone of the movie – I’m sure the women watching the movie will feel the same."

        toshiro "Well, if you say so…"

    elif mc_walk_choice == "respectful":
        "(The actors go to their places.)"

        direct "Action!"

        "(MC’s and Tōshiro’s characters walk forward together, but MC waits a few steps to walk behind him. The director looks neutral. Filming ceases.)"

        direct "Cut!"

        toshiro "See? Not hard at all."

        MC "Maybe that was a little too old fashioned… I’m not sure that fits with the tone of the movie."

        toshiro "It’ll be fine, don’t worry. You just did what everyone expects you to do – no one will think anything of it."

    jump oldscene

label oldscene:
    MC "I hope you don’t find the dialogue in this scene too disrespectful!"

    older_actress "Nonsense, dear! It’s only a script – acting is our job, after all."

    older_actor "Besides, I find it quite interesting! It’s not like we could talk like this to our parents when we were young… (chuckles) I have to admit I’m a little jealous."

    prod "Remember, [mcName]-san, we want this scene to shock the viewers… but it can’t be too shocking, alright?"

    MC "I’ll keep that in mind."

    "(The actors move to their places.)"

    direct "Action!"

    MC "(thinking) Now, what should I do? How about…"

    menu:
        "(BE OUTSPOKEN) Even though my character is estranged from her parents, she’ll still act respectful… but she needs to speak her mind.":
            $ mc_dialogue_choice = "outspoken"
        "(BE AGGRESSIVE) My character has no reservations about speaking her mind – if she doesn’t like her parents, she needs to show it!":
            $ mc_dialogue_choice = "aggressive"

    if mc_dialogue_choice == "outspoken":
        MC "(calmly) Father, I know you care about me… but this is my life, not yours. I’ll make you proud if you give me the opportunity to – I’m old enough to make my own decisions."

        older_actor "Kimiko-san…"

        "(MC’s “mother” and “father” embrace sadly, and MC turns away from them with a regretful but poised look. The director looks pleased. Filming ceases.)"

        direct "Cut!"

        MC "How did I do?"

        older_actor "I started to tear up a bit… I couldn’t help but imagine my daughter saying the same thing."

        older_actress "You have a very powerful presence, dear."

        MC "(bows) Thank you."

    elif mc_dialogue_choice == "aggressive":
        MC "(angrily) You have no place to tell me who I should love, father! You were never there for me when I was a child! I shouldn’t even call you my father…"

        older_actor "Kimiko-san…"

        "(MC’s “mother” and “father” embrace sadly, and MC turns away from them bitterly. The director looks neutral. Filming ceases.)"

        direct "Cut!"

        MC "How did I do?"

        older_actor "I was worried for a moment… I thought you really were mad at me!"

        older_actress "You have a very… strong presence."

        MC "Oh…"

    jump producer_scene

label producer_scene:
    prod "You’ve done quite well in your last few films. I truly think you’re on your way to something great, MC. You should be very proud."

    menu:
        "(How much longer until I’m on one of those fancy magazine covers?)":
            $ mc_response = "magazine"
        "(Oh, you flatter me too much. Though I do hope good things are coming…!)":
            $ mc_response = "humble"

    if mc_response == "magazine":
        prod "Keep up the good work and keep your manners in check, and we’ll see. For now, you’ve got a new role to nail."
    elif mc_response == "humble":
        prod "I wouldn’t say it if you didn’t deserve it. And I’m not the only one who has faith in you…"

    prod "Brand new script, fresh off the press and written just for you."

    "(a rustling sound. He produces a script.)"

    prod "Congratulations, again." 
    prod "(He hands MC the script) This one is called…"

    menu:
        "(Bucket Movie A)":
            $ chosen_movie = "A"
        "(Bucket Movie B)":
            $ chosen_movie = "B"

    prod "Stay sharp, MC. This director’s a tough one to please. You’ve got the talent, just make sure you watch the atmosphere. Things have been a little more lively lately. Don’t let anything slip past you, okay?"

    "(Scene changes to set.)"

    MC "I should go check in on the others..."
    jump talktuah

label talktuah:
    menu:
        "Talk to Kazuo":
            jump kazuo_conversation
        "Talk to Tōshiro":
            jump toshiro_conversation
        "Talk to Setsuko":
            jump setsuko_conversation
        "Talk to Kiyo":
            jump kiyo_conversation
        "Don’t talk to anyone":
            jump skip_conversation

label kazuo_conversation:
    kazuo "MC! It’s nice to see you. How are things?"

    menu:
        "(I didn’t think we’d end up seeing each other again. But I’m well.)":
            $ mc_kazuo_greeting = "again"
        "(It has been a while, hasn’t it? I’m doing nicely.)":
            $ mc_kazuo_greeting = "while"

    if mc_kazuo_greeting == "again":
        MC "I didn’t think we’d end up seeing each other again. But I’m well."
        kazuo "Oh, uh… I guess you’ve been getting much better roles than me. My sister was all giddy after your last film – I think she wrote me two whole pages on it."
        MC "That’s so sweet!"
        kazuo "She always loves those stories about girls marching out on their own."
    elif mc_kazuo_greeting == "while":
        MC "It has been a while, hasn’t it? I’m doing nicely."
        kazuo "I’m glad to hear that. I wish I could say the same, ha!"
        MC "What’s going on?"

    "(Kazuo shifts from foot to foot, looking around the studio.)"

    kazuo "I’ve been thinking… maybe I should take some time off, get an office job or something."

    menu:
        "(Really? Why?)":
            $ mc_kazuo_office_question = "why"
        "(Business is that bad?)":
            $ mc_kazuo_office_question = "business"

    kazuo "Things haven’t been bad, but they have been a little um… stagnant. Directors seem to be moving away from the kind of films that need a guy like me."

    MC "A guy like you?"

    kazuo "You know… Sorta…"

    menu:
        "(Boring?)":
            $ mc_kazuo_type = "boring"
        "(Nice?)":
            $ mc_kazuo_type = "nice"

    kazuo "Yeah. That’s putting it simply, I guess. (he grimaces) They need someone more domineering, you know? Someone who really puts out that go-getter, leader air. Like Tōshiro! He’s been really on the rise lately, not that he was ever not popular but… He makes all us guys look plainstandard when he’s on screen. Kinda like you, with the ladies."

    MC "Every hero needs a friend, don’t they?"

    kazuo "(laughs) I suppose. But even then, I’m more of a comic relief."

    MC "People need to laugh."

    kazuo "Do they…? The movies have all seemed so serious. Lately, it just seems humor isn’t what the people want."

    MC "Do you know what they want?"

    kazuo "I wish I did. But I’m thinking that it’s not me. I might be better off behind a desk – something in the government, maybe. There seem to be a lot of new positions opening up. I just want to do something to prove I’m a little useful…"

    MC "What about the army?"

    kazuo "Ha! I don’t know if I’m quite that brave. I probably wouldn’t last a week."

    "(He pauses, then looks around.)"

    kazuo "Do you read the global news, much?"

    menu:
        "(Of course, I need to know what’s happening.)":
            $ mc_global_news = "yes"
        "(I’d much rather read Osaka Shimbun.)":
            $ mc_global_news = "local"

    if mc_global_news == "yes":
        kazuo "Then, have you heard about what’s going on in Manchuria? I don’t know a lot, but the whole thing seems–"
    elif mc_global_news == "local":
        kazuo "Well, there’s this thing happening in China. They don’t say a lot about it, but–"

    "(A production manager enters.)"

    manager "Hello, Tachibana Kazuo, the director wanted a word about your entrance. Please be courteous, he’s a bit on edge today."

    kazuo "Of course. I’ll be right there! Well, MC, let’s give it our best. At least one more hurrah, right?"

    jump talktuah

label toshiro_conversation:
    toshiro "Well, if it isn’t the little starlet herself. How’re you, MC?"

    menu:
        "(Fine. Busy.)":
            $ mc_tosh_response = "busy"
        "(A lot better with the current company.)":
            $ mc_tosh_response = "flirty"

    if mc_tosh_response == "busy":
        MC "Fine. Busy."
        toshiro "But you still find time for me. How sweet."
        MC "…"
        toshiro "No need to be so icy. I’m just making conversation, aren’t I? I swear, women seem to be getting more and more defensive these days. Can’t a guy just chat with a pretty lady?"
        MC "What do you want to talk about, then?"

    elif mc_tosh_response == "flirty":
        MC "A lot better with the current company."
        toshiro "I’m glad the feeling is mutual." 
        toshiro "(he winks) If we keep getting cast together, maybe we’ll finally get one of those romances."
        MC "Pardon?"
        toshiro "All on screen, of course. The audience loves a charming duo, don’t they? And we seem to play off each other well, don’t we?"
        MC "Did you rehearse any of your character’s lines, or just these?"

    toshiro "And she stays feisty! You’re lucky men are still going for that. You know, I was so worried a few years ago when all those films about jazz singers and single ladies were coming out – loved to watch them, but movies are just a fantasy, aren’t they?"

    "(He leans against the wall, crossing his arms.)"

    toshiro "The problem was when girls started trying to imitate it. The country doesn’t run on dresses and makeup. I’m glad things are moving back in the right direction."

    MC "The right direction?"

    toshiro "Men acting like men, Japan acting like Japan. Wear whatever you want, I think western ladies look great – you seen that Mary Pickford? Fantastic – but leave that on the screen. My next film after this is a soldier movie. Isn’t that the best?"

    menu:
        "(But won’t that be violent?)":
            $ mc_tosh_soldier_movie = "violent"
        "(That’s so admirable!)":
            $ mc_tosh_soldier_movie = "admirable"

    if mc_tosh_soldier_movie == "violent":
        MC "But won’t that be violent?"
        toshiro "Violence, no. Wouldn’t want to scar up a nice face, would I? But the idea behind it – war, victory, the glory of the nation. People don’t pay us enough attention because they think we’re some small island country. But we’re on the rise, and I wanna show that."
        MC "By being in a movie…?"
        toshiro "What, would you rather I go to war?"
        MC "It would be braver."
        toshiro "(clicks his tongue) There’s a difference between the kind of man who goes to the battlefield and the kind of man who unites his nation. No one needs a national symbol of some boring, faceless kid covered in soot. They need a reminder of what true, Japanese masculinity looks like. That’s how I’m serving my country."

        menu:
            "(Wow, what a hero…)":
                $ mc_tosh_hero_react = "wow"
            "(We’re lucky to have you.)":
                $ mc_tosh_hero_react = "lucky"

        toshiro "Course, if I’m called to battle, I’ll serve. But it’d be a waste. Just like sitting me behind some desk – can you imagine that? What a sad life."

    elif mc_tosh_soldier_movie == "admirable":
        MC "That’s so admirable!"
        toshiro "We are, aren’t we? We don’t need to keep churning out those silly movies with people tripping over their feet or going stupid for a pretty pair of eyes. We need something with substance."
        MC "Do you feel like this will be enough?"
        toshiro "Course not. This is just a starting point. But you can already feel it in the streets, can’t you? The whole city is buzzing. People want to rally for something."

        "(He leans back, running a hand through his hair.)"

    toshiro "Y’know, rumor has it that there’s a new international studio opening up. Maybe something in China, or Hong Kong."

    MC "Really?"

    toshiro "Yup. And any studio worth their weight will be looking for some rising talent to pull. I’m thinking I might try and go outta the country, finally get something good on those poor people’s screens."

    "(He looks MC up and down, then leans in.)"

    toshiro "Think you’d join me?"

    MC "I–"

    "(From offscreen, the director starts shouting.)"

    direct "Where is my leading man? This isn’t some kind of playground, get over here!"

    toshiro "Always interrupting. Anyway, think on it, yeah?"

    "(He exits.)"

    MC "(internal) An international stage… What would that look like?"

    jump talktuah


label setsuko_conversation:
    setsuko "MC! Oh, thank goodness, a friendly face." 
    setsuko "(she gives MC a kiss on the cheek) How are you? It’s been too long since we’ve met!"

    menu:
        "(I’ve been well! But what about you?)":
            $ mc_setsuko_greeting = "well"
        "(It’s been so much work lately – the roles just don’t stop!)":
            $ mc_setsuko_greeting = "busy"

    if mc_setsuko_greeting == "well":
        MC "I’ve been well! But what about you?"
        setsuko "(her face falls for a moment, only to be replaced with an even wider smile) That’s wonderful! As for me, I’ve been on a bit of a break, I suppose. Everything at the studio seemed a little slow, so I was given some time to go visit family."
        MC "That sounds nice."
        setsuko "It is! Though I do miss acting whenever I’m gone. I know I’m not supposed to want so much attention but… a little can’t hurt!" 
        setsuko "(she giggles) Even if my parents disagree!"
        MC "You’re your own person, you’re allowed to have some fun."
        setsuko "But not too much~"
        MC "Of course not. We still have an appearance to keep!" 
        MC "(she also laughs)"

    elif mc_setsuko_greeting == "busy":
        MC "It’s been so much work lately – the roles just don’t stop!"
        setsuko "I’m so happy for you. I do wish I could say the same for myself."
        MC "What do you mean?"
        setsuko "Nothing bad! Work has just been a little slow lately, you know how these things come in waves. Sometimes you’re the title character, sometimes you’re just the singer in the background." 
        setsuko "(she sighs) Though I haven’t been a main in so long…"

        menu:
            "(It’s not for everyone.)":
                $ mc_setsuko_reassurance = "realist"
            "(Your time will come!)":
                $ mc_setsuko_reassurance = "optimist"

        if mc_setsuko_reassurance == "realist":
            MC "It’s not for everyone."
        else:
            MC "Your time will come!"
        
        setsuko "You’re right. I just need to be patient and grateful for what I have. At least, that’s what my parents have been saying. They don’t even want me to have this much time on screen! They always preferred the stage – so much more ‘dignified.’ But I just think movies are so fun. And they mean we get to spend more time together!"
        MC "What a lovely gift that is."

    setsuko "Do you want to hear something interesting?"

    MC "What?"

    setsuko "I’ve heard from the other girls at home that the whole ‘western girl’ thing is starting to go out of fashion. Directors have been looking for more wholesome, Japanese girls lately. Do you think that might mean…"

    menu:
        "(I wouldn’t get my hopes up.)":
            $ mc_setsuko_future = "caution"
        "(This might be your moment!)":
            $ mc_setsuko_future = "hope"

    if mc_setsuko_future == "caution":
        MC "I wouldn’t get my hopes up."
        setsuko "You’re right… I was getting ahead of myself. Everything is moving forward, not backward." 
        setsuko "(she sighs) I hope there’s still a spot for me in that new world."
        MC "There will always be period films."
        setsuko "And uptight mothers to play! I’ve got the best model for that role."
        MC "Do you think you’ll continue acting?"
        setsuko "Maybe. If the work ever picks up again, I’d like to. As much as the idea of marriage sounded nice a few years ago, I think I’d miss this too much."

    elif mc_setsuko_future == "hope":
        MC "This might be your moment!"
        setsuko "Wouldn’t that just be wonderful?"
        MC "I hope I won’t be excluded from that new genre."
        setsuko "Don’t be ridiculous! You’re so versatile – you can play anyone. You’re not like me, all stuck in the same typecast. But please, if the tides do change, save some of the good roles for me!"
        MC "Always. You’ve been my favorite partner from the start."
        setsuko "Oh, MC! I just hope this isn’t all my own fantasy. I know that I’m just a small actress, but I just don’t want to go back to my old life."
        MC "Then don’t!"

    setsuko "Everything just seems to change so quickly. The trends, the atmosphere… You’ve felt it too, right? There’s a strange sort of buzz in the air. I don’t know if it’s excitement or anxiety but I can feel my skin prickling at every little bit of gossip!"

    "(From offscreen, the director starts shouting. A production manager enters.)"

    manager "Wada Setsuko, the director would like to see you. He’s quite touchy, so please be patient with him."

    setsuko "I guess that’s enough chit-chat for now. But I have so much to tell you, MC! We must keep in touch – I want to see you more often than on these sets!"

    MC "We both have to work hard, then."

    setsuko "Well, I’m not worried about this one, at least. You’re my good luck charm. Whenever you’re with me in a film, it’s a hit!"

    jump talktuah


label kiyo_conversation:
    kiyo "[mcName]! How have you been, darling?"

    menu:
        "(The best I’ve ever been!)":
            $ mc_kiyo_greeting = "best"
        "(I’ve been doing alright. And you?)":
            $ mc_kiyo_greeting = "alright"

    if mc_kiyo_greeting == "best":
        MC "The best I’ve ever been!"
        kiyo "That much is clear. You’ve got that ‘ingenue’ glow about you. I remember when I first caught that color – it’s like honey to flies. The roles start pouring in. How have you been adjusting to the attention?"
    elif mc_kiyo_greeting == "alright":
        MC "I’ve been doing alright. And you?"
        kiyo "Now that’s the kind of answer I’d expect from someone like Setsuko, not a breakout star like yourself! Don’t think I haven’t been following your films. You are simply candy to the eyes of any director right now."

    MC "It’s all been a bit overwhelming…"
    menu:
        "(But quite honestly, I love it.)":
            $ mc_kiyo_overwhelm = "love"
        "(Sometimes I wonder if I’ll be able to handle it.)":
            $ mc_kiyo_overwhelm = "doubt"

    if mc_kiyo_overwhelm == "love":
        kiyo "Isn’t it just wonderful? Parents make such a fuss about all the publicity and the contracts and this and that, but to have your name appear on those big, beautiful posters – well, I can’t imagine a greater pleasure."
    elif mc_kiyo_overwhelm == "doubt":
        kiyo "Darling, we all doubt ourselves."
        MC "Even you?"
        kiyo "(laughs) Of course! You don’t think my knees were shaking the first time I stepped in front of a camera? I couldn’t eat the whole morning, I was so scared I’d be sick right there on set. But you get used to it. You learn to love it. I’m certain you’ve already started to feel it."

    MC "How do you handle it all?"

    kiyo "Handle what? The pressure, the parents?"

    menu:
        "(The pressure.)":
            $ mc_kiyo_handle = "pressure"
        "(The parents.)":
            $ mc_kiyo_handle = "parents"

    if mc_kiyo_handle == "pressure":
        kiyo "Pressure creates diamonds, MC. Taking the easy, soft route will never reward you in the same way as a well-fought journey."
        MC "I don’t know if I’m the fighting type."
        kiyo "(rolls her eyes) I don’t mean the mindless muscle and showy brawls. I mean the intellectual fights. The ones you have quietly with the directors and the producers, where you barter for your image. A little extra bat of the eye, an extra tear for the close-up – making yourself alluring, absolutely impossible to ignore."
        MC "But how does that make the pressure any lighter?"
        kiyo "Because once you’ve got them wrapped around your finger, they’ll make it all work for you. The best movies are written with you in mind, the best roles saved and the best cast members reserved to play alongside you. It’s momentum. Their attention follows you, lifts you. It feeds you. You’ll never be stuck as long as you can keep everyone watching."
        MC "How do you do that?"
        kiyo "Just never stop. No matter what anyone says, just keep fighting with every bit of your pride until you get what you deserve."
    elif mc_kiyo_handle == "parents":
        kiyo "Why should you care what they have to say?"
        MC "They raised me, they’re wiser and older and–"
        kiyo "And they’ve never stood where you’re standing, have they? Our parents, bless them for all they’ve done, have only seen one way of living. They’re stuck in the past, on the empire and facelessness and duty. They never even tried to see themselves as something greater. But you, MC, are greater."
        MC "Are you sure?"
        kiyo "Certain. If I had simply walked the easiest path – I hardly had a shortage of suitors, you know – I could be comfortably living in some nice Tokyo home with a husband and a child and be bored to death. Frankly, I would wish I was dead! Maybe some women can stand that life, but I couldn’t."

    MC "And you never regret it?"

    kiyo "What’s there to regret? A lost lover? My love is for the screen. I don’t need one romance or one lifestyle when I can have them all. Call me greedy, gluttonous, whatever you’d like, but I am living this life for the satisfaction of myself."

    MC "But what if I can’t have them all?"

    kiyo "You wait. You’ll learn to adapt, be versatile. You won’t always have the power, but when you do, you build yourself a palace. Decorate it however you like and wait in there whenever the people get fussy. Then present yourself once again, and capture their hearts. It’s been working for me."

    menu:
        "(Your new films have been… different.)":
            $ mc_kiyo_opinion = "different"
        "(What if I want to do something different?)":
            $ mc_kiyo_opinion = "new"

    if mc_kiyo_opinion == "different":
        MC "Your new films have been… different."
        kiyo "I’ve always loved the avant-garde. And there’s always going to be a craving for something new. But I wouldn’t risk it if I didn’t know that my career is stronger than a single failure. I’ve built reputation. That’s why I can do whatever I’d like."
    elif mc_kiyo_opinion == "new":
        MC "What if I want to do something different?"
        kiyo "Then make sure you have the charm to keep pulling in that audience. You’re a star in your movies, of course. But can you be a star in all movies? Build a reputation so strong, so impenetrable that a wave of critics could never sway your fans."

    "(A manager enters.)"

    manager "Yamaguchi Kiyo, you’re wanted on set. The director–"

    kiyo "Is such an uptight fellow. Don’t worry, I won’t ruffle any feathers." 
    kiyo "(she turns back to MC) You are special. Make sure that everyone knows it."

    jump talktuah

label skip_conversation:
    "(MC decides not to talk to anyone and moves on to the next part of the scene.)"
    jump CH1QTE3

label CH1QTE3:
    setsuko "I’m excited to be in a film with you, MC-chan! We always work so well together."

    MC "I feel the same way! We get to be sisters in this film, too – it’ll be just like real life, almost."

    setsuko "(laughs) Almost! Let’s go over our lines one more time before the filming starts…"

    "(Some time passes. The producer walks over.)"

    prod "Alright, ladies, I hope you two have your lines memorized."

    setsuko "I think so…"

    MC "(gently nudges her) We’ll do great, don’t worry. We’re ready to film now, sir."

    prod "That’s the spirit. Places, everyone!"

    direct "Action!"

    setsuko "(in character) Little sister, you mustn't act this way. It’s not proper for geisha like ourselves to be disloyal to our patrons. I think… well…"

    MC "(thinking) Oh no, she’s forgotten the rest of her lines! I should…"

    menu:
        "(IGNORE) I’ll let her figure it out on her own. Besides, we can just reshoot if she messes up.":
            $ mc_help_choice = "ignore"
        "(HELP) I know it isn’t in the script, but maybe I can improvise to jog her memory!":
            $ mc_help_choice = "help"

    if mc_help_choice == "ignore":
        setsuko "(wincing) What was my line again?"

        direct "(sighs) Cut!"

        prod "“I may be a rule follower, but that keeps me alive. It would do you some good to be one, too.”"

        setsuko "Ohhh, that’s right. Thank you, sir."

        direct "We’ll need to reshoot – let’s take this scene from the top. Don’t let her forget her lines, MC-san."

        MC "I won’t."

        "(Setsuko is visibly embarrassed, and MC feels a pang of guilt.)"

    elif mc_help_choice == "help":
        MC "You’re the old-fashioned one, elder sister, always following the rules."

        setsuko "You’re right – I may be a rule follower, but that keeps me alive. It would do you some good to be one, too."

        MC "Well, the rules are changing. I don’t want the past to hold me back from my future."

        "(Filming ceases. The director looks pleased.)"

        prod "That wasn’t in the script, but I have to say, that was a good save! I think I prefer it to the original line."

        MC "Thank you, sir, I was just looking out for my co-star."

        setsuko "(smiles) I can always count on you, MC-san."
    jump QTE3

label QTE3:
    male_actor "Normally I’m not one to play a bumbling fool, but I think the audience will appreciate the humor of this scene."

    MC "I agree. I’ve done a few roles like this before, but I’m still not quite used to playing the 'femme fatale'... I hope I don’t get typecast!"

    male_actor "I’m sure you won’t be, don’t worry about it."

    prod "Speaking of femme fatale, we’ll need a lot of that in this scene – but not too much, you know the drill. Alright, places, everyone!"

    direct "Action!"

    "(Filming begins, and the male actor’s character enters the scene.)"

    male_actor "Momo-chan, I’m here!"

    MC "(thinking) How should I play this scene?"

    menu:
        "(BE SWEET) I’ll act similarly to Setsuko’s character. She’s my sister, and I’m doing a favor for her in this scene.":
            $ femme_fatale = "sweet"
        "(BE MANIPULATIVE) I’ll do what I can to get what I want – for my character, that is.":
            $ femme_fatale = "manipulative"

    if femme_fatale == "sweet":
        MC "Hayakawa-kun, I’m so happy to see you! I hope you don’t mind if I ask for a favor…"

        male_actor "What is it, dearest?"

        MC "Well, times have been rough for my sister and I, but she is in need of a new kimono… Even though your prices are high, you’re the only merchant I trust to provide something fitting my sister. Oh, I’m so embarrassed, but will you please help me?"

        male_actor "I don’t know… I need to meet my company’s quota…"

        MC "It’ll only be this once! I’ll never ask for anything from you again, I promise."

        male_actor "Well, if you say so… Fine, just this once."

        MC "Oh, Hayakawa-kun, thank you so much!"

        "(Filming ceases. The director looks content.)"

        direct "Cut!"

        prod "MC-san, I can sense the manipulation, but you’re far too sweet – that’s more fitting of Setsuko’s character."

        MC "Should we reshoot?"

        prod "We don’t have the time for that, I’m afraid, this take will have to do."

    elif femme_fatale == "manipulative":
        MC "Oh, you’re finally here… I was worried you had abandoned me."

        male_actor "Never, my love!"

        MC "I can always count on you… say, I need a favor, one that only you can fulfill."

        male_actor "What is it?"

        MC "You see… oh, I hate to ask this of you, but my sister needs a new kimono. We’ve really been struggling to get by, and you’re the only person I can trust to help me."

        male_actor "Well, I do have some I need to get off my hands… Can you afford them?"

        MC "Perhaps not now, but in the meantime, you’ll have my attention…"

        "(MC flirtatiously places her hand on his arm, and the man gasps.)"

        MC "Please?"

        male_actor "Alright… I’ll get you the kimono. But just this once."

        MC "And I’ll always be grateful, Hayakawa-kun."

        "(Filming ceases. The director looks pleased.)"

        direct "Cut!"

        prod "Fantastic work, MC-san! I would be counting all my coins if I had a woman like that… one sweet word, and the next thing I know, they’ll all disappear!"

        MC "Thank you, sir. I enjoy playing these roles, even if I don’t quite agree with them."

    "(Scene changes. MC is on set with Setsuko, and she is in a hospital bed.)"

    MC "This is certainly my first time filming a scene like this!" 
    MC "(laughs) I’ve never been covered in so many bandages before."

    setsuko "You should be glad you’re just acting and haven’t actually broken anything – trust me, it’s the last thing you want to happen to you."

    MC "It isn’t even on the list of things I want to happen to me!"

    "(They exchange a few laughs, and the producer approaches.)"

    prod "This is our final scene, ladies. We want it to really leave a lasting impression – do you think you can do that?"

    setsuko "With MC here, I’m sure of it."

    MC "You flatter me, Setsuko-san. I wouldn’t be anywhere near where I am today if it weren’t for you."

    prod "Let’s keep that energy up. Places, everyone!"

    direct "Action!"

    setsuko "(in character) Sister… none of this would have happened had you done what I told you to. I would still have my patron if it weren’t for your meddling, and you wouldn’t be suffering like this."

    MC "(thinking) How should I respond?"

    menu:
        "(BE IMPASSIONED) I really have to sell this speech, so I’ll be angry and give it my all.":
            $ hospital_scene = "impassioned"
        "(BE MELANCHOLY) This scene has to be dramatic, so I need to match that tone if I want to get a good reaction from the audience.":
            $ hospital_scene = "melancholy"

    if hospital_scene == "impassioned":
        MC "(angrily) Sister, don’t you understand?! In our world, the only thing we can do is submit to men, but we will never be rewarded for it. Look at us! You’re practically broke, and I nearly had my life taken from me. All we do is suffer. Why must geisha even exist?"

        "(The director looks pleased. Filming ceases.)"

        prod "Fantastic job, MC-san! That blew me away."

        MC "(bows) Thank you, sir."

        setsuko "I agree… You really are the star of the show."

    elif hospital_scene == "melancholy":
        MC "(sadly) Sister… don’t you understand? In our world, the only thing we can do is submit to men… but we will never be rewarded for it. Look at us. You’re practically broke, and I nearly had my life taken from me. All we do is suffer… why must geisha even exist?"

        "(The director looks neutral. Filming ceases.)"

        prod "Not bad, MC-san… That was a very somber way to end the film. Hopefully our audience won’t be too sad watching it."

        MC "I hope they’ll receive it well…"

    jump CH1FINALE


label CH1FINALE:
    manager "And that’s a wrap, thank you everybody."

    crew "Thank you!"

    prod "Well done, MC. Truly, one of your best performances – I doubt you’ll ever be a side character again once this one shows."

    menu:
        "(I’d better not!)":
            $ mc_wrap_response = "confident"
        "(I’ll be happy with anything I can do.)":
            $ mc_wrap_response = "grateful"

    if mc_wrap_response == "confident":
        MC "I’d better not!"
        prod "Never shy with me, are you? What happened to that shaky, nervous girl I first met?" 
        prod "(laughs) I’m glad you feel able to talk to me, MC."
    elif mc_wrap_response == "grateful":
        MC "I’ll be happy with anything I can do."
        prod "I’ll find you the best. Never hesitate to come speak with me when you need."

    MC "Actually, I’ve been meaning to ask you something."

    prod "Of course, go ahead."

    menu:
        "(Have things seemed rather on-edge lately? In the West?)":
            $ mc_question = "on_edge"
        "(Are there any major projects you’re working on?)":
            $ mc_question = "projects"
        "(Am I doing enough?)":
            $ mc_question = "enough"

    if mc_question == "on_edge":
        prod "On edge?" 
        prod "(his eyes dart to the ground and back) I wouldn’t say that, exactly. A little tense or excited, maybe. But truly, it’s nothing you need to worry about."
        prod "Whatever might be going on, it’s not going to concern you. It’s more of a management situation – I mean, it would be. All paperwork, the boring things."
        prod "You keep on doing what you’re doing and don’t mind anyone acting odd, alright?"

    elif mc_question == "projects":
        prod "Actually…" 
        prod "(a brief glimmer of excitement) There have been discussions of opening a new studio overseas. The details are still being kept quiet, but when I know more, you’ll be the first actress I tell."
        prod "On an unrelated note – you happen to be fluent in Mandarin, yes?"
        MC "I am, though I haven’t practiced in a year or so."
        prod "That’s good to know. It might be a good time to start brushing up on those skills."
        MC "(she smiles) But it’s completely unrelated."
        prod "(he smiles back) Of course. Just a random, passing thought."

    elif mc_question == "enough":
        prod "What? MC, you’re doing more than enough. What brought this on?"
        MC "I just wonder… Do you think I’m interesting enough to be a star?"
        prod "Have you been speaking with Kiyo?"
        menu:
            "(A bit.)":
                $ mc_kiyo_conversation = "kiyo"
            "(More with Setsuko. She seems to be struggling.)":
                $ mc_kiyo_conversation = "setsuko"

        if mc_kiyo_conversation == "kiyo":
            prod "(sighs) There are a lot of strong personalities in this industry, as I’m sure you’ve noticed. But I don’t want you to be caught up in their glamour. Sure, they’re flashy. They attract attention. But that’s not always a good thing."
        elif mc_kiyo_conversation == "setsuko":
            prod "(sighs) There are a lot of strong personalities in this industry, as I’m sure you’ve noticed. But I don’t want you to be caught up in their glamour. Sure, they’re flashy. They attract attention. But that’s not always a good thing."

        MC "What do you mean?"
        prod "Trends change. For a long time, a loud, garish woman like Yamaguchi wouldn’t have been allowed anywhere near a stage, let alone a camera. But suddenly, she’s the star of the screen. Your friend, Wada, better suited an older kind of fantasy – she’s easy to like, never too much to see or speak with."
        MC "It seems like Kiyo is the better role model, then."
        prod "I’m not too sure about that. Things are starting to change, maybe even reverse a little. Being too forward or too laid back – both can be a detriment."
        prod "What you have is versatility. You adapt, you shift with the times. Don’t lose track of that because some new fashion has taken hold. You need to keep walking that line, for all our sakes."

    "(He gives MC a pat on the head.)"

    prod "You’re making a name for yourself. That’s good. I’m proud of you – we all are. Don’t lose sight of who you are, though, even when you put on a show. See you soon."

    "(He waves, then leaves the room.)"

    MC "(internal) Don’t lose sight of who I am… But, who am I?"

    jump start2
