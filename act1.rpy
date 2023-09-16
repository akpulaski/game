default scene107_menu = set()
default scene103_menu = set()
default scene103_label104_menu = set()
default scene104_choices2_menu = set()
default scene105_choices2_menu = set()


label scene_101:
    "Where did an old life end?"

    "Where did the new one begin?"

    "Could it all happen within the same lifetime?"
    
    "Especially for those who were looking for a place to start all over."
    
    "Maybe even called a certain space their own."

    "Most people had one at one point in their lives."
    
    "Whether it be with parents, grandparents, or even people they aren’t even related to."
    
    "A place to go to at the end of the day to destress from the rest of the day."

    "There are days where I do wonder if I can just turn back just to make things more comfortable."

    "More…safe."

    "Maybe it’s best to not dwell on those sorts of thoughts."

    anita "This place looks so nice and quiet."
    
    anita "It seems perfect."

    "I took some of my handheld belongings to the door at the far end of the left side hallway."
    
    "Which I was sure it would feel like a never ending hike up and down all those stairs later on in the day."
    
    "But who was I to complain about what a lot of people my age go through at this stage of life?"

    "But I was sure that a lot more of those people had something I didn’t. "

    "Help carrying my whole life up into this new apartment."

    ##[Creaking Door SFX]
    play sound creakingDoor

    "But before I even reached my apartment for the first time, I came to a sudden stop as I heard one of the other doors down the hallway open with a loud creak."
    
    "I took a peek over my shoulder to see a woman about my age with long brown hair."
    
    "She looked rather cozy in her choice of clothing too."

    "Before I could get the chance to apologize for possibly staring at her, she spoke to me first with a voice as soft as a bell."

    elleanor "Oh Hello! You must be a new tenant here. It’s always nice to see new faces at Holmes Hideaway."

    anita "How did you know I was new here?"

    elleanor "By your bags, silly!"

    "Looking down at my arms, I saw the handful of bags of various aquatic themed items that I had still planned to place in my bathroom."
    
    "I could feel my face flush with embarrassment, made only worse by the fact she was someone I didn’t know."

    anita "Oh yeah…my bad."

    anita "Sorry, it’s been a really long drive for me."

    elleanor "It’s okay."
    
    elleanor  "Everyone makes mistakes."
    
    elleanor "Especially when they must be really tired from traveling overnight to be here so early in the morning."
    
    elleanor "You must be exhausted."

    anita "I’m not doing…terribly."
    
    anita "As long as I have my friend, double espresso macchiato, right by my side, I should be all good."

    elleanor "Oh dear…"

    elleanor "Maybe I can give you a helping hand so you don't need to rely on caffeine as much?"

    jump scene101_choices
    return

label scene101_choices:
    menu:
        "That would be nice.":
            jump scene101_label101
        "No thank you.":
            jump scene101_label102
    return

label scene101_label101:
    anita "That would actually be really nice of you if you have the time to help me for a little bit."
    
    anita "I don’t want to take up too much of your time if you’re busy."

    elleanor "I wouldn’t have offered it if I didn’t have the time today to help get the new girl settled in."

    anita "Let me just place the stuff I have in the bathroom."

    elleanor "Alright."
    
    elleanor "I can get some more of your belongings and bring them up to your door."
    
    elleanor "Which one might that be if you don't mind me asking."
    
    anita "Oh, I guess you do need to know where to put my stuff."
    
    anita "It’s the one on the far left, 323."

    elleanor "Oh!"
    
    elleanor "That's right next to mine!"
    
    elleanor "Guess that makes us neighbors."

    elleanor "Thank you so much for letting me know."
    
    elleanor "I’ll get to it then, Miss…"

    anita "Oh!"

    anita "Uhh, Anita."

    anita "That’s what my mother calls me."
    $ elleanor_name = "Elleanor"

    elleanor "Mine calls me Elleanor when I get in trouble."
    
    elleanor "But on a good day, it's Elly."

    anita "I'll let you know that you aren't in trouble, Elly… hahaha!"
    
    "It didn’t take me long to catch up with Elleanor back outside to grab more of my possessions."
    
    "We continued on in this rhythmic pattern for a couple of hours."
    
    "We went to the moving van, back upstairs to my apartment, and placed the boxes in specific rooms."
    
    "Wash, rinse, and repeat." 

    "Because of course… the elevator is broken."
    
    "Yay."

    "After a couple hours, my apartment was full of moving boxes."
    
    "Not a single room was left empty by the time we settled the last box in its neat little place."

    anita "That should be the last of it."
    
    anita "Thank you so much."

    anita "I know it was really hard work."
    
    anita "But you have no idea how much I appreciate your hard work, Elleanor."

    elleanor "Oh it’s no trouble at all."
    
    elleanor "I am just happy to help someone when they really need it the most."

    elleanor "It’s just a shame that if I didn’t come out of my humble abode, that you would have done all of this by yourself."

    elleanor "If you don’t mind me asking, why is that?"

    anita "It’s… as long as it is complicated to explain."
    
    anita "I’m sorry."

    elleanor "You don’t need to apologize all the time."
    
    elleanor "Especially since there is nothing to apologize for."
    
    elleanor "I am not offended or hurt in any way."

    anita "I’m-"

    "Elleanor raised a finger as if she was going to wag it disapprovingly."
    
    "Who was she, my grandmother?"
    
    "But, like I would have done with my granny, I cut myself short before I could finish my apology."

    anita "Okay."

    elleanor "Good job!"
    
    elleanor "You’re already learning!"

    anita "It’ll take a while for an old habit to die hard."
    
    anita "But, we all have to start somewhere, I guess."

    elleanor "Exactly."
    
    elleanor "All it takes are a few cute little baby steps."

    anita "Even though I am not cute, nor am I little."
    
    anita "But I can always get started on that stupidly long hike."

    elleanor "Well I hope you have a wonderful long hike."
    
    elleanor "While you do that, I should actually be on my way."
    
    elleanor "I planned on meeting a friend for coffee."
    
    elleanor "They have been waiting for me long enough."
    
    elleanor "I hope that we can catch up at a later time."

    anita "I'm sure we will one of these days."
    
    anita "It's been really nice to meet you, Elleanor."

    elleanor "It’s been a real pleasure to get the chance to meet you too, Miss Anita."
    
    elleanor "Take care now!"

    anita "Bye!"


    jump scene101_ending
    return
label scene101_label102:
    anita "No thank you. But the fact that you offered is really sweet. Thank you ehhh…"

    anita "Jeez. I’ve been eating up your time and I never gave you my name. I’m really sorry."

    elleanor "Oh no! It’s quite alright! Don’t feel like you are wasting anything of mine. I am always free whenever you would like any kind of help."

    elleanor "Or even if you just want someone to talk to whenever you feel lonely."

    $ elleanor_name = "Elleanor"

    elleanor "Just call out ‘Elleanor’ and I’ll come running. Hahaha."

    anita "Hahaha. Well uhh…It’s nice to meet you-"

    anita "ELLEANOR!"

    "Elleanor covered one of her ears for a quick moment before looking at me slightly confused. Even from my sudden outburst, she was still able to laugh it off for whatever reason."

    "That woman must’ve had the patience of a saint to deal with my awkward reaction to just her name."

    elleanor "But Elly will do just fine if that is what you prefer to call me. What might your name be, sweetie?"

    anita "Anita… Anita is fine. I’m sorry for…whatever that was. I just get a bit on edge around new people."

    elleanor "It’s quite alright, You have nothing to worry about here. Everyone is super sweet in their own special way."

    anita "Thanks for the reassurance. I honestly really needed it."

    elleanor "You’re more than welcome. Hopefully, I’ll see you around. Bye!"

    anita "Bye!"
    jump scene101_ending
    return

label scene101_ending:
    "When I finally had a moment to just relax and reflect on how to arrange everything, I slumped onto the couch. While I shifted my position to lay my back against the cushions, I took this blissful moment of silence to breathe deeply. "

    "Just let the world do its own thing while I could just be left alone to my own devices as well. That’s all I want right now. "

    "No driving."

    "No screaming."

    "No fights. "

    "Just Anita."

    "If…that is really considered a good thing or not, I was not entirely sure."

    jump scene_102
    return

