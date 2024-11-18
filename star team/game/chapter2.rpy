label start2:
    MC "Change is a strange thing. You think you’re smart enough to notice it – you live in this world, you’ll know if something is coming."

    scene black with fade
    MC "But then suddenly, it’s not a whisper anymore. It’s a wave."

    # Flashbacks begin
    toshiro "You’re overreacting. It’s a merge, Kazuo. You’re not getting fired."

    kazuo "This is just… I don’t know, aren’t you concerned?"

    toshiro "No? Why would I be concerned? So we do fewer films, work with fewer directors. Honestly, sounds like a burden off my back. Make fewer movies and make ‘em better, right?"

    kazuo "You’re always talking about movies and acting and the press… Don’t you think this is bigger than that?"

    toshiro "I don’t. But I do think yammering like a little paranoid boy is gonna piss everyone off."

    kazuo "I’m just… Something feels wrong."

    toshiro "Yeah, it’s probably your back from all that hunching and worrying."

    scene black with fade
    MC "Laws come sweeping in, the streets packed with soldiers. Over and over, movies pulled from theaters before screening."

    MC "Mark ups and re-markups. Arrests. The news started to sound the same – our nation. Do it for our nation."

    MC "Our people. The Emperor. Japan."

    MC "And the people changed too. The girls I saw donning lipstick and gossiping in cafes turned into the mothers of soldiers."

    MC "Young boys were standing straighter, no longer telling fairytales, but repeating the phrases from the radio."

    MC "Our people."

    MC "Our nation."

    MC "Japan."

    # Flashback with Kiyo and Producer
    prod "Yamaguchi, I’m telling you right now that you’re at risk."

    kiyo "At risk? For what? I understand the last film didn’t perform well, but–"

    prod "Your last movie wasn’t a matter of bad performance. You – WE were censored."

    kiyo "Censored?"

    prod "Banned. Completely. You might think your actions outside of here don’t matter, that you can just say what you want and flaunt your love for barbarians, but your actions are bigger than you."

    kiyo "I was only praising Western fashions. It was one comment!"

    prod "A comment that ended up in the damn newspaper! You might as well have declared yourself with the Allied forces for all that the censors care."

    prod "Clean up your act, or you’ll be cut. We’re only making two movies a month. We can’t afford to lose any of them to some fame-chasing braggart."

    kiyo "As if you care for anything more than money."

    prod "Right now, I just wanna stay out of trouble. Do the same. If not for the studio, then do it to save your own neck."

    MC "And so it was in that new world. A world that centered on our four islands, our nation, our people. On Japan alone, and above all."

    jump CH2prod

