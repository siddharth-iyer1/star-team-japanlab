label kazuo_conversation:
    stop music
    play sound "crowd-ambience.mp3" loop volume 0.5
    kazuo "[mcName]! It’s nice to see you. How are things?"
    play sound "page turn.mp3" volume 0.5
    menu:
        "I didn’t think we’d end up seeing each other again. But I’m well.":
            $ mc_kazuo_greeting = "again"
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
        "It has been a while, hasn’t it? I’m doing nicely.":
            $ mc_kazuo_greeting = "while"

    if mc_kazuo_greeting == "again":
        MC "I didn’t think we’d end up seeing each other again. But I’m well."
        play sound "page turn.mp3" volume 0.5
        kazuo "Oh, uh… I guess you’ve been getting much better roles than me. My sister was all giddy after your last film – I think she wrote me two whole pages on it."
        play sound "page turn.mp3" volume 0.5
        MC "That’s so sweet!"
        play sound "page turn.mp3" volume 0.5
        kazuo "She always loves those stories about girls marching out on their own."
        play sound "page turn.mp3" volume 0.5
    elif mc_kazuo_greeting == "while":
        MC "It has been a while, hasn’t it? I’m doing nicely."
        play sound "page turn.mp3" volume 0.5
        kazuo "I’m glad to hear that. I wish I could say the same, ha!"
        play sound "page turn.mp3" volume 0.5
        MC "What’s going on?"
        play sound "page turn.mp3" volume 0.5

    "(Kazuo shifts from foot to foot, looking around the studio.)"
    play sound "page turn.mp3" volume 0.5

    kazuo "I’ve been thinking… maybe I should take some time off, get an office job or something."
    play sound "page turn.mp3" volume 0.5

    menu:
        "Really? Why?":
            $ mc_kazuo_office_question = "why"
        "Business is that bad?":
            $ mc_kazuo_office_question = "business"

    kazuo "Things haven’t been bad, but they have been a little um… stagnant. Directors seem to be moving away from the kind of films that need a guy like me."
    play sound "page turn.mp3" volume 0.5
    MC "A guy like you?"
    play sound "page turn.mp3" volume 0.5
    kazuo "You know… Sorta…"
    play sound "page turn.mp3" volume 0.5

    menu:
        "Boring?":
            $ mc_kazuo_type = "boring"
            $ relationship_score -= 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
        "Nice?":
            $ mc_kazuo_type = "nice"
            $ relationship_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    kazuo "Yeah. That’s putting it simply, I guess. (he grimaces) They need someone more domineering, you know? Someone who really puts out that go-getter, leader air. Like Tōshiro! He’s been really on the rise lately, not that he was ever not popular but… He makes all us guys look plainstandard when he’s on screen. Kinda like you, with the ladies."
    play sound "page turn.mp3" volume 0.5
    MC "Every hero needs a friend, don’t they?"
    play sound "page turn.mp3" volume 0.5
    kazuo "(laughs) I suppose. But even then, I’m more of a comic relief."
    play sound "page turn.mp3" volume 0.5
    MC "People need to laugh."
    play sound "page turn.mp3" volume 0.5
    kazuo "Do they…? The movies have all seemed so serious. Lately, it just seems humor isn’t what the people want."
    play sound "page turn.mp3" volume 0.5
    MC "Do you know what they want?"
    play sound "page turn.mp3" volume 0.5
    kazuo "I wish I did. But I’m thinking that it’s not me. I might be better off behind a desk – something in the government, maybe. There seem to be a lot of new positions opening up. I just want to do something to prove I’m a little useful…"
    play sound "page turn.mp3" volume 0.5
    MC "What about the army?"
    play sound "page turn.mp3" volume 0.5
    kazuo "Ha! I don’t know if I’m quite that brave. I probably wouldn’t last a week."
    play sound "page turn.mp3" volume 0.5
    "(He pauses, then looks around.)"
    play sound "page turn.mp3" volume 0.5
    kazuo "Do you read the global news, much?"
    play sound "page turn.mp3" volume 0.5
    menu:
        "Of course, I need to know what’s happening.":
            $ mc_global_news = "yes"
            $ westernization_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "I’d much rather read Osaka Shimbun.":
            $ mc_global_news = "local"
            $ westernization_score -= 1
            $ nationalism_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Red Flash.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    if mc_global_news == "yes":
        kazuo "Then, have you heard about what’s going on in Manchuria? I don’t know a lot, but the whole thing seems–"
        play sound "page turn.mp3" volume 0.5
    elif mc_global_news == "local":
        kazuo "Well, there’s this thing happening in China. They don’t say a lot about it, but–"
        play sound "page turn.mp3" volume 0.5

    "(A production manager enters.)"
    play sound "page turn.mp3" volume 0.5
    manager "Hello, Tachibana Kazuo, the director wanted a word about your entrance. Please be courteous, he’s a bit on edge today."
    play sound "page turn.mp3" volume 0.5
    kazuo "Of course. I’ll be right there! Well, [mcName], let’s give it our best. At least one more hurrah, right?"
    play sound "page turn.mp3" volume 0.5
    jump talktuah