label scene_102:

    ## [Anita is in her apartment, squaring away the last of her boxes to their proper places. SFX of a thump accompanies the onomatopoeia below.]
    play sound movingBoxThump

    anita "Ah… that’s the last box I have to bring up. Ow, my arms…"

    "I had to take a moment to sit down and rub my tired arms."
    anita "And there’s still so much left to unpack. Um, where should I start first? Maybe this box… ?"

    "I peek at the huge cardboard package I set down moments before. "
    "The tape sealing the box shut parts easily under the sharp edge of my scissors. I set the pair aside before flipping open the lid, peering at its contents, and mentally situating them inside my apartment."

    anita "Plates for the cupboards, tea towels for the drawers, and as for the utensils, they should be placed—hm? What’s this?"

    "I reach into the depths of cloth-wrapped ceramics, pulling out a wayward mug that likely fell from its protective wrappings. I heave a mournful sigh as I delicately trace the deep crack along the side."


    anita "My favorite mug! Oh, you poor thing, you’ll leak if I pour anything into you. What a shame. I’ll have to take it out later with the rest of the trash—"

    "I feel my foot catch on something and I stumble. Too late, the mug slips from my grasp and falls to the floor with a—"

    ## [Blackout screen indicating sudden flashback. SFX of glass shattering. Have SFX and blackouts happen at the same time?]
    play sound cafeGlassBreak

    cafe_waiter "I’ve got it, miss! Were you hurt any… where…?"

    "I couldn’t think. My mind went blank. I stared at the screen of my phone with my eyes wide open as terror sank its teeth into my soul. "

    cafe_waiter "Err, miss? A-are you alright? Do you need me to—?"

    anita "No thank you!"

    "I painfully replied as I bolted out of the cafe—heart hammering, throat clogging—as my pounding footsteps drowned out the waiter’s concerned calls."

    "After running what felt like a mile, my thumb shakily punched the contact for Allen <3. It rang once, twice, thrice, and then the call connected."

    allen "Hello?"

    "I opened my mouth."

    "The words won’t come."
    "WHY WON’T THEY COME!?"

    allen "If you aren’t going to say something, I’m hanging up."

    anita "WAIT! I-I—"

    "I choked. It was hard to speak, but I forced my voice to work. Each word set my throat on fire. I took a deep, stuttering breath and tried again. I need to know this."

    "Even if it hurts…"

    anita "O-On Isabelle’s a-account, sh-I tagged you in a ph-photo you took t-t-together y-yesterday."

    allen "So?"

    anita "Sh-I said i-it’s my f-first photo with h-h-my new b-boyfriend."

    anita "Th-that’s wrong, isn’t it? I-I’m the one you’re d-dating, r-right?"

    allen "Anita, we've talked about this so many times. I can’t understand a word you say when you’re acting hysterical."

    "He’s right. If I’m going to despise him for the rest of life, I might as well make what I want to say clear."

    anita "We’ve been together for years! I brought you your favorite coffee every morning, brought you homework and class notes when you were sick, baked you a cake every birthday, and I even named our future cat together!"

    anita "You said you wanted a life with me…"

    anita "Don’t you still want that?"

    allen "…"

    anita "…"

    anita "… Why won’t y-you say a-anything?"

    "I waited in agony for an answer. A beat passed. "

    "He sighed."

    allen "I don’t want to see you anymore. Let’s end it here."

    allen "Now."

    allen "Get your shit and get out of my life."

    anita "Wait, Allen! PLEASE DON’T LEAVE ME—!"

    "I hear a click."

    "I hear his dial tone."

    "I tried to call the same number a dozen times, but he kept his silence. Everything after that was a painful blur of screaming and bawling."

    # [Scene change, back to Anita’s apartment. SFX of ticking clock]
    play sound clockTic

    "I stare at the broken mug shattered to shards on the floor for maybe…minutes? Hours? I don’t know anymore. "

    "The world was fuzzy. My hands shake. My shoulders ache. My breaths stagger  as I try to take them in, out, deep—count and hold—before letting it out. "

    anita "Don’t think about him anymore, Anita."

    anita "You’re here to get away from it."

    anita "It may be fresh but You’re fine, it shouldn’t affect you anymore."

    anita "Let’s hope all of the years of manipulating me is a blessing in disguise. Just remember what your therapist said."

    anita "You are beautiful."

    anita "You are worthy."

    anita "You are loved."

    "Even if that last one is a lie."

    anita "I am not some random, desperate stalker girl who couldn’t take a hint where most of the campus turned against you."

    anita "This is a new place where no one knows your name! It’s a new beginning with new neighbors who won’t gossip or post embarrassing photos of you or snicker behind your back."

    anita "I am Anita Carver and I am-"

    anita "..."

    anita "I am pathetic enough to talk to myself…"

    "Who am I kidding? Moving here changes nothing. It’s only a matter of time before I make a mistake and everyone here will—"

    ## [SFX of cat scratching door]
    play sound catScratchDoor

    anita "Huh?"

    ## [SFX footsteps, then door opening]
    play sound footstepsWood
    play sound doorOpen

    anita "Err… A cat?"

    "A midnight black cat gazes back at me through half-lidded eyes. Despite how bored they seemed (if such an expression existed for cats), I couldn’t help but feel like we’re looking into each other’s souls. "


    "It was uncomfortable, to put it lightly."

    anita "What are you doing here, kitty? Are you lost?"

    "The cat yawns. Cats have really sharp teeth."

    anita "Ah? Wait!"

    "It slips into the apartment before I can close the door, padding through the entryway on swift paws. It hops on the dining table and sits, staring at me expectantly. "

    anita "Erm, I-I’m sorry, but I don’t have anything for you to eat. I haven’t shopped for groceries yet."

    "The cat narrows its eyes and yowls. I can’t tell at all if it’s mad or not."


    anita "I-I don’t understand. What is it that you want from me?"


    "Its ear twitches. It stretches its neck, pawing at something there."

    "I come closer and inspect the tag."


    anita "Void? Is that your name?"

    ##Cat Meowing SFX
    play sound meow1


    void "Meow."


    anita "Um, I’ll consider that as a yes."

    anita "I take it this means you’re lost, then?"

    ##Cat Meowing SFX
    play sound meow2

    void "Meow."


    "Void meows their affirmation once more. This is almost incredible. Having my own way of communicating with a cat."

    anita "Hm, there’s no phone number on the back of your collar. How am I supposed to find your owner?"


    "Void says nothing and merely stares at me some more. You are absolutely no help right now."

    anita "Well you seem to be in good health, and your coat is only a little messy. It’s not matted or anything.  You couldn’t have been missing for long. And there’s not a lot of mud on your paws either, so you’re not outside too much." 

    anita "Do you live in this building with your owner?"

    ## Cat Meowing SFX	
    play sound meow1 

    void "Meow"

    anita "Maybe…"

    anita "Oh no…"

    anita "One of my neighbors knows who your owner is."

    anita "That means…"

    anita "{b}I have to talk to them!{/b}"

    "I plopped down onto my couch in shere misery at the idea of talking to people right now. Void leaps off the table and pads away. They pause and toss a glance over their shoulder, meowing in order to get my attention."


    anita "D-do you want me to come with you?"
    ## Cat Meowing SFX
    play sound meow3

    void "Meow."

    anita "Oh, um, but what about my unpacking?"

    ## Irritated Cat SFX
    play sound angryCat1

    "Void makes more of a weird grumbling noise, clearly showing  irritation at me."

    "I feel myself caving in and sigh. "

    anita "… Oh, why not? I can put off squaring my things away for an hour or so."

    anita "I just hope this leads somewhere."

    "Void chuffs (is that a good thing?) and turns its back on me, tail swishing lazily as it pitter-patters off."

    anita "Ah, wait for me!"

    jump scene_103


    return

label scene_103:

    "I…really don’t want to do this. I should be settling in, trying to get some realm of normalcy. Just…being left alone."

    "But…I don’t have the heart to leave a little kitty on her own. Like…"

    "It doesn’t matter. Don’t worry, I’ll find them."

    "As I picked up Void I must have not had a good grip on him as he jumped right out of my arms. Terrified that I already lost the little guy, I scrambled to try and get him."

    "Thankful god he only started rubbing against the door across from me."

    "Maybe he’s telling me something…"

    "Please be right. With a deep breath and a shaky hand, I knock on the door."

    ## Door knocking SFX
    play sound doorKnock1

    "A minute goes by. Nothing. Maybe they didn’t hear me?"

    ## Door knocking SFX
    play sound doorKnock1

    vivian "Hold on!"

    "The harsh command from a woman from behind the door made me and Void jump a little. From the sounds of it, I would guess she’s close to my age."

    "The door was then yanked open to see an alternate styled girl towering over me dressed in mostly black. Her size might be due  to her massive boots though. From the look on her face, my presence wasn’t very welcomed."

    vivian "Can I help you?"

    anita "Y-yes, I was wondering, miss…um…"

    "Oh god I don’t even know her name. Yet I’m here offering her a cat. This is just…nice."

    vivian "Vivian."

    $ vivian_name = "Vivian"

    anita "Thank you. Miss Vivan, this cat came scratching at my door. When he jumped out of my arms he came to your door."

    anita "So I was wondering if-"

    vivian "I don’t own a cat. The only pet I have is a parakeet."

    "Did I say something wrong? Why is she coming off so rude?"

    anita "I’m sorry. I’ll…I’ll get going now."

    "Before I was able to make it a few feet down the hall, Vivian’s voice rang out to me. This time in a more gentle tone."

    vivian "Hold on"

    "More afraid of the consequences if I didn’t listen to her, I halted right in front of my door. Taking a deep breath for courage, I turn to face Vivian again."

    vivian "Do you wanna come in for a minute? I’ll call up all the people I know in the complex to see if they’re missing a cat."

    "My first initial thoughts were absolutely not. She scares me as much as it is before our small conversation. "

    "But this was important. This wasn’t about me, it’s about Void. If she can help me, I can…step outside my comfort zone this one time."

    anita "…Okay."
    
    "The inside of Vivian’s apartment was both exactly what I expected and nothing what I expected at all. It was of course dark with hues of purple due to some kind of lighting. I could see horror memorabilia and CD’s for heavy metal bands."

    "But the overall theme of what I can see of the entire apartment was celestial."
    
    "If all of the shades and blinds weren’t drawn, I could tell that the walls were painted white and black with hints of gold due the decor that mimicked planets and stars."
    
    "The lighting I noticed earlier I realized now was a projector showing different galaxies across the celing."

    "It felt like an upgraded version of a teenager’s bedroom but it’s still the most beautifully decorated apartment I’ve been in."

    "I’m even too scared to sit on her couch in fear of Void scratching it up."

    jump scene_103_choices
    return

label scene_103_choices:
    menu:
        set scene103_menu
        "Look at the bookshelf":
            jump scene_103_label101
        "Look into the kitchen":
            jump scene_103_label102
        "Look at the side table":
            jump scene_103_label103
        "Look at her parakeet":
            jump scene_103_label104

    return

