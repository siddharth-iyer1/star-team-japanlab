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

label QTE2:
    label QTE2menu:
        $ time = 12.5
        $ timer_range = 12
        $ timer_jump = 'QTE2menu_slow'
        show screen countdown

        menu:
            "(ACT COY) I’ll keep my expressions understated. It wouldn’t be proper to overshadow the main character – I don’t want to be too flamboyant.":
                hide screen countdown
                play sound "page turn.mp3" volume 0.5
                $ mc_scene_path = "coy"
                $ trendiness_score -= 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Red Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                $ renpy.pause(0.5)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                MC "(in character) Shinjiro, I… I don’t know if I can tell you how I feel…"
                play sound "page turn.mp3" volume 0.5
                direct "Very demure, MC-san… maybe not quite what I expected with your character, but I think it can work. Let’s work on getting our next scene filmed now, okay?"
                play sound "page turn.mp3" volume 0.5
                toshiro "(whispers) Gee, MC… it was hard to tell if you were even in love with me. Really sell it to me next time, alright?"
                play sound "page turn.mp3" volume 0.5
                MC "(rolls eyes)"
                play sound "page turn.mp3" volume 0.5            
                jump afterQTE2
            "(ACT EXPRESSIVE) I’ll make my emotions very clear on my face! Even though I don’t say a lot, I can still show a lot.":
                hide screen countdown
                jump QTE2menu_slow
    label QTE2menu_slow:
        play sound "page turn.mp3" volume 0.5
        $ mc_scene_path = "expressive"
        $ trendiness_score += 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
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
        jump afterQTE2

label QTE3:
    label QTE3menu:
        $ time = 12.5
        $ timer_range = 12
        $ timer_jump = 'QTE3menu_slow'
        show screen countdown

        menu:
            "(SWANKY) I need to live it up! The only way I can keep the scene going is by contributing to the lively energy.":
                hide screen countdown
                play sound "page turn.mp3" volume 0.5
                $ westernization_score += 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Purple Empty Idle.png", "Green Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                $ renpy.pause(0.5)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                $ dance_path = "swanky"
                MC "(snaps fingers and sways with the beat, taking a long draw from the cigarette) (thinking) I can feel the energy of the room!"
                play sound "page turn.mp3" volume 0.5
                direct "Well done, everyone! If the music were any louder, I’m afraid the police wouldn’t be so convinced we were filming a movie!"
                play sound "page turn.mp3" volume 0.5
                direct "Wonderful performance, MC-san! I can see your training in the performing arts serves you well… although I wasn’t aware they taught that kind of dancing!"
                play sound "page turn.mp3" volume 0.5
                MC "(laughs) Thank you, sir!"
                play sound "page turn.mp3" volume 0.5
                jump explore2                
            "(CASUAL) I’ll lay low and keep it cool. I’m not a major character in this scene, anyway.":
                hide screen countdown
                jump QTE3menu_slow
    label QTE3menu_slow:
        play sound "page turn.mp3" volume 0.5
        $ westernization_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Purple Empty Idle.png", "Red Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ dance_path = "casual"
        MC "(sways subtly to the beat, keeping in the background) (thinking) I’m just part of the scenery for this one..."
        play sound "page turn.mp3" volume 0.5
        direct "I was expecting to see a little more energy from you, given your dancing background… but I’m sure your performance will suffice."
        play sound "page turn.mp3" volume 0.5
        MC "I understand, sir. I’ll try harder next time."
        play sound "page turn.mp3" volume 0.5        
        jump explore2