label CH2prod:
    prod "I’m glad you’ve survived the changes, MC. It’s been a rough year for all of us – thank you for always adapting."

    menu:
        "It’s not as though I have much of a choice…":
            $ response = "choice"
        "We all have a role to play in supporting the nation.":
            $ response = "role"

    if response == "choice":
        prod "(slight grimace) You make it sound as if you resent that. Do you?"

        menu:
            "Maybe a bit. (chance to lose immunity)":
                MC "Maybe a bit."
                # Trigger any consequence logic here if applicable
            "Of course not, I apologize. I’m grateful to still be employed.":
                MC "Of course not, I apologize. I’m grateful to still be employed."

    elif response == "role":
        prod "Yes, we do."

    prod "Movies aren’t just a way to entertain the masses anymore. Now, they’re a symbol of unity for Japan – a reminder of who we are, where we come from. Why we’re fighting. And, with that said, I have a new job for you."

    # Bucket movie options
    call bucket_movies

    prod "Let me know if you have any questions. Remember, these roles are bigger than you now. But that doesn’t mean you need to be any bigger. Keep yourself in check. Show them what they want to see, both in front of and behind the camera."

    scene change_to_set with fade
    kiyo "I can’t believe all these new laws. Censorship… What a ridiculous concept. Hiding things from the audience only makes them more tantalizing."

    setsuko "Oh, I don’t know, I think the new wave of films have been quite nice. There aren’t so many offputting scenes."

    kiyo "Offputting? What, you mean like kissing?"

    setsuko "Maybe, but I mean… There’s a sense of consistency nowadays – not so many politics and outside influences trying to tell you to be anything but Japanese!"

    kiyo "This industry thrived on controversy."

    setsuko "Clearly not, seeing as your last film didn’t even make it to theaters!"

    MC "Hello…"

    setsuko "MC! Finally, please try to talk some sense into Kiyo – I’m scared she’s going to get herself into even more trouble."

    MC "What kind of trouble?"

    kiyo "Apparently, I’m too ‘controversial’ for modern audiences. I even got pulled aside and threatened to tone it down. These censors have no idea what art even means anymore!"

    MC "What made your last film censorable?"

    kiyo "For starters, it would seem my body language is simply too ‘disagreeable’ – risque and American, like I can only play some kind of harlot or something! Blame the scriptwriters, not me!"

    setsuko "You’ve also been quite outspoken…"

    kiyo "I hardly think it’s controversial to say that these movies are formulaic. What happened to individuality, to the close-ups and passion we were doing with our old films?"

    setsuko "We don’t want to discourage the people from the war effort!"

    kiyo "Oh, it’s not the men I worry about. It’s those mothers happily waving their sons off to go die – like they’re never weeping at the shrines or lying awake terrified!"

    setsuko "What a horrible thing to talk about! MC, don’t you agree?"

    menu:
        "Kiyo has a point…":
            $ stance = "kiyo"
        "Setsuko is right.":
            $ stance = "setsuko"

    if stance == "kiyo":
        MC "I’ve seen the families of the men who get drafted. They never quite seem as happy as the ones we play…"

        kiyo "Anyone can just smile and look pretty, shed a glamorous tear, but where’s the reality? Nobody wants to see just another movie about how glorious war is when they know it isn’t!"

        setsuko "Stop it! Stop talking like that! Don’t you want to see us win?"

        kiyo "Of course I do! I love this country!"

        setsuko "Then why do you keep talking like you hate us?"

        kiyo "(sighs) I don’t hate Japan, I just don’t like this false, perfect image we’re giving of it. All the stories are the same, nothing feels alive anymore. There’s nothing human, can’t you feel it?"

    elif stance == "setsuko":
        MC "It’s important we show everyone how things should be. We’re at war, we can’t afford any kind of public upset."

        setsuko "Exactly. We can’t fight, but we can support those who are! It’s our duty as women – what good would it do to show us mourning and crying over and over again? It’s just selfish. Our sacrifices are different. You’ve said it yourself."

        kiyo "Maybe it would give those who are mourning and crying a little bit of peace? To know they’re not alone?"

        setsuko "It’s better to show the world we want to have. Be a role model for those women!"

        kiyo "I suppose you would consider that kind of woman a role model."

        setsuko "What’s that supposed to mean?"

        kiyo "That perfect little girl you’ve always played. You’ve never stepped out of line even once, have you? You’ve never spoken up, never challenged anyone. This is just the perfect sort of atmosphere for women like you, isn’t it?"

        setsuko "At least my films get to be seen."

    toshiro "(whistles) Ladies, ladies, what’s got us all riled up?"

    kiyo "Nothing that concerns you."

    toshiro "Calm down, hon, put those claws away. I was just asking a question. You know I hate to see your pretty face all screwed up like that."

    kiyo "You’d be just as angry if you were being told you’re a risk to the industry."

    toshiro "Yeah, I probably would be. Good thing I’m doing just fine."

    kiyo "Really? You haven’t noticed anything strange or different about the films we’re shooting?"

    toshiro "Nope. In fact, I’d say they’re just getting better. You should stop complaining – you’re still here, aren’t you? It’s not that hard to stay on their good side, you just need to talk less. Try it."

    "(he winks, then strides off.)"

    kiyo "Of course he’s happy. All the movies are about guys just like that nowadays. They can have anything they want with a fraction of the effort. It’s so pathetic."

    menu:
        "You’re being a little harsh, aren’t you?":
            $ harsh = True
        "That’s nothing new, though.":
            $ harsh = False

    if harsh:
        MC "Look at Kazuo. He’s never quite gotten the kind of recognition as Tōshiro, but I’d say he works twice as hard."

        kiyo "Yes, MC. Look at Kazuo. He’s not exactly leading man material, is he?"

        setsuko "Now that’s just cruel!"

        kiyo "I’m not insulting him, it’s just true. He has none of the qualities that make a man attractive – he stutters, he’s mousy, he’s small – and yet he’s never failed to show up next to Tōshiro on that screen. I make one bad move and I’m immediately getting shunted into walk-on parts!"

        setsuko "Kazuo is getting those roles because he’s good at them. That’s how it works here. Maybe you’re just not right for the scripts they’re writing."

        kiyo "Or maybe they need to write more than one type of script."

        MC "She has a point – you could try toning things down a bit? Just… do what they say."

        kiyo "Hm. Not all of us were made with such a flimsy sense of pride, girl."

    else:
        MC "All of our roles have been about the man we’re acting with. We’re the love interest, or the sister, or the mother… There just aren’t a lot of things for us to be."

        kiyo "And now there are even less."

        MC "We just have to work with what we have."

        kiyo "And are you satisfied with that?"

        setsuko "It doesn’t matter if she is or isn’t! We’re actors, not directors, not writers, and not politicians! We don’t decide what we say or do – we follow the script and that’s it."

        kiyo "That was your dream, when you started acting? Just to follow a script, get your paycheck, get your fame."

        setsuko "No, of course not."

        kiyo "Then what did you want?"

        setsuko "(shakes her head) You’re just trying to mess with me again. Well, I’m not playing your games. I’m here to work, to do what I’m supposed to do for my country and my family. I’m not just in it to prove something."

    kiyo "Fine. Do what feels right to you."

    setsuko "At least I’ll still have a job tomorrow. Maybe you should start thinking more practically, and put aside your pride for once in your life."

    setsuko "(leaves in a huff)"

    kiyo "Maybe here, you do exactly what they say. Maybe that’s enough for you. But don’t let yourself turn out like that – you’re more than the cast around you. You’ve got a soul."

    "(Kiyo leaves.)"

    MC "(internal) Everything is so strained… If we can’t even maintain peace among ourselves, what can we do?"

    jump producer_discussion