label scene_103_label101:
    "Her collection of horror and heavy metal is a lot more obscure than I first thought. I’ve never heard of any of these bands or movies. "
    "I picked up one of the movies out of curiosity."
    "…What the heck is Puppet Master?"
    "I put it back and decided to see what her taste in music was like as well. An older style stereo was right on the kitchen counter so I decided to press play."

    ## Crappy heavy metal music starts to play.
    play audio vivianMetal
    "My ears felt as though they were starting to bleed with how loud the music was. It frightened Void as I dropped him so I could cover my ears."

    vivian "Ah! Why did you do that?"

    "Vivian had to shout out to me to hear her as she dashed out of the kitchen to turn it off. My ears are now ringing as I try to find Void."

    vivian "Sorry about that. I had a party last night at a friend’s. Guess I forgot to turn it down."

    vivian "Hope it didn’t freak you or your cat out too much."

    anita "I-it’s fine. And he’s not my-"

    "By the time I was able to find and grab Void, she was already back on her phone in the kitchen. How can she still hear after that?"

    python:
        scene103_menu.add("Look at the bookshelf")

    jump scene_103_choices
    return
label scene_103_label102:
    "I could see Vivian in the kitchen talking to who I assume were different tenants. Even if at first she scared me, she doesn’t have to do this for me or for Void."
    "Wanting to see how much of her overall theme expands around her apartment, I took a quick peek inside of Vivian’s kitchen. "
    "To my surprise it did. Her back splash was painted black while everything else was white, just like in her living room. But gold stars and moons gave the room so much life."
    "I hope I can decorate my apartment like this."

    vivian "That’s not the point Avery! I’ll get you the cash I owe you later. Now do you own a cat or not asshole?"

    vivian "…"

    vivian "I swear to god if you don’t tell me now, I will make you eat your spine!"

    "At least she wasn’t actively yelling at me like that when I first met her. I wonder what made her so upset though."

    "Maybe I should leave her to do her thing. I don’t wanna get caught up in…that."

    python:
        scene103_menu.add("Look into the kitchen")

    jump scene_103_choices
    return
label scene_103_label103:

    "Being in my arms for as long as he has, Void started to get fussy again and jumped right out of my arms once again where he planted on one of her side tables."

    ##Crashing sound


    "When he landed, Void knocked over an extravagant looking box. Holding my breath in fear of it breaking, thankfully it didn’t. The only thing that came out though was this strange gold coin with a square hole cut out of it. "

    "When I picked it up to put it back in its container, I couldn’t help but look at the symbols carved into it. It’s…oddly beautiful."

    "I wonder what they mean…"

    vivian "What was that?"


    "Vivian’s voice calling out made me freak out as I scrambled to put her belongings back where they belong. It was too late though as Vivian came nearly racing in."

    "And she. Looks. Mad. I don’t blame her as she snatches the coin and its box out of my trembling hands. "

    vivian "Gimme that! I let you into my home and you start going through my things? Not only that, I'm trying to help you!"

    vivian "What is wrong with you?"

    anita "I’m sorry! I’m sorry! I didn’t mean to do anything! T-the cat jumped out of my arms and knocked it over. I swear it was an accident."

    anita "I-I’m sorry, I should go…"

    "Trying to fight off tears until I got back to my own apartment, I picked up Void and tried to make a dash for it."

    vivian "Wait…"

    "I stopped as I heard Vivian’s faint command. I could see Vivian taking in deep breaths, as if to calm herself and think of her next course of action."

    vivian "Okay. I believe you. Just…that coin means a lot to me. So I don’t like anyone touching that in particular."

    anita "W-what makes it so important?"

    vivian "I’m not comfortable telling just anyone about it."
    vivian "Regardless, sorry for blowing up at you. As you can tell, people skills aren't exactly my specialty. I’m still working on it."
    vivian "But I can tell that you’re not a bad person."
    vivian "Unfortunately, I called all the people I know around this dump and none of them own a black cat."

    anita "B-but what can I do? What if no one here owns him?"

    vivian "Maybe it might have a chip? Call up the vet down the street to see if it has one. If it does, they’ll find his owner."

    vivian "And the only person I couldn’t get a hold of was Mory. I just got a new phone and I guess not all of my contacts transferred over."
    vivian "I hope that dork is home."

    vivian "You can hit him up. He’s a nice guy."

    anita "Those are good ideas. Thank you so much. For everything."
    vivian "Don’t worry about it. If you need anything else,don’t be afraid to hit me up anytime Anita. I’m always up."

    "With Void tucked tightly in my arms, I exited Vivian’s apartment to the nearly blinding light compared to the darkness I was just in."

    "Even if at first she has a scary, defensive exterior, she turned out to be a very pleasant person."

    "…I never told her my name though."

    jump scene_104
    return
label scene_103_label104:
    "Over by the TV was an enormous bird cage in the shape of a house. Inside was a beautiful blue and white bird with speckles of black on its wings."
    "I couldn’t help but smile as I listened to its hypnotic song. If only I had the nerve to ask if I could pet it."
    "I didn’t like how Void was staring at it like it was a snack though. I turned my back to the cage now so it’s out of Void’s line of sight."
    "Bad kitty!"

    vivian "Ain’t she pretty? I named her Lovie."

    anita "Oh, that’s a pretty name."

    vivian "Right? I named her after H.P. Lovecraft."

    anita "Oh that’s…very fitting."

    vivian "Yeah, I got her about a week ago. I’m working on getting another one so she’s not lonely. I’d love to be here for her but I gotta work all the time."

    vivian "And birds are happier with a companion so I hope my boss will give me the extra hours."

    anita "Where do you work?"

    vivian "Heh, wanna take a wild guess?"

    jump scene_103_label104_choices

    python:
        scene103_menu.add("Look at her parakeet")

    jump scene_103_choices

    return
label scene_103_label104_choices:
    menu:
        set scene103_label104_menu
        "Coffee Shop":
            jump scene103_label104_label101
        "Occult Store":
            jump scene103_label104_label102
        "Strip Club":
            jump scene103_label104_label103
    return

label scene103_label104_label101:
    vivian "Ding ding! We have a winner."

    vivian "Yeah I’ve been working there for about a year now. It’s not total shit but it’s not my dream job either."

    vivian "I’m still in school too though to get it. I take online classes at night."

    anita "It’s great that you have so much determination. What’s your major?"

    vivian "I know it’s gonna sound nuts coming from me but I’m a marketing major."

    anita "Well for how hard it sounds like you’re working, I hope you get it one day."

    "Vivian didn’t respond to my last comment. All she did was give me a tiny smile. That spoke more than a dictionary ever could."

    vivian "So uh, I’ll get back to calling around."

    "And with that she went back to her spot in the kitchen and resumed her search. "

    "Even if she doesn’t like to admit it, Vivian is very sweet."

    "Hopefully one day we could be…friends…"

    jump scene_103_choices

    return

label scene103_label104_label102:
    vivian "Am I really that much of a basic goth to you?"
    vivian "Next you’re gonna say I work at Hot Topic."
    vivian "..."
    vivian "Though I am a regular at both. Don’t hate."

    python:
        scene103_label104_menu.add("Occult Store")
    jump scene_103_label104_choices
    return
label scene103_label104_label103:
    vivian "…"

    vivian "I’m just gonna pretend I didn’t hear you say that."
    python:
        scene103_label104_menu.add("Strip Club")
    jump scene_103_label104_choices
    return

label scene_104:
    "Well, I’m committed to this cat now. Vivian told me to check this one by myself. I guess it doesn’t hurt to try talking to people once in a while. She was nice to me. I don’t really understand it, but to each their own."

    "Void purrs in arms. I’m supporting him from below with my forearms and pressing him against my chest gently. Feels cozy."

    "There’s a very fluffy doormat; it says 'Welcome!' in a stylized way that feels, of course, welcoming."

    "I wipe my feet on the carpet of the hallway - just in case I need to go in. I really, REALLY don’t want to, but you never know."

    "I arch myself a little over the mat, knocking on the door with a sudden bout of trepidation that I am unable to explain myself. There’s cold air rushing behind me; I’m not sure what to do."

    jump scene_104_choices

    return

label scene_104_choices:
    $ scene_104_ignored = False
    menu:
        "Look behind you":
            jump scene_104_label101
            $ scene_104_ignored = False
        "Ignore it":
            jump scene_104_label102
            $ scene_104_ignored = True
    return

label scene_104_label101:
    "There is a dreadful feeling in my stomach. I need to dispel it with a little courage."
    "I look behind me."
    "…"
    "Just the corny wallpaper. "
    jump scene_104_continued

    return

label scene_104_label102:
    "I don’t want to look behind me. I don’t feel safe. In fact, I’m washed up by the feeling that looking back would be the absolute worst possible decision at this moment."
    "…"
    jump scene_104_continued

    return

label scene_104_continued:
    "The knock felt like an eternity ago, but it really has only been about four seconds. Should I knock again?"

    "Whatever that uneasiness was, it got cut short by someone calling."

    mory "Coming!"

    "I prepare myself to show Void to whoever is about to present themself."

    "…Please let this be fast. I’m feeling a little dizzy."

    "The door opens in a swift, gentle motion. A man presents himself with a big smile."

    "I… uh…"

    "Uhhh…"

    "Why is he happy?"

    "He’s tall and smells strongly of lemons. I don’t really like lemons, but it’s pleasant enough."

    "Behind him I can see an extraordinarily well kept apartment brimming with life. It’s well decorated, with a lot of paintings, shelves, books; paired well with the grassy, wholesome scent."
    "It gets somewhat overpowered by his citrics, but I still can pick up on it."

    "There are a lot of plants; The only one I recognize is the thyme by the window and TV."

    if scene_104_ignored:
        "Whatever I was feeling vanished as soon as he opened the door."
        mory "Oh, hel–"
        "I barely process what he said before I instinctively grab Void by his torso and inch him forward. His smile makes me a little jealous. I avoid eye contact with it."
        anita "Is this cat yours, Mr… Uh… Mr…"
        "I forgot his name I forgot his name I forgot his name!"
        jump scene104_choices2
    else:
        jump scene104_choices2
    return

