init python:
    import csv
    import random
    import io
    import os

    base_dir = os.path.join(config.basedir, "game", "csv files")

    # Construct file paths dynamically
    movie_data_fp = os.path.join(base_dir, "Movie DB - prewar movies.csv")
    fp = os.path.join(base_dir, "Movie DB - movie stats.csv")

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
        fp = io.StringIO(movie_stats_data)
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
define young_male_actor = Character("Young Male Actor")
define young_actress_1 = Character("Young Actress 1")
define young_actress_2 = Character("Young Actress 2")

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

screen end_panel():
    modal True
    zorder 200

    # Background
    add "starpower_background.png":
        align (0.5, 0.5)
        zoom 1.2  # Slightly larger background

    frame:
        background None
        xalign 0.5
        yalign 0.5
        xpadding 80
        ypadding 60

        vbox:
            spacing 40
            xalign 0.5
            yalign 0.5

            # Title
            text "Final Scores" size 70 color "#FFFFFF" xalign 0.5 bold True

            # Main content row
            hbox:
                spacing 80  # Increased horizontal spacing
                xalign 0.5

                # Trendiness Column
                vbox:
                    spacing 15
                    text "Trendiness" size 35 color "#FFFFFF" xalign 0.5
                    add p_star:
                        zoom 0.55  # Slightly larger stars
                        xalign 0.5
                    text str(trendiness_score) size 30 color "#FFFFFF" xalign 0.5
                    text "Were you outspoken, true to your heart, and with the times?":
                        size 32
                        color "#FFFFFFDD"
                        xalign 0.5
                        xmaximum 300
                        text_align 0.5

                # Westernization Column
                vbox:
                    spacing 15
                    text "Westernization" size 35 color "#FFFFFF" xalign 0.5
                    add b_star:
                        zoom 0.55
                        xalign 0.5
                    text str(westernization_score) size 30 color "#FFFFFF" xalign 0.5
                    text "Did the introduction of Western influences change your style?":
                        size 32
                        color "#FFFFFFDD"
                        xalign 0.5
                        xmaximum 300
                        text_align 0.5

                # Nationalism Column
                vbox:
                    spacing 15
                    text "Nationalism" size 35 color "#FFFFFF" xalign 0.5
                    add g_star:
                        zoom 0.55
                        xalign 0.5
                    text str(nationalism_score) size 30 color "#FFFFFF" xalign 0.5
                    text "During troubling times, did you stand by your country?":
                        size 32
                        color "#FFFFFFDD"
                        xalign 0.5
                        xmaximum 300
                        text_align 0.5

                # Industry Relations Column
                vbox:
                    spacing 15
                    text "Industry Relations" size 35 color "#FFFFFF" xalign 0.5
                    add relationship_bar:
                        zoom 0.38  # Scaled down
                        xalign 0.5
                    text str(relationship_score) + "/15" size 30 color "#FFFFFF" xalign 0.5
                    text "With so much on your plate, how strong were your relationships?":
                        size 32
                        color "#FFFFFFDD"
                        xalign 0.5
                        xmaximum 300
                        text_align 0.5

    # Close button
    textbutton "Close":
        action Hide("end_panel")
        xalign 0.5
        yalign 0.92  # Moved up slightly
        background "#FFFFFF30"
        padding (40, 12)
        hover_background "#FFFFFF50"
        text_size 28

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
            play osund "page turn.mp3" volume 0.5
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
            $ trendiness_score += 1
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

        movie2 = {
            "name": movie1_title,
            "description": movie1_description,
            "role": movie1_role,
        }

        movie1 = {
            "name": movie2_title,
            "description": movie2_description,
            "role": movie2_role,
        }

    call screen movie_role_choice(movie1, movie2)

    if chosen_movie == "movie2":
        "You have chosen the role in [movie1['name']]."
        $ trendiness_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    elif chosen_movie == "movie1":
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
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

            $ renpy.pause(0.5)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
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

label afterQTE1:
    MC "(thinking) Setsuko’s work is done, but mine is just starting. It’s time for me to prepare for my scene."
    play sound "page turn.mp3" volume 0.5

    # Transition to MC’s scene
    direct "Action!"
    play sound "page turn.mp3" volume 0.5

    jump QTE2menu