label toshiro_conversation:
    stop music
    play sound "crowd-ambience.mp3" loop volume 0.5
    toshiro "Well, if it isn’t the little starlet herself. How’re you, MC?"
    play sound "page turn.mp3" volume 0.5
    menu:
        "(Fine. Busy.)":
            $ mc_tosh_response = "busy"
            $ relationship_score -= 1
        "(A lot better with the current company.)":
            $ mc_tosh_response = "flirty"
            $ relationship_score += 1

    if mc_tosh_response == "busy":
        MC "Fine. Busy."
        play sound "page turn.mp3" volume 0.5
        toshiro "But you still find time for me. How sweet."
        play sound "page turn.mp3" volume 0.5
        MC "…"
        play sound "page turn.mp3" volume 0.5
        toshiro "No need to be so icy. I’m just making conversation, aren’t I? I swear, women seem to be getting more and more defensive these days. Can’t a guy just chat with a pretty lady?"
        play sound "page turn.mp3" volume 0.5
        MC "What do you want to talk about, then?"
        play sound "page turn.mp3" volume 0.5

    elif mc_tosh_response == "flirty":
        MC "A lot better with the current company."
        play sound "page turn.mp3" volume 0.5
        toshiro "I’m glad the feeling is mutual." 
        play sound "page turn.mp3" volume 0.5
        toshiro "(he winks) If we keep getting cast together, maybe we’ll finally get one of those romances."
        play sound "page turn.mp3" volume 0.5
        MC "Pardon?"
        play sound "page turn.mp3" volume 0.5
        toshiro "All on screen, of course. The audience loves a charming duo, don’t they? And we seem to play off each other well, don’t we?"
        play sound "page turn.mp3" volume 0.5
        MC "Did you rehearse any of your character’s lines, or just these?"
        play sound "page turn.mp3" volume 0.5

    toshiro "And she stays feisty! You’re lucky men are still going for that. You know, I was so worried a few years ago when all those films about jazz singers and single ladies were coming out – loved to watch them, but movies are just a fantasy, aren’t they?"
    play sound "page turn.mp3" volume 0.5
    "(He leans against the wall, crossing his arms.)"
    play sound "page turn.mp3" volume 0.5
    toshiro "The problem was when girls started trying to imitate it. The country doesn’t run on dresses and makeup. I’m glad things are moving back in the right direction."
    play sound "page turn.mp3" volume 0.5
    MC "The right direction?"
    play sound "page turn.mp3" volume 0.5
    toshiro "Men acting like men, Japan acting like Japan. Wear whatever you want, I think western ladies look great – you seen that Mary Pickford? Fantastic – but leave that on the screen. My next film after this is a soldier movie. Isn’t that the best?"
    play sound "page turn.mp3" volume 0.5
    menu:
        "(But won’t that be violent?)":
            $ mc_tosh_soldier_movie = "violent"
            $ nationalism_score -=1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "(That’s so admirable!)":
            $ mc_tosh_soldier_movie = "admirable"
            $ nationalism_score +=1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    if mc_tosh_soldier_movie == "violent":
        MC "But won’t that be violent?"
        play sound "page turn.mp3" volume 0.5
        toshiro "Violence, no. Wouldn’t want to scar up a nice face, would I? But the idea behind it – war, victory, the glory of the nation. People don’t pay us enough attention because they think we’re some small island country. But we’re on the rise, and I wanna show that."
        play sound "page turn.mp3" volume 0.5
        MC "By being in a movie…?"
        play sound "page turn.mp3" volume 0.5
        toshiro "What, would you rather I go to war?"
        play sound "page turn.mp3" volume 0.5
        MC "It would be braver."
        play sound "page turn.mp3" volume 0.5
        toshiro "(clicks his tongue) There’s a difference between the kind of man who goes to the battlefield and the kind of man who unites his nation. No one needs a national symbol of some boring, faceless kid covered in soot. They need a reminder of what true, Japanese masculinity looks like. That’s how I’m serving my country."
        play sound "page turn.mp3" volume 0.5
        menu:
            "(Wow, what a hero…)":
                $ mc_tosh_hero_react = "wow"
            "(We’re lucky to have you.)":
                $ mc_tosh_hero_react = "lucky"
                python:
                    if mc_tosh_soldier_movie == violent:
                        nationalism_score +=1
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

        toshiro "Course, if I’m called to battle, I’ll serve. But it’d be a waste. Just like sitting me behind some desk – can you imagine that? What a sad life."
        play sound "page turn.mp3" volume 0.5
    elif mc_tosh_soldier_movie == "admirable":
        MC "That’s so admirable!"
        play sound "page turn.mp3" volume 0.5
        toshiro "We are, aren’t we? We don’t need to keep churning out those silly movies with people tripping over their feet or going stupid for a pretty pair of eyes. We need something with substance."
        play sound "page turn.mp3" volume 0.5
        MC "Do you feel like this will be enough?"
        play sound "page turn.mp3" volume 0.5
        toshiro "Course not. This is just a starting point. But you can already feel it in the streets, can’t you? The whole city is buzzing. People want to rally for something."
        play sound "page turn.mp3" volume 0.5
        "(He leans back, running a hand through his hair.)"
        play sound "page turn.mp3" volume 0.5
    toshiro "Y’know, rumor has it that there’s a new international studio opening up. Maybe something in China, or Hong Kong."
    play sound "page turn.mp3" volume 0.5
    MC "Really?"
    play sound "page turn.mp3" volume 0.5
    toshiro "Yup. And any studio worth their weight will be looking for some rising talent to pull. I’m thinking I might try and go outta the country, finally get something good on those poor people’s screens."
    play sound "page turn.mp3" volume 0.5
    "(He looks MC up and down, then leans in.)"
    play sound "page turn.mp3" volume 0.5
    toshiro "Think you’d join me?"
    play sound "page turn.mp3" volume 0.5
    MC "I–"
    play sound "page turn.mp3" volume 0.5
    "(From offscreen, the director starts shouting.)"
    play sound "page turn.mp3" volume 0.5
    direct "Where is my leading man? This isn’t some kind of playground, get over here!"
    play sound "page turn.mp3" volume 0.5
    toshiro "Always interrupting. Anyway, think on it, yeah?"
    play sound "page turn.mp3" volume 0.5
    "(He exits.)"
    play sound "page turn.mp3" volume 0.5
    MC "(internal) An international stage… What would that look like?"
    play sound "page turn.mp3" volume 0.5
    jump talktuah