label scene104_choices2:
    menu:
        set scene104_choices2_menu
        "Avery":
            jump scene104_choices2_101
        "Mory":
            jump scene104_choices2_102
        "Anita":
            jump scene104_choices2_103
        "Say gibberish and hope he corrects you":
            jump scene104_choices2_104
    return

label scene104_choices2_101:
    mory "Oh god no! I’d want to be anyone but him."

    mory "{b}Vivian{/b} has the biggest grudge against that guy."

    mory "I’m not entirely sure what happened but I think she owes him money after her roommate ran off on her. I keep asking if she needs help but she’s fiercely independent."

    anita "But then why is she mad at him?"

    mory "He cheated on his girlfriend, who is her best friend. It was a…really messy time here."

    anita "Oh…"

    anita "that poor girl…"

    anita "I just…hope she can move on from that."

    mory "Yeah me too. But it’s better that you weren’t here for it."

    anita "…I’ll take your word for it."

    python:
        scene104_choices2_menu.add("Avery")

    jump scene104_choices2

    return

label scene104_choices2_102:
    $ mory_name = "Mory"
    mory "Oh hey! That’s right! How did you know my name?"
        
    anita "Vivian told me while I was talking to her."

    anita "I guess I just needed a minute to remember."

    mory "Don’t feel too bad, I’m horrible at remembering names and faces too from time to time."

    jump scene104_continued2

    return

label scene104_choices2_103:
    mory "Haha, okay I have to admit. That’s pretty adorable."

    mory "Super wrong but very cute anyways.."

    "As long as he’s laughing with me and not at me that’s all that matters."

    "Also, his laugh is adorable."

    python:
        scene104_choices2_menu.add("Anita")

    jump scene104_choices2

    return

label scene104_choices2_104:
    mory "I’m…sorry?"

    anita "Oh you know…JohnaSamaTimothy"

    anita "…It’s French right?"

    mory "Even if I was French, that’s still not my name."

    mory "You know, it’s fine if I tell you. I’m not going to be offended."

    anita "No! I promise I got this!"

    python:
        scene104_choices2_menu.add("Say gibberish and hope he corrects you")

    jump scene104_choices2

    return

label scene104_continued2:

    mory "…"

    anita "O-oh. Sorry."

    mory "Hehe. That’s fine. But no, the cat isn’t mine, dear."

    ## There’s a small pause with no dialogue box.
    pause 1 

    mory "I assume you’re the new tenant. It's sad that you were told my name before I could introduce myself though hehe."

    anita "Oh… Yes. I’m new here."

    mory "Welcome, miss! Always nice seeing some new faces here and there."

    anita "Thank you. I’m Anita."
    mory "…"

    mory "Are you feeling alright?"

    "No. I’m really dizzy from talking so much today."

    anita "Yes, I’m alright."

    "He laughed. Seems surprisingly nice. I don’t think he’s gonna bite me for now."

    mory "Oh, that’s fine. I’m also a little shy."

    "Yeah… shy…."

    mory "Well, nice to meet you, Anita! Are you trying to find his owner?"

    "He’s onto me."

    anita "Y-yes. He was scratching at my door."

    mory "Well, none of the tenants have any pets aside from the parakeet next door."

    anita "I met Vivian’s parakeet. They’re really pretty."

    mory "Yeah I know she is…"

    mory "Lovie, I mean! Not Vivian!"

    mory "I mean yes, she is pretty but um…"

    mory "…Please don’t tell her I said any of this."

    anita "Hehe, I promise I won’t."

    mory "Oh thank you!"

    mory "But that’s awesome! I love animals as well! I’m trying to get a little pet myself."

    mory "But no, the cat isn’t mine."

    anita "Is he a stray?"

    mory "No, he got a collar."


    "I wanna cry."

    anita "R-right."

    "Why did you interject like that again? You learned about this very long ago.
    He steps a little closer and starts petting {b}Void.{/b}"

    mory "Don’t worry about it, I know how it is. I won’t judge you."

    anita "W-why would you judge him?"

    "…Oh."

    mory "…"

    mory "You should call {b}Mr. Lamlor{/b}. He might know."

    anita "Who?"

    mory "The landlord."

    "How did we not think of calling the landlord?"

    anita "Good idea. Can you give me his number?"

    mory "Sure! I can give you mine too."

    "I pull up my phone and he pulls his. I feel a little embarrassed to open my phone close to people, because my wallpaper is a photo of a certain someone. I know they don’t care or even know who that is, but I still don’t feel very good showing people like that."
    "I need to change it."

    "His phone has a green case, and I think his wallpaper is some kind of cute bug. Eccentric. He opens his contact list and I open mine. A little tingling in my brain rapidly morphs into a personal heatwave as I see a familiar name in it."

    "I already have Mr. Lamlor’s number."

    "…I’ll just pretend to add the number."

    "He asks me to add his number as well. I obey without questioning."

    mory "Give me a call whenever you need anything. I’ll always be there to help!"

    anita "Thank you."

    mory "Also, seeing that you met Vivian, have you met Elly?"

    anita "Elleanor? Oh, yes, I have met her."

    mory "She’s awesome. I haven’t seen her in a bit and I won’t be leaving for today. Lots of work. Can you say I’ll return her watering can tomorrow? She doesn’t have a phone."

    anita "She doesn’t?"

    mory "No, and she’s tight on money."

    anita "Okay. Sure."

    mory "Thank you!"

    anita "Nice meeting you. Sorry for interrupting your work."

    mory "Oh, it’s ok. I love meeting new people!"


    "{b}He isn’t bothered? A first!{/b}"

    anita "G-good to know. I’ll be going now."

    mory "I’ll be here whenever you need anything!"


    "…"

    "He’s staring at me. Or am I staring at him? I don’t know. This is getting awkward. I should go."

    "I turn around and leave immediately."

    mory "Bye!"

    "I can see him waving with a big smile as I turn around."

    "He’s sweet enough"

    "At least I didn’t screw it up this ti–"
    ## Sound: Door closing
    play sound doorClosing

    "…"
    "I got startled by the door."

    "I’m so pathetic. I hope that no one saw that. They’ll make fun of me."

    "Then I’ll have to move again."

    jump scene_105

    return

label scene_105:
    ## [Anita is walking down a hallway]
    play sound footstepsWood

    "Void doesn’t belong to Vivian or Mory. This is bad. Talking to two people was terrifying enough, much less two strangers that I have to live next to. How many more people do I have to make a fool of myself in front of until I meet Void’s owner?"

    "Vivian and Mory are probably together and laughing at me as soon as I leave. I feel so stupid. I’ll never be able to show my face outside my door after what happened today. I don’t want to know what everyone is saying about me. I can’t go through that all again!"

    "Stupid. Stupid. Stupid-"

    "Stop!"

    "I need to stop! "

    "I..am worthy…"

    "Yeah, remember that Anita. You are worthy. "

    anita "Why didn’t your owner place their contact information into your nametag, Void? All I have to do is go directly to their apartment and drop you off, but I can’t."

    "Not even a meow to reply back to me. He’s just resting in my arms like nothing is going on. It would be nice not to worry about anything right now. "

    "I wish I was a cat."

    "Ah. I’m at the next door already?! I wanted to take my time heading down the hall but my feet were going faster than my mind. I’m not prepared for another conversation! I should just leave!"

    jump scene105_choices

    return
label scene105_choices:
    menu:
        "Knock on the door":
            jump scene105_label101
        "Leave":
            jump scene105_label102

    return
label scene105_label102:

    "No…I can’t do this…"

    "I don’t have the mental strength to go through with this. Two people already know a side of me that I didn’t want to show anyone."

    "A weird, fidgety girl with no one to fall back on."

    "I can’t add someone else onto that list."

    "Void shook off the tears that rolled off my cheeks and landed on his head. I didn’t even realize I was crying. My body was expressing emotions I didn’t want them to."

    ## Cat Growling SFX
    play sound angryCat2

    "Making a few steps towards my front door, Void grew more tense while a low, guttural noise I haven’t heard him make rang through the halls. While this is going on, another kind of guttural was making its way to my ears."

    "Perhaps some pets will make him calm down. Or maybe it will help calm me down. "

    ##Gross Gargling SFX
    play sound monsterGrowl

    "IT'S NOT HELPING! IT'S NOT HELPING! IT'S NOT HELPING! "
    "Out of the shadows down the hallway, an enormous human-esque gray beast glared at me and Void with hungry eyes and a wide mouth to match. "
    "I don't know where it came from or how it suddenly got here."
    "But I'm not sticking around to find out."
    "Running for my life as I have a death grip on Void, I arrived at Elly's front door. I nearly missed it in my state of utter fear. "

    ##Door pounding SFX
    play sound doorPound

    "Pounding on her door, desperate for a safe haven, I only peeked over my shoulder to see as it trudged it's body stop by step closer to me and a now freaked out Void. "

    anita "Elly! Please let us in! In the love of God!"

    "I do whatever I can to save us but as it inched closer, I'm starting to accept my possible demise. The only reason I'm trying so hard is for Void."

    "Please! If not for me then for him!"

    "PLEASE!"
    jump scene105_continues

    return
label scene105_label101:
    "I shake my head intensely as I clung Void in my arms. No, I can’t do that. I have to find Void’s owner!"
    "It’ll be fine, Anita. You can do this for Void. She deserves to have a loving home where she can be safe and wanted."
    "…"
    "Knock on the door, ask the question, and then—"
    jump scene105_continues
    return