label afterQTE2:
    # Transition to the jazz club scene
    MC "Ugh, I really can’t stand the stink of all this smoke."
    play sound "page turn.mp3" volume 0.5
    kiyo "(exhales smoke from her cigarette) That’s too bad, MC-chan, you’ll have to get used to it soon if you want to pull this scene off."
    play sound "page turn.mp3" volume 0.5
    MC "You mean I have to smoke? I never signed up for that!"
    play sound "page turn.mp3" volume 0.5
    toshiro "(laughs) You’re such a little girl, MC-chan! But you’re not supposed to be playing that – you’re a woman now, and a rebellious one at that."
    play sound "page turn.mp3" volume 0.5

    jump QTE3menu

label explore2:
    scene street bg
    call screen streetView2

label CH1PT2:
    scene office bg
    stop music
    play music "tokyo kenbutsu.mp3" loop
    prod "Your reputation is growing, [mcName]. I’ve even heard your name on the streets and in town – you’ve attracted some dedicated fans."
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
    prod "You’ve got another role! (He hands [mcName] the script) This one is called…"
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

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)


    prod "Shooting starts next week – start looking over your lines. You’ve got some experience on your side, not to mention that handful of fans. Still, stay alert and do your best. We’re proud of you, MC. I’m proud of you."
    play sound "page turn.mp3" volume 0.5

    scene studio bg with fade
    stop music
    play music "crowd-ambience.mp3" loop volume 0.5

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

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)


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

    jump CH1PT2QTE