label QTE4:
    label QTE4menu:
        $ time = 12.5
        $ timer_range = 12
        $ timer_jump = 'QTE4menu_slow'
        show screen countdown

        menu:
            "(MIMIC) I’ll mimic what I saw a character do in a Western movie – audiences will love that!":
                hide screen countdown
                play sound "page turn.mp3" volume 0.5
                $ westernization_score += 2
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Purple Empty Idle.png", "Green Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                $ renpy.pause(0.5)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                "([mcName] stands with her thumb out in a hitchhiker’s gesture. Then, she stretches out her leg and raises the hem of her skirt over her calf. The director raises an eyebrow. Filming ceases.)"
                play sound "page turn.mp3" volume 0.5
                direct "Cut!"
                play sound "page turn.mp3" volume 0.5
                prod "MC-san, please speak with me."
                play sound "page turn.mp3" volume 0.5
                MC "Is everything alright, sir?"
                play sound "page turn.mp3" volume 0.5
                prod "That was very Hollywood, MC… you clearly know your stuff. However, we aren’t making that kind of movie – we don’t want our audience to get the wrong idea. Too much skin might attract the wrong kind of attention!"
                play sound "page turn.mp3" volume 0.5
                MC "I understand."
                play sound "page turn.mp3" volume 0.5
                direct "Alright everyone, from the top! Get back in your places…"
                play sound "page turn.mp3" volume 0.5
                jump CH1ToshiroTransition                
            "(REFERENCE) I’ll reference what I saw a character do in a Western movie, but I won’t copy it exactly.":
                hide screen countdown
                jump QTE4menu_slow
    label QTE4menu_slow:
        play sound "page turn.mp3" volume 0.5
        $ westernization_score +=1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Purple Empty Idle.png", "Red Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "([mcName] stands with her thumb out in a hitchhiker’s gesture, looking forward with a confident look in her eyes. The director looks satisfied. Filming ceases.)"
        play sound "page turn.mp3" volume 0.5
        direct "Cut!"
        play sound "page turn.mp3" volume 0.5
        prod "Good job, MC-san – very forward, but not too scandalous. Our audience might not be able to handle anything too bold, if you get what I mean."
        play sound "page turn.mp3" volume 0.5
        MC "I understand. Thank you, sir."
        play sound "page turn.mp3" volume 0.5
        jump CH1ToshiroTransition

label QTE5:
    label QTE5menu:
        $ time = 12.5
        $ timer_range = 12
        $ timer_jump = 'QTE5menu_slow'
        show screen countdown

        menu:
            "(BE BOLD) I’ll walk in front of him – we may be fiances, but our characters view each other as equals.":
                hide screen countdown
                play sound "page turn.mp3" volume 0.5
                $ trendiness_score += 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                $ renpy.pause(0.5)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                "(The actors go to their places.)"
                play sound "page turn.mp3" volume 0.5
                direct "Action!"
                play sound "page turn.mp3" volume 0.5
                "([mcName]’s and Tōshiro’s characters walk forward together, and MC visibly moves to walk in front of him. The director looks surprised, yet pleased. Filming ceases.)"
                play sound "page turn.mp3" volume 0.5
                direct "Cut!"
                play sound "page turn.mp3" volume 0.5
                toshiro "That was certainly something, MC-chan."
                play sound "page turn.mp3" volume 0.5
                MC "I think it fits with the tone of the movie – I’m sure the women watching the movie will feel the same."
                play sound "page turn.mp3" volume 0.5
                toshiro "Well, if you say so…"
                play sound "page turn.mp3" volume 0.5
                jump oldscene              
            "(BE RESPECTFUL) He is a man, and I am playing his fiancee, so I should walk behind him. That’s the proper thing to do.":
                hide screen countdown
                jump QTE5menu_slow
    label QTE5menu_slow:
        play sound "page turn.mp3" volume 0.5
        $ trendiness_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Purple Empty Idle.png", "Red Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        "(The actors go to their places.)"
        play sound "page turn.mp3" volume 0.5
        direct "Action!"
        play sound "page turn.mp3" volume 0.5
        "([mcName]’s and Tōshiro’s characters walk forward together, but MC waits a few steps to walk behind him. The director looks neutral. Filming ceases.)"
        play sound "page turn.mp3" volume 0.5
        direct "Cut!"
        play sound "page turn.mp3" volume 0.5
        toshiro "See? Not hard at all."
        play sound "page turn.mp3" volume 0.5
        MC "Maybe that was a little too old fashioned… I’m not sure that fits with the tone of the movie."
        play sound "page turn.mp3" volume 0.5
        toshiro "It’ll be fine, don’t worry. You just did what everyone expects you to do – no one will think anything of it."
        play sound "page turn.mp3" volume 0.5
        jump oldscene