label producer_discussion:
    prod "MC, great, you’re here. I wanted to discuss something with you. Have a seat."

    menu:
        "Is everything alright?":
            MC "Is everything alright?"
            prod "Yes! Of course, everything is fine. I just wanted to let you know that there have been some… concerns with our recent film releases."
        "Am I in trouble?":
            MC "Am I in trouble?"
            prod "No, not at all! Not you, at least. There have just been some concerns, recently, from the higher offices."

    MC "Concerns?"

    prod "As one of the three remaining studios, we have a duty to play in creating films that don’t just entertain, but offer audiences a sense of unity. We must propagate correct morals, you understand that."

    menu:
        "Yes, but I miss the old kinds of films. (immunity -)":
            MC "Yes, but I miss the old kinds of films. Nowadays, things have gotten so extreme, haven’t they? It makes me wonder what a moral film even is."
            prod "A film that doesn’t disrupt the public peace, MC."
            MC "Even if that means lying?"
            prod "(leans forward) We are not lying. If you want to keep your job, you’ll never utter such a terrible accusation again."
            MC "You look scared."
            prod "I’m not– MC, you’re on thin ice. Do you want to end up like Yamaguchi? Or like Tachibana?"
            MC "…What do you mean?"
        "Of course.":
            MC "Of course. I cannot serve my country as a soldier, and I am not a sister or mother. It is all I can do to support the nation."
            MC "(internal) Even if all I do is spin lies…"
            prod "Good. Thank you for always being a model for the others here. Sometimes it feels as though you and Watanabe are the only ones I can rely on."
            MC "What about Setsuko?"
            prod "Ah yes, Wada. She’s been quite safe since the start. I used to worry she was too safe, actually. (a small laugh) Things have certainly changed, haven’t they…"
            MC "For the better, of course."
            MC "(internal) Another little lie. When will I stop?"
            prod "Right. Absolutely."

    prod "That actually brings me to my main point."

    prod "Tachibana has been removed from our studio. It is likely Yamaguchi will be facing a similar outcome, soon."

    menu:
        "But Kazuo hasn’t done anything wrong! (if Kazuo’s letter was read)":
            MC "But Kazuo hasn’t done anything wrong!"
            prod "(a look of panic) Have you been in contact with him?"
            menu:
                "Yes (immunity -).":
                    MC "Yes."
                    prod "To what extent, exactly?"
                    MC "He’s sent me letters."
                    prod "Do you have them with you?"
                    MC "They’re at my home."
                    prod "(covers his face with his hands) Destroy them."
                    menu:
                        "What? No!":
                            MC "What? No! All they say are–"
                            prod "Don’t tell me! Don’t tell anyone. Please, MC, for my sake if not for your own."
                            MC "He’s speaking the truth. He’s probably the only one right now!"
                            prod "There is no 'truth,' MC! There are just 'approved' and 'banned,' and right now, Kazuo is banned. And you are banned from contact with him, unless you want to join him in unemployment."
                            MC "This isn’t right."
                            prod "That doesn’t matter. Not anymore."
                            prod "(stands, placing his hands on the desk) I’m ending this conversation."
                        "Why?":
                            MC "Why?"
                            prod "Because Tachibana is no longer an ally to this nation, MC."
                            MC "Those letters are private."
                            prod "If you’re suspected of colluding with him, the police will think otherwise. And you’re not colluding with him, correct?"
                            MC "…No. He’s just my friend."
                            prod "Not anymore. Not so long as your name is associated with this studio. Do you understand?"
                            MC "Yes."
                "No…":
                    MC "No…"

        "What happened?":
            MC "What happened?"
            prod "There was an order for his removal – concern regarding his stance in this war."
            MC "I see…"
            MC "(internal) I suppose he didn’t keep his opinions to his letters…"
            MC "And Kiyo?"
            prod "I don’t know if you’ve been reading the magazines but… she’s not exactly the most popular person right now. She’s talented, so we want to keep using her but… (shakes his head) She makes it so difficult with her behavior. Please, MC, don’t be like her. We can’t afford to lose our two best."
            MC "(internal) He’s not including Setsuko in that category…? Even though she’s been doing so well lately?"

    prod "(straining a smile) You’ve been assigned to a new role, MC. It’s a big one, and we’re counting on you. Please, do your best."
    prod "(glances at the door, then whispers) If not for the country then… for yourself. In case you outlast this. And we… I hope you do."