label setsuko_conversation:
    stop music
    play sound "crowd-ambience.mp3" loop volume 0.5
    setsuko "MC! Oh, thank goodness, a friendly face." 
    play sound "page turn.mp3" volume 0.5
    setsuko "(she gives MC a kiss on the cheek) How are you? It’s been too long since we’ve met!"
    play sound "page turn.mp3" volume 0.5
    menu:
        "(I’ve been well! But what about you?)":
            $ mc_setsuko_greeting = "well"
            $ relationship_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "(It’s been so much work lately – the roles just don’t stop!)":
            $ mc_setsuko_greeting = "busy"

    if mc_setsuko_greeting == "well":
        MC "I’ve been well! But what about you?"
        play sound "page turn.mp3" volume 0.5
        setsuko "(her face falls for a moment, only to be replaced with an even wider smile) That’s wonderful! As for me, I’ve been on a bit of a break, I suppose. Everything at the studio seemed a little slow, so I was given some time to go visit family."
        play sound "page turn.mp3" volume 0.5
        MC "That sounds nice."
        play sound "page turn.mp3" volume 0.5
        setsuko "It is! Though I do miss acting whenever I’m gone. I know I’m not supposed to want so much attention but… a little can’t hurt!" 
        play sound "page turn.mp3" volume 0.5
        setsuko "(she giggles) Even if my parents disagree!"
        play sound "page turn.mp3" volume 0.5
        MC "You’re your own person, you’re allowed to have some fun."
        play sound "page turn.mp3" volume 0.5
        setsuko "But not too much~"
        play sound "page turn.mp3" volume 0.5
        MC "Of course not. We still have an appearance to keep!" 
        play sound "page turn.mp3" volume 0.5
        MC "(she also laughs)"
        play sound "page turn.mp3" volume 0.5

    elif mc_setsuko_greeting == "busy":
        MC "It’s been so much work lately – the roles just don’t stop!"
        play sound "page turn.mp3" volume 0.5
        setsuko "I’m so happy for you. I do wish I could say the same for myself."
        play sound "page turn.mp3" volume 0.5
        MC "What do you mean?"
        play sound "page turn.mp3" volume 0.5
        setsuko "Nothing bad! Work has just been a little slow lately, you know how these things come in waves. Sometimes you’re the title character, sometimes you’re just the singer in the background." 
        play sound "page turn.mp3" volume 0.5
        setsuko "(she sighs) Though I haven’t been a main in so long…"
        play sound "page turn.mp3" volume 0.5

        menu:
            "It’s not for everyone.":
                $ mc_setsuko_reassurance = "realist"
                $ relationship_score -= 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
            "Your time will come!":
                $ mc_setsuko_reassurance = "optimist"
                $ relationship_score += 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)

        if mc_setsuko_reassurance == "realist":
            MC "It’s not for everyone."
            play sound "page turn.mp3" volume 0.5
        else:
            MC "Your time will come!"
            play sound "page turn.mp3" volume 0.5
        
        setsuko "You’re right. I just need to be patient and grateful for what I have. At least, that’s what my parents have been saying. They don’t even want me to have this much time on screen! They always preferred the stage – so much more ‘dignified.’ But I just think movies are so fun. And they mean we get to spend more time together!"
        play sound "page turn.mp3" volume 0.5
        MC "What a lovely gift that is."
        play sound "page turn.mp3" volume 0.5
    setsuko "Do you want to hear something interesting?"
    play sound "page turn.mp3" volume 0.5

    MC "What?"
    play sound "page turn.mp3" volume 0.5
    setsuko "I’ve heard from the other girls at home that the whole ‘western girl’ thing is starting to go out of fashion. Directors have been looking for more wholesome, Japanese girls lately. Do you think that might mean…"
    play sound "page turn.mp3" volume 0.5
    menu:
        "(I wouldn’t get my hopes up.)":
            $ mc_setsuko_future = "caution"
            $ relationship_score -=1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
        "(This might be your moment!)":
            $ mc_setsuko_future = "hope"
            $ relationship_score += 1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)

    if mc_setsuko_future == "caution":
        MC "I wouldn’t get my hopes up."
        play sound "page turn.mp3" volume 0.5
        setsuko "You’re right… I was getting ahead of myself. Everything is moving forward, not backward." 
        play sound "page turn.mp3" volume 0.5
        setsuko "(she sighs) I hope there’s still a spot for me in that new world."
        play sound "page turn.mp3" volume 0.5
        MC "There will always be period films."
        play sound "page turn.mp3" volume 0.5
        setsuko "And uptight mothers to play! I’ve got the best model for that role."
        play sound "page turn.mp3" volume 0.5
        MC "Do you think you’ll continue acting?"
        play sound "page turn.mp3" volume 0.5
        setsuko "Maybe. If the work ever picks up again, I’d like to. As much as the idea of marriage sounded nice a few years ago, I think I’d miss this too much."
        play sound "page turn.mp3" volume 0.5

    elif mc_setsuko_future == "hope":
        MC "This might be your moment!"
        play sound "page turn.mp3" volume 0.5
        setsuko "Wouldn’t that just be wonderful?"
        play sound "page turn.mp3" volume 0.5
        MC "I hope I won’t be excluded from that new genre."
        play sound "page turn.mp3" volume 0.5
        setsuko "Don’t be ridiculous! You’re so versatile – you can play anyone. You’re not like me, all stuck in the same typecast. But please, if the tides do change, save some of the good roles for me!"
        play sound "page turn.mp3" volume 0.5
        MC "Always. You’ve been my favorite partner from the start."
        play sound "page turn.mp3" volume 0.5
        setsuko "Oh, MC! I just hope this isn’t all my own fantasy. I know that I’m just a small actress, but I just don’t want to go back to my old life."
        play sound "page turn.mp3" volume 0.5
        MC "Then don’t!"
        play sound "page turn.mp3" volume 0.5

    setsuko "Everything just seems to change so quickly. The trends, the atmosphere… You’ve felt it too, right? There’s a strange sort of buzz in the air. I don’t know if it’s excitement or anxiety but I can feel my skin prickling at every little bit of gossip!"
    play sound "page turn.mp3" volume 0.5

    "(From offscreen, the director starts shouting. A production manager enters.)"
    play sound "page turn.mp3" volume 0.5

    manager "Wada Setsuko, the director would like to see you. He’s quite touchy, so please be patient with him."
    play sound "page turn.mp3" volume 0.5

    setsuko "I guess that’s enough chit-chat for now. But I have so much to tell you, MC! We must keep in touch – I want to see you more often than on these sets!"
    play sound "page turn.mp3" volume 0.5
    MC "We both have to work hard, then."
    play sound "page turn.mp3" volume 0.5
    setsuko "Well, I’m not worried about this one, at least. You’re my good luck charm. Whenever you’re with me in a film, it’s a hit!"
    play sound "page turn.mp3" volume 0.5
    jump talktuah