label QTE6:
    label QTE6menu:
        $ time = 12.5
        $ timer_range = 12
        $ timer_jump = 'QTE6menu_slow'
        show screen countdown

        menu:
            "(BE CANDID) Even though my character is estranged from her parents, she’ll still act respectful… but she needs to speak her mind.":
                hide screen countdown
                play sound "page turn.mp3" volume 0.5
                $ nationalism_score += 1
                $ trendiness_score += 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Flash.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                $ renpy.pause(0.5)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                MC "(calmly) Father, I know you care about me… but this is my life, not yours. I’ll make you proud if you give me the opportunity to – I’m old enough to make my own decisions."
                play sound "page turn.mp3" volume 0.5
                older_actor "Kimiko-san…"
                play sound "page turn.mp3" volume 0.5
                "([mcName]’s “mother” and “father” embrace sadly, and MC turns away from them with a regretful but poised look. The director looks pleased. Filming ceases.)"
                play sound "page turn.mp3" volume 0.5
                direct "Cut!"
                play sound "page turn.mp3" volume 0.5
                MC "How did I do?"
                play sound "page turn.mp3" volume 0.5
                older_actor "I started to tear up a bit… I couldn’t help but imagine my daughter saying the same thing."
                play sound "page turn.mp3" volume 0.5
                older_actress "You have a very powerful presence, dear."
                play sound "page turn.mp3" volume 0.5
                MC "(bows) Thank you."
                play sound "page turn.mp3" volume 0.5
                stop music
                play music "minato chanson.mp3" loop
                jump explore3
            "(BE ASSERTIVE) My character has no reservations about speaking her mind – if she doesn’t like her parents, she needs to show it!":
                hide screen countdown
                jump QTE6menu_slow
    label QTE6menu_slow:
        play sound "page turn.mp3" volume 0.5
        $ trendiness_score += 1
        $ nationalism_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Green Flash.png", "Red Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        MC "(angrily) You have no place to tell me who I should love, father! You were never there for me when I was a child! I shouldn’t even call you my father…"
        play sound "page turn.mp3" volume 0.5
        older_actor "Kimiko-san…"
        play sound "page turn.mp3" volume 0.5
        "([mcName]’s “mother” and “father” embrace sadly, and MC turns away from them bitterly. The director looks neutral. Filming ceases.)"
        play sound "page turn.mp3" volume 0.5
        direct "Cut!"
        play sound "page turn.mp3" volume 0.5
        MC "How did I do?"
        play sound "page turn.mp3" volume 0.5
        older_actor "I was worried for a moment… I thought you really were mad at me!"
        play sound "page turn.mp3" volume 0.5
        older_actress "You have a very… strong presence."
        play sound "page turn.mp3" volume 0.5
        MC "Oh…"
        play sound "page turn.mp3" volume 0.5
        stop music
        play music "minato chanson.mp3" loop
        jump explore3