label green2:
    scene studio bg
    kiyo "“Not so bad” – how inspirational."
    play sound "page turn.mp3" volume 0.5
    setsuko "Do you hate marriage, Kiyo?"
    play sound "page turn.mp3" volume 0.5
    kiyo "Of course not! I’d love to have a handsome man on my arm and a sweet little boy to dress up and show off – oh it would drive my sisters mad! But I’m my own person first. I’m not tossing away an opportunity for the first man who asks."
    play sound "page turn.mp3" volume 0.5
    setsuko "He’s not the first…"
    play sound "page turn.mp3" volume 0.5
    kiyo "Even better, then! You’ve got options. Make them wait, focus on your career."
    play sound "page turn.mp3" volume 0.5
    setsuko "But why would they want me once I fail? No one would want to marry an actress who couldn’t make it…"
    play sound "page turn.mp3" volume 0.5
    kiyo "There you go again – “I’m going to fail, I’m going to fail.” Stop saying such self-effacing nonsense!"
    play sound "page turn.mp3" volume 0.5
    setsuko "But I’m not what they want, am I?"
    play sound "page turn.mp3" volume 0.5
    kiyo "Not right now, certainly. But you can fix that."
    play sound "page turn.mp3" volume 0.5
    menu:
        "I think Setsuko is fine as she is.":
            $ setsuko_advice = "fine"
            $ relationship_score +=1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
        "I don’t think it’s something to be fixed.":
            $ setsuko_advice = "fix"

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    kiyo "Really? Then tell me, [mcName], what do you think she should do?"
    play sound "page turn.mp3" volume 0.5
    MC "Write your mother back…"
    menu:
        "At least meet with this man – maybe he’s nice?":
            $ mother_advice = "meet"
            $ relationship_score -=1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
        "Keep being as you are. You got this role, after all.":
            $ mother_advice = "stay"
            $ relationship_score +=1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)


    if mother_advice == "meet":
        kiyo "I’m sure he’s lovely. But after all this, you’ll just settle down? Just give up?"
        play sound "page turn.mp3" volume 0.5
        setsuko "How is marriage giving up?"
        play sound "page turn.mp3" volume 0.5
        kiyo "You can’t be a wife and a growing star. You need to be desirable, not some kind of role model."
        play sound "page turn.mp3" volume 0.5
    else:
        kiyo "And “this role” is just a bit part. It’s a step down from the last."
        play sound "page turn.mp3" volume 0.5
        setsuko "That’s why I’m considering just stopping here!"
        play sound "page turn.mp3" volume 0.5
        kiyo "And you truly think that’ll make you happy?"
        play sound "page turn.mp3" volume 0.5
        setsuko "Maybe. Not everyone can strike out on their first try, like you."
        play sound "page turn.mp3" volume 0.5
        kiyo "Are you suggesting it was just luck for me?"
        play sound "page turn.mp3" volume 0.5
        setsuko "Of course not!"
        play sound "page turn.mp3" volume 0.5

        kiyo "I’m not just some rich girl who happened to be nearby when some director had a last minute casting call. I didn’t get here by chance. I had to work for this. And you? You have talent, but that’s all!"
        play sound "page turn.mp3" volume 0.5
        setsuko "If I have talent, then why am I not getting cast?"
        play sound "page turn.mp3" volume 0.5
        kiyo "Because you don’t do your research. You play the same girl at home, on screen, in front of the producers – sweet Setsuko with her perfect kimono and gentle voice. Always lets the men speak first, always bows her head… You’re what everyone wants in a bride in the countryside, maybe, but this is the city. This is the silver screen."
        play sound "page turn.mp3" volume 0.5
    kiyo "(Kiyo looks between MC and Setsuko. A manager comes by.)"
    play sound "page turn.mp3" volume 0.5
    manager "Kiyo, the director would like to go over the last scene."
    play sound "page turn.mp3" volume 0.5
    kiyo "Of course." 
    play sound "page turn.mp3" volume 0.5
    kiyo "(she turns back to Setsuko, briefly) If you keep playing yourself down, you’ll end up in the same situation as that White Orchid business. Except next time, I won’t be helping you."
    play sound "page turn.mp3" volume 0.5
    menu:
        "What happened with your last film?":
            $ setsuko_last_film = "ask"
        "(stay quiet, let Setsuko be – she’s had enough)":
            $ setsuko_last_film = "quiet"

    if setsuko_last_film == "ask":
        setsuko "The reviews were just… so mean."
        play sound "page turn.mp3" volume 0.5
        MC "How so?"
        play sound "page turn.mp3" volume 0.5
        setsuko "They called me plain. Nothing to offer, seen it a million times already. I guess… it’s just like Kiyo was saying. There are hundreds of girls just like me. My screen partner was so angry. He told my team he would never work with me again. I’d never seen my producer look so disappointed. When he called me into his office to give me this role, I really thought he was going to fire me."
        play sound "page turn.mp3" volume 0.5
        MC "And that’s why you were considering quitting?"
        play sound "page turn.mp3" volume 0.5
        setsuko "Yes. Especially after my mother’s letter came in. Maybe I’m not the type who can keep Japan interested, right now. I’m too traditional, too ‘perfect.’"
        play sound "page turn.mp3" volume 0.5
        MC "(laughs) “Too perfect”?"
        play sound "page turn.mp3" volume 0.5
        setsuko "(flushes) You know what I mean! I’ll never be like you, or like Kiyo. And if that’s not what the studios want, then what more can I do? I don’t know if I can take any more critiques like that…"
        play sound "page turn.mp3" volume 0.5
        MC "I understand. But at least stay for this movie, okay? I need my best friend."
        play sound "page turn.mp3" volume 0.5
        setsuko "(Setsuko nods, her eyes a little watery.)"
        play sound "page turn.mp3" volume 0.5
        setsuko "Oh no, now they’re going to yell at me for smudging my makeup. I’d better go clean up. (she pauses) Thank you, MC. You’ve given me a little hope."
        play sound "page turn.mp3" volume 0.5
    else:
        setsuko "Well, I’d better go clean up, I suppose. If it’s my last role, I want to look my best, right?" 
        play sound "page turn.mp3" volume 0.5
        setsuko "(she smiles, but there’s no joy in it) I’ll see you on set, [mcName]."
        play sound "page turn.mp3" volume 0.5

    jump CH1PT2QTE