label kiyo_conversation:
    stop music
    play sound "crowd-ambience.mp3" loop volume 0.5
    kiyo "[mcName]! How have you been, darling?"
    play sound "page turn.mp3" volume 0.5
    menu:
        "(The best I’ve ever been!)":
            $ mc_kiyo_greeting = "best"
            $ trendiness_score +=1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "(I’ve been doing alright. And you?)":
            $ mc_kiyo_greeting = "alright"
            $ relationship_score +=1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    if mc_kiyo_greeting == "best":
        MC "The best I’ve ever been!"
        play sound "page turn.mp3" volume 0.5
        kiyo "That much is clear. You’ve got that ‘ingenue’ glow about you. I remember when I first caught that color – it’s like honey to flies. The roles start pouring in. How have you been adjusting to the attention?"
        play sound "page turn.mp3" volume 0.5
    elif mc_kiyo_greeting == "alright":
        MC "I’ve been doing alright. And you?"
        play sound "page turn.mp3" volume 0.5
        kiyo "Now that’s the kind of answer I’d expect from someone like Setsuko, not a breakout star like yourself! Don’t think I haven’t been following your films. You are simply candy to the eyes of any director right now."
        play sound "page turn.mp3" volume 0.5

    MC "It’s all been a bit overwhelming…"
    play sound "page turn.mp3" volume 0.5
    menu:
        "(But quite honestly, I love it.)":
            $ mc_kiyo_overwhelm = "love"

        "(Sometimes I wonder if I’ll be able to handle it.)":
            $ mc_kiyo_overwhelm = "doubt"

    if mc_kiyo_overwhelm == "love":
        kiyo "Isn’t it just wonderful? Parents make such a fuss about all the publicity and the contracts and this and that, but to have your name appear on those big, beautiful posters – well, I can’t imagine a greater pleasure."
        play sound "page turn.mp3" volume 0.5
    elif mc_kiyo_overwhelm == "doubt":
        kiyo "Darling, we all doubt ourselves."
        play sound "page turn.mp3" volume 0.5
        MC "Even you?"
        play sound "page turn.mp3" volume 0.5
        kiyo "(laughs) Of course! You don’t think my knees were shaking the first time I stepped in front of a camera? I couldn’t eat the whole morning, I was so scared I’d be sick right there on set. But you get used to it. You learn to love it. I’m certain you’ve already started to feel it."
        play sound "page turn.mp3" volume 0.5

    MC "How do you handle it all?"
    play sound "page turn.mp3" volume 0.5

    kiyo "Handle what? The pressure, the parents?"
    play sound "page turn.mp3" volume 0.5
    menu:
        "(The pressure.)":
            $ mc_kiyo_handle = "pressure"
        "(The parents.)":
            $ mc_kiyo_handle = "parents"

    if mc_kiyo_handle == "pressure":
        kiyo "Pressure creates diamonds, MC. Taking the easy, soft route will never reward you in the same way as a well-fought journey."
        play sound "page turn.mp3" volume 0.5
        MC "I don’t know if I’m the fighting type."
        play sound "page turn.mp3" volume 0.5
        kiyo "(rolls her eyes) I don’t mean the mindless muscle and showy brawls. I mean the intellectual fights. The ones you have quietly with the directors and the producers, where you barter for your image. A little extra bat of the eye, an extra tear for the close-up – making yourself alluring, absolutely impossible to ignore."
        play sound "page turn.mp3" volume 0.5
        MC "But how does that make the pressure any lighter?"
        play sound "page turn.mp3" volume 0.5
        kiyo "Because once you’ve got them wrapped around your finger, they’ll make it all work for you. The best movies are written with you in mind, the best roles saved and the best cast members reserved to play alongside you. It’s momentum. Their attention follows you, lifts you. It feeds you. You’ll never be stuck as long as you can keep everyone watching."
        play sound "page turn.mp3" volume 0.5
        MC "How do you do that?"
        play sound "page turn.mp3" volume 0.5
        kiyo "Just never stop. No matter what anyone says, just keep fighting with every bit of your pride until you get what you deserve."
        play sound "page turn.mp3" volume 0.5
    elif mc_kiyo_handle == "parents":
        kiyo "Why should you care what they have to say?"
        play sound "page turn.mp3" volume 0.5
        MC "They raised me, they’re wiser and older and–"
        play sound "page turn.mp3" volume 0.5
        kiyo "And they’ve never stood where you’re standing, have they? Our parents, bless them for all they’ve done, have only seen one way of living. They’re stuck in the past, on the empire and facelessness and duty. They never even tried to see themselves as something greater. But you, MC, are greater."
        play sound "page turn.mp3" volume 0.5
        MC "Are you sure?"
        play sound "page turn.mp3" volume 0.5
        kiyo "Certain. If I had simply walked the easiest path – I hardly had a shortage of suitors, you know – I could be comfortably living in some nice Tokyo home with a husband and a child and be bored to death. Frankly, I would wish I was dead! Maybe some women can stand that life, but I couldn’t."
        play sound "page turn.mp3" volume 0.5

    MC "And you never regret it?"
    play sound "page turn.mp3" volume 0.5

    kiyo "What’s there to regret? A lost lover? My love is for the screen. I don’t need one romance or one lifestyle when I can have them all. Call me greedy, gluttonous, whatever you’d like, but I am living this life for the satisfaction of myself."
    play sound "page turn.mp3" volume 0.5
    MC "But what if I can’t have them all?"
    play sound "page turn.mp3" volume 0.5
    kiyo "You wait. You’ll learn to adapt, be versatile. You won’t always have the power, but when you do, you build yourself a palace. Decorate it however you like and wait in there whenever the people get fussy. Then present yourself once again, and capture their hearts. It’s been working for me."
    play sound "page turn.mp3" volume 0.5
    menu:
        "(Your new films have been… different.)":
            $ mc_kiyo_opinion = "different"
            $ trendiness_score +=1
            python:
                p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                relationship_bar = what_relationship_bar_to_use(relationship_score)
            show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "(What if I want to do something different?)":
            $ mc_kiyo_opinion = "new"

    $ renpy.pause(0.5)
    show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)

    if mc_kiyo_opinion == "different":
        MC "Your new films have been… different."
        play sound "page turn.mp3" volume 0.5
        kiyo "I’ve always loved the avant-garde. And there’s always going to be a craving for something new. But I wouldn’t risk it if I didn’t know that my career is stronger than a single failure. I’ve built reputation. That’s why I can do whatever I’d like."
        play sound "page turn.mp3" volume 0.5
    elif mc_kiyo_opinion == "new":
        MC "What if I want to do something different?"
        play sound "page turn.mp3" volume 0.5
        kiyo "Then make sure you have the charm to keep pulling in that audience. You’re a star in your movies, of course. But can you be a star in all movies? Build a reputation so strong, so impenetrable that a wave of critics could never sway your fans."
        play sound "page turn.mp3" volume 0.5

    "(A manager enters.)"
    play sound "page turn.mp3" volume 0.5

    manager "Yamaguchi Kiyo, you’re wanted on set. The director–"
    play sound "page turn.mp3" volume 0.5

    kiyo "Is such an uptight fellow. Don’t worry, I won’t ruffle any feathers." 
    play sound "page turn.mp3" volume 0.5
    kiyo "(she turns back to MC) You are special. Make sure that everyone knows it."
    play sound "page turn.mp3" volume 0.5

    jump talktuah

label skip_conversation:
    "([mcName] decides not to talk to anyone and moves on to the next part of the scene.)"
    play sound "page turn.mp3" volume 0.5
    jump CH1QTE3