label scene105_continues:
    elleanor "Anita?"

    "I yelp and jump a few inches away from the door. Void yowls as he’s launched out of my hands and scrambles around the corner."

    anita "WAIT! COME BACK!"

    "I reached out to him, but it wasn’t enough. Void disappears down the hall in a black blur. "

    elleanor "Oh, I’m so sorry for startling both of you! Are you alright?"

    anita "Ah, um, y-yes…"

    anita "I think…"

    elleanor "What was that in your arms just now? A cat?"

    anita "Y-yes. I-I’m trying to find his owner, b-but now…"

    elleanor "I see. I’m sure he’ll come back."

    elleanor "Oh! Why don’t you come inside while we wait? I bought this wonderful new tea and I would love to hear your thoughts."

    anita "Th-This is your apartment?"

    elleanor "Oh no I broke into this one."

    anita "What?!"

    elleanor "Haha I’m kidding, I’m kidding. Of course this is my apartment dear."

    "Thank god she said that, I have the police on speed dial. "

    anita "O-oh, but I-I couldn’t impose—"

    elleanor "Please, take this as an apology for scaring your cat away. Won’t you come in?"

    anita "A-alright then. Thank you."

    "Elleanor held the door open for me as I stepped in. How polite."

    "In a word, her place could be summed up as—homey. Soft lavender walls with gray accents, wooden shelves filled with books and cute trinkets, a modest couch with embroidered pillows, and a small tea table covered with pink cloth and a white lace doily completed the picture. "

    "It was vintage, tasteful, and ultimately—homey. I could stay here forever. The floral incense is finally putting me at the sweet peace I needed."

    "Elleanor gestures for me to take a seat at a small, round table as she flits to the kitchen stove for the proffered peach oolong tea, and I oblige. I would hate to refuse a generous gesture from my host."

    elleanor "If you don’t mind my asking, do you often reunite missing cats with their owners in your free time?"
 
    anita "N-not really. U-um, Void showed up on my doorstep and I thought it would be the right thing to do. If I lost my pet and someone found it, I would really like it if they would do what they could to bring it back to me."

    anita "So I’ve been going to all of my neighbors asking if they knew Void. But no one knows who Void’s owner is."

    "I sigh, disappointed in knowing that I might be letting someone out there worry about their best friend. I’m so sorry. I’m doing my best."

    elleanor "Hm, that’s a pity. Perhaps I can help?"
        
    anita "W-would you? But how?"

    elleanor "Of course! Anything for a future friend."

    elleanor "I work at the pet shop not too far from here. I can spread the word about a missing cat. If anyone is looking for him, I’m sure it will be one of the first places they’ll look."

    elleanor "Oh, I can even make up a missing poster to post in there! How fun!"

    "I wouldn’t exactly call any of this ‘fun.’ A missing animal is actually terrifying, especially in my care. I panic nearly daily about how I’m gonna be able to take care of myself."

    elleanor "But alas, I can’t say I know anyone that lives here with a cat. But then again what would I know? I moved in shortly before you did, so I can’t claim to know much about our other neighbors either."

    anita "It’s alright really. Vivian already called around to everyone she knew here and no one said anything either."

    anita "How long ago did you move here though?"

    elleanor "About a month ago. So I completely understand the feelings of wanting to belong more than anyone else here."

    elleanor "So if you need anyone to vent your feelings and anxieties out to, don’t ever be afraid to come around. We can share some tea and chat until your heart feels lighter."

    anita "You’ve been nothing but kind to me Elly. Even when you don’t have to. I can’t thank you enough."


    "Elly took her hands in mine softly as I tensed up while also being at enough comfort to let her. It was like being held by someone that actually cared about me. "

    "It was a nice change…"

    elleanor "My heart goes out to those in need Anita."

    ## [SFX, kettle whistling]
    play sound kettleWhistle

    elleanor "Ah! It sounds like the tea is ready. Please, wait just a moment."


    anita "Th-that’s okay, I—!"

    "Elleanor let go of my hands and left me before I could finish my sentence, disappearing behind the partition that separated the living room from the kitchen. "

    jump scene105_choices2

    return
label scene105_choices2:
    menu:
        set scene105_choices2_menu
        "Look at the Bookshelf":
            jump scene105_choices2_label101
        "Look at the Tea Set":
            jump scene105_choices2_label102
        "Look at the Trinkets":
            jump scene105_choices2_label103
        "Walk Around":
            jump scene105_choices2_label104
    return
label scene105_choices2_label101:
    "While I took the time to wait for Elleanor to come back with the tea, my line of attention went to her bookshelf. There weren’t very many books to choose from. "
    "A few autobiographies."
    "A couple installments in a fantasy series I have been meaning to pick up."
    "Along with a few…books on the occult? Huh? I never would have thought a sweetheart like Elleanor would even want to know about the occult, let alone read about it. "
    "I guess you can’t judge a book by its cover."
    "…"
    "Pun unintended."

    "But one book drew my eyes to it for some unknown reason. Picking it up, I saw it was a book on local urban legends. A page was folded over. "
    "'The Hermit?'" 
    "'Not much has been documented about this unknown force, hence the name it has been given. But rumors spread that upon it's death, parts it's body were scattered all across the world. Each one gifting the one who processes a piece of it's body the curse of seeing what should be left unseen.'"
    "My curiosity made me interested. Maybe I could-"

    elleanor "Almost ready~"

    "Fumbling the book in my hands, I shoved it back in its proper place. "

    "It doesn't stop me from being curious though…"

    jump scene105_continues2

    return
label scene105_choices2_label102:
    "From the looks of it, this tea set looks like a family heirloom of some kind. The delicately painted flowers and vines adorned with a gold rim along the sides all looked so ornate and refined. "
    "Elleanor has a nice taste in antique china.  "
    python:
        scene105_choices2_menu.add("Look at the Tea Set")
    jump scene105_choices2
    return
label scene105_choices2_label103:
    "On the side table, there was an array of little items that looked right in place with anyone else’s home. A trinket dish full of different pieces of jewelry, buttons, and a couple of batteries. "
    "At least the jewelry is pretty."
    "I wish I could afford this kind of jewelry. "
    python:
        scene105_choices2_menu.add("Look at the Trinkets")
    jump scene105_choices2
    return
label scene105_choices2_label104:
    "I got up from my chair to stretch my legs for a little bit. The first place I went to is the closest window to peer down at the street below. "
    "People walking by."
    "Pet owners walking their dogs."
    "Children playing uncomfortably close to the street. "
    "It all still feels so new but yet the sounds outside are starting to grow fondly to me."
    python:
        scene105_choices2_menu.add("Walk Around")
    jump scene105_choices2
    return
label scene105_continues2:
    "My hands and heart feel colder and more empty now…"
    "Was he right?"
    "Am I needy?"
    "…"
    "I am worthy…I am worthy."
    "It wasn’t long though before Elleanor emerged from the kitchen carrying a tea set on a silver platter. She set the china and daintily poured the tea with all the elegance of a noblewoman. "
    "I couldn’t stop my staring. I envied her level of grace when I knew it’s wrong for me to do so. Elleanor seems so amazingly put together that it’s hard to imagine her as anything but."
    "Unlike me. My career, my attempt at a romantic relationship, my friendships, my family, my mental state…"
    "Why can’t I be like Elly…"

    elleanor "Is something wrong with the tea, Anita?"

    "Elly’s tender voice cut its way through the thick fog of my mind. It frightened me a little but seeing her concerned expression made me come back to reality. "

    anita "H-huh? Oh, no, nothing is wrong. I was lost in thought! I-it smells…"

    "As I take in a deep sniff of the steam coming off the tea, the world begins to tilt. I put a hand to my head, clenching my eyes shut as my head spins. The last thing I felt was my body hitting the plush carpet with a thud."

    "I hear Elleanor scream something, but her words are drowned by the dull throbbing filling my ears."

    "Then as suddenly as it came, I felt the colors and shapes of the world coming back to me. I lift my head, blinking everything back into place."

    elleanor "Oh thank god Anita! Are you alright?"

    anita "I-I’m fine. I-I just feel a little d-dizzy."

    anita "I-It’s probably because I haven’t eaten much today. You know, moving and everything. I’ll probably feel better once I go back to my apartment."
    
    elleanor "Oh my. Here, have some tea and cookies on your way out! I don’t want to see you fainting again before you return home!"

    "Scurrying to put together a sort of care package for me, she let me borrow a thermos of hot tea and a container of cookies."

    anita "Oh, you do-"

    "Elly didn’t let me finish before shoving a cookie into my mouth."

    elleanor "I won’t hear of it. It’s really nothing."


    anita "Oh, thank you."


    "I nibbled on the cookie that was already in my mouth. Yummy. As I brought the thermos to my mouth, there was a—"

    ## Cat Scratching SFX
    play sound catScratchDoor

    anita "Void?"
    "I leave my seat for the door. Sure enough, Void is back, staring up at me from the other side of the door in a strangely familiar way that triggers a rush of deja vu."

    "The way he slips into the apartment only serves to strengthen the sensation. Unlike last time, though, he didn’t perch on the table amidst the fine china. He clambers up my leg and curls around my shoulders like a weighted scarf instead. I can already feel my back strain from his weight."

    "If I voice my complaints aloud though, I suddenly sense that those claws in my arm will dig deeper than necessary. "


    anita "Ow! What the hell!"


    elleanor "Aw, look! He came back! He’s so sweet."

    "Judging from the staredown Void gave Elleanor, I don’t think he shares the same sentiment. He looks like he’s about to scratch her face off."

    "…"

    "I swiftly transfer Void to my arms and clutch him tightly against my chest. He squirms, yowling, but I never relented my hold on him as I edge to the door."


    anita "I-I better be going now th-that Void is here. Thank you for your kindness, Elleanor, I’ll see you soon!"


    elleanor "Bye!"

    "Elleanor opened her mouth (no doubt to trap me here longer with promises of tea and cookies), but I would rather not be more of a nuisance longer than I have been."
    "The longer I converse, the higher my chances of ruining our acquaintanceship. I like spending time around Elleanor, she’s a very sweet woman."
    "The less she sees me, the longer I can selfishly exist in her world."

    "So, with that said, I slowly left out the door to the next tenant’s door."
    jump scene_106

    return
