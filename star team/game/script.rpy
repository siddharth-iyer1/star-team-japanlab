
define mcName = "Assertive Feminine Voice"
define MC = Character("[mcName]")
define prod = Character("Producer")
define direct = Character("Director")
define setsuko = Character("Setsuko")
define toshiro = Character("Toshiro")
define kiyo = Character("Kiyo")
define kazuo = Character("Kazuo")

label start:
    scene solidblack

    MC "Who am I?"

    MC "That’s an interesting question, I suppose."

    MC "I’m a woman. I was born in Osaka, Japan, in 1915."
    
    MC "My favorite color is red, but I rarely get to wear it."

    MC "But that doesn’t answer your question, does it?"

    MC "So, tell me – who am I?"

    scene glitch

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

    show image0

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

    show chap1
    with dissolve

    scene chap1
    with Pause(5.0)

    show studio bg
    with dissolve

    direct "What do you mean she can’t make the shot? What’s her excuse? Doesn’t she understand how big of an opportunity this is?"

    prod "Her family sends their regrets, sir, but her doctor doesn’t recommend she leave the hospital until her lungs have cleared."

    direct "This is a disaster – we don’t have this space forever. Should we just cut the character?"

    prod "It may be too late for that. Why don’t we get one of the younger girls to stand in? She just has to look nice, right?"

    direct "(sighs, grumbles) At least let me get a look at them. These girls are here for their voices, not their faces. We don’t need some oni wasting space on the film."

    show mainC

    MC "Hahaha!"

    direct "Where did that one come from?"

    prod "That would be [mcName], I believe."

    direct "What school?"

    prod "The Naniwa Conservatoire. Her family is quite well-to-do – I believe she’s been taking lessons since childhood. Would you–"

    direct "Get her in costume. I want her back here in five minutes."

    prod "Yes, sir."

    prod "[mcName]?"

    MC "Hm? Oh! Hello, sir."

    prod "We are in a bit of an emergency situation. One of our actresses has fallen ill and we need someone to fill in her place. The director has chosen you."

    MC "What, me?"
    MC "Oh my gosh!" # Visible excitement

    # MC's thoughts
    MC "My first role! At sixteen! But that poor actress, I almost feel guilty…"

    menu:
        "I know I’m only an amateur, but I’ll give it my all!":
            MC "I know I’m only an amateur, but I’ll give it my all!"

        "I’m not sure if I should…":
            MC "I’m not sure if I should…"

    prod "No need for stress – it’s a walk-on role."

    MC "Oh… ([mcName] is slightly disappointed...)"

    prod "That doesn’t mean it’s not important. The director chose you. Let me show you to the costuming room – we need you back here as soon as possible for a run-through."

    # Producer exits the frame
    prod "Follow me. (The producer exits the room.)"

    # MC left alone
    MC "That was how it began – a total accident. A role so small my name might not even appear in the credits. But that moment…"
    MC "The feeling of powder on my cheeks, like hot sand on my skin."
    MC "Whether warm from the lights or from the mixture of pride and sheer terror that coursed my body."
    MC "I was stiff as a board, I’m sure. Yet that was the first time I felt so alive. So very real."

 # MC and Producer dialogue

    scene office bg
    MC "Thank you. It was just a bit part…"

    menu:
        "but I’m grateful nonetheless.":
            prod "Well, you were outstanding. So much so that…"

        "so I’m ready to move on to bigger things.":
            prod "Quite a spark you’ve got there. You’re going to need that ambition, because…"

    prod "You’ve been contracted to a new role."

    # Film selection and script handover
    # Here you would insert the film selection logic.
    # For simplicity, we will assume it's a placeholder.

    prod "Here is your script. Rehearsals will start promptly next Tuesday. I’m obligated to tell you to represent us well, though I doubt you’ll have any trouble with that."
    MC "Of course."

    # Setting changes to the movie set
    scene studio bg

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

    MC "Setsuko?"

    setsuko "(jumps) MC! What are you doing? I thought you were supposed to be rehearsing!"

    MC "I wanted to hear more about…"

    menu:
        "the gossip around the academy.":
            setsuko "(smirks conspiratorially) Well, I heard that it was one of our girls who got selected for that fill-in role! No one knows who, exactly, but what a bold move! Imagine volunteering for something like that… I know I’d do it without a second thought, but the older tutors are always telling me I come across way too eager."
            setsuko "It’s too ‘modern’ or ‘not ladylike’ or something. But what’s wrong with that? I think that’s what the people like nowadays, anyway!"

        "the other actors here.":
            setsuko "(smirks conspiratorially) Hm, well I haven’t really spoken to him yet, but I did see this right 'relevant hot guy' talking with the director earlier. I don’t think he’s a big star or anything, but maybe he is! He’s certainly got the looks for it! (she blushes) Not that I’m interested. I’m just saying…"

    MC "What’s wrong with being interested?"

    setsuko "I don’t want him to think I’m too forward!"

    MC "I wonder if people still like shy girls these days…"

    setsuko "You’re right! Actually, just last week I saw this magazine headline: 'He’s Your Husband, Not Your Parents’!' These trends change so fast… It feels like just a year ago we were being told to shut up and stick to our homes. But now you see all these modern girls walking around in their heels and their bold colors!"

    MC "I don’t know how to keep up with it."

    setsuko "I don’t really know either – but I guess you can find out a lot through the news and the things people say on the street. We should both keep our ears sharp! And I’ll let you know if I learn anything really interesting."

    # Transition to the next part of the game
    jump explore_scene

