label start2:
    MCWar "Change is a strange thing. You think you’re smart enough to notice it – you live in this world, you’ll know if something is coming."
    play sound "page turn.mp3" volume 0.5

    scene black with fade
    MCWar "But then suddenly, it’s not a whisper anymore. It’s a wave."
    play sound "page turn.mp3" volume 0.5
    # Flashbacks begin
    scene office_war
    show flashback
    toshiroWar "You’re overreacting. It’s a merge, Kazuo. You’re not getting fired."
    play sound "page turn.mp3" volume 0.5

    kazuoWar "This is just… I don’t know, aren’t you concerned?"
    play sound "page turn.mp3" volume 0.5

    toshiroWar "No? Why would I be concerned? So we do fewer films, work with fewer directors. Honestly, sounds like a burden off my back. Make fewer movies and make ‘em better, right?"
    play sound "page turn.mp3" volume 0.5

    kazuoWar "You’re always talking about movies and acting and the press… Don’t you think this is bigger than that?"
    play sound "page turn.mp3" volume 0.5

    toshiroWar "I don’t. But I do think yammering like a little paranoid boy is gonna piss everyone off."
    play sound "page turn.mp3" volume 0.5

    kazuoWar "I’m just… Something feels wrong."
    play sound "page turn.mp3" volume 0.5

    toshiroWar "Yeah, it’s probably your back from all that hunching and worrying."
    play sound "page turn.mp3" volume 0.5
   
    hide flashback
    scene black with fade
    MCWar "Laws come sweeping in, the streets packed with soldiers. Over and over, movies pulled from theaters before screening."
    play sound "page turn.mp3" volume 0.5

    MCWar "Mark ups and re-markups. Arrests. The news started to sound the same – our nation. Do it for our nation."
    play sound "page turn.mp3" volume 0.5

    MCWar "Our people. The Emperor. Japan."
    play sound "page turn.mp3" volume 0.5

    MCWar "And the people changed too. The girls I saw donning lipstick and gossiping in cafes turned into the mothers of soldiers."
    play sound "page turn.mp3" volume 0.5

    MCWar "Young boys were standing straighter, no longer telling fairytales, but repeating the phrases from the radio."
    play sound "page turn.mp3" volume 0.5

    MCWar "Our people."
    play sound "page turn.mp3" volume 0.5

    MCWar "Our nation."
    play sound "page turn.mp3" volume 0.5

    MCWar "Japan."
    play sound "page turn.mp3" volume 0.5

    scene office_war
    show flashback
    # Flashback with Kiyo and Producer
    prod "Yamaguchi, I’m telling you right now that you’re at risk."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "At risk? For what? I understand the last film didn’t perform well, but–"
    play sound "page turn.mp3" volume 0.5

    prod "Your last movie wasn’t a matter of bad performance. You – WE were censored."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Censored?"
    play sound "page turn.mp3" volume 0.5

    prod "Banned. Completely. You might think your actions outside of here don’t matter, that you can just say what you want and flaunt your love for barbarians, but your actions are bigger than you."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "I was only praising Western fashions. It was one comment!"
    play sound "page turn.mp3" volume 0.5

    prod "A comment that ended up in the damn newspaper! You might as well have declared yourself with the Allied forces for all that the censors care."
    play sound "page turn.mp3" volume 0.5

    prod "Clean up your act, or you’ll be cut. We’re only making two movies a month. We can’t afford to lose any of them to some fame-chasing braggart."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "As if you care for anything more than money."
    play sound "page turn.mp3" volume 0.5

    prod "Right now, I just wanna stay out of trouble. Do the same. If not for the studio, then do it to save your own neck."
    play sound "page turn.mp3" volume 0.5

    MCWar "And so it was in that new world. A world that centered on our four islands, our nation, our people. On Japan alone, and above all."
    play sound "page turn.mp3" volume 0.5

    jump CH2prod