label CH1PT2QTE:

    MC "(thinking) I can’t believe I’m the lead actress in this movie! There’s no room for error – my reputation could be on the line if I don’t perform well."
    play sound "page turn.mp3" volume 0.5
    toshiro "(Tōshiro approaches from behind and places his hand on MC’s shoulder. MC jumps.)"
    play sound "page turn.mp3" volume 0.5
    toshiro "Relax, [mcName]-chan, it’s just me."
    play sound "page turn.mp3" volume 0.5
    MC "That isn’t very proper of you, Watanabe-san."
    play sound "page turn.mp3" volume 0.5
    toshiro "I know, I know… but we’re playing fiances in this movie, so maybe it’s alright."
    play sound "page turn.mp3" volume 0.5
    "([mcName] gently takes his hand off her shoulder.)"
    play sound "page turn.mp3" volume 0.5
    MC "I’d prefer if you got into character another way, thank you very much – besides, we need to get ready to film."
    play sound "page turn.mp3" volume 0.5
    toshiro "As you wish… (whispers) feisty, I like it."
    play sound "page turn.mp3" volume 0.5
    "([mcName] rolls her eyes as Tōshiro leaves.)"
    play sound "page turn.mp3" volume 0.5
    MC "(thinking) The nerve of that man…"
    play sound "page turn.mp3" volume 0.5
    "([mcName] straightens out her clothes, a chic French dress from a high-end department store – no doubt a dress Kiyo would envy. It feels foreign, in every sense of the word, but the delicate fabric fills MC with a sense of excitement. She is a star, and she looks like one.)"
    play sound "page turn.mp3" volume 0.5
    prod "I expect big things from you today, MC-san. I know you won’t disappoint me."
    play sound "page turn.mp3" volume 0.5
    MC "Thank you, sir, I won’t."
    play sound "page turn.mp3" volume 0.5
    "([mcName] and the other actors go to their positions on set.)"
    play sound "page turn.mp3" volume 0.5
    direct "Action!"
    play sound "page turn.mp3" volume 0.5
    "([mcName]'s character stands alone on the side of the road. In this brief scene, she is meant to call over a car by herself."
    play sound "page turn.mp3" volume 0.5
    MC "(thinking) I know I’m playing a modern girl, and I need to be bold… but I can’t be too bold. What should I do? Maybe…"
    play sound "page turn.mp3" volume 0.5
    jump QTE4

label CH1ToshiroTransition:
    toshiro "Excited for our scene together?"
    play sound "page turn.mp3" volume 0.5
    MC "(crosses her arms) Shouldn’t we be rehearsing? Besides, it’s not like this will be our first time on screen together."
    play sound "page turn.mp3" volume 0.5
    toshiro "Just trying to diffuse the tension… (peers over at the script) So, we’re just walking in this scene? Sounds easy enough."
    play sound "page turn.mp3" volume 0.5
    MC "(thinking) There’s a lot more nuance than meets the eye, depending on how you play it… Now, what should I do?"
    play sound "page turn.mp3" volume 0.5
    jump QTE5

label oldscene:
    MC "I hope you don’t find the dialogue in this scene too disrespectful!"
    play sound "page turn.mp3" volume 0.5
    older_actress "Nonsense, dear! It’s only a script – acting is our job, after all."
    play sound "page turn.mp3" volume 0.5
    older_actor "Besides, I find it quite interesting! It’s not like we could talk like this to our parents when we were young… (chuckles) I have to admit I’m a little jealous."
    play sound "page turn.mp3" volume 0.5
    prod "Remember, [mcName]-san, we want this scene to shock the viewers… but it can’t be too shocking, alright?"
    play sound "page turn.mp3" volume 0.5
    MC "I’ll keep that in mind."
    play sound "page turn.mp3" volume 0.5
    "(The actors move to their places.)"
    play sound "page turn.mp3" volume 0.5
    direct "Action!"
    play sound "page turn.mp3" volume 0.5
    MC "(thinking) Now, what should I do? How about…"
    play sound "page turn.mp3" volume 0.5
    jump QTE6
label explore3:
    scene street bg
    call screen streetView3
    stop music
    play music "minato chanson.mp3" loop