# BUCKET MOVIE HERE
    prod "I’m glad to be working together again, MC."

    scene
    with fade

    kiyo "I can feel them watching me."

    setsuko "It’ll get better, things are just really tense right now."

    kiyo "Right now? It’s been years now, Setsuko."

    MC "Hello."


    setsuko "MC, how are you?"

    menu:
        "I’ve been better.":
            MC "I’ve been better."
            kiyo "Don’t I know it… Come here, let’s chat a little."
        "I’m okay.":
            MC "I’m okay."
            setsuko "I’m glad, if that’s true. Why don’t you join us? We were just talking a bit."

    MC "Are things alright?"

    setsuko "Of course!"

    kiyo "You’re a terrible liar, Setsuko."

    setsuko "That’s mean!"

    kiyo "Forgive me if this is the one place where I can voice an opinion."

    MC "What’s going on?"

    kiyo "What’s going on is that this is going to be my last film."

    setsuko "You don’t know that–"

    kiyo "I do, and you know what? I’ve accepted it."

    kiyo "I’m not suited for this kind of world. This isn’t the dream I had, all those years ago. I wanted to be someone special. The kind of woman that left a mark on those she met."

    setsuko "You are! You’re one of the best actresses out there!"

    kiyo "Please, stop trying to be nice. You can lie to yourself, but don’t lie to me. Every time I see my name in the papers… I don’t even want to look anymore. I’m all wrong to them. I love this country. I love my people. But they don’t love me."

    setsuko "We love you."

    kiyo "That isn’t enough. I wish it was, but it’s not."

    MC "Kiyo…"

    toshiro "(enters) God, you’d think someone just died. Where’re those pretty smiles?"

    kiyo "What do you want?"

    toshiro "I want someone to tell me what the hell is going on. First, Kazuo starts talking all doomsday, then he gets fired, now you’re all whispering like you’ve got some kind of conspiracy going on."

    toshiro "Any of you care to explain? MC, you’ve always been my girl – tell me."

    MC "(internal) Does he really not know…?"

    menu:
        "The studio is making changes. That’s it.":
            MC "The studio is making changes. That’s it."
            toshiro "Really? You too, huh? I swear, everyone is acting like the world’s falling apart. We’re winning this war. I don’t get what all the fuss is."
            kiyo "We must live in different realities."
            toshiro "Maybe. But you know, I don’t think Kazuo actually got fired."
            setsuko "He did, he–"
            toshiro "Nah, he probably got drafted and just didn’t want us to worry. He’s always been like that – little peacekeeper."
        "Can you keep a secret?":
            toshiro "Anything for you."
            MC "I got a letter from him."
            toshiro "Me too. Whole bunch of nonsense, I couldn’t even get through half of it. Kid’s a moron if he believes in any of that anti-Japanese propaganda they’re pushing overseas."
            MC "Then you know what’s going on."
            toshiro "If you’re trying to tell me he’s gotten carted off by the cops or something, you’re wrong. You know, I don’t even think he got fired."
            setsuko "What? Then what happened?"
            toshiro "He probably got drafted and freaked out, started writing a whole bunch of stuff he didn’t believe. He’s always been like that – bit of a coward."

    toshiro "Personally, I think it’s an honor to get to serve like that."

    setsuko "I do too. My brother keeps talking about it, how he might receive his notice soon."

    toshiro "Hope he doesn’t start throwing a fit, too!"

    kiyo "Why don’t you just go, then, if you’re so eager?"

    toshiro "(shrugs) I’m needed here. I keep the people excited about this war. Anyone can hold a gun – I’m sure even lil Kazuo’s got one cradled right now. I was given something special though. It’s my duty to show up on that screen."

    kiyo "You’re despicable."

    toshiro "According to the magazines, that’s an adjective for you."

    setsuko "Everyone here is just doing their best, aren’t they? We’re just doing what we’ve been told."

    menu:
        "And you’re satisfied with that? (immunity-).":
            MC "And you’re satisfied with that?"
            setsuko "What else do you want me to do?"
            MC "Say something. Do something."
            setsuko "I am doing something. Every day that I’m here I’m making sure that people have hope. I’m showing people that we are in a country that’s worth fighting for."
            MC "What about this is worth saving?"
            setsuko "It won’t always be this way. The war will end and then–"
            kiyo "And then we’ll all be happy. With our thousands dead and mouths taped shut and–"
        "Setsuko i