label CH2prod:
    hide flashback
    prod "I’m glad you’ve survived the changes, [mcName]. It’s been a rough year for all of us – thank you for always adapting."
    play sound "page turn.mp3" volume 0.5

    menu:
        "It’s not as though I have much of a choice…":
            $ response = "choice"
        "We all have a role to play in supporting the nation.":
            $ response = "role"

    if response == "choice":
        prod "(slight grimace) You make it sound as if you resent that. Do you?"

        menu:
            "Maybe a bit.":
                MCWar "Maybe a bit."
                # Trigger any consequence logic here if applicable
            "Of course not, I apologize. I’m grateful to still be employed.":
                MCWar "Of course not, I apologize. I’m grateful to still be employed."

    elif response == "role":
        prod "Yes, we do."
        play sound "page turn.mp3" volume 0.5
    

    prod "Movies aren’t just a way to entertain the masses anymore. Now, they’re a symbol of unity for Japan – a reminder of who we are, where we come from. Why we’re fighting. And, with that said, I have a new job for you."
    play sound "page turn.mp3" volume 0.5

    # Bucket movie options
    prod "Let me know if you have any questions. Remember, these roles are bigger than you now. But that doesn’t mean you need to be any bigger. Keep yourself in check. Show them what they want to see, both in front of and behind the camera."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "I can’t believe all these new laws. Censorship… What a ridiculous concept. Hiding things from the audience only makes them more tantalizing."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "Oh, I don’t know, I think the new wave of films have been quite nice. There aren’t so many offputting scenes."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Offputting? What, you mean like kissing?"
    play sound "page turn.mp3" volume 0.5

    setsukoWar "Maybe, but I mean… There’s a sense of consistency nowadays – not so many politics and outside influences trying to tell you to be anything but Japanese!"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "This industry thrived on controversy."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "Clearly not, seeing as your last film didn’t even make it to theaters!"
    play sound "page turn.mp3" volume 0.5

    MCWar "Hello…"
    play sound "page turn.mp3" volume 0.5

    setsukoWar "[mcName]! Finally, please try to talk some sense into Kiyo – I’m scared she’s going to get herself into even more trouble."
    play sound "page turn.mp3" volume 0.5

    MCWar "What kind of trouble?"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Apparently, I’m too ‘controversial’ for modern audiences. I even got pulled aside and threatened to tone it down. These censors have no idea what art even means anymore!"
    play sound "page turn.mp3" volume 0.5

    MCWar "What made your last film censorable?"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "For starters, it would seem my body language is simply too ‘disagreeable’ – risque and American, like I can only play some kind of harlot or something! Blame the scriptwriters, not me!"
    play sound "page turn.mp3" volume 0.5

    setsukoWar "You’ve also been quite outspoken…"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "I hardly think it’s controversial to say that these movies are formulaic. What happened to individuality, to the close-ups and passion we were doing with our old films?"
    play sound "page turn.mp3" volume 0.5

    setsukoWar "We don’t want to discourage the people from the war effort!"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Oh, it’s not the men I worry about. It’s those mothers happily waving their sons off to go die – like they’re never weeping at the shrines or lying awake terrified!"
    play sound "page turn.mp3" volume 0.5

    setsukoWar "What a horrible thing to talk about! [mcName], don’t you agree?"
    play sound "page turn.mp3" volume 0.5

    menu:
        "Kiyo has a point…":
            $ stance = "kiyoWar"
        "Setsuko is right.":
            $ stance = "setsukoWar"

    if stance == "kiyoWar":
        MCWar "I’ve seen the families of the men who get drafted. They never quite seem as happy as the ones we play…"
        play sound "page turn.mp3" volume 0.5

        kiyoWar "Anyone can just smile and look pretty, shed a glamorous tear, but where’s the reality? Nobody wants to see just another movie about how glorious war is when they know it isn’t!"
        play sound "page turn.mp3" volume 0.5

        setsukoWar "Stop it! Stop talking like that! Don’t you want to see us win?"
        play sound "page turn.mp3" volume 0.5

        kiyoWar "Of course I do! I love this country!"
        play sound "page turn.mp3" volume 0.5

        setsukoWar "Then why do you keep talking like you hate us?"
        play sound "page turn.mp3" volume 0.5

        kiyoWar "(sighs) I don’t hate Japan, I just don’t like this false, perfect image we’re giving of it. All the stories are the same, nothing feels alive anymore. There’s nothing human, can’t you feel it?"
        play sound "page turn.mp3" volume 0.5

    elif stance == "setsukoWar":
        MCWar "It’s important we show everyone how things should be. We’re at war, we can’t afford any kind of public upset."
        play sound "page turn.mp3" volume 0.5

        setsukoWar "Exactly. We can’t fight, but we can support those who are! It’s our duty as women – what good would it do to show us mourning and crying over and over again? It’s just selfish. Our sacrifices are different. You’ve said it yourself."
        play sound "page turn.mp3" volume 0.5

        kiyoWar "Maybe it would give those who are mourning and crying a little bit of peace? To know they’re not alone?"
        play sound "page turn.mp3" volume 0.5

        setsukoWar "It’s better to show the world we want to have. Be a role model for those women!"
        play sound "page turn.mp3" volume 0.5

        kiyoWar "I suppose you would consider that kind of woman a role model."
        play sound "page turn.mp3" volume 0.5

        setsukoWar "What’s that supposed to mean?"
        play sound "page turn.mp3" volume 0.5

        kiyoWar "That perfect little girl you’ve always played. You’ve never stepped out of line even once, have you? You’ve never spoken up, never challenged anyone. This is just the perfect sort of atmosphere for women like you, isn’t it?"
        play sound "page turn.mp3" volume 0.5

        setsukoWar "At least my films get to be seen."
        play sound "page turn.mp3" volume 0.5

    toshiroWar "(whistles) Ladies, ladies, what’s got us all riled up?"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Nothing that concerns you."
    play sound "page turn.mp3" volume 0.5

    toshiroWar "Calm down, hon, put those claws away. I was just asking a question. You know I hate to see your pretty face all screwed up like that."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "You’d be just as angry if you were being told you’re a risk to the industry."
    play sound "page turn.mp3" volume 0.5

    toshiroWar "Yeah, I probably would be. Good thing I’m doing just fine."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Really? You haven’t noticed anything strange or different about the films we’re shooting?"
    play sound "page turn.mp3" volume 0.5

    toshiroWar "Nope. In fact, I’d say they’re just getting better. You should stop complaining – you’re still here, aren’t you? It’s not that hard to stay on their good side, you just need to talk less. Try it."
    play sound "page turn.mp3" volume 0.5

    "(he winks, then strides off.)"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Of course he’s happy. All the movies are about guys just like that nowadays. They can have anything they want with a fraction of the effort. It’s so pathetic."
    play sound "page turn.mp3" volume 0.5

    menu:
        "You’re being a little harsh, aren’t you?":
            $ harsh = True
        "That’s nothing new, though.":
            $ harsh = False

    if harsh:
        MCWar "Look at Kazuo. He’s never quite gotten the kind of recognition as Tōshiro, but I’d say he works twice as hard."
        play sound "page turn.mp3" volume 0.5

        kiyoWar "Yes, [mcName]. Look at Kazuo. He’s not exactly leading man material, is he?"
        play sound "page turn.mp3" volume 0.5

        setsukoWar "Now that’s just cruel!"
        play sound "page turn.mp3" volume 0.5

        kiyoWar "I’m not insulting him, it’s just true. He has none of the qualities that make a man attractive – he stutters, he’s mousy, he’s small – and yet he’s never failed to show up next to Tōshiro on that screen. I make one bad move and I’m immediately getting shunted into walk-on parts!"
        play sound "page turn.mp3" volume 0.5

        setsukoWar "Kazuo is getting those roles because he’s good at them. That’s how it works here. Maybe you’re just not right for the scripts they’re writing."
        play sound "page turn.mp3" volume 0.5

        kiyoWar "Or maybe they need to write more than one type of script."
        play sound "page turn.mp3" volume 0.5

        MCWar "She has a point – you could try toning things down a bit? Just… do what they say."
        play sound "page turn.mp3" volume 0.5

        kiyoWar "Hm. Not all of us were made with such a flimsy sense of pride, girl."
        play sound "page turn.mp3" volume 0.5

    else:
        MCWar "All of our roles have been about the man we’re acting with. We’re the love interest, or the sister, or the mother… There just aren’t a lot of things for us to be."
        play sound "page turn.mp3" volume 0.5

        kiyoWar "And now there are even less."
        play sound "page turn.mp3" volume 0.5

        MCWar "We just have to work with what we have."
        play sound "page turn.mp3" volume 0.5

        kiyoWar "And are you satisfied with that?"
        play sound "page turn.mp3" volume 0.5

        setsukoWar "It doesn’t matter if she is or isn’t! We’re actors, not directors, not writers, and not politicians! We don’t decide what we say or do – we follow the script and that’s it."
        play sound "page turn.mp3" volume 0.5

        kiyoWar "That was your dream, when you started acting? Just to follow a script, get your paycheck, get your fame."
        play sound "page turn.mp3" volume 0.5

        setsukoWar "No, of course not."
        play sound "page turn.mp3" volume 0.5

        kiyoWar "Then what did you want?"
        play sound "page turn.mp3" volume 0.5

        setsukoWar "(shakes her head) You’re just trying to mess with me again. Well, I’m not playing your games. I’m here to work, to do what I’m supposed to do for my country and my family. I’m not just in it to prove something."
        play sound "page turn.mp3" volume 0.5

    kiyoWar "Fine. Do what feels right to you."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "At least I’ll still have a job tomorrow. Maybe you should start thinking more practically, and put aside your pride for once in your life."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "(leaves in a huff)"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Maybe here, you do exactly what they say. Maybe that’s enough for you. But don’t let yourself turn out like that – you’re more than the cast around you. You’ve got a soul."
    play sound "page turn.mp3" volume 0.5

    "(Kiyo leaves.)"
    play sound "page turn.mp3" volume 0.5

    MCWar "(internal) Everything is so strained… If we can’t even maintain peace among ourselves, what can we do?"
    play sound "page turn.mp3" volume 0.5

    jump producer_discussion