label producer_scene:
    scene office bg
    stop music
    play music "tokyo kenbutsu.mp3" loop
    prod "You’ve done quite well in your last few films. I truly think you’re on your way to something great, [mcName]. You should be very proud."
    play sound "page turn.mp3" volume 0.5
    menu:
        "How much longer until I’m on one of those fancy magazine covers?":
            $ mc_response = "magazine"
        "Oh, you flatter me too much. Though I do hope good things are coming…!":
            $ mc_response = "humble"

    if mc_response == "magazine":
        prod "Keep up the good work and keep your manners in check, and we’ll see. For now, you’ve got a new role to nail."
        play sound "page turn.mp3" volume 0.5
    elif mc_response == "humble":
        prod "I wouldn’t say it if you didn’t deserve it. And I’m not the only one who has faith in you…"
        play sound "page turn.mp3" volume 0.5

    prod "Brand new script, fresh off the press and written just for you."
    play sound "page turn.mp3" volume 0.5
    "(He produces a script.)"
    play sound "page turn.mp3" volume 0.5
    prod "Congratulations, again."
    play sound "page turn.mp3" volume 0.5
    prod "(He hands [mcName] the script) This one is called…"
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
        play sound "click.mp3" volume 1.5
        "You have chosen the role in [movie1['name']]."
        $ nationalism_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Red Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    elif chosen_movie == "movie2":
        play sound "click.mp3" volume 1.5
        "You have chosen the role in [movie2['name']]."
        $ nationalism_score += 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)


    prod "Stay sharp, [mcName]. This director’s a tough one to please. You’ve got the talent, just make sure you watch the atmosphere. Things have been a little more lively lately. Don’t let anything slip past you, okay?"
    play sound "page turn.mp3" volume 0.5
    scene studio bg

    MC "I should go check in on the others..."
    play sound "page turn.mp3" volume 0.5
    jump talktuah

label talktuah:
    menu:
        "Talk to Kazuo":
            stop music
            play sound "crowd-ambience.mp3" loop volume 0.5
            jump kazuo_conversation
        "Talk to Tōshiro":
            stop music
            play sound "crowd-ambience.mp3" loop volume 0.5
            jump toshiro_conversation
        "Talk to Setsuko":
            stop music
            play sound "crowd-ambience.mp3" loop volume 0.5
            jump setsuko_conversation
        "Talk to Kiyo":
            stop music
            play sound "crowd-ambience.mp3" loop volume 0.5
            jump kiyo_conversation
        "Don’t talk to anyone":
            stop music
            play sound "crowd-ambience.mp3" loop volume 0.5
            jump skip_conversation

label CH1QTE3:
    setsuko "I’m excited to be in a film with you, MC-chan! We always work so well together."
    play sound "page turn.mp3" volume 0.5
    MC "I feel the same way! We get to be sisters in this film, too – it’ll be just like real life, almost."
    play sound "page turn.mp3" volume 0.5
    setsuko "(laughs) Almost! Let’s go over our lines one more time before the filming starts…"
    play sound "page turn.mp3" volume 0.5
    "(Some time passes. The producer walks over.)"
    play sound "page turn.mp3" volume 0.5
    prod "Alright, ladies, I hope you two have your lines memorized."
    play sound "page turn.mp3" volume 0.5
    setsuko "I think so…"
    play sound "page turn.mp3" volume 0.5
    MC "(gently nudges her) We’ll do great, don’t worry. We’re ready to film now, sir."
    play sound "page turn.mp3" volume 0.5
    prod "That’s the spirit. Places, everyone!"
    play sound "page turn.mp3" volume 0.5
    direct "Action!"
    play sound "page turn.mp3" volume 0.5
    setsuko "(in character) Little sister, you mustn't act this way. It’s not proper for geisha like ourselves to be disloyal to our patrons. I think… well…"
    play sound "page turn.mp3" volume 0.5
    MC "(thinking) Oh no, she’s forgotten the rest of her lines! I should…"
    play sound "page turn.mp3" volume 0.5
    jump QTE7

