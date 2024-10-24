init python:
    import csv
    import random

    movie_data_fp = "/Users/siddharthiyer/Documents/GitHub/star-team-japanlab/star team/game/csv files/Movie DB - movies.csv"
    class MovieMetaData:

        def __init__(self, id, title, description, role):
            self.id = id
            self.title = title
            self.description = description
            self.role = role

    def get_two_movies_from_era_0():
        movies = []
        with open(movie_data_fp, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Era'] == '0':
                    movies.append(MovieMetaData(row['movieRoleId'], row['title'], row['description'], row['role']))

        return random.sample(movies, 2)

    def get_movie_scores(movieRoleId):
        fp = "/Users/siddharthiyer/Documents/GitHub/star-team-japanlab/star team/game/csv files/Movie DB - movie stats.csv"
        with open(fp, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['movieRoleId'] == movieRoleId:
                    return row['modernity'], row['exoticism'], row['nationalism']

#Define characters
define mcName = "Assertive Feminine Voice"
define MC = Character("[mcName]", window_background=Frame("images/mc_textbox.png", 25, 25) )
define prod = Character("Producer",image="producer")
define direct = Character("Director")
define setsuko = Character("Setsuko",image="setsuko", window_background=Frame("images/setsuko_textbox.png", 25, 25))
define toshiro = Character("Toshiro",image="toshiro", window_background=Frame("images/toshiro_textbox.png", 25, 25))
define kiyo = Character("Kiyo",image="kiyo", window_background=Frame("images/kiyo_textbox.png", 25, 25))
define kazuo = Character("Kazuo")

image chap1_movie = Movie(size=(1920, 1080), channel='movie', play="images/chap1.webm")
image intro_movie = Movie(size=(1920, 1080), channel='movie', play="images/intro_movie.webm")

# For Star Power Images
image background_strip = "images/Star Power Background.png"
image star_p = "images/Purple Empty Idle.png"
image star_b = "images/Blue Empty Idle.png"
image star_g = "images/Green Empty Idle.png"

#Define character sprites
image MC = "MC.png"
image side setsuko = "setsuko.png"
image side toshiro = "toshiro.png"
image side kiyo = "kiyo.png"
image side producer = "producer.png"
# Define initial scores
default modernity_score = 10
default exoticism_score = 10
default nationalism_score = 10

# Screen for star and points
screen star_with_score(star_image, score, xpos, ypos):

    fixed:
        xpos xpos
        ypos ypos

        add star_image zoom 0.2  # Adjust zoom to resize the star

        text "[score]":
            xpos 50
            ypos 48
            xanchor 0.5
            yanchor 0.5
            size 20  # Adjust text size as needed
            color "#ffffff"  # Text color

screen score_display(p_score, b_score, g_score):

    # Display the background image at the left corner
    add "background_strip" xpos 0 ypos -80 zoom 0.18

    # Display the stars with scores using the helper screen
    use star_with_score("star_p", p_score, xpos=20, ypos=10)
    use star_with_score("star_b", b_score, xpos=120, ypos=10)
    use star_with_score("star_g", g_score, xpos=220, ypos=10)

screen stats_bar():
    frame:
        background "#333333"
        xalign 0.5
        yalign 0.0
        padding (10, 10, 10, 10)
        hbox:
            spacing 50

            vbox:
                text "Modernity" size 20
                text "[modernity_score]" size 20

            vbox:
                text "Exoticism" size 20
                text "[exoticism_score]" size 20

            vbox:
                text "Nationalism" size 20
                text "[nationalism_score]" size 20


''' PLACEHOLDER FOR DEFAULT SELECTION IMAGES '''

image movie1_poster = "images/kiyo.png"
image movie2_poster = "images/setsuko.png"

# default movie1 = {
#     "name": "Echoes of Tradition",
#     "description": "This silent film portrays the life a once-beloved samurai whose notorious bad luck taints his and his wife's reputation. After being deemed unfit to serve his lord, the samurai must then endure a series of trials that prove his loyalty and deference.",
#     "role": "Supporting Actress, Samurai's Wife",
#     "poster": "images/kiyo.png"
# }

# default movie2 = {
#     "name": "Moonlit Tango",
#     "description": "A man's job promotion sends him from Kyoto to the bustling city of Tokyo. It's there that he meets a lively woman, one who captivates his attention with her extravagant clothing, and her affinity for listening to jazz with a cigarette between her lips.",
#     "role": "Lead Actress",
#     "poster": "images/kiyo.png"
# }

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
                text "Description: [movie1['description']]" size 25 color "#CCCCCC"
                text "Role: [movie1['role']]" size 25 color "#CCCCCC"

                frame:
                    yfill True
                    background None

                # Button to choose this role
                textbutton "Accept Role" action [SetVariable("chosen_movie", "movie1"), Return()] style "role_button" text_color "#CCCCCC" align (0.4, 0.5)

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
                text "Description: [movie2['description']]" size 25 color "#CCCCCC" align (0.5, 0.5)
                text "Role: [movie1['role']]" size 25 color "#CCCCCC"

                frame:
                    yfill True
                    background None


                # Button to choose this role
                textbutton "Accept Role" action [SetVariable("chosen_movie", "movie2"), Return()] style "role_button" text_color "#CCCCCC" align (0.4, 0.5)

label start:

    show screen score_display(modernity_score, exoticism_score, nationalism_score)

    stop music
    scene solidblack

    MC "Who am I?"

    MC "That’s an interesting question, I suppose."

    MC "I’m a woman. I was born in Osaka, Japan, in 1915."

    MC "My favorite color is red, but I rarely get to wear it."

    MC "But that doesn’t answer your question, does it?"

    MC "So, tell me – who am I?"

    play sound "click reverb.mp3"
    MC "Don’t be nervous. This is what I do. I am whoever you want me to be. Just tell me."

    show greysil

    python:
        mcName = renpy.input("Name:", length=16)
        mcName = mcName.strip()
        if not mcName:
            mcName = "Main Character"

    scene solidblack

    MC "[mcName]. Interesting. Did you know that changing names is a common practice among actresses?"

    MC "Oh, that’s what I forgot to tell you. I’m an actress, and forgive my arrogance, but quite a good one, too."

    MC "Now, as an actress, I’ve had quite a number of stories to tell. Whirlwind romances, a wrenching tragedy, a soft, sweet girl appearing only to support the glittering ingenue."

    MC "There is a glamor to the screen – it all glows in that dark room, the only light amid a backdrop of silence. It is stunning. Captivating."

    MC "The voices you could picture from the radio suddenly belong to people – to women and men with faces and expressions that seize you by the heart and force it to beat to a rhythm of their own design."

    MC "Oh yes, it’s a spectacle. All the audience weeps and laughs together. Well, all together in attendance."

    MC "In that moment, perhaps there is unity. But once the lights return and the world is no longer scripted, what becomes of the characters?"

    MC "They disappear. They melt back into their original forms – the actors. But even then, the show never stops. For in the day, in the night, between each bite at each meal, the performance goes on. That is what it means to be a star."

    MC "You cannot rely on the lights of the set to carry you through to the next role. No, you must shine of your own accord. You must never go out. And you must reach far beyond your own space."

    MC "Would you like to hear how I did it?"

    menu:
        "Yes":
            MC "Thank you for indulging me."
        "No":
            MC "Hm, perhaps another time then."
            return

    MC "I hope my story will be an interesting enough exchange..."
    
    show intro_movie

    scene intro 1

    MC "I’m from Osaka, you already know that.My parents were a perfect sort of couple – father a hardworking government officer, mother a housewife that put all others to shame. Meals were quiet, but never uncomfortable."

    scene intro 2

    MC "I always loved to sing. I’d put on private performances for myself, singing the same songs I’d heard at the festivals and in school. And at nine, my mother took notice. She enrolled me in music lessons with a strict but kind tutor, Ō Shūka, though she preferred I called her by her Chinese name, Wang Qiuxia."

    MC "We spent long days together – I often saw her more than my own family. She spoke to me in both Japanese and Mandarin, broken parts of the latter until I could finally hold a conversation in full. I owe much of my career to her and her guidance."

    scene intro 3

    MC "At the Aoi Matsuri in 1928, I was given the opportunity – no doubt with some strings pulled by Ms. Wang and my parents – to perform on a public stage. It was a night that would change my life."

    MC "A man in the audience, whether or not his presence was a coincidence, treated my song as an audition and offered me a spot in the Naniwa Conservatoire, a top acting school. Though I kept an air of quiet humility as I accepted, as I signed my first contract, there was not a drop of reservation between my trembling fingers."   

    hide intro 3

    show chap1_movie zorder 10
    pause

    show studio bg

    direct "What do you mean she can’t make the shot? What’s her excuse? Doesn’t she understand how big of an opportunity this is?"

    prod "Her family sends their regrets, sir, but her doctor doesn’t recommend she leave the hospital until her lungs have cleared."

    direct "This is a disaster – we don’t have this space forever. Should we just cut the character?"

    prod "It may be too late for that. Why don’t we get one of the younger girls to stand in? She just has to look nice, right?"

    direct "(sighs, grumbles) At least let me get a look at them. These girls are here for their voices, not their faces. We don’t need some oni wasting space on the film."

    show MC

    MC "Hahaha!"

    direct "Where did that one come from?"

    prod "That would be [mcName], I believe."

    hide MC

    direct "What school?"

    prod "The Naniwa Conservatoire. Her family is quite well-to-do – I believe she’s been taking lessons since childhood. Would you–"

    direct "Get her in costume. I want her back here in five minutes."

    prod "Yes, sir."

    prod "[mcName]?"

    show MC

    MC "Hm? Oh! Hello, sir."

    hide MC

    prod "We are in a bit of an emergency situation. One of our actresses has fallen ill and we need someone to fill in her place. The director has chosen you."

    show MC
    MC "What, me?"
    MC "Oh my gosh!" # Visible excitement

    # MC's thoughts
    MC "My first role! At sixteen! But that poor actress, I almost feel guilty…"

    menu:
        "I know I’m only an amateur, but I’ll give it my all!":
            MC "I know I’m only an amateur, but I’ll give it my all!"
            $ modernity_score += 1

        "I’m not sure if I should…":
            MC "I’m not sure if I should…"
            $ modernity_score -= 1

    show screen score_display(modernity_score, exoticism_score, nationalism_score)

    hide MC

    prod "No need for stress – it’s a walk-on role."

    show MC

    MC "Oh… ([mcName] is slightly disappointed...)"

    hide MC

    prod "That doesn’t mean it’s not important. The director chose you. Let me show you to the costuming room – we need you back here as soon as possible for a run-through."

    # Producer exits the frame
    prod "Follow me. (The producer exits the room.)"

    show MC
    # MC left alone
    MC "That was how it began – a total accident. A role so small my name might not even appear in the credits. But that moment…"
    MC "The feeling of powder on my cheeks, like hot sand on my skin."
    MC "Whether warm from the lights or from the mixture of pride and sheer terror that coursed my body."
    MC "I was stiff as a board, I’m sure. Yet that was the first time I felt so alive. So very real."

 # MC and Producer dialogue

    scene office bg

    show MC
    MC "Thank you. It was just a bit part…"

    hide MC
    menu:
        "but I’m grateful nonetheless.":
            prod "Well, you were outstanding. So much so that…"

        "so I’m ready to move on to bigger things.":
            prod "Quite a spark you’ve got there. You’re going to need that ambition, because…"
            $ modernity_score += 2

    show screen score_display(modernity_score, exoticism_score, nationalism_score)

    prod "You’ve been contracted to a new role."

    python:
        movie_choices = get_two_movies_from_era_0()

        movie1_title = movie_choices[0].title
        movie1_description = movie_choices[0].description
        movie1_role = movie_choices[0].role

        movie2_title = movie_choices[1].title
        movie2_description = movie_choices[1].description
        movie2_role = movie_choices[1].role

        modernity_score1, exoticism_score1, nationalism_score1 = map(int, get_movie_scores(movie_choices[0].id))
        modernity_score2, exoticism_score2, nationalism_score2 = map(int, get_movie_scores(movie_choices[1].id))

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
        $ modernity_score += modernity_score1 - modernity_score2
        $ exoticism_score += exoticism_score1 - exoticism_score2
        $ nationalism_score += nationalism_score1 - nationalism_score2
    elif chosen_movie == "movie2":
        "You have chosen the role in [movie2['name']]."
        $ modernity_score += modernity_score2 - modernity_score1
        $ exoticism_score += exoticism_score2 - exoticism_score1
        $ nationalism_score += nationalism_score2 - nationalism_score1

    show screen score_display(modernity_score, exoticism_score, nationalism_score)

    prod "Here is your script. Rehearsals will start promptly next Tuesday. I’m obligated to tell you to represent us well, though I doubt you’ll have any trouble with that."

    MC "Of course."

    # Setting changes to the movie set

    # MC and Setsuko dialogue
    setsuko "Oh, this is just thrilling! I can’t believe we’re here, together, in our first film!"

    MC "First… yes."

    MC "I don’t know if I should tell her it isn’t my first…"

    setsuko "I heard that one of the actresses in 'first film name' got kicked out, and they had a random chorus girl take her place! It’s so embarrassing – I don’t know how I’d return to the company. But whoever filled in – what a lucky girl! What I wouldn’t give to have that chance."

    MC "(slightly uncomfortable) Wow, that’s quite a story. Where did you hear that?"


    setsuko "Where haven’t I heard! It’s all the talk around the academy–"

    prod "Ladies, that’s enough chatting. We’re starting soon. [mcName], please save your voice unless you’re going over your lines. Wada, what on earth are you doing in your regular clothes? Go see costumes immediately."

    setsuko "(in a whisper) What a killjoy! Oh, but [mcName], I’ll tell you more later!"

    # Setsuko hurries off
    setsuko "."
    MC "(internal) What should I do right now?"

    menu:
        "Rehearse alone.":
            MC "I’ll just go over my lines quietly."
            # End the scene and transition to next part
            jump after_film_scene

        "Find Setsuko.":
            # Leads to the scene in blue
            jump find_setsuko_scene

label after_film_scene:
    # Insert after film scene logic here
    MC "I rehearsed by myself..."

    jump explore_scene

label find_setsuko_scene:
    scene studio bg # Replace with the appropriate background
    show MC
    MC "Setsuko?"
    hide MC
    show setsuko
    setsuko "(jumps) MC! What are you doing? I thought you were supposed to be rehearsing!"
    hide setsuko
    show MC
    MC "I wanted to hear more about…"
    hide MC
    show setsuko
    menu:
        "the gossip around the academy.":
            setsuko "(smirks conspiratorially) Well, I heard that it was one of our girls who got selected for that fill-in role! No one knows who, exactly, but what a bold move! Imagine volunteering for something like that… I know I’d do it without a second thought, but the older tutors are always telling me I come across way too eager."
            setsuko "It’s too ‘modern’ or ‘not ladylike’ or something. But what’s wrong with that? I think that’s what the people like nowadays, anyway!"

        "the other actors here.":
            setsuko "(smirks conspiratorially) Hm, well I haven’t really spoken to him yet, but I did see this right 'relevant hot guy' talking with the director earlier. I don’t think he’s a big star or anything, but maybe he is! He’s certainly got the looks for it! (she blushes) Not that I’m interested. I’m just saying…"
    hide setsuko
    show MC
    MC "What’s wrong with being interested?"
    hide MC
    show setsuko
    setsuko "I don’t want him to think I’m too forward!"
    hide setsuko
    show MC
    MC "I wonder if people still like shy girls these days…"
    hide MC
    show setsuko
    setsuko "You’re right! Actually, just last week I saw this magazine headline: 'He’s Your Husband, Not Your Parents’!' These trends change so fast… It feels like just a year ago we were being told to shut up and stick to our homes. But now you see all these modern girls walking around in their heels and their bold colors!"
    hide setsuko
    show MC
    MC "I don’t know how to keep up with it."
    hide MC
    show setsuko
    setsuko "I don’t really know either – but I guess you can find out a lot through the news and the things people say on the street. We should both keep our ears sharp! And I’ll let you know if I learn anything really interesting."

    # Transition to the next part of the game
    jump explore_scene

label explore_scene:
    scene street bg # Replace with the appropriate background

    # Exploration choices
    menu:
        
        "Magazine Stand":
            # Description of the modern girl movement and fashion
            "You browse through the magazines, noticing a strong emphasis on the modern girl movement. Articles encourage women to make their own decisions and stand out in society."
            menu:
                "Continue Exploring?":
                    jump explore_scene
                "Stop Exploring":
                    "You decided to leave and go to the producer's office"

        "Two Young Women":
            # Scandalous gossiping about a friend
            "You overhear two young women gasping and clutching their pearls. They seem to be making fun of a friend who’s stuck in a boring, traditional marriage."
            menu:
                "Continue Exploring?":
                    jump explore_scene
                "Stop Exploring":
                    "You decided to leave and go to the producer's office"
        "Newspaper":
            # Discussion of exoticism and talkies
            "You glance at the newspaper, which discusses exoticism and the rise of talkies, along with mentions of importations from America and other parts of Asia."
            menu:
                "Continue Exploring?":
                    jump explore_scene
                "Stop Exploring":
                    "You decided to leave and go to the producer's office"
        "Letter from Setsuko":
            # Gossip about another girl
            "You read a letter from Setsuko, gossiping about a girl from their school who was supposed to be a big star. Unfortunately, she got cast in a few traditional roles and was dunked on by the critics. Setsuko mentions that this girl starred alongside the guy from their film together – someone she’s totally not into."
            menu:
                "Continue Exploring?":
                    jump explore_scene
                "Stop Exploring":
                    "You decided to leave and go to the producer's office"
    # After exploration
    MC "The world’s changing so fast… I hope I’m able to make it out here."

    # Scene change to MC with Producer
    scene office bg  # Replace with the appropriate background

    prod "Five years ago I never would’ve thought I’d be seeing one of my actresses in a talkie. I didn’t even think we’d have talkies by now! I’m proud of you, MC."
    show MC
    MC "Thank you…"

    show office bg
    menu:
        "I really didn’t expect things to take off so fast.":
            prod "No need to be humble. You’ve got something special. Even that quack of a director could tell just from a single look."

        "But I never really doubted myself.":
            prod "There’s that spunk again. Keep that spark – the people like a clever girl."

    prod "And on that note, I’ve got some exciting news."

    # Producer produces a script
    prod "You’ve got another role!"
    # He hands MC the script
    prod "This one is called…"

    # Player picks between two bucket movies
    # Insert bucket movie selection logic here

    prod "Shooting starts next week – start looking over your lines. Take a deep breath, you’ll be fine. The last movie did well and the stakes are low, alright? Do your best."

    # Scene change to the set
    scene studio bg  # Replace with the appropriate background

    # Kiyo and Tōshiro conversation
    kiyo "Ohh, that was you was it? I thought you were divine, but that girl you were with… What was her name?"

    toshiro "Suga… something?"

    kiyo "Doesn’t matter. She was so plain. Such a shame! Things probably would’ve gone much smoother if you got someone more lively."

    # Kiyo notices MC
    kiyo "Hello you! (she beckons MC over) Don’t be shy – we don’t bite."

    MC "(internal) Are you sure…?"

    toshiro "Hm. (he looks MC up and down) Your face… Have we met before?"

    show MC
    MC "I believe so. I’m MC, I think we did (name of first bucket movie) a year or so ago? I was–"
    show studio bg
    toshiro "Impossible. I would’ve remembered a face like yours. (he smirks) But maybe I’ll give that one another watch – join me, make it a reunion?"

    menu:
        "I wouldn’t mind reliving some moments.":
            toshiro "We’ll talk a little later, then?"
            kiyo "(clears throat) I can’t imagine you’d have time, what with your schedule. Weren’t you just saying you have another film lined up right after this?"
            toshiro "Films are easy to come by. This is a rare opportunity."
            kiyo "(clearly disgruntled) MC, where did you get your dress?"

        "Only if I can bring my friend, Setsuko. Do you remember her too?" :
            toshiro "Um… if you want–"
            kiyo "How cute! Maybe I’ll tag along, we can make a night of it. But we ladies might have to do some shopping first. Your dress…"
    show MC
    MC "My dress?"
    show studio bg
    kiyo "It’s so quaint. Cute, I suppose – reminds me of that little rural town I visited back as a girl. Which is fine, of course, plenty of girls are still attached to that schoolgirl look. I just think it’s become a bit… outdated, don’t you think?"

    # A third person approaches
    kazuo "Hey everyone. (he notices MC) I don’t think we’ve met – this is my first movie, actually. I’m Tachibana Kazuo."
    show MC
    MC "MC, it’s nice to meet you."
    show studio bg
    toshiro "You need something?"

    kazuo "I just thought we might want to do a bit of rehearsal? Run through some lines, or something…"

    kiyo "Fantastic idea, Tachibana."

    kazuo "Tachibana."

    kiyo "Okay. Watanabe-san, do you want to go into the hallway? We can work on that second scene together."

    toshiro "Sure. (towards [mcName]) See you later?"

    # The two leave, now just Kazuo and MC
    kazuo "So, do you want to do a read-through?"
    show MC
    MC "Oh…"

    menu:
        "Actually, I think I’m in that second scene as well.":
            jump scene_in_blue  # leads to scene in blue

        "That sounds nice.":
            jump scene_in_green  # leads to scene in green

label scene_in_blue:
    # Logic for scene in blue
    return

label scene_in_green:
    # Logic for scene in green
    return

    


    return