label producer_discussion:
    prod "[mcName], great, you’re here. I wanted to discuss something with you. Have a seat."
    play sound "page turn.mp3" volume 0.5

    menu:
        "Is everything alright?":
            MCWar "Is everything alright?"
            play sound "page turn.mp3" volume 0.5

            prod "Yes! Of course, everything is fine. I just wanted to let you know that there have been some… concerns with our recent film releases."
            play sound "page turn.mp3" volume 0.5

        "Am I in trouble?":
            MCWar "Am I in trouble?"
            play sound "page turn.mp3" volume 0.5

            prod "No, not at all! Not you, at least. There have just been some concerns, recently, from the higher offices."
            play sound "page turn.mp3" volume 0.5

    MCWar "Concerns?"
    play sound "page turn.mp3" volume 0.5

    prod "As one of the three remaining studios, we have a duty to play in creating films that don’t just entertain, but offer audiences a sense of unity. We must propagate correct morals, you understand that."
    play sound "page turn.mp3" volume 0.5

    menu:
        "Yes, but I miss the old kinds of films.":
            MCWar "Yes, but I miss the old kinds of films. Nowadays, things have gotten so extreme, haven’t they? It makes me wonder what a moral film even is."
            play sound "page turn.mp3" volume 0.5

            prod "A film that doesn’t disrupt the public peace, [mcName]."
            play sound "page turn.mp3" volume 0.5

            MCWar "Even if that means lying?"
            play sound "page turn.mp3" volume 0.5

            prod "(leans forward) We are not lying. If you want to keep your job, you’ll never utter such a terrible accusation again."
            play sound "page turn.mp3" volume 0.5

            MCWar "You look scared."
            play sound "page turn.mp3" volume 0.5

            prod "I’m not– [mcName], you’re on thin ice. Do you want to end up like Yamaguchi? Or like Tachibana?"
            play sound "page turn.mp3" volume 0.5

            MCWar "…What do you mean?"
            play sound "page turn.mp3" volume 0.5

        "Of course.":
            MCWar "Of course. I cannot serve my country as a soldier, and I am not a sister or mother. It is all I can do to support the nation."
            play sound "page turn.mp3" volume 0.5

            MCWar "(internal) Even if all I do is spin lies…"
            play sound "page turn.mp3" volume 0.5

            prod "Good. Thank you for always being a model for the others here. Sometimes it feels as though you and Watanabe are the only ones I can rely on."
            play sound "page turn.mp3" volume 0.5

            MCWar "What about Setsuko?"
            play sound "page turn.mp3" volume 0.5

            prod "Ah yes, Wada. She’s been quite safe since the start. I used to worry she was too safe, actually. (a small laugh) Things have certainly changed, haven’t they…"
            play sound "page turn.mp3" volume 0.5

            MCWar "For the better, of course."
            play sound "page turn.mp3" volume 0.5

            MCWar "(internal) Another little lie. When will I stop?"
            play sound "page turn.mp3" volume 0.5

            prod "Right. Absolutely."
            play sound "page turn.mp3" volume 0.5


    prod "That actually brings me to my main point."
    play sound "page turn.mp3" volume 0.5

    prod "Tachibana has been removed from our studio. It is likely Yamaguchi will be facing a similar outcome, soon."
    play sound "page turn.mp3" volume 0.5

    menu:
        "But Kazuo hasn’t done anything wrong! (if Kazuo’s letter was read)":
            MCWar "But Kazuo hasn’t done anything wrong!"
            play sound "page turn.mp3" volume 0.5

            prod "(a look of panic) Have you been in contact with him?"
            play sound "page turn.mp3" volume 0.5

            menu:
                "Yes.":
                    MCWar "Yes."
                    play sound "page turn.mp3" volume 0.5

                    prod "To what extent, exactly?"
                    play sound "page turn.mp3" volume 0.5

                    MCWar "He’s sent me letters."
                    play sound "page turn.mp3" volume 0.5

                    prod "Do you have them with you?"
                    play sound "page turn.mp3" volume 0.5

                    MCWar "They’re at my home."
                    play sound "page turn.mp3" volume 0.5

                    prod "(covers his face with his hands) Destroy them."
                    play sound "page turn.mp3" volume 0.5

                    menu:
                        "What? No!":
                            MCWar "What? No! All they say are–"
                            play sound "page turn.mp3" volume 0.5

                            prod "Don’t tell me! Don’t tell anyone. Please, [mcName], for my sake if not for your own."
                            play sound "page turn.mp3" volume 0.5

                            MCWar "He’s speaking the truth. He’s probably the only one right now!"
                            play sound "page turn.mp3" volume 0.5

                            prod "There is no 'truth,' [mcName]! There are just 'approved' and 'banned,' and right now, Kazuo is banned. And you are banned from contact with him, unless you want to join him in unemployment."
                            play sound "page turn.mp3" volume 0.5

                            MCWar "This isn’t right."
                            play sound "page turn.mp3" volume 0.5

                            prod "That doesn’t matter. Not anymore."
                            play sound "page turn.mp3" volume 0.5

                            prod "(stands, placing his hands on the desk) I’m ending this conversation."
                            play sound "page turn.mp3" volume 0.5

                        "Why?":
                            MCWar "Why?"
                            play sound "page turn.mp3" volume 0.5

                            prod "Because Tachibana is no longer an ally to this nation, [mcName]."
                            play sound "page turn.mp3" volume 0.5

                            MCWar "Those letters are private."
                            play sound "page turn.mp3" volume 0.5

                            prod "If you’re suspected of colluding with him, the police will think otherwise. And you’re not colluding with him, correct?"
                            play sound "page turn.mp3" volume 0.5

                            MCWar "…No. He’s just my friend."
                            play sound "page turn.mp3" volume 0.5

                            prod "Not anymore. Not so long as your name is associated with this studio. Do you understand?"
                            play sound "page turn.mp3" volume 0.5

                            MCWar "Yes."
                            play sound "page turn.mp3" volume 0.5

                "No…":
                    MCWar "No…"
                    play sound "page turn.mp3" volume 0.5


        "What happened?":
            MCWar "What happened?"
            play sound "page turn.mp3" volume 0.5

            prod "There was an order for his removal – concern regarding his stance in this war."
            play sound "page turn.mp3" volume 0.5

            MCWar "I see…"
            play sound "page turn.mp3" volume 0.5

            MCWar "(internal) I suppose he didn’t keep his opinions to his letters…"
            play sound "page turn.mp3" volume 0.5

            MCWar "And Kiyo?"
            play sound "page turn.mp3" volume 0.5

            prod "I don’t know if you’ve been reading the magazines but… she’s not exactly the most popular person right now. She’s talented, so we want to keep using her but… (shakes his head) She makes it so difficult with her behavior. Please, [mcName], don’t be like her. We can’t afford to lose our two best."
            play sound "page turn.mp3" volume 0.5

            MCWar "(internal) He’s not including Setsuko in that category…? Even though she’s been doing so well lately?"
            play sound "page turn.mp3" volume 0.5


    prod "(straining a smile) You’ve been assigned to a new role, [mcName]. It’s a big one, and we’re counting on you. Please, do your best."
    play sound "page turn.mp3" volume 0.5

    prod "(glances at the door, then whispers) If not for the country then… for yourself. In case you outlast this. And we… I hope you do."
    play sound "page turn.mp3" volume 0.5