label CH1PT3QTE:
    male_actor "Normally I’m not one to play a bumbling fool, but I think the audience will appreciate the humor of this scene."
    play sound "page turn.mp3" volume 0.5
    MC "I agree. I’ve done a few roles like this before, but I’m still not quite used to playing the 'femme fatale'... I hope I don’t get typecast!"
    play sound "page turn.mp3" volume 0.5
    male_actor "I’m sure you won’t be, don’t worry about it."
    play sound "page turn.mp3" volume 0.5
    prod "Speaking of femme fatale, we’ll need a lot of that in this scene – but not too much, you know the drill. Alright, places, everyone!"
    play sound "page turn.mp3" volume 0.5
    direct "Action!"
    play sound "page turn.mp3" volume 0.5
    "(Filming begins, and the male actor’s character enters the scene.)"
    play sound "page turn.mp3" volume 0.5
    male_actor "Momo-chan, I’m here!"
    play sound "page turn.mp3" volume 0.5
    MC "(thinking) How should I play this scene?"
    play sound "page turn.mp3" volume 0.5
    jump QTE8

label next:
    "(Scene changes. MC is on set with Setsuko, and she is in a hospital bed.)"
    play sound "page turn.mp3" volume 0.5
    MC "This is certainly my first time filming a scene like this!" 
    play sound "page turn.mp3" volume 0.5
    MC "(laughs) I’ve never been covered in so many bandages before."
    play sound "page turn.mp3" volume 0.5
    setsuko "You should be glad you’re just acting and haven’t actually broken anything – trust me, it’s the last thing you want to happen to you."
    play sound "page turn.mp3" volume 0.5
    MC "It isn’t even on the list of things I want to happen to me!"
    play sound "page turn.mp3" volume 0.5
    "(They exchange a few laughs, and the producer approaches.)"
    play sound "page turn.mp3" volume 0.5
    prod "This is our final scene, ladies. We want it to really leave a lasting impression – do you think you can do that?"
    play sound "page turn.mp3" volume 0.5
    setsuko "With [mcName] here, I’m sure of it."
    play sound "page turn.mp3" volume 0.5
    MC "You flatter me, Setsuko-san. I wouldn’t be anywhere near where I am today if it weren’t for you."
    play sound "page turn.mp3" volume 0.5
    prod "Let’s keep that energy up. Places, everyone!"
    play sound "page turn.mp3" volume 0.5
    direct "Action!"
    play sound "page turn.mp3" volume 0.5
    setsuko "(in character) Sister… none of this would have happened had you done what I told you to. I would still have my patron if it weren’t for your meddling, and you wouldn’t be suffering like this."
    play sound "page turn.mp3" volume 0.5
    MC "(thinking) How should I respond?"
    play sound "page turn.mp3" volume 0.5
    jump QTE9