label scene_106:
    "All I was doing was going around in circles getting the same results. No one I came across even owned a cat, let alone an adorable black one."
    "Going back and forth down the 3rd floor hallway, I contemplated what exactly I could do for a cat I didn't even own. I'm sure Void was missing his mommy or daddy."
    "Once I took a moment to take a nice long breath, I looked down at my feet to realize that Void wasn't right there like he had been since I found him. "
    "Taking my eyes off the floor, I looked over my shoulder to see Void staring blankly at one of the doors behind me. I stepped closer to the door Void was intensely focused on."

    anita "Wow. That must be some interesting door. Huh, buddy?"

    "As if to respond to my unfunny joke, Void started scratching at the door as if he wanted to be let in. "
    "Maybe this was Void’s way of telling me that this is where his owner lives? Thank goodness for this smart little boy!"
    "With that, I waited for someone to open the door in slight anticipation for what may occur with the person behind that door. "
    "Would they assume that I stole their cat? Or would they think I was some crazy cat lady that thought he was one of my children…"
    "Or maybe they are nice? Who knows? One can only be so optimistic about someone they have never met."
    "…"
    "…"
    "If they ever open the door. "

    ## [Door knocking SFX]
    play sound doorKnock2
    "I took it upon myself to knock on the door to see if anyone is actually home. Taking a few more moments to wait patiently for the occupant to at least welcome their cat back inside. "
    "…"
    "…"

    anita "Hello? Is anyone home?"
    "It was starting to get ridiculous at that point. Slight irritation set in as I pressed my ear against the door to see if there was any kind of life inside whatsoever. "
    "I just hoped that Void’s owner didn't just abandon him to go live somewhere else. Or worse, kicked him out of his home to let him wander around and possibly d-"

    ## [Loud banging SFX]
    

    anita "JESUS?!?!"

    "My compulsive reaction to my heart leaping out of my chest led to me landing backwards onto the floor. Staring wide eyed at the door in front of me, I pondered about what exactly just happened right before me. "
    "Who exactly is there in that room? Someone who really didn't want to didn't want to be disturbed. Or someone just mocking my attempts to get in contact with me by scaring me away. "
    "Either way, I got back up on my feet and faced the stranger in front of me."

    anita "Excuse me! I have your cat!"

    anita "…"

    anita "Void?"

    anita "…"

    anita "He's a black cat with yellow ey-"

    ## [Loud banding SFX x3]

    "Yup, I’m not staying around for that."

    anita "HAVE A NICE DAY?!?!"


    "With that obvious hint of ungodly rage, I scooped Void up and made a mad dash to my own apartment door. With Void in my arm, I fiddled with my key ring to look for the right one. "
    "Shuffling through them one by one, I struggle to find a specific goddamn key. My breathing paced with my thumping heartbeat. Grabbing for the last key on the ring, I inserted it into the lock to hear the most satisfying click of my life. "

    ## [Slamming door SFX]
    

    "Once we were safe inside, I slammed the door behind me with an unintentionally loud thud. Now that all was quiet, the only sound I heard was the blood rushing to my ears and the click of locking my door. "
    "My legs gave up on me as I slid my back against the front door. Now, I was just wondering what the hell their problem was. All I wanted to do was give them their cat back. "
    "Was I really doing such a bad thing? But all I had were good intentions. "
    "I don't understand. Void didn't even want to move from that door. Even though all the person inside did was nearly give me a heart attack."
    "My breathing hitched as I tried my best to keep my composure. The lump in my throat I was afraid of came up to set in its place as I tried to do my exercises. "
    "Inhale"
    "Hold"
    "Exhale"
    "Ho-"

    ## [Cat meow SFX]
    play sound meow2
    void "Meow"

    "My eyes shot open the moment I heard that sweet little meow. Letting the air slip out of my lungs, I finally let Void out of my arms. "

    anita "Sorry buddy. I was just…having a moment right there."
    anita "Are you doing okay?"


    "Void stared at me with those sweet yet piercing eyes for a moment. Before I could even process another thought, Void rubbed up against my shins sweetly. "
    "Not being able to resist Void’s sweet gesture, I returned the favor by scratching his back gingerly. "

    anita "You really are the sweetest boy, aren't you?"

    void "Meow."

    "I couldn’t help but let out a small giggle. Sometimes, it did seem like Void could actually understand what I was saying like any other person. Either that or it may just be my loneliness letting me believe that a cat understood what I was feeling. "

    anita "I think It's about time we both try to at least calm down a little bit. Then we get around to calling the landlord."

    "I picked Void up in my arms as I got on my feet to head towards the bedroom. Once I closed the door behind me, Void jumped right onto the bed to look for his special spot. "
    "The moment he picked his spot, I layed down on my side to face Void. My eyes surveyed him as if I was inspecting a new species. "
    "At least I know where you came from. But what is going on with your owner? I know someone is home if there was someone pissed enough to retaliate against me by banging on the door. Which by the way is rude!"
    "But regardless, even if your owner is in a lousy mood I can’t give up. Clearly you love them and I need to see if they really are a good home to you. "
    "I don’t want to send you back to a place where you won’t be loved."
    "…"

    "Like me…"
    jump scene_107

    return
label scene_107:
    "I’m at my bed fiddling with my phone. Void is loafing on top of my pillows grooming himself. He seems to really like being around me for some reason. Does he miss his owner so much he wishes to stick with me until then?"
    "He must be very desperate."
    "I’ll take the opportunity that I’m doing literally nothing right now and call the landlord at once, he might know something - at least, if he wants to actually talk to me. "
    "Phone’s already here. Time to go. I’m gonna do it. I’m gonna call this jerk."
    "…"
    "Time to actually call him now."
    "Actually…"
    "I took a pic of Void loafing. Cute."
    "Do I really have to call him? It’s not like Void is bothering anyone, but I feel like this cat has something to do with that empty apartment. I’ll ask."
    "Ring…"
    "Ring…"
    "Riiiiiiiinnnnnnggg…"
    "He picked it up."
    "Rats!"

    lamlor "Hello?"

    anita "Hi, Mr. Lamlor. It’s Anita."

    lamlor "Who?"

    "My soul left my body."

    lamlor "Oh… I think I remember you now. The new tenant. What do you want?"


    "Nevermind, it forced its way back in."

    anita "I… uh… found this cat walking around the building. He has a collar. I thought you might know who he belongs to."

    lamlor "No phone number on the collar?"

    anita "No."

    lamlor "Well, it might have wandered in from somewhere. I don’t know how that would work, though."

    lamlor "None of the tenants have pets outside of that damn parakeet."

    lamlor "That thing keeps me up at night."


    "Rude."

    lamlor "Listen, I have stuff to do. Only call me if it’s important. Anything else?"


    "He doesn’t. He’s a landlord. At most he turns the water on and off."

    anita "Well, I was just a little curious about that empty apartment. Is the tenant really missing?"

    lamlor "Oh? That’s news to me. Which apartment?"

    anita "313."

    lamlor "Oh. Tom ain’t missing. He’s just out on vacation. I think. It’s been a while, but he’s keeping rent paid and not bothering anyone, so I don’t really care if he’s home or not. He still does talk to me on his phone and sends me payment receipts."
    lamlor "I suggest you don’t keep intruding in other tenant’s personal lives anymore."
    lamlor "A piece of advice, don't make other people's business your business."

    "What? You’re the one intruding! I just asked a question."
    "Just apologize, Anita. It's best not to think too hard about it."

    anita "Sorry, Mr. Lamlor. Just curiosity."

    lamlor "Right. Anyway, gotta go. Bye Anita."


    "He hung up. Still the same jerk. I didn’t use the money Allen to–"
    "Sigh."
    "Why am I like this?"
    "Well, the plan now I think is to take Void to the vet. He’s cute lounging like that, but I need to check if he has any tracking chips. I just HAD to get sidetracked, but I rather spend my time with a pet than with someone that thinks anything of me. "
    "I have a few things to unpack, but I’ll do that later. There’s a vet clinic on the other side of the road, I think I’m gonna make a call."
    jump scene107_choices
    return
label scene107_choices:
    menu:
        set scene107_menu
        "Phone in":
            jump scene107_label101
        "Vegetate a little":
            jump scene107_label102
    return