# BUCKET MOVIE HERE
    prod "I’m glad to be working together again, [mcName]."
    play sound "page turn.mp3" volume 0.5

    scene
    with fade

    kiyoWar "I can feel them watching me."
    play sound "page turn.mp3" volume 0.5


    setsukoWar "It’ll get better, things are just really tense right now."
    play sound "page turn.mp3" volume 0.5


    kiyoWar "Right now? It’s been years now, Setsuko."
    play sound "page turn.mp3" volume 0.5


    MCWar "Hello."
    play sound "page turn.mp3" volume 0.5


    setsukoWar "[mcName], how are you?"
    play sound "page turn.mp3" volume 0.5

    menu:
        "I’ve been better.":
            MCWar "I’ve been better."
            play sound "page turn.mp3" volume 0.5

            kiyoWar "Don’t I know it… Come here, let’s chat a little."
            play sound "page turn.mp3" volume 0.5

        "I’m okay.":
            MCWar "I’m okay."
            play sound "page turn.mp3" volume 0.5

            setsukoWar "I’m glad, if that’s true. Why don’t you join us? We were just talking a bit."
            play sound "page turn.mp3" volume 0.5


    MCWar "Are things alright?"
    play sound "page turn.mp3" volume 0.5

    setsukoWar "Of course!"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "You’re a terrible liar, Setsuko."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "That’s mean!"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Forgive me if this is the one place where I can voice an opinion."
    play sound "page turn.mp3" volume 0.5

    MCWar "What’s going on?"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "What’s going on is that this is going to be my last film."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "You don’t know that–"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "I do, and you know what? I’ve accepted it."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "I’m not suited for this kind of world. This isn’t the dream I had, all those years ago. I wanted to be someone special. The kind of woman that left a mark on those she met."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "You are! You’re one of the best actresses out there!"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Please, stop trying to be nice. You can lie to yourself, but don’t lie to me. Every time I see my name in the papers… I don’t even want to look anymore. I’m all wrong to them. I love this country. I love my people. But they don’t love me."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "We love you."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "That isn’t enough. I wish it was, but it’s not."
    play sound "page turn.mp3" volume 0.5

    MCWar "Kiyo…"
    play sound "page turn.mp3" volume 0.5

    toshiroWar "(enters) God, you’d think someone just died. Where’re those pretty smiles?"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "What do you want?"
    play sound "page turn.mp3" volume 0.5

    toshiroWar "I want someone to tell me what the hell is going on. First, Kazuo starts talking all doomsday, then he gets fired, now you’re all whispering like you’ve got some kind of conspiracy going on."
    play sound "page turn.mp3" volume 0.5

    toshiroWar "Any of you care to explain? [mcName], you’ve always been my girl – tell me."
    play sound "page turn.mp3" volume 0.5

    MCWar "(internal) Does he really not know…?"
    play sound "page turn.mp3" volume 0.5

    menu:
        "The studio is making changes. That’s it.":
            MCWar "The studio is making changes. That’s it."
            play sound "page turn.mp3" volume 0.5

            toshiroWar "Really? You too, huh? I swear, everyone is acting like the world’s falling apart. We’re winning this war. I don’t get what all the fuss is."
            play sound "page turn.mp3" volume 0.5

            kiyoWar "We must live in different realities."
            play sound "page turn.mp3" volume 0.5

            toshiroWar "Maybe. But you know, I don’t think Kazuo actually got fired."
            play sound "page turn.mp3" volume 0.5

            setsukoWar "He did, he–"
            play sound "page turn.mp3" volume 0.5

            toshiroWar "Nah, he probably got drafted and just didn’t want us to worry. He’s always been like that – little peacekeeper."
            play sound "page turn.mp3" volume 0.5

        "Can you keep a secret?":
            toshiroWar "Anything for you."
            play sound "page turn.mp3" volume 0.5

            MCWar "I got a letter from him."
            play sound "page turn.mp3" volume 0.5

            toshiroWar "Me too. Whole bunch of nonsense, I couldn’t even get through half of it. Kid’s a moron if he believes in any of that anti-Japanese propaganda they’re pushing overseas."
            play sound "page turn.mp3" volume 0.5

            MCWar "Then you know what’s going on."
            play sound "page turn.mp3" volume 0.5

            toshiroWar "If you’re trying to tell me he’s gotten carted off by the cops or something, you’re wrong. You know, I don’t even think he got fired."
            play sound "page turn.mp3" volume 0.5

            setsukoWar "What? Then what happened?"
            play sound "page turn.mp3" volume 0.5

            toshiroWar "He probably got drafted and freaked out, started writing a whole bunch of stuff he didn’t believe. He’s always been like that – bit of a coward."
            play sound "page turn.mp3" volume 0.5


    toshiroWar "Personally, I think it’s an honor to get to serve like that."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "I do too. My brother keeps talking about it, how he might receive his notice soon."
    play sound "page turn.mp3" volume 0.5

    toshiroWar "Hope he doesn’t start throwing a fit, too!"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "Why don’t you just go, then, if you’re so eager?"
    play sound "page turn.mp3" volume 0.5

    toshiroWar "(shrugs) I’m needed here. I keep the people excited about this war. Anyone can hold a gun – I’m sure even lil Kazuo’s got one cradled right now. I was given something special though. It’s my duty to show up on that screen."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "You’re despicable."
    play sound "page turn.mp3" volume 0.5

    toshiroWar "According to the magazines, that’s an adjective for you."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "Everyone here is just doing their best, aren’t they? We’re just doing what we’ve been told."
    play sound "page turn.mp3" volume 0.5

    MCWar "..."
    menu:
        "And you’re satisfied with that?":
            MCWar "And you’re satisfied with that?"
            play sound "page turn.mp3" volume 0.5

            setsukoWar "What else do you want me to do?"
            play sound "page turn.mp3" volume 0.5

            MCWar "Say something. Do something."
            play sound "page turn.mp3" volume 0.5

            setsukoWar "I am doing something. Every day that I’m here I’m making sure that people have hope. I’m showing people that we are in a country that’s worth fighting for."
            play sound "page turn.mp3" volume 0.5

            MCWar "What about this is worth saving?"
            play sound "page turn.mp3" volume 0.5

            setsukoWar "It won’t always be this way. The war will end and then–"
            play sound "page turn.mp3" volume 0.5

            kiyoWar "And then we’ll all be happy. With our thousands dead and mouths taped shut and–"
            play sound "page turn.mp3" volume 0.5

        "Setsuko is right. We shouldn’t fight.":
            MCWar "Setsuko is right. We shouldn’t fight."
            play sound "page turn.mp3" volume 0.5

            kiyoWar "Duty, duty, duty. I’m so sick of that word. It’s my duty to wear some silly smock. It’s my duty to be a perfect wife. It’s my duty to watch my friends be shipped out overseas and applaud them for dying–"
            play sound "page turn.mp3" volume 0.5

            toshiroWar "It’s a necessary sacrifice."
            play sound "page turn.mp3" volume 0.5

            kiyoWar "None of this is necessary."
            play sound "page turn.mp3" volume 0.5

            setsukoWar "You can’t just think of yourself. We’re not just individuals, we’re a whole. All of us together, our Emperor, we make up the soul of the nation."
            play sound "page turn.mp3" volume 0.5

            kiyoWar "I’m starting to doubt this nation ever had a soul."
            play sound "page turn.mp3" volume 0.5


    toshiroWar "Oi, watch it, all of you."
    play sound "page turn.mp3" volume 0.5


    toshiroWar "You keep those kinds of opinions to yourself, alright? I don’t wanna see another friend go missing. Just toe the line – don’t make things more complicated than they have to be."
    play sound "page turn.mp3" volume 0.5

    toshiroWar "Kinuya-san! Fantastic timing. I wanted to ask you about a line in scene four…"
    play sound "page turn.mp3" volume 0.5

    kiyoWar "He’s right. I’ve made my peace."
    play sound "page turn.mp3" volume 0.5

    setsukoWar "Let’s just… make this the best film yet."
    play sound "page turn.mp3" volume 0.5

    kiyoWar "You two better not forget me when I’m gone."
    play sound "page turn.mp3" volume 0.5

    MCWar "We could never."
    play sound "page turn.mp3" volume 0.5

    MCWar "(internal) And just like that, our little group had changed forever. And maybe I had, too. Maybe I really needed to decide who I was. Or maybe I needed to keep it hidden, and hope the world changed instead."
    play sound "page turn.mp3" volume 0.5

    return