label CH1FINALE:
    play music "crowd-ambience.mp3" loop volume 0.5
    manager "And that’s a wrap, thank you everybody."
    play sound "page turn.mp3" volume 0.5
    crew "Thank you!"
    play sound "page turn.mp3" volume 0.5
    prod "Well done, [mcName]. Truly, one of your best performances – I doubt you’ll ever be a side character again once this one shows."
    play sound "page turn.mp3" volume 0.5
    menu:
        "I’d better not!":
            $ mc_wrap_response = "confident"
            $ trendiness_score += 1
            $ relationship_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "I’ll be happy with anything I can do.":
            $ mc_wrap_response = "grateful"
            $ trendiness_score -= 1
            $ relationship_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    if mc_wrap_response == "confident":
        MC "I’d better not!"
        prod "Never shy with me, are you? What happened to that shaky, nervous girl I first met?" 
        prod "(laughs) I’m glad you feel able to talk to me, MC."
    elif mc_wrap_response == "grateful":
        MC "I’ll be happy with anything I can do."
        prod "I’ll find you the best. Never hesitate to come speak with me when you need."

    MC "Actually, I’ve been meaning to ask you something."
    play sound "page turn.mp3" volume 0.5
    prod "Of course, go ahead."
    play sound "page turn.mp3" volume 0.5
    menu:
        "Have things seemed rather on-edge lately? In the West?":
            $ mc_question = "on_edge"
            $ westernization_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Green Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "Are there any major projects you’re working on?":
            $ mc_question = "projects"
        "Am I doing enough?":
            $ mc_question = "enough"

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    if mc_question == "on_edge":
        prod "On edge?" 
        play sound "page turn.mp3" volume 0.5
        prod "(his eyes dart to the ground and back) I wouldn’t say that, exactly. A little tense or excited, maybe. But truly, it’s nothing you need to worry about."
        play sound "page turn.mp3" volume 0.5
        prod "Whatever might be going on, it’s not going to concern you. It’s more of a management situation – I mean, it would be. All paperwork, the boring things."
        play sound "page turn.mp3" volume 0.5
        prod "You keep on doing what you’re doing and don’t mind anyone acting odd, alright?"
        play sound "page turn.mp3" volume 0.5

    elif mc_question == "projects":
        prod "Actually…" 
        play sound "page turn.mp3" volume 0.5
        prod "(a brief glimmer of excitement) There have been discussions of opening a new studio overseas. The details are still being kept quiet, but when I know more, you’ll be the first actress I tell."
        play sound "page turn.mp3" volume 0.5
        prod "On an unrelated note – you happen to be fluent in Mandarin, yes?"
        play sound "page turn.mp3" volume 0.5
        MC "I am, though I haven’t practiced in a year or so."
        play sound "page turn.mp3" volume 0.5
        prod "That’s good to know. It might be a good time to start brushing up on those skills."
        play sound "page turn.mp3" volume 0.5
        MC "(she smiles) But it’s completely unrelated."
        play sound "page turn.mp3" volume 0.5
        prod "(he smiles back) Of course. Just a random, passing thought."
        play sound "page turn.mp3" volume 0.5

    elif mc_question == "enough":
        prod "What? [mcName], you’re doing more than enough. What brought this on?"
        play sound "page turn.mp3" volume 0.5
        MC "I just wonder… Do you think I’m interesting enough to be a star?"
        play sound "page turn.mp3" volume 0.5
        prod "Have you been speaking with Kiyo?"
        play sound "page turn.mp3" volume 0.5
        menu:
            "A bit.":
                $ mc_kiyo_conversation = "kiyo"
            "More with Setsuko. She seems to be struggling.":
                $ mc_kiyo_conversation = "setsuko"

        if mc_kiyo_conversation == "kiyo":
            prod "(sighs) There are a lot of strong personalities in this industry, as I’m sure you’ve noticed. But I don’t want you to be caught up in their glamour. Sure, they’re flashy. They attract attention. But that’s not always a good thing."
            play sound "page turn.mp3" volume 0.5
        elif mc_kiyo_conversation == "setsuko":
            prod "(sighs) There are a lot of strong personalities in this industry, as I’m sure you’ve noticed. But I don’t want you to be caught up in their glamour. Sure, they’re flashy. They attract attention. But that’s not always a good thing."
            play sound "page turn.mp3" volume 0.5

        MC "What do you mean?"
        play sound "page turn.mp3" volume 0.5
        prod "Trends change. For a long time, a loud, garish woman like Yamaguchi wouldn’t have been allowed anywhere near a stage, let alone a camera. But suddenly, she’s the star of the screen. Your friend, Wada, better suited an older kind of fantasy – she’s easy to like, never too much to see or speak with."
        play sound "page turn.mp3" volume 0.5
        MC "It seems like Kiyo is the better role model, then."
        play sound "page turn.mp3" volume 0.5
        prod "I’m not too sure about that. Things are starting to change, maybe even reverse a little. Being too forward or too laid back – both can be a detriment."
        play sound "page turn.mp3" volume 0.5
        prod "What you have is versatility. You adapt, you shift with the times. Don’t lose track of that because some new fashion has taken hold. You need to keep walking that line, for all our sakes."
        play sound "page turn.mp3" volume 0.5

    "(He gives [mcName] a pat on the head.)"
    play sound "page turn.mp3" volume 0.5
    prod "You’re making a name for yourself. That’s good. I’m proud of you – we all are. Don’t lose sight of who you are, though, even when you put on a show. See you soon."
    play sound "page turn.mp3" volume 0.5
    "(He waves, then leaves the room.)"
    play sound "page turn.mp3" volume 0.5
    MC "(internal) Don’t lose sight of who I am… But, who am I?"
    play sound "page turn.mp3" volume 0.5

    python:
        p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
        relationship_bar = what_relationship_bar_to_use(relationship_score)

    show screen end_panel
    MC "Until the next time!"