label scene107_label101:

    "Ring… Ring… Ring…"

    receptionist "Hello, this is Pet’s Love Animal Clinic. How can I help you?"

    anita "Hi, I’d like to take my cat for a check-up."

    "Well, I guess it’s my cat for now."
    receptionist "Sure! We’re about to close, but we have some openings if you hurry. Where do you live, dear?"

    anita "In the apartment complex just outside."

    receptionist "Oh, that’s great! If you feel like you’re too busy and it is so close to the end of the day, we can schedule it for tomorrow."

    anita "No!"

    anita "I-I mean…um…"

    anita "I’ll be there in a m-minute."

    receptionist "Okay, then can I get your name and the name of your cat?"

    anita "I’m Anita and my cat is Void."

    receptionist "See you soon, Ms. Anita! Please, pet Void for me!"

    anita "Thank you, ma’am. I’ll be there in a little."

    "Such a sweetheart. She doesn’t know I suck."

    "I’ll pet Void. He does deserve it, after all."

    call screen petVoid

    ## [Note: Void is on the screen. Pet him and you can continue]


    "Cutie. Let’s find your owner. You can’t stay with me if you got someone else you love, right?"

    "I’ll be your last resort, at least."

    "Gathering my things, I also feel some weird dread in the pit of my stomach, just like earlier today. It's most likely nothing…"

    "I love this purse. It’s purple and a little shiny."

    "I don’t have a pet cage. Nor a car. Nor bicycle. He seems very well behaved, so carrying him there will be easy. I try picking him up, but something isn’t right. He started staring at the wall and hissing at it."

    "I know typical cat behavior when I see it. He’s looking at something, seemingly through the wall. I get him up from the pillow and he complies, but seems a little dreadful, just like me."

    "Something isn’t right here, but I gotta go before the clinic closes."

    "I leave my apartment, lock the door, walk down the hallway, come back to see if I actually locked the door, then finally get into the elevator."

    "This little guy is so polite. I keep petting him all the way down the first floor within the lift. He understands me."

    "I leave the main hall and go outside the building."

    "…"

    ##[In a weird, shaky, large font]
    "{sc=4}{font=fonts/Bitter-VariableFont_wght.ttf}{size=*1.8}{b}SOMEONE IS WATCHING ME.{/b}{/size}{/font}{/sc}"

    "My head swings backwards as if by instinct to look at the windows at the floor I live in, where I can see both mine and Tom’s window."
    "There’s someone in Tom’s apartment."
    "Barely visible through the dim sunset."
    "My spine chills."
    "I’m scared."
    "Void doesn’t seem to react as strongly, but he also sees it from my shoulder. I know it."
    "They gaze at the back of my eyes. I stare back at what I assume is their only eye."
    "…"
    "This is not like any of my hallucinations. There was something behind me back there in the hallway, at Mory’s door, and it is here again."
    "I will make up an excuse to crash at Vivian’s place tonight. She barely knows me, but I refuse to sleep alone tonight."
    "I use every muscle fiber I have in my neck to turn back around and keep walking to the vet. My muscles are frozen, but I force them to move. "
    "I do my best to not think about it. This short trip feels unending."
    "Despite everything, I arrived."
    "I meet the receptionist there. She’s pretty. Prettier than me."


    receptionist "Hello, are you Ms. Anita?"


    "I simply shook my head."

    receptionist "Wonderful! Dr. Hood is already waiting for you, right there."


    "She points to a door right next to me."

    receptionist "We can discuss payment afterwards."

    anita "T-thank you."

    "The clinic is very well cleaned and has a very gentle aura. I like it. Makes me feel at home. I would love to work here. There are a bunch of toys and magazines, and cute animal posters. One of them is of a Corgi smiling. I love it."

    "I go through the door. The vet is a man in his 50’s. He’s bald, and looks pleasant enough."


    doctorh "Hello there! Is this the cute fella I heard about?"

    anita "W-well…um…"

    "You’re already ruining it. Why do I keep doing this?"
    "I put Void on a table, and pet him a little. The doctor approaches with a small light."

    anita "You see, I found this cat and I mean it must have an owner right? He has a collar and everything so…um…"

    anita "I’m…I’m sorry I don’t really know what I’m doing."

    doctorh "From what I can understand, you want me to check if Void is microchipped?"

    "He asks this while shining a light into Void’s eyes. It looks like they’re being pretty thorough with him. Just please be gentle."

    anita "Y-yes."

    doctorh "That shouldn’t be too hard now. Let me just see the little guy and I’ll take him back to see if he has a chip."

    "With a surprising amount of hesitation, I let this strange man I hardly know take Void back to hopefully do what he says he’s going to do. Then, I go back to the waiting room and sit on a bench. The receptionist is there behind a desk."

    "Minutes pass but they feel like agony. I don’t want to go back to my apartment."

    "All I have are the posters on the wall to keep me company. At least all the cute pets are keeping me company."

    "But it almost feels like they’re…staring at me."

    "Even… blinking at me."

    "Their normal faces soon twisted into toothy grins unseen on people let alone animals. The receptionist seems to vanish from my view."

    "Soon they started to conjoin into this grotesque creature made of different pets on the wall in front of me. There were fur, feathers, and scales meshing together to make an ungodly… thing."

    "I didn’t dare breathe. The lack of air was starting to burn my lungs. This can’t be happening again."

    "Not in public."

    "It’s been so long."


    doctorh "Ms. Anita, we’re done! I have good and bad news!"

    "I didn’t move a muscle, but inside, I jumped in my seat. The vet scared me. But thankfully, everything was back to how it should be."
    "Air was starting to return as I tried to destress from whatever that was. I have to focus on what he has to say about Void."

    doctorh "We ran a few tests on Void, and I haven’t found any microchips. Sorry. Nothing we can do on our end - without a chip or phone number, there’s nothing we can do to find a record. That’s the bad news."


    "Even though I was expecting it, this took me by surprise."

    anita "W-what can I do now? I don’t think I can take the right care of him."

    doctorh "Well, we’ll be on the lookout for anyone that’s looking for a black cat called Void. In the meantime, you can make posts on social media or put up flyers around town. We have your phone number and we'll give you a call if anything comes up."

    doctorh "The good news is, she’s perfectly healthy."


    doctorh "In due time, her owner will come around to collect this good little girl."

    anita "..."

    anita "Don’t you mean 'him'?"

    doctorh "No, dear, this is a female."

    anita "O-oh… Sorry. I don’t know how I didn’t notice it earlier. Thank you."

    doctorh "You’re welcome young lady. Just a suggestion, get a pet carrier. He could have jumped right off your arms or gotten into a fight with other pets."

    anita "Yes, sir. I will."

    "I held Void and paid for the visit as if my body was on autopilot, and left."
    "No chip. No step closer. But at least she’s healthy. Someone I knew always said health came first. I’ll never financially recover from this, but if there’s anything I like to spend my money on, it is with pets."
    "It’s a good thing I’ve always wanted a pet, but I feel entrapped in this situation now. I had no plans to suddenly look after a cat, but I’m not enough of an asshole to just dump her in a shelter, even though that would be the right thing to do."
    "I forced my way back to the building. At least she’s not being as fidgety this time."
    "I didn't look at the window to see if the shadow was still there. I don’t want to know."
    "At the entrance I meet Vivian. She’s dressed with some pretty, dark clothes. Looks like she’s about ready to go out."
    "I wonder what it’s like sometimes."
    "Wait…"
    "She’s going out?"
    "Oh no."



    vivian "Hey."

    anita "O-oh. Hi, Vivian."

    vivian "Don’t worry about earlier today. All’s good."


    "She made her way over to give soft pets to Void and I do a little as well. I opened up a big hearty smile, and Vivian mimicked me with her own grin. It looks fantastic on her. She must really love animals."

    vivian "Found his owner yet?"

    anita "N-no. I was at the vet, just giving him a check-up and seeing if he had a chip. Nothing… And also, it’s a she."

    vivian "Oh. She looks okayish. I don’t think you had to take her to the vet for that verdict. But hey, it didn't hurt."

    vivian "Anyhow, I’m on my way to get wasted. Later."


    "She left. I just waved. I don’t think she cared much that I didn’t say anything."

    "Now that she is gone, I don’t have anywhere to sleep. I don’t want to bother Mory either. It would be awkward to ask a boy that."

    "I… I don't wanna go back inside. I don’t have a good feeling about this."

    jump scene_108
    return
label scene107_label102:

    "I’m feeling very tired."
    "…"
    "I just remembered staring at Mory and then walking away."
    "I ain’t sleeping tonight. That’s for sure. Does he hate me? I don’t think so. But what if he does? Am I overthinking? This is awful. I hate this."
    "Vivian and Elleanor were pretty nice to me. At least, Vivian was until I screwed up. Or Void did. Well, it’s my fault because I brought Void into her apartment."
    "Am I making all of this about me? I can’t do this. I can’t do this."
    "Just calm down. Nothing is happening and you’re already having another episode."
    "It’s okay. It’s okay. No one hates you. No one hates you, Anita."
    "Not that I know of, at least."
    "My mind is a mess."
    "I just want to take a nap, but I gotta at least get to the vet before the end of the day."
    "I’m annoying myself at this point."
    python:
        scene107_menu.add("Vegetate a little")
    jump scene107_choices
    return
