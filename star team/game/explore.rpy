screen streetView():
    zorder 5
    imagebutton:
        idle "post_office_dot.png"  # Use a simple test image
        hover "post_office_dot.png"
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
    play sound "page turn.mp3" volume 0.5
    setsuko "Dear [mcName],"
    setsuko "I do miss you so much! Everyone at the academy still asks about you - especially Katsuhiko, do you remember him?"
    setsuko "I wouldn't be surprised if he proposed to you the moment you come home! Though I'm sure your feelings about him haven't changed on bit"
    setsuko "Have you heard the news about Haruhi? The poor thing, she just arrived in town three days ago and she’s heartbroken. The way the critics spoke of her was so cruel, calling her ‘boring’ and ‘plain’! I think I’d absolutely shatter if anyone said such things about me."
    setsuko "I don’t know if I’d be able to take on another role. I thought she did a lovely job, didn’t you? Especially next to that handsome young man… It made me wonder how I might have played that role differently if they’d given it to me. Maybe one day I’ll get to try!"
    setsuko "Do come and visit us here – it’s getting rather dull without any word from you. And I wouldn’t mind a souvenir or two from Tokyo, if you have the time! You know how I’ve always loved those prints."
    setsuko "Perhaps I’ll get one for myself, if I finally find a long-term studio! Oh, I dream too much, don’t I? All the same, I miss you so much. Love from all us at the academy and all your friends and family back home!"
    "-Wada Setusko"
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
    "March 10, 1933"
    "EMBRACE MODERN LOOKS"
    "Fashions from the United States take young women, calling themselves 'modern girls,' by storm!"
    "A NEW KIND OF MUSIC"
    "Jazz singers have been all the rage lately~ Join us at the Blue Sky Lounge on Saturdays at 8PM to hear a soulful, vibrant sound unlike anything before!"

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
    "March 10 1933"
    "BID FAREWELL TO THE BENSHI"
    "The once-beloved members of our theater industry fade as an influx of new ‘talkies’ take to the silver screen. “They’ve been trying to get rid of us for years,” said former-benshi Nakashima Kazuo. “First it was those regulations, then those scripts, now we’re just a ghost of the past…”"
    "JAPN WITHDRAWS FROM THE LEAGUE OF NATIONS"
    "In light of efforts in Manchuria, officials have decided it is for the best that Japan withdraw from the League."

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

screen streetView2():
    zorder 5
    imagebutton:
        idle "post_office_dot.png"  # Use a simple test image
        hover "post_office_dot.png"
        xalign 0.5
        yalign 0.8
        action [ToggleScreen("streetView2"), Jump("parents_letter")]
    imagebutton:
        idle "news_dot.png"  # Use a simple test image
        hover "news_dot.png"
        xalign 0.95
        yalign 0.3
        action [ToggleScreen("streetView2"), Jump("newspaper2")]
    imagebutton:
        idle "radio_dot.png"  # Use a simple test image
        hover "radio_dot.png"
        xalign 0.775
        yalign 0.25
        action [ToggleScreen("streetView2"), Jump("magazine2")]
label newspaper2:
    play sound "page turn.mp3" volume 0.5
    "April 14, 1935"
    "JAPAN CONTINUES SUCCESSFUL VENTURES INTO MANCHUKUO"
    "Our glorious military has been able to move into the region of Heibei, allowing for futher unification of the zones between our nation and future territories."
    "A CELEBRATION OF OUR EMPEROR"
    "National sentiment has called for a great restoration of the Emperor's glory. Military leaders and citizens alike have vocalized their support for a more Japnese Japan."
    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView2
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump CH1PT2
            return
label magazine2:
    play sound "page turn.mp3" volume 0.5
    "April 14, 1935"
    "JAPANESE STARLET LOVES THE WESTERN LOOK"
    "Rising star Yamaguchi Kiyo was recently seen sporting a short, curled bob. When it comes to fashion, Yamaguchi has always been ahead of the curve!"
    "ARE RED LIPS FOR YOU?"
    "To rough or not to rouge? Makeup artist Tachibana Miyuki gives her insight into whether the Americans have it right with the bold glossy look, or if a simple dab is enough!"

    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView2
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump CH1PT2
            return