label explore_scene:
    scene bg street_view  # Replace with the appropriate background

    # Exploration choices
    menu:
        "Magazine Stand":
            # Description of the modern girl movement and fashion
            "You browse through the magazines, noticing a strong emphasis on the modern girl movement. Articles encourage women to make their own decisions and stand out in society."

        "Two Young Women":
            # Scandalous gossiping about a friend
            "You overhear two young women gasping and clutching their pearls. They seem to be making fun of a friend who’s stuck in a boring, traditional marriage."

        "Newspaper":
            # Discussion of exoticism and talkies
            "You glance at the newspaper, which discusses exoticism and the rise of talkies, along with mentions of importations from America and other parts of Asia."

        "Letter from Setsuko":
            # Gossip about another girl
            "You read a letter from Setsuko, gossiping about a girl from their school who was supposed to be a big star. Unfortunately, she got cast in a few traditional roles and was dunked on by the critics. Setsuko mentions that this girl starred alongside the guy from their film together – someone she’s totally not into."

    # After exploration
    MC "The world’s changing so fast… I hope I’m able to make it out here."

    # Scene change to MC with Producer
    scene bg producer_office  # Replace with the appropriate background

    producer "Five years ago I never would’ve thought I’d be seeing one of my actresses in a talkie. I didn’t even think we’d have talkies by now! I’m proud of you, MC."

    mc "Thank you…"

    menu:
        "I really didn’t expect things to take off so fast.":
            producer "No need to be humble. You’ve got something special. Even that quack of a director could tell just from a single look."

        "But I never really doubted myself.":
            producer "There’s that spunk again. Keep that spark – the people like a clever girl."

    producer "And on that note, I’ve got some exciting news."

    # Producer produces a script
    producer "You’ve got another role!"
    # He hands MC the script
    producer "This one is called…"

    # Player picks between two bucket movies
    # Insert bucket movie selection logic here

    producer "Shooting starts next week – start looking over your lines. Take a deep breath, you’ll be fine. The last movie did well and the stakes are low, alright? Do your best."

    # Scene change to the set
    scene bg movie_set  # Replace with the appropriate background

    # Kiyo and Tōshiro conversation
    kiyo "Ohh, that was you was it? I thought you were divine, but that girl you were with… What was her name?"

    toshiro "Suga… something?"

    kiyo "Doesn’t matter. She was so plain. Such a shame! Things probably would’ve gone much smoother if you got someone more lively."

    # Kiyo notices MC
    kiyo "Hello you! [she beckons MC over] Don’t be shy – we don’t bite."

    MC "(internal) Are you sure…?"

    toshiro "Hm. [he looks MC up and down] Your face… Have we met before?"

    MC "I believe so. I’m MC, I think we did [name of first bucket movie] a year or so ago? I was–"

    toshiro "Impossible. I would’ve remembered a face like yours. [he smirks] But maybe I’ll give that one another watch – join me, make it a reunion?"

    menu:
        "I wouldn’t mind reliving some moments.":
            toshiro "We’ll talk a little later, then?"
            kiyo "[clears throat] I can’t imagine you’d have time, what with your schedule. Weren’t you just saying you have another film lined up right after this?"
            toshiro "Films are easy to come by. This is a rare opportunity."
            kiyo "[clearly disgruntled] MC, where did you get your dress?"

        "Only if I can bring my friend, Setsuko. Do you remember her too?" :
            toshiro "Um… if you want–"
            kiyo "How cute! Maybe I’ll tag along, we can make a night of it. But we ladies might have to do some shopping first. Your dress…"

    MC "My dress?"

    kiyo "It’s so quaint. Cute, I suppose – reminds me of that little rural town I visited back as a girl. Which is fine, of course, plenty of girls are still attached to that schoolgirl look. I just think it’s become a bit… outdated, don’t you think?"

    # A third person approaches
    kazuo "Hey everyone. [he notices MC] I don’t think we’ve met – this is my first movie, actually. I’m Tachibana Kazuo."

    MC "MC, it’s nice to meet you."

    toshiro "You need something?"

    kazuo "I just thought we might want to do a bit of rehearsal? Run through some lines, or something…"

    kiyo "Fantastic idea, Tachibana."

    kazuo "Tachibana."

    kiyo "Okay. Watanabe-san, do you want to go into the hallway? We can work on that second scene together."

    toshiro "Sure. (towards [mcName]) See you later?"

    # The two leave, now just Kazuo and MC
    kazuo "So, do you want to do a read-through?"

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