label scene_108:
    "Today has been… a long, very disappointing day. "
    "I still don’t know whose cat this is and I feel like I’m being mentally tortured for no reason. Is it too much to ask to have a normal life?"
    "Why can’t I have that? "
    "What have I done to deserve all of this?"
    "Without even realizing it, I kneeled down right in the middle of the sidewalk while tears started to stream down my face. All the while strangers just walk on past me, staring at me without saying a word. "
    "I just feel…so hopeless."
    "In the middle of my panic attack, I felt a vibration against my chest. Looking down I saw Void curled up to me, purring away like the world isn’t imploding on him…I mean her."
    "Slowly, I reached a sweaty hand to Void and stroked her back. This only made her purrs louder. Is it making her happy? I can’t tell. But she seems to be liking it."

    anita "I’m so sorry Void…I’m so…so sorry…"

    "It was all I could say at the moment. It took most of my mental energy just to say that to a cat. I really am a lost cause."
    "But…I don’t have time to feel sorry for myself. I have a creature that depends on me in the meantime until I find her owner."
    "I don’t have anything to take care of a cat so before going home, I need to head to the pet store. It’s a good thing there’s one a few blocks down. "
    "It’s already very late, I need to hurry!"
    "Getting back on my feet, I bolted all the way there with a now mad Void in my arms."

    anita "Sorry…again."

    "The little gal is frightened by the speed in which I run. I stop before she throws up in my shirt and I have one more problem to deal with later. She seems exhausted as well, I don’t wanna jog her awake."
    "There it is. Furry Friends. Glad they’re so close to home, otherwise it would be too dark to get home safely. There are a bunch of cats, dogs, rodents, reptiles and decorations around the entrance. Looks like they don’t sell animals, which is a plus in my book."
    "There is this adorable bunny table decor that instantly catches my attention. If I hadn’t heavily restrained myself, I would have had impulse-bought it."
    "Just looking at it made me feel a little better. "
    "Looking around the brightly lit isle, I reached for all the cat items in the shelves, and came to a conclusion I should’ve had in the complex’s main hall, where I still had some Wi-Fi:"
    "I have absolutely no idea what a cat needs."
    "Oh god, don’t freak out again, you just got over one."

    elleanor "Anita! Hi!"

    anita "AHHHH!"

    "I thought my soul was gonna leave its body as I darted behind me to see a familiar face. Elleanor was looking exactly the same as when I met her earlier but with an employee’s apron on. She leans over with a warm smile approaching Void."

    anita "Please…don't do that again."

    elleanor "Oh, I'm so sorry. I was so excited to see you that I forgot that you startle easily."

    elleanor "I see you still have your little furry friend though. No luck finding her owner?"

    anita "N-no."

    elleanor "I’m so sorry to hear that dear. Something will come up soon. I’m sure of it."

    elleanor "But in the meantime, I suppose you’re here to buy some supplies for this little cutie. I’d be more than happy to give you a hand!"

    "She reaches for Void and pets her in the head with soft pats. She isn’t purring. Must be fast asleep."

    "Just like me in a few hours…!"

    "But as Elly started piling all kinds of toys, treats, and food, I could feel my wallet and myself start to cry. All the while she sounds even elated at the idea that I’m keeping Void."

    "Elly is a sweetheart, but I can’t…"

    "I’m gonna go bankrupt at this rate."

    anita "I’m sorry for interrupting you but…I don’t know if I can afford all of this…$"

    elleanor "Oh don’t worry, I can help pay for some of it if you need the help."

    elleanor "I can even throw in my employee discount!"

    jump scene108_choices

    return
label scene108_choices:
    menu:
        "Accept the Offer":
            jump scene108_label101
        "Decline the Offer":
            jump scene108_label102
    return

label scene108_label101:
    anita "I mean, if it’s really not a bother to you, I would really appreciate it."

    anita "Thank you…"

    elleanor "Oh it’s no bother at all. Anything to help my friends and neighbors."

    ## Multiple scanning SFX
    play sound barcodeScan

    "I’m glad it saves me money and all but…why does it still make me feel pathetic?"
    "Like I can’t survive all on my own, even when I’m living alone?"
    "For god’s sake I’m depending on the charity of my neighbor to feed someone else’s cat!"
    "Just…I need to stop thinking too much about this. It’s a nice thing someone did for me and I should just say thank you and move on."
    jump scene108_continued
    return
label scene108_label102:
    anita "Please don’t. I don’t want you to go through all that work for me."

    anita "Besides, I don’t want you to get in trouble. What if your boss notices something weird in the system or something?"
        
    elleanor "Alright if you’re sure…"

    anita "Oh no please don’t take it as-"

    elleanor "No, it’s fine. Really. Thank you for looking out for me and my job."

    elleanor "I…really need the money."

    ## Multiple scanning SFX
    play sound barcodeScan
    "While Elly was ringing up my haul, I still can’t get over how it looks like her feelings are hurt. I know she told me one thing but her expression is telling me another."
    "I really hope she doesn’t hate me for turning away her help."
    jump scene108_continued
    return

label scene108_continued:
    "Trudging all of Void’s new treasures is gonna be a bit hard with no way of getting it all home."
    "Is it okay to borrow a shopping cart if I plan to give it back?"
    "No! Bad! That’s still stealing!"
    "But I have to do it. For Void! But before I could step out the door with a cat and two arms full of goods, Elly followed behind me."

    elleanor "Oh Anita wait! If you need a way to get home, you can borrow my bike."

    elleanor "I don’t want you carrying all that and your little friend back to Cuddlebug."

    anita "Really? What about you when you get off work?"

    elleanor "Oh don’t worry about me. It’s a nice night out for a walk anyways."

    anita "You really don't need to be doing all of this for me."

    anita "I don’t really know what to say. Thank you."

    elleanor "That’s all you need to say."

    elleanor "Just go out the back and it’ll be there."

    elleanor "Now hurry on home. I don’t want it being too dark out."


    "As Elly instructed, her bike rested up against the bricked wall of the alley way. It's a cute baby blue with a basket on the handle bars."
    "So I loaded all of my items in the back and Void in the front, I proceeded to peddle my way home. All the while feeling a little at peace as the crisp night air raced through my hair. Void seemed to be liking it too as she just cuddled up in the basket."
    "I have to admit…it’s pretty cute."

    ## Unknown creature in creepy font
    "{font=fonts/Creepster-Regular.ttf}{size=*3}You can never escape…{/size}{/font}"

    "I halted the bike as I frantically observed my surroundings to see who or what could be saying anything to me."
    "But that’s…impossible right? I was actively moving, it’s not like I was walking or standing still. Who was…talking to me."
    "Seeing nothing, I slowly started to peddle off again. Once I was sure there was nothing, I sped up exponentially as fear took more of a hold of me the more I thought about it. What if there was something actually there?"
    "As I reached my building, I felt a wave of relief crashing over me. Now I just need to get all this stuff, Elly’s bike and Void inside. "

    anita "I don’t need to keep carrying you, do I?"

    ## Meowing SFX
    play sound meow3 

    "As if on command, Void leaped gracefully out of the basket and right at my side. Didn’t try to wander off or anything. It's actually kind of amazing."

    anita "Good kitty."

    "Trudging all of this was going to break my back I swear! At least Void is good and walking right alongside me. She’d better for all the stuff I got her."
    "Even pushing Elly’s bike into the elevator was a pain. I could barely fit myself in. The ride up was agony as the pressure of everything nearly caved in on me."

    ## Elevator ding SFX
    play sound elevatorDing
    anita "Finally!"


    "Sweet baby Jesus! The third floor! I'm nearly home!"
    "The now familiar scents of citrus and heavy metal were strangely starting to become a comfort to me. "
    "Dragging all crap back to my apartment though is the battle. At least Void is enjoying herself though as she stares at me struggling. "
    "Slamming open my door, I plopped all of my things inside. The little princess walked right into my apartment like she already claimed it as her home. "
    "I don't know how to feel about this. Devastated that her owner must be missing her or overjoyed about how cute it is."
    "After shutting the door, I made my way next door to leave Elly's bike resting gingerly against the-"

    ## Unknown Creature in creepy font
    "{font=fonts/Creepster-Regular.ttf}{size=*3}YOU CAN NEVER ESCAPE!{/size}{/font}"


    "I was frozen in fear when the same voice from before was now shouting into my ear. Hot breath was steaming down my neck as I slowly turned to see a mistake onto humanity. "
    "A thin human-like creature towered over me, staring at me with glazed over eyes. The skin around his mouth was stretched ear to ear into a forced grin. Baring it's teeth at me like it wants to devour me."
    "I couldn't even scream. So much was racing through my mind that screaming didn't even come to me. I couldn't decide between fight or flight. My body acted on its own as I ran like the Devil himself was chasing after me. "
    "Prying open my door and locking it, my sights lined with Void's as she was trying to process what was wrong with me. My first instinct was to protect her so I kneeled to the ground to use my body as a shield. "

    ## Door pounding and scratching SFXs
    play sound catScratchDoor

    ## Creature in creepy font
    "{font=fonts/Creepster-Regular.ttf}{size=*3}YoU cAN't EsCaPe!{/size}{/font}"

    "The pounding and scratching kept on for what felt like my eternal torment. Even Void was trembling underneath me. The only thing that mattered to me in this moment was the safety of this cat. "
    "Screw mine! This little girl did nothing wrong!"
    anita "I get it! Somehow I deserve this!"

    anita "Just please don't hurt Void!"
    "I shouted back at the monster. I'd give anything just for this nightmare."

    "Maybe out of loss of interest or simply boredom, the beast's attack on my door faded more and more over the passing minutes. Until it disappeared all together. "

    "Not wanting to take the chance, I stayed in my protective position until I felt Void be more at peace. She even started rubbing up against me which was…very welcoming at this moment."

    "All my body could do was drop to the floor with a thud. Only trying to not land on Void. "

    "I laid motionless as Void continued to rub up on me and purr. Could it be her way of thanking me for protecting her? I don't know. "

    "The little bit of energy I had left was spent on petting this cat to let her know that I'm okay. My breathing was harsh and shallow but looking at this little girl felt safe but me at sweet ease. "


    anita "I have no idea why my 'imaginary friends' are getting more out of hand."

    anita "Or that it feels like they're not so imaginary anymore."

    anita "But I won't let anything hurt you. I promise."

    ## Meowing SFX at the same time as the dialogue. 
    play sound meow4

    void "Meow."

    "Her response was all I needed to feel like everything will actually be alright. "

    "The world may be a crazy place right now."

    "Or maybe I'm just crazy. "

    "But with Void by my side, it feels like I can take it on and make it out in one piece. "

    "Too bad someone is looking for you. "

    "Oh well, at least I can take comfort in the company at the moment. "

    "But for now I passed out on the floor, not even wanting to get into my own bed. I just felt nice enough with Void snuggled up next to me. "

    "I like this."

    "Good night Void."

    return