label QTE7:
    label QTE7menu:
        $ time = 12.5
        $ timer_range = 12
        $ timer_jump = 'QTE7menu_slow'
        show screen countdown

        menu:
            "(PLAY INTO TRADITION) Setsuko's character is a traditional geisha. Her line must be about following custom.":
                hide screen countdown
                play sound "page turn.mp3" volume 0.5
                $ nationalism_score += 1
                $ relationship_score += 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Purple Empty Idle.png", "Green Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                $ renpy.pause(0.5)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                setsuko "(wincing) What was my line again?"
                play sound "page turn.mp3" volume 0.5
                direct "(sighs) Cut!"
                play sound "page turn.mp3" volume 0.5
                prod "“I may be a rule follower, but that keeps me alive. It would do you some good to be one, too.”"
                play sound "page turn.mp3" volume 0.5
                setsuko "Ohhh, that’s right. Thank you, sir."
                play sound "page turn.mp3" volume 0.5
                direct "We’ll need to reshoot – let’s take this scene from the top. Don’t let her forget her lines, MC-san."
                play sound "page turn.mp3" volume 0.5
                MC "I won’t."
                play sound "page turn.mp3" volume 0.5
                "(Setsuko is visibly embarrassed, and [mcName] feels a pang of guilt.)"
                play sound "page turn.mp3" volume 0.5
                jump CH1PT3QTE           
            "(CHALLENGE TRADITION) Modern girls are so popular lately. Her line must be about challenging the status quo":
                hide screen countdown
                jump QTE7menu_slow
    label QTE7menu_slow:
        play sound "page turn.mp3" volume 0.5
        $ trendiness_score -= 1
        $ relationship_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Purple Empty Idle.png", "Red Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        MC "You’re the old-fashioned one, elder sister, always following the rules."
        play sound "page turn.mp3" volume 0.5
        setsuko "You’re right – I may be a rule follower, but that keeps me alive. It would do you some good to be one, too."
        play sound "page turn.mp3" volume 0.5
        MC "Well, the rules are changing. I don’t want the past to hold me back from my future."
        play sound "page turn.mp3" volume 0.5
        "(Filming ceases. The director looks pleased.)"
        play sound "page turn.mp3" volume 0.5
        prod "That wasn’t in the script, but I have to say, that was a good save! I think I prefer it to the original line."
        play sound "page turn.mp3" volume 0.5
        MC "Thank you, sir, I was just looking out for my co-star."
        play sound "page turn.mp3" volume 0.5
        setsuko "(smiles) I can always count on you, [mcName]-san."
        play sound "page turn.mp3" volume 0.5
        jump CH1PT3QTE
    