label parents_letter:
    play sound "page turn.mp3" volume 0.5
    "Our beloved daughter,"
    "We cannot begin to express how porud we are of your recent success. Even the most old-fashioned of our friends have made their way to at least one of your films."
    "No one has had anything but kind words and praise for you."
    "There have been a few gentelmen calling at the house, wondering when you'll be home. I know we haven't discussed marriage in a very long time and, as much as we would love to see you in a shiromuku, your life is yours to decide."
    "Please come visit us when you have time. Your mother wants to prepare you all the new dishes she's learned at the recreational center. Again, we want to let you know that we are pleased with your accomplishements and wish you continued luck."
    "- Your father and Mother"
    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView2
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump CH1PT2
            return



screen streetView3():
    zorder 5
    imagebutton:
        idle "post_office_dot.png"  # Use a simple test image
        hover "post_office_dot.png"
        xalign 0.5
        yalign 0.8
        action [ToggleScreen("streetView3"), Jump("wang_letter")]
    imagebutton:
        idle "news_dot.png"  # Use a simple test image
        hover "news_dot.png"
        xalign 0.95
        yalign 0.3
        action [ToggleScreen("streetView3"), Jump("newspaper3")]
    imagebutton:
        idle "radio_dot.png"  # Use a simple test image
        hover "radio_dot.png"
        xalign 0.775
        yalign 0.25
        action [ToggleScreen("streetView3"), Jump("magazine3")]
label newspaper3:
    play sound "page turn.mp3" volume 0.5
    "November 7, 1937"
    "ITALY JOINS THE MOVEMENT AGAINST COMMUNISM"
    "Last year, Japan signed a treaty with Germany pledging its dedication to fighting the Communist threat. Now, it is reported that Italy has signed the pact as well – Japan welcomes its new ally with great respect."
    "A BRILLIANT DISPLAY OF LOYALTY IN MANCHUKUO"
    "Locals in Manchukuo have been organizing a festival akin to the autumn festivals here in Japan. They aim to bring the glorious culture and prosperity of our nation across the sea. Further details are listed below:"
    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView3
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump producer_scene
            return
label magazine3:
    play sound "page turn.mp3" volume 0.5
    "November 7, 1937"
    "HOW TO STYLE YOURSELF LIKE CLAUDETTE COLBERT"
    "It’s no secret that the American star Claudette Colbert has captivated the senses of men and women all across Japan. We invited a fashion expert all the way from the United States to give you tips on how to catch your own Clark Gable~"
    "A FOCUS ON THE REAL MAN"
    "New film The Shopkeeper’s Daughter brings to life a whole new genre – shomingeki – telling the story of the little man! “We finally get to see our stories on screen,” said student Koyagi Mariko through teary eyes. “It’s like I’m watching myself!”"
    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView3
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump producer_scene
            return
label wang_letter:
    play sound "page turn.mp3" volume 0.5
    "Dear [mcName],"
    "It’s been such a joy to hear your voice again, even if it’s through a screen. Of course, my friends and I miss the live performances of the benshi, but I do admit that I’m biased toward my favorite student. I do hope you get to display your singing talents in person once more."
    "I wanted to write to ask if you’d like to come and visit me sometime soon. I intend to return to China soon. I have family in Manchukuo and they have been growing somewhat uneasy with some of the sentiments being expressed. I will admit I feel equally uncomfortable with the increased presence of the military in our town."
    " I miss you greatly and would love a chance to say goodbye, though I understand that you are quite busy with your new life. Stay strong through all changes – you have proven your resilience. I am not an easy teacher! Your parents and I are unspeakably proud of you."
    "- Tutor Wang"
    menu:
        "Keep Exploring?":
            play sound "page turn.mp3" volume 0.5
            call screen streetView3
        "Done Exploring.":
            play sound "page turn.mp3" volume 0.5
            MC "The world’s changing so fast… I hope I’m able to make it out here."
            play sound "page turn.mp3" volume 0.5
            jump producer_scene
            return