label QTE8:
    label QTE8menu:
        $ time = 12.5
        $ timer_range = 12
        $ timer_jump = 'QTE8menu_slow'
        show screen countdown

        menu:
            "(BE SWEET) I’ll act similarly to Setsuko’s character. She’s my sister, and I’m doing a favor for her in this scene.":
                hide screen countdown
                play sound "page turn.mp3" volume 0.5
                $ trendiness_score -= 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Purple Empty Idle.png", "Green Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                $ renpy.pause(0.5)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                MC "Hayakawa-kun, I’m so happy to see you! I hope you don’t mind if I ask for a favor…"
                play sound "page turn.mp3" volume 0.5
                male_actor "What is it, dearest?"
                play sound "page turn.mp3" volume 0.5
                MC "Well, times have been rough for my sister and I, but she is in need of a new kimono… Even though your prices are high, you’re the only merchant I trust to provide something fitting my sister. Oh, I’m so embarrassed, but will you please help me?"
                play sound "page turn.mp3" volume 0.5
                male_actor "I don’t know… I need to meet my company’s quota…"
                play sound "page turn.mp3" volume 0.5
                MC "It’ll only be this once! I’ll never ask for anything from you again, I promise."
                play sound "page turn.mp3" volume 0.5
                male_actor "Well, if you say so… Fine, just this once."
                play sound "page turn.mp3" volume 0.5
                MC "Oh, Hayakawa-kun, thank you so much!"
                play sound "page turn.mp3" volume 0.5
                "(Filming ceases. The director looks content.)"
                play sound "page turn.mp3" volume 0.5
                direct "Cut!"
                play sound "page turn.mp3" volume 0.5
                prod "[mcName]-san, I can sense the manipulation, but you’re far too sweet – that’s more fitting of Setsuko’s character."
                play sound "page turn.mp3" volume 0.5
                MC "Should we reshoot?"
                play sound "page turn.mp3" volume 0.5
                prod "We don’t have the time for that, I’m afraid, this take will have to do."
                jump next          
            "(BE MANIPULATIVE) I’ll do what I can to get what I want – for my character, that is.":
                hide screen countdown
                jump QTE8menu_slow
    label QTE8menu_slow:
        play sound "page turn.mp3" volume 0.5
        $ trendiness_score += 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        show screen score_display("Purple Empty Idle.png", "Red Flash.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        MC "Oh, you’re finally here… I was worried you had abandoned me."
        play sound "page turn.mp3" volume 0.5
        male_actor "Never, my love!"
        play sound "page turn.mp3" volume 0.5
        MC "I can always count on you… say, I need a favor, one that only you can fulfill."
        play sound "page turn.mp3" volume 0.5
        male_actor "What is it?"
        play sound "page turn.mp3" volume 0.5
        MC "You see… oh, I hate to ask this of you, but my sister needs a new kimono. We’ve really been struggling to get by, and you’re the only person I can trust to help me."
        play sound "page turn.mp3" volume 0.5
        male_actor "Well, I do have some I need to get off my hands… Can you afford them?"
        play sound "page turn.mp3" volume 0.5
        MC "Perhaps not now, but in the meantime, you’ll have my attention…"
        play sound "page turn.mp3" volume 0.5
        "([mcName] flirtatiously places her hand on his arm, and the man gasps.)"
        play sound "page turn.mp3" volume 0.5
        MC "Please?"
        play sound "page turn.mp3" volume 0.5
        male_actor "Alright… I’ll get you the kimono. But just this once."
        play sound "page turn.mp3" volume 0.5
        MC "And I’ll always be grateful, Hayakawa-kun."
        play sound "page turn.mp3" volume 0.5
        "(Filming ceases. The director looks pleased.)"
        play sound "page turn.mp3" volume 0.5
        direct "Cut!"
        play sound "page turn.mp3" volume 0.5
        prod "Fantastic work, MC-san! I would be counting all my coins if I had a woman like that… one sweet word, and the next thing I know, they’ll all disappear!"
        play sound "page turn.mp3" volume 0.5
        MC "Thank you, sir. I enjoy playing these roles, even if I don’t quite agree with them."
        play sound "page turn.mp3" volume 0.5
        jump next

label QTE9:
    label QTE9menu:
        $ time = 12.5
        $ timer_range = 12
        $ timer_jump = 'QTE9menu_slow'
        show screen countdown

        menu:
            "(CRITIQUE BOTH) Try to unite tradition and modernity. The real problem is something else.":
                hide screen countdown
                play sound "page turn.mp3" volume 0.5
                $ trendiness_score += 1
                python:
                    p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
                    relationship_bar = what_relationship_bar_to_use(relationship_score)
                show screen score_display("Green Flash.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                $ renpy.pause(0.5)
                show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
                MC "(angrily) Sister, don’t you understand?! In our world, the only thing we can do is submit to men, but we will never be rewarded for it. Look at us! You’re practically broke, and I nearly had my life taken from me. All we do is suffer. Why must geisha even exist?"
                play sound "page turn.mp3" volume 0.5
                "(The director looks pleased. Filming ceases.)"
                play sound "page turn.mp3" volume 0.5
                prod "Fantastic job, MC-san! That blew me away."
                play sound "page turn.mp3" volume 0.5
                MC "(bows) Thank you, sir."
                play sound "page turn.mp3" volume 0.5
                setsuko "I agree… You really are the star of the show."
                jump CH1FINALE          
            "(CRITIQUE TRADITION) Assert modernity over tradition. Modern girls are on the rise, after all.":
                hide screen countdown
                jump QTE9menu_slow
    label QTE9menu_slow:
        play sound "page turn.mp3" volume 0.5
        $ relationship_score -= 1
        python:
            p_star, b_star, g_star = what_star_sprites_to_use(trendiness_score, westernization_score, nationalism_score)
            relationship_bar = what_relationship_bar_to_use(relationship_score)
        $ renpy.pause(0.5)
        show screen score_display("Purple Empty Idle.png", "Blue Empty Idle.png", "Green Empty Idle.png", "industry_relations_idle", trendiness_score, westernization_score, nationalism_score)
        MC "(sadly) Sister… don’t you understand? In our world, the only thing we can do is submit to men… but we will never be rewarded for it. Look at us. You’re practically broke, and I nearly had my life taken from me. All we do is suffer… why must geisha even exist?"
        play sound "page turn.mp3" volume 0.5
        "(The director looks neutral. Filming ceases.)"
        play sound "page turn.mp3" volume 0.5
        prod "Not bad, [mcName]-san… That was a very somber way to end the film. Hopefully our audience won’t be too sad watching it."
        play sound "page turn.mp3" volume 0.5
        MC "I hope they’ll receive it well…"
        play sound "page turn.mp3" volume 0.5
        jump CH1FINALE