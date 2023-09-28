label scene_201: 
    #black bg probably
    
    anita "Mmhmm...."
    
    "Hm... What time is it? It's so dark. I know I left my phone somewhere around--"
    
    anita "Ngh!"
    
    scene anitaRoom bg
    
    "I recoil from the bright beam burning my eyes."
    
    "Where is the dimmer...? Oh, there it is."
    
    "That's better."
    
    "Ah, I'm so thirsty. I should pour myself something to drink. Now where was the flashlight feature for my phone again...?"
    
    "I peel myself out of bed, slipping into a pair of slippers, phone in hand to illuminate a path through the dark room. I shuffle my way to the kitchen."
    
    "Thankfully, my search for the light switch was short-lived. Finding a newly unpacked mug from the cupboards was shorter. Before I can turn on the tap to fill my mug, however, I hear a-"
    
    #SFX: Thumping Noise
    
    "THumP! tHUmp! ThuMP!"
    
    "Wh-what was that?"
    
    anita "Void? Where are you?"
    
    "No response. No meowing, no scratching of paws on wood, nothing. She's not here."
    
    "I let out a shaky breath."
    
    "I-it's fine. It would be better if I didn't bother her with something as minor as this, anyway. Maybe it was one of the neighbors asking for help?"
    
    "I peek through the peephole."
    
    "It's dark. I don't see anything moving in the shadows, but I can still hear something thumping in the hallway."
    
    "What should I do? What if someone fell and couldn't call out for help? I can't stand here and do nothing!"
    
    "Can I?"
    
    jump scene201_choices

label scene201_choices: 
    menu: 
        "Open the Door and Investigate.": 
    
            jump scene201_label101
    
        "Keep the Door Closed.": 
    
            jump scene201_label102

label scene201_label101: 
    "N-no, I-I can't ignore this!"
    
    "I'm scared, but... what if it's Mory on the other side of the door? Or Vivian? Or Elleanor?" 
    
    "I'll never be able to forgive myself if something happens to them! I have to go and do something!"
    
    "I grip the knob with clammy hands and turn."
    
    scene hallway bg
    
    "...It's quiet."
    
    "The thumping noise, it's... gone."
    
    "As soon as I left my apartment, the hallway fell silent."
    
    anita "H-Hello? I-Is anyone there?"
    
    "There was no answer."
    
    "Why is no one answering? Are they seriously injured?"
    
    "... No, that doesn't make sense. They would call out, wouldn't they?"
    
    "Not unless this was a-"
    
    anita "A... prank?"
    
    "My breath catches. Phantom images invade my mind."
    
    "Will Vivian pop out of nowhere in a scary monster costume screaming how she'll eat me? Is Mory behind the corner with a video recorder to capture my sobs? No, what if Elleanor comes from behind to pour a bucket of blood over me?"
    
    "They're here, aren't they?! I shouldn't have bothered them earlier while searching for Void's owner! What did I do to make them hate me?! What can I do to make them stop?!"
    
    "My throat constricts."
    
    "No, not again. Not now!"
    
    "I gasp, scrambling for breath."
    
    "I can't-"
    
    "I have to-"
    
    scene anitaDoor bg
    
    "My apartment- the door-"
    
    "Where is it?! I can't see-!"
    
    "My phone groans in protest as my grip tightens."
    
    "Wait, that's it! My phone!"
    
    "My fingers fumble along the sides until they run against the hard ridge of a button. A shaft of light pierces through the night, illuminating the door to my apartment."
    
    "I nearly sob in relief. My door! There it is-!"
    
    "SQUELCH!"
    
    anita "AH!"
    
    #SFX: Wet Squishy Footprints
    
    "Wh-what did I just step in?! Why is the floor wet?!"
    
    "A-are those... footprints? But why are they so huge? And that shape... it doesn't look human or any animal I\'ve ever seen. They\'re all over the hallway too, as if it was pacing up and down the corridor, waiting for-"
    
    "I lift my phone higher and shine its light down the dark depths of the hallway."
    
    #CG: Monster
    
    #VFX: Camera Shake
    
    anita "AH... AH...!"
    
    scene anitaRoom bg
    
    "My fingers catch on the knob of my door. I swiftly dash into my apartment, slam the door shut, engage the deadbolt, and throw myself under the covers of my bed."
    
    "I didn't dare to shut my eyes that night. Why does that thing keep wanting to hunt me down and eat me?"
    
    $ sawCreature = True
    
    jump scene201_continues

label scene201_label102: 
    "N-no, I shouldn't go outside. What if I try to help and make things worse?"

    "Or maybe it's not an emergency after all. What if it's just a branch knocking against a window?"

    "It would be embarrassing if someone saw me kicking up a fuss over something so inane. My neighbors will think I'm crazy. I shouldn't give them any reason to hate me earlier than possible. I should stay inside before anyone sees."

    "I drain the rest of my mug and wash it, shoving the suspicious sounds coming from outside out of my mind. I slip under the covers of my bed and close my eyes."

    "At least, I try to."

    "I stare at the wall of my bedroom in confusion. I can feel it. There's something there beyond the drywall in Tom's apartment. I feel a tug in my gut, drawing me closer. Helpless, I wander forward to the familiar call."

    "Why do I feel like I know them, though? How can I sense their presence?"

    "My fingers brush against the smooth surface separating our apartments. I press my ear against the wall, listening closely for a sign."

    astaroth "...exitium...potentia...mors..."

    "Wh-what is that? Am I hearing things?"

    "Those words... they're sending chills down my spine. Every hair on my arm stands on end."

    "I don't know what this is, but it's clear I need to leave. I've been seeing and hearing things that aren't there."

    "Have I gone crazy?"

    "Have I finally lost it?"

    "I squeeze my eyes shut, staving off the tears threatening to spill."

    "Maybe I have. It would make sense. It's a suitable punishment for someone like me."

    $ heardChanting = True 

    jump scene201_continues

label scene201_continues: 
    "It's morning. I finally slept, but I feel like I've hardly had a wink of rest."

    "I don't know where to begin describing what happened. Was it a dream? A nightmare? A hallucination?"

    "I cover my mouth, barely restraining a sob."

    "I moved here to escape everything that happened with Allen, but nothing has changed. Everything is worse. I'm getting worse. The walls are closing in, and I can't find a way to stop it from crushing me."

    if sawCreature: 

        "What did I see last night? Who was that monster in the hallway? Why were they there?"

        "That grotesque figure... that formless face..."

    if heardChanting: 

        "What did I hear last night? Who was in Tom's apartment? What was that chanting about?"

        "That oddly familiar presence... That chilling voice..."

    "Thinking about it is enough for my heart to be gripped by a wave of dread."

    "I don't understand what's happening to me. Reality has become a nightmare. I don't know what is real and what isn't anymore."

    "Am I dreaming? Is this a nightmare?"

    "Please, let me sleep. If not and I'm awake, then..."

    play audio meow1

    void "Mreow!"

    anita "V-Void? You're back! Where have you been?"

    play audio meow2

    void "Mreow."

    anita "Oh, right. You can't answer. That was stupid of me."

    "Void nudges my hand. I faintly smile and scratch behind her ears, making her purr."

    call screen petVoid

    anita "I'm sorry you're stuck with such a uselss person, kitty. If it were anyone else, the person petting you would be your owner. Not me. They must be worred sick about you."

    #Show angry Void

    void "Grr."

    anita "Ow!"

    "She bit my hand. Not enough to draw blood, but it still hurts."

    anita "What was that for?"

    void "Hmph."

    "Void leaps off the bed without another word, scampering out the door."

    "I should follow her example and officially start the day instead of wallowing in bed."

    "I slip out from under the covers and pad over to the kitchen. I fix myself and Void breakfast, pondering over my list errands today- namely, unpacking the rest of my boxes."

    "I glance over at the sea of cardboard packages filling the living room. I can feel what little motivation I had to start the day flee me."

    "I'll just... grab a bit of fresh air before tackling that. A walk would do some good to clear my head after the events of last night."

    scene hallway bg

    "I grab my keys and step out into the hallway, Void meowing after me."

    "I cough and cover my nose."

    anita "Wh-what's that smell? Oh goodness, I don't feel well."

    "I look at the source."

    "It's Tom's apartment. The once pristine door from yesterday was long gone. Mold dominated the wooden frame overnight, enveloping the painted wood with its tainted hue."

    "How did this happen? There's no way for mold to spread this quickly, right?"

    "I-I should take a picture to show the landlord. I don't think Tom would appreciate seeing what happened to his door when he returns."

    scene vivianDoor bg

    #door minigame

    "This is only the second day I've been here, and yet countless incidents have already taken place. I shouldn't leave Void alone in my apartment. Who knows what will happen to her? I'm too weak to protect her, but at least I'll know she's by my side."

    jump scene202


label scene202: 

    vivian "Hey girl! What's up?!"

    #Image: Vivian in costume

    "A screech escapes me as I hold onto the leash for dear life. I turn to see a humanoid type thing with a Jack-O-Lantern for a head. As any means to protect myself and Void, I chuck my phone at the unknown entity."

    vivian "Ow! Son of a bitch chill out Anita, it's me!"

    "Underneath the pumpkin head is a now slightly irritated Vivian. Now looking sweaty but still merry from the events of her night. Her makeup is all smudged and she either lost or ditched the wig. At least someone is having fun tonight."

    anita "I'm... so sorry! I didn't realize it was-"

    vivian "Nah, don't worry bout it. Do I look mad bout it? I'm not mad bout it."

    vivian "Don't you dare answer that question or else I swear to god I will rip out all your bones, rearrange them and make ya do Cha Cha Slide."

    "Well that is... a creative one."

    "I don't know hwo this person is but I think they body swapped with Vivian!"

    "..."

    "Or you know she's very intoxicated, that makes more sense. I don't know if it's from alcohol or weed but all that matters is that Vivian is out of it."

    "I take a few deep sniffs."

    "Yup, alcohol. Specifically tequila."

    "Stepping away from her while trying to keep Void close to me, I observe Vivian to see she's the violent kind of drunk. She doesn't seem like it at least upon first glance."

    "No, it's the harder liquor that makes you violent."

    "Just like with... mom..."

    #Background: Black

    mom "Anita, stop it right now! There is nothing outside!"

    young "Yes there is, mommy! It's right next to Emma! It has fifty eyes and everything!"

    "I'm remembering it so clearly now. It was the morning of my sixth birthday. The house was decorated so nicely with balloons and streamers since we were expecting guests to arrive soon for my party."

    "It didn't stop mom from hitting the bottle of vodka early."

    "The smell of it still makes me think of her."

    emma "Mom! Make her stop! She's starting to freak me out!"

    emma "She's making things up again!"

    young "I am not! Now I hope it eats you!"

    "That set my sister off as she lunged at me, pulling at my hair and hitting me. Which is almost funny to me now since she took something imaginary so seriously."

    mom "Girls enough!"

    "Within an instant, my sister and I fell silent. Mother took in a sharp inhale and she pinched the bridge of her nose. We waited patiently for what our fearless overlord had to say."

    mom "Okay. Here is how this is gonna go. It's either we go and have fun with everyone who is coming for you."

    mom "Or, mommy gets on the phone and calls everyone to let them know they wasted their time coming here for your birthday. Which one do you want?"

    young "..."

    young "I'm sorry... I'll stop."

    mom "Good girl. Are you ready, Drew?"

    dad "Coming, hon!"

    mom "Alright, there's still cleaning around the house that needs to be done before everyone arrives. Give me a hand."

    "While my mother's back was turned, Emma gave me the nastiest smirk as if she knew she won our little fight. The worst part was that she was right."

    "In a fit of desperation for any kind of validation, I remembered grabbing my dad's arm before he got past the front door to pick up around the yard."

    young "You believe me about the monsters..."

    young "Don't you, daddy?"

    dad "..."

    dad "I'm busy, sweetheart. WHy don't you and Emma go play?"

    "That was the moment I knew that neither one of my parents saw what I could. I wanted to be in denial like both of them so badly. But there was no denying what was always right in front of me."

    "It just would have been nice to... actually have them beside me unconditionally. Emma always has them but it's too much to ask for their love to be shared. She still does. I just needed to take long deep breaths. Just like what the therapist said."

    "Do your breathing exercises."

    "Inhale."

    "Hold."

    "Exhale."

    "Ho-"

    "Yet the next thing I know, I feel my damp cheek beneath my fingertips. How long hand tears been rolling down my face?"

    scene vivianDoor bg 

    vivian "Hey? Ya aight?"

    "Quickly wiping the tears away, I divert my full attention back to Vivian who is now leaning against the wall. God how much did she have to drink?"

    anita "I feel like I should be asking you the same thing."

    vivian "You think I can't handle myself? I ain't some chump! I am invin-"

    vivian "..."

    vivian "I'm gonna be sick now."

    "Withoug skipping a beat she proceeds to projectile vomit all over the hall floor. Mr Lamlor is gonna have a fun time hearing about this complaint."

    "I know I should leave well enough alone and go back inside to get some sleep. I don't want to get involved in a situation like this again."

    "But each time I look back at Vivian struggling to keep herself together, I couldn't help but see someone crying out for help but has too much pride to actually say the words."

    "It's like if I ignored Void even though she needed my help."

    "It's worth a shot, right?"

    anita "Do you want any-"

    vivian "I know what you're gonna say and I don't want it! This girl can-"

    vivian "Oh god!"

    "Vivian clenched her stomach as she slid down to the floor. This girl was obviously in more pain than she wanted to admit."

    "As if she wants to still preserve whatever pride she has left, Vivian looks my way and weakly nods. Taking this as my cue, I start thinking on how to actually help her."

    "Who could possibly be up at this hour that's willing to lend a hand? I frantically look around to all of the other doors down the hall as I try to think."

    vivian "Just... get Mory... that bastard sleeps less than I do."

    scene moreDoor bg 

    play audio doorKnock1

    "At her insistence, I go up to his door and lightly knock on it. The fear that he was asleep still plagues my subconscious."

    vivian "Ugh move."

    #SFX Kicking Door

    "Clearly this wasn't a concern for Vivian as she started kicking at his door with all of her might. She has a talent for scaring me and Void."

    anita "Ssssh, people are still sleeping."

    vivian "Fuck people, I'm in pain."

    "Before Vivian can pull back for another kick, Mory yanks the door open with a look of sheer terror that he has every right to have."

    mory "What? What happened?! Is the building on fire?"

    vivian "No, but my insides are."

    mory "O-oh not again. I've told you before that if you planned on partying this hard to call me so I can pick you up. I don't want you going home alone by yourself or someone that could hurt you. You know it's dangerous."

    vivian "Eh, I took a taxi. Give me a break."

    "It's more concerning that this happens so much that they need a game plan."

    anita "I think you can assume now why I knocked on your door."

    mory "I can... smell it."

    vivian "Oh shove it!"

    "As if she didn't just openly insult him, Vivian dug into her pockets and threw a ring of keys at Mory. One of her keychains is an anime bunny. It's really cute."

    scene vivianDoor bg

    "Locating the right key to her apartment as if by memoy, Mory proceeded to lean down to her level to wrap her arm around his shoulder. I did the same with her other arm as we shuffled inside her apartment."

    "The two of us gently left Vivian sitting upright n her couch as we each took a seat on each side of her. I don't feel right leaving someone after learning that someone is this drunk. Too much could happen and I don't want to take that risk."

    "I could tell by how Mory is staying that he's thinking the exact same thing."

    "Though the situation was a little tense for Mory and I, Vivian was sitting in between us with a grin that would make the Chesire Cat jealous."

    vivian "Hey, hey guys, I got somethin' I need to tell ya."

    vivian "So I have a brother that works at a gas station on Halloween night."

    vivian "Guess that makes him my pump-kin."

    "That was so stupid that Mory and I both had to hold in a laugh."

    vivian "I made out with a vampire last Halloween. Do ya wanna know what it felt like? It was a pain in the neck."

    "Why do I have the sense of humor of an old person? That one got a laugh out of the both of us while Void just looks disappointed in all of the humans in the room."

    "It feels... nice though to have fun with people close to my age. Sure it didn't start off that way but I'm glad the mood changed."

    mory "Sure that really sucks but I feel more bad for witches. They must have a hard time trying to find their makeup brand."

    mory "They hate to run out of their mas-scare-a."

    "That one got more of a laugh out of us. Vivian has the excuse of being hammered whereas I've got nothing."

    "I don't really see the harm in joining in."

    anita "Where do ghosts like to go for vacation?"

    anita "Mali-boo!"

    "All Three" "Hahahaha!"

    "That last one was so bad it sent all of us into hysterics. Who knew all three of us have a terrible sense of humor?"

    "After a huge fit of laughter faded away, the room became almost eerily quiet. We all must be thinking about the weird tension in the hallway."

    "Maybe I can help break the awkwardness... I hope."

    anita "So... how did the party go? From how you came home you looked like you had a lot of fun."

    vivian "Oh dude, it was so much fun! My coworkers and I hit up this house party where everyone had to be in costume so it was on point!"

    vivian "There was a costume contest where I got jipped! I lost out to a sexy Play-Doh and a dude dressed up as a sexy waitress."

    vivian "I won in a drinking contest, we passed around a bong."

    mory "I knew I smelt weed on you."

    vivian "That's because a certain SOMEONE won't be my dealer."

    mory "That's too bad that they'll never be."

    vivian "They would make more money than being a middle manager."

    mory "They'd rather have thier morals than money."

    vivian "Eh, screw morals make money."

    vivian "..."

    mory "..."

    anita "..."

    "The awkwardness came back again. Oh no! What do I do now?"

    vivian "...I'm sorry."

    vivian "For snapping at you, I mean."

    "My head veered in Vivian's direction, almost unsure if that was meant to be directed at me. From Mory's empathetic expression this was something that he's heard plenty of times. So it must be for me."

    vivian "I just don't like owing people favrs. They always end up biting me in the ass later on so I'd rather not deal with that."

    vivian "So it has nothing to do with you. It's other people."

    vivian "It's... other people..."

    "As if her personality flipped a switch, Vivian brought her knees to her chest tightly and started... crying? Void leaps up next to her and starts rubbing up against her."

    vivian "I didn't have that good of a time..."

    vivian "Just... why can't I once just wear something that I want to feel pretty in without some creep wanting to grope or cat call me?!"

    vivian "All I heard all night was \"You wanna play my game, baby?\" or \"Being with me is the fun kind of torture.\""

    vivian "So I thought maybe drinking could make it all just a little bit more tolerable."

    vivian "Sure I could have left but I cam there with coworkers. If I make things weird at a place with all of their friends it's gonna be weird at work too. And I really need this job..."

    vivian "It's not fair! It's not fucking fair!"

    vivian "Why does this keep happening to me?"

    mory "I wish I knew how to answer that. I'm so sorry Viv."

    anita "I am too."

    "To try and give her some kind of comfort, Mory and I wrap our arms around her in a safe embrace. I know I would want one in her situation."

    "Vivian stays in her same position, not moving an inch. But she isn't protesting either so maybe she's liking the fact that we're trying."

    "Maybe..."

    vivian "..."

    vivian "Move."

    "Pushing her way out of our arms, Vivian fumbles her way to her kitchen where she starts retching over her sink. It's not a pretty sight."

    "Mory is holding her hair back while I rub her back in small circles."

    anita "It's okay, let it all out."

    #SFX: Thump

    "Suddenly, Vivian's knees buckle in on themselves making her collapse to the floor. Mory tries to hold her up but gravity won out in the end as she fell to the floor."

    anita "Oh my god! Are you okay?"

    vivian "... I think I'm dying."

    anita "WHAT?! OH MY GOD!"

    anita "I'm calling an ambulance!"

    vivian "Nah, nah, don't do that. That costs money."

    vivian "Just hand me my coin."

    anita "Your.... coin? You just said you were dying and you want that!"

    "While I was hving my freak out session, More made his way back into the living room and came back with the same golden coin that Vivian was oddly overly protective of."

    "Grabbing it from him, Vivian brings it up to her eye so that she look through the square hole carved out of the middle."

    "...I have no idea what's going on right now."

    "Should I be scared because I'm starting to..."

    mory "Vivian, what are you doing?"

    vivian "I'm seeing if I'm going to die, what did it look like?"

    anita "It looks like you're... staring through a coin."

    vivian "Ugh I don't expect you to understand."

    vivian "Hm, that's weird."

    vivian "It's not working."

    mory "But it always works as soon as you put it to your eye."

    mory "How is that possible?"

    vivian "Don't you think I know that jackass? Come on you stupid piece of garbage!"

    "As if trying to get an old fashioned tv to work, Vivian tried banging the coin against the cabinet. I'm... not seeing what this is accomplishing."

    anita "Then... I don't know... please help me to understand. I'm a little confused on how a coin can see if you need medical attention."

    anita "I'm just... really concerned for your well being."

    vivian "..."

    vivian "Fine. Just because it showed me that you're a decent person."

    "With a scoff Vivian pulls herself back up, using the sink to steady herself."

    "Oh go, did I say something wrong again? She looks like she's upset at me for asking at all or that she feels forced into telling me a dark secret. The uncertainty of her emotions make me cling onto Void even tighter."

    vivian "Look, I am not in the mood to repeat myself so you better be listening the first time around. Got it?"

    anita "Y-yes, I'm listening."

    vivian "Good."

    vivian "You see, this coin right here? Well whenever I look through this fucking thing. I can see what's gonna happen in the future."

    vivian "It usually shows me not so good things that will happen. So I wanna see if tonight is going to finally be the end of Vivian Moore from alcohol poisoning."

    "Can drunk Vivian please keep her emotions consistent? I can't tell if she's mad or just being dramatic."

    "... Also did she just say she has a fortune telling coin?"

    "I might be seen as a doormat by most people but I'm not gullible."

    mory "Please take this serious Viv."

    vivian "What? I deserve to have a little fun tonight. Let me have this."

    anita "I don't want to sound like I doubt you or anything but it sounds a little... out there to be real. The fact that something like that would exit would be more well known, don't you think."

    vivian "That's because it's a long time family secret. It came into my family's possession because most of us haven't gone nuts using it."

    anita "I'm sorry, I'm just having a really hard time believing it."

    vivian "Alright, let me tell ya this then. How do you think I knew your name?"

    vivian "This little baby predicted you would come here."

    anita "You... could have heard it around the apartment complex."

    vivian "First off, this guy over here is the only one I have more than small talk with or outright hate."

    vivian "And second, how was your conversation with Elleanor?"

    "My questions were caught in my throat as soon as I heard Elly's name. How did she know I was talking to her when I first got here?"

    "It's either Vivian was stalking a person she's never even met at that point or... it's true."

    vivian "Now if you both could kindly shut the fuck up so I can concentrate."

    vivian "..."

    "While Vivian peers through the coin though, her face changed from that of drunken joy to unadulterated horror."

    "It's the quickest I've ever seen anyone sober up as she looks in my direction with her pupils dilated. Is she shaking?"

    anita "Um... Vivian... are you-"

    vivian "Get out."

    mory "Wait what? What did-"

    vivian "I said... get..."

    vivian "OUT!"

    vivian "GET OUT!"

    vivian "BOTH OF YOU! OUT! GET THE FUCK OUT!"

    scene hallway bg

    "Without thinking twice, Void and I did as she screamed and left. I have no idea what Vivian is going through or what she saw but it's in my best interest to not question it right now."

    "I could hear Mory trying to calm her down but all she did was keep yelling the same thing over and over again through the door."

    "Not long after Void and I left, Mory did the same looking disappointed in himself."
    
    "This... this is all my fault again, isn't it?"
    
    "I'm not that stupid, I could tell by the way Vivian was looking at me that it has to do with me somehow. I made her go manic."
    
    "I'm so sorry Vivian..."
    
    anita "I-is she going to be okay?"
    
    mory "Yeah... she's fine. I've seen her through some pretty rough drunk benders."
    
    mory "She's a lot tougher than she looks."
    
    #Awkward silence with no dialog box. 
    
    mory "Hey, why don't all three of us calm down at my place? I think we all need it."
    
    anita "That... would actually be really nice. Right, Void?"
    
    play audio meow3
    
    void "Meow"
    
    mory "Heh, I'd be more than happy to have you."
    
    jump scene_203

label scene_203: 
    "I don't know how to describe what I am feeling."
    
    "I haven't met Vivian for long, but I still did feel she liked me a lot despite a few... blunders. Here and there. Mine and Void's."
    
    "And yet I ruined it..."
    
    "I don't know ho wor what I did but with how manic Vivian suddenly became."
    
    "Please forgive me..."
    
    "Mory invited me to his apartment but I'm a little nervous about entering after what just happened."
    
    "Along with the fact it's been a while since I've been into a man's apartment like this. As much as I don't want to think about Allen, he keeps haunting my mind in a way."
    
    "I don't feel very well. I kind of want to bawl my eyes out but not in front of anybody. I'm sure it wasn't Vivian's intention, but I feel like I wronged her by being in her life already through some weird means."
    
    "Is it really me? Is it the coin?"
    
    "Whatever it is, I'm so conflicted about knowing what she saw or even if it's true or not."
    
    "Mory opened the door to his apartment. Now his apartment smells like strawberries and it is so pleasantly sweet it washes some of my depression away. Some o fmy energies feel like they have been restored."
    
    "What does this man even do to get his place smelling this good? I want to ask for some of it."
    
    mory "Welcome to my place! Couch is over there, have a seat. Do you want some tea?"
    
    "Oh. I left home and forgot to take my morning brew. Or did I? I don't remember."
    
    anita "I'd like some coffee, please."
    
    mory "Oh! Now we're talking. Despite looks, I like coffee just a tad bit more."
    
    mory "I bum a lot of coffee off of Vivian actually hehe."
    
    anita "Oh! Did you know that I used to work at a coffee shop? I made so so so many types of coffee and learned so much! My favorite one was... a double expresso... macchiato..."
    
    anita "..."
    
    anita "I-I'm sorry. I didn't mean to run my mouth like that."
    
    mory "That's quite alright, Anita! Coffee is my cup of tea!"
    
    "That was a long hanging fruit. He's awesome."
    
    mory "What do you like in your coffee? I can't make you a macchiato, sadly."
    
    anita "Hm..."
    
    anita "How about black, but with a lot of sugar?"
    
    mory "Coming right up!"
    
    "He went to the kitchen in a joyful way. His apartment is so lively and the green scenery is great with the pearl white coloring. Such a contrast to the astringent, gothic vibes of Vivian's and the vintage vibers of Elly."
    
    jump scene203_choices 

label scene203_choices: 
    menu: 
        "Look at the plants.": 

            jump scene203_label101

        "Look at the fireplace.": 

            jump scene203_label102
        
        "Look at the paintings.": 

            jump scene203_label103

        "Look out the window.": 

            jump scene203_label104

label scene203_label101: 
    "The several different species of flora brightens up the already pleasant atmosphere. Shades of blues, pinks, and yellows can make anyone's day even a little bit better. Maybe this explains why he is always in such a good mood?"

    "I would be too if this is what I woke up to everyday. It seems like a lot of work to keep them all so healthy and vibrant, but it's worth all the trouble to make oneself and others feel more at peace."

    "I wish I could keep plants like these. Every plant I get ends up dying in a few weeks time."

    "Maybe one day my green thumb will come in."

    jump scene203_continues

label scene203_label102: 
    "I take a few steps closer to the gas fireplace. Which is unironically perfect to have during this time of year. Especially when the air outside is starting to get more chilly."

    "I crouch down ever so slightly to extend my hands out like I am warming them over a campfire. In some ways, it feels nice and rustic. Even if it isn't a log cabin in the middle of the woods, the accomodations in here makes an apartment on the 3rd floor feel like one."

    jump scene203_continues

label scene203_label103: 
    "I diverted my attention to the artwork over the fireplace. They all have their own little bits of personality to them. One is a simple painting of a small bundle of yellow flowers. Another one is a landscape picture of the coral reef. "

    "The last one was of an abstract image of a group of cats playing what seems to be jazz music under the moonlight. It is initially a bit funny to look at. But the more I think about it, the more it does explain the type of person Mory is."

    "Calm."

    "He is indeed a cat person."

    "But overall, just that he takes a slower approach to see things through to the end."

    "Or that is at least how I interpret it."

    "I wouldn't be surprised if I was wrong though."

    jump scene203_continues

label scene203_label104: 
    "I pull back the beige curtains a tiny bit to take a look at the city in a brand new life at night. "

    "The music thumping all across down, lights decorating the dark scenery, people my age partying their worries and cares away."

    "It was almost nice to see if it wasn't also depressing."

    "But as I keep staring through the window I could see everything is a bit... too dark outside."

    "To ease my growing curiosity, my fingertips met the glass but I could feel there was something over the glass itself. Are these windows tinted?"

    "Why would Mory have tinted windows? Maybe it might be a way to help the plants grow better inside."

    "Or at least that’s how I want to see it."

    jump scene203_continues

label scene203_continues: 
    "Mory came back gleefully with two cups of coffee, one in each hand. Sat down on the couch opposite to me, legs crossed and handed me the steaming mug."
    
    mory "There you go, ma’am. With a mountain of sugar, of course!"
    
    "Mory handed me a colored ceramic mug filled with a brew worthy of being sipped. It has the most pleasant aroma I’ve ever had a whiff of, even after working years in that shop."
    
    "I don’t think I would make something this great when I worked at the Sunrise Cafe for ten more years. Mory is, clearly, on a whole other level when it comes to brewing coffee."
    
    "I wish I had any amount of that skill."
    
    "And, no surprises, it tastes as good as it smells. How did he guess the amount of sugar that perfectly? It is absolutely INCREDIBLE."
    
    "I can taste notes of almonds and chocolate."
    
    "This man is as cozy as it gets. I need some insight into his skills."
    
    anita "This is absolutely incredible, Mory. I cannot BELIEVE coffee this good could exist!"
    
    "Before he seemed a bit weary or pensive, but as soon as my compliment got processed, he let out an amazing ear to ear smile. Cute."
    
    mory "Glad you like it!"
    
    mory "One day I wish to grow my own coffee beans, but it is a little out of scope for this apartment."
    
    anita "That’s such a wild dream. I hope you get around to it one day. That’s gonna be so cool. I will definitely be one of your regular customers."
    
    mory "Thanks. That’s great to hear."
    
    mory "For now I’m a little stuck in this apartment, but I have big dreams and a whole lot of ambition. You’re gonna have it for free!"
    
    anita "Your ambition to chase that dream is what matters!"
    
    "I wish I had a tenth of this much energy and determination. He’s so upbeat."
    
    "I don’t really know how it feels to be this good at a hobby."
    
    "If anything…I’ve forgotten what it’s like to have dreams. It seems like everything is a waking nightmare."

    mory "How about you?"

    anita "What about me?"
    
    mory "Any wild dreams?"

    "Is he secretly a mind reader?"

    anita "Oh... uh... I really want to become an artist. You know, draw stuff?"

    mory "Awesome dream! I tried the same once, but didn’t really work out. I was {i}really{/i} bad."

    anita "I used to be god awful! But I had a rough childhood and drawing was what kept me from being overwhelmed, so I guess I won through pure insistence."

    mory "Oh. I’m sorry to hear that. You seem to be doing fine now, aren’t you?"

    anita "Somewhat. I had a few tough years, but I’m feeling a lot better."

    mory "I would love to see what you draw someday."

    anita "Once I gain the confidence to, I’d like to show you."

    "I do in fact feel better than how I used to, but today and yesterday were a little hard to wrap my head around. I’m not used to people treating me nicely."

    "The only people who genuinely cared about me were a few school friends and co-workers. And they probably cared for me out of obligation. Maybe Allen did as well in the beginning."

    "I don’t remember why I fell for him. But I still can’t get him out of my mind."

    "Now I’m depressed again. Thank you, brain. At least Void seems to be having fun. She jumped on Mory’s lap and made herself very comfortable."

    "Maybe another sip will make me feel better."

    anita "No, Void! Get down! You’re gonna make him spill hot coffee on you!"

    mory "Oh, it’s alright, Anita. He’s such a sweetheart!"

    #SFX: Meow
    play audio meow3

    void "Meow."

    anita "He’s a she actually. I only found out yesterday."

    mory "’m so sorry sweet baby girl. You’re the prettiest little princess."

    "Acting like she’s not offended at all, she curls herself up and purrs so loud I can hear it all the way over here. "

    "Well, if Mory doesn’t mind, who am I to judge?"

    "Void sat right up and is joyfully fidgeting on Mory’s legs while he drinks his coffee. I’m a little afraid, but I trust his careful demeanor."

    "I’m a little jealous."

    mory "She is the cutest celery…!"

    anita "...Celery?"

    mory "Oh. I just said the first thing that came to mind."

    anita "She really is a cute… uhh… cassava?"

    "This is hard! What in tarnation is a cassava?"

    "He smiled and let out a giggle."

    mory "I love cassava!"

    anita "Say, what's cassava?"

    mory "A South American root vegetable. I love it."

    mory "I’m trying to grow some actually."

    anita "I never had it. I only knew by name, and it sounds a little funny."

    mory "You should try it! It is very.... stringy."

    mory "..."

    anita "..."

    mory "I can tell you’re confused. We needed to address the elephant in the room."

    "I completely forgot. The coffee and small talk was so good that the coin incident left my mind."

    anita "Uhh… Yeah, about that."

    mory "You see, that coin shows her something bad or trivial that is going to happen to her soon whenever she looks through the hole."

    anita "…I’m still not sure if I believe her. I know she isn’t any kind of prankster, but…"

    mory "Oh, I know right. I know it sounds crazy but that coin has some kind of magical power."

    "I’m genuinely confused. Magical…?"

    "What exactly does that mean?"

    anita "You mean magical as in sorcery? Dark arts? Mystical?"

    mory "Yup."

    "Okay. I don’t think I have any other way of reacting to this appropriately. I stare at him for a few seconds before collecting my thoughts, leaning a little forward on the sofa and speaking my mind."

    anita "That is..."

    anita "SO COOL!"

    mory "Yeah, I know it is pretty cool. Whenever she uses it, I get to hear all about it."

    mory "She has all of them written down somewhere. After a while she tends to forget what she sees so she jots them down for later."

    anita "Then why didn't she tell you this time? Does she use it often?"

    mory "I don't know and that’s what’s making me really worried. This is the first time she didn't tell me anything. I’ve never seen her act so scared over it either."

    mory "And no, she only uses it if she really needs to."

    mory "Maybe this time she was drunk and didn’t like what she saw?"

    anita "Maybe she saw something bad that is going to happen to you? Maybe that’s why she was so mad."

    "Oh my god. He is blushing red like a damn tomato. I can’t tell if I made him uncomfortable or not."

    "I am starting to think he may like Vivian. Aw, how cute."

    mory "Oh… uh… I guess so…?"

    anita "If she cares about you, something bad happening to you means the coin would show that, doesn’t it?"

    mory "That makes… a lot of sense…when you put it like that. But I’m not really sure though."

    anita "This may sound a little crazy asking but…do you have one as well? I feel like you do. C’mon."

    mory "Oh, I do! But it's not a coin."

    mory "I can show you."

    "This rollercoaster isn’t ending anytime soon. He ALSO has a magical object?"

    "I’m not sure if I should be scared or not. Maybe I’m just really naive. But my inner child is dying to know if magic is actually real."

    "He puts his mug on the table to his side, picks up Void, puts her on the ground and walks to a closet next to where he was standing."

    "He opens it up and reveals many new plants. At first I didn’t understand, but I quickly understood what was happening."

    anita "Dude..."

    anita "You actually deal weed!"

    mory "Oh, no no, silly. It's not weed!"

    "Oh. He’s right. They are different, looking like almost alien plants. On top of the closet there is a watering can, slightly rusty and ornate."

    "I get up from my seat to get a closer view, hopping over. This childlike enthusiasm of mine must be getting on his nerves. But what can I do? This is awesome!"

    "I just found out magic exists!"

    "Well, I don’t think I should have said it is weed."

    "The plants are labeled based on what seem like their properties, like /“Medicinal/” and /“Aromatic/”."

    "Wait… did he use some of these plants in the coffee?"

    "…Am I gonna die?"

    anita "This one is labeled as aromatic. Did you use any of it for the coffee?"

    mory "Oh no! They aren’t edible. Found out the hard way."

    "That would have been really creepy. Feeding me a completely magical substance unbeknownst to me might be a crime."
    
    "Mory reaches for the can on top of the closet and shows it to me, asking me to hold. It is a little heavier than I was expecting, but it is beautiful. Normally watering cans are made from plastic or just normal metal. This is different."

    "It feels very… warm. I can’t describe it in any other way, but it is not actually hot."

    "I give it a good look around."

    anita "Is this the object?"

    mory "Yes. This closet is of plants I watered with it. It changes them, makes them grow a lot faster and gets them special properties. This one here for example is rosemary watered with the can."

    "He pointed to a purple plant that forms a spiral with its body and has very thin leaves. It’s labeled as \“Medicinal\”."

    anita "How do you know what they do at first sight?"

    mory "I don’t, I have to test them."

    anita "Isn’t that, like, dangerous? You may accidentally eat something you shouldn’t, again."

    mory "It is, but I haven’t died yet, sooo… I don’t think it can make poisonous plants. They at worst tasted awful and I’ve only gotten sick twice."

    anita "If you say so. But how did you even notice they had these properties?"

    mory "I… Uhh… Let’s not tackle that for now."

    "That was a little awkward. Why did I have to say that?"

    "I give a good look again at the closet trying to see any new weird plants and see another watering can tucked on top of the closet."

    anita "Is that Elly’s can?"

    mory "It is! When I want to actually grow other plants that are not mystical, I use a normal can. Which I broke accidentally."

    anita "How?"

    mory "Slipped out of my hand while I was watering my balcony plants. Thankfully, it didn’t hit anyone."

    "I don’t know why but the situation sounds funny. A lot more funny in my head than in his."

    mory "Do you think Viv calmed down?"

    anita "Hmm… I think so. It’s been a bit. Are you going to check on her?"

    mory "I will. I know this sounds a little lazy of me, but can you give the can back to Elly for me? I’ll go out and actually buy one for myself later."

    mory "I’ll go give Vivian a visit in the meantime, see if listening to her crappy music will make her feel better."

    "He picked up Elly’s can from the top of the closet. I’ll do it, because I want to thank Elly for what she did yesterday."

    anita "Leave to me, Mory. You’re a sweetheart. I’m sure Vivian thinks so as well."

    "There I go running my mouth again."

    mory "Hahah… Thank you." 

    mory "Here you go, and thank you again"

    "He gave me the watering can. I’m gonna hold Void’s leash instead of carrying both. At Least she’s good about being on a leash and following my lead. What a well trained cat."

    "I like Mory a lot. Such a receptive gentleman. Vivian got great luck for having him as a neighbor. I hope he stays friends with me as well, and feels nice getting treated well."

    "Don’t you think, Void? You do, don’t you, sweetie?"

    #SFX: Meowing
    play audio meow2

    void "Meow."

    anita "Stop reading my mind. That’s rude."

    "Let’s get this to Elly and give her a warm hug for what she did yesterday!"

    jump scene_204 

label scene_204: 
    "Mory holds the door open for me as I exit his apartment. The engulfing feeling of worry for Vivian's health still weighing on me. I can tell by the look on Mory's face that he feels the exact same way. "

    "Before leaving, I turn to face him with the reassurance I know he needs."
    
    anita "Vivian is a strong person. I'm sure she will get better in no time."

    mory "Yeah. You're right about that. But to stop worrying about a friend is easier said than done sometimes, you know?"

    anita "I totally get what you mean."

    mory "I just hope all goes well for you guys too."

    anita "You too, Mory. I'll see you around. "

    mory "See ya later, Anita."

    mory "You too, little one."

    anita "Heh, say bye, Void."

    scene hallway bg

    "With the little girl in my arms, I take one of her front paws and move it up and down to try and be silly. It made him chuckle a little. "

    "Mory wave to me and Void before we go our separate ways. I can hear the gentle knocking on Vivian’s door. Within a matter of a few seconds, I’m all alone again. "

    "But at least I won’t be alone for too long. I still need to give this watering can back to Elleanor for Mory. WIth my mission on my mind, I put Void bank down and walk towards Elleanor’s door to give it a gentle knock. "

    show ellyRoom bg

    elleanor "Anita!"

    "It didn't take long for Elleanor to answer the door. Once she knew I was standing in front of her, a warm and gentle smile adorned her face. Which is a bit of a shock to me to see her be so energetic. I know if I had a late shift, I would not be so keen on having guests the next day. "

    "I guess Elleanor and I are just built differently. "

    elleanor "It's so nice to see you again, sweetie. What brings you back to my humble abode?"

    anita "Well, Mory wanted to bring this back to you. But he got sidetracked by taking care of Vivian while she's sick. So, he asked me to bring this to you instead while it was still on his mind."

    anita "Sooooo..."
    
    anita "Here you go."

    "I hold the watering can straight in front of me, waiting for Elleanor to take it. She gently took it from my hands with an appreciative smile on her face. "

    elleanor "Thank you, dear. Been a while since I saw this bad boy. Now I can finally throw out that old milk jug!"

    anita "You're welcome!"

    anita "..."

    anita "I guess I should really get out of your hair then. I'll see you later, Elleanor."

    "You don't need to rush yourself out. I was actually going to offer if you would like some tea or coffee while you are here. "

    "It's the least I can do after you just returned what belongs to me. "

    "I stand in front of Elleanor's front door in silence for a brief moment. Looking down at Void right by my feet to see what she thinks. But like most of the time anyway, she looks completely indifferent about the awkward tension as she stares directly at me. "

    anita "I guess it would be alright if I stay a while. If you don't mind, of course. "

    elleanor "Like I said the other day, I wouldn't have offered my time if I didn't have it. "

    anita "I really appreciate it. Especially since I would think you would be catching up on sleep after your late shift last night."

    elleanor "Oh, don't worry about me. I'm not tired at all. "

    elleanor "I know it's a terrible habit, but it's a regular routine for me. I take the late shifts often. So, I have gotten used to not relying on a full night's sleep for quite a while now. "

    elleanor "But enough about me. Come in. My offer still stands for tea or coffee if you would like."

    anita "I actually really shouldn't have any more caffeine in my system. I just had coffee with Mory. If I have any more today, I might be up all night."

    "Even though I already do spend half of my nights up looking outside my window to see what is looking back. But she doesn't need to know that."

    "Even with the rejected offer to the one thing that gets me through the day, I stepped through Elleanor’s door."

    "Yet when I made my way in, I noticed the leash no longer has any slack on it. I turn to see Void sitting there as she was."

    anita "Come on now, don't be rude."

    "Feeling like I have to, I make the short trek back to Void to pick her up and bring her inside. "

    "Seeing the now familiar vintage decor makes me feel at ease to know that someone wants me to visit their home not just once, but twice in a short period of time."

    "I take a spot on the couch as Void curls up right next to me. Elleanor takes the opposite side of me as she brushes off her skirt."

    jump scene204_choices

label scene204_choices: 
    menu: 
        "I heard strange noises." if heardChanting: 
            jump scene204_label101
        "I saw something strange." if sawCreature: 
            jump scene204_label102
        "Everything is going well.": 
            jump scene204_label103

label scene204_label101: 
    elleanor "You did? That’s very odd, I didn’t hear anything."

    anita "That’s because it was like some kind of a chant coming from inside apartment 313. I couldn’t understand anything it was saying."

    anita "It’s kind of freaking me out. Should I be worried about it?"

    elleanor "Oh no dear. I know some people who partake in Pagan rituals from time to time. I’m sure it’s harmless."

    elleanor "Vivian does the same thing and she hasn’t burnt the building down yet."

    elleanor "Well, you already know of my strange little hobby. Regardless, it’s still pretty fascinating."

    anita "I don’t know if that makes me feel any better or not."

    elleanor "I just think you’re putting too much thought into it."

    "I thought no one was in that apartment though…"

    "But maybe Elly is right. It might just be the hallucinations getting to me. Maybe they’re starting to manifest into voices too. Like earlier with me and Void."

    "It’s just nice enough that she’s willing to listen to my crazy rambles."

    jump scene204_continues

label scene204_label102: 
    elleanor "…Define strange?"

    "I describe what I saw to her down to the tiniest gruesome detail. I’ve seen this one more than once already so I have it ingrained into my memory now."

    elleanor "That’s so peculiar. When I was coming in from my shift, everything seemed normal. Or at least as normal as they can be this time of year. "

    elleanor "Are you sure it’s not just a bad dream?"

    anita "No it’s not! I could see it! I could smell it! I could hear it!"

    elleanor "But could you feel it?"

    anita "..."

    anita "No..."

    elleanor "And that’s what I’m trying to tell you dear. Seeing things doesn’t automatically make them real."

    elleanor "I can see that you have a very active imagination. I think that might have a lot to do with what’s going on."

    elleanor "Does that help clear anything up?"

    "No..."

    anita "I... think so?"

    elleanor "Good, now why don’t we clear our minds from all the negativity and enjoy this time."

    "She’s probably right but I know what I saw. It’s either that thing is roaming the halls right now or I really am off the deep end…"

    "Regardless it’s nice to be heard for once."
    
    jump scene204_continues

label scene204_label103: 
    "Maybe right now isn't the best time to make an acquaintance worry about something that doesn't affect their own life. "

    anita "Everything has been peachy keen so far!"

    anita "Everyone has surprisingly been really nice to me."

    elleanor "Why do you say surprisingly like you didn't expect it to happen?"

    "Oh no! Why did she have to catch that? Curse my big mouth!"

    "I'd hate to admit it, but she caught me there. I don't want to invite Elleanor to my pity party. But she did ask so it would be rude of me not to answer. "

    "I don't need to go into great detail, right?"

    anita "I just have been dealt a really rough hand in life."

    anita "It's a lot to explain. I just don't want to overwhelm you with my life story out of the blue. You know?"

    elleanor "I completely understand. We all have had our trials and tribulations to become the people we are today."

    elleanor "It's what makes us all human, after all."

    jump scene204_continues

label scene204_continues: 
    anita "Thank you for understanding Elly. I know it's a lot for anyone to take in."

    elleanor "You are more than welcome, dear. It's the least I can do for a lost soul like yourself."

    elleanor "But for the time being, why don't we lighten the mood?"

    anita "How?"

    elleanor "Well, like do you have any plans for the future? What are your hopes and dreams? I would love to know."

    anita "The future? The closest thing I can think of to a plan is to maybe look into the local coffee shop to see if they're hiring to make some money and keep up with rent and utilities."

    anita "And now a pet I guess."

    anita "It’s not exactly what I want to be doing but it pays the rent and other stuff."

    elleanor "I know exactly what you mean. I’m working at ‘Furry Friends’ only to make ends meet."

    elleanor "I mean, I have a masters in Psychology for god’s sake. I should be helping people but I’m stuck selling pet food."

    elleanor "It can be a little depressing some days but you can only go up in life."

    "I will never understand how she can be this chipper about everything. Even when she says that she’s depressed."

    anita "I mean aside from that, I don't know. Hopefully I can work more on my art career? I just don't know if putting my all into it is the best idea for me right now."

    anita "I want to put my graphic design degree to use but I also need to take care of myself first. And Void too for the time being."

    elleanor "Oh wow! You draw too?!"

    elleanor "Ehm well, I do it more as a hobby rather than a potential career path. But, that must mean you are amazing at it."

    elleanor "I would love to see your masterpieces someday!"

    anita "You have to wait in line. Mory asked first heh."

    anita "All of my art supplies are still in boxes though. But once I have everything out, you will be the second person to see my messy doodles."

    elleanor "Oh hush! I'm sure that you have a natural talent. If anyone here has the messy doodles, it's definitely me."

    anita "If you have anything you are comfortable enough to show me, I can be the judge for whose doodles are messier."

    elleanor "I actually do right here."

    "Elleanor leaps up from her seat with a pep in her step towards her bookshelf. Along the bottom shelf, she pulled out a brown leather bound book with a buckled strap on it."

    "Plopping herself back down on the seat next to me, she flipped through the pages at a slow pace. I take my time to scan each page thoroughly."

    "The first few pages are of different objects in her apartment."

    "Her antique tea set."

    "Her bookends."

    "Even a bowl of fruit."

    "The more pages she flipped, the subjects changed from objects to people. Different expressions of people that I have gotten to know these last few days."

    "Mory."

    "Vivian."

    "But the one that genuinely made me laugh for a brief second was the page of Mr. Lamlor in different stages of anger. From slight irritation all the way to unbridled fury."

    anita "Wow! What did Mr. Lamlor do to deserve your praise?"

    elleanor "Initially, nothing. But when he saw my original sketch of him, he threatened to raise my rent if I continued to be that \"freak who stalks people just to get them on paper\"."

    elleanor "So I tore it out and threw it away. And now I have this to replace what was once missing."

    anita "I understand being uncomfortable, but he didn't need to be such an asshole about it."

    elleanor "Thank you! Finally, someone can see how much of a jerk he is for no reason."

    anita "You know, you can call him an asshole if you truly think he is one."

    elleanor "..."

    elleanor "He is the biggest asshole to roam this Earth."

    anita "Hahaha. There ya go."

    "As our laughter died down, there was still one thought that remained in my mind. Whoever may or may not live in the complex that Void stared at last night. As much as I would love to pretend that nothing happened. It's something that continues to eat at me."

    "If someone were to know, it must be Elleanor. Even if it may be something as obscure as the occult. And I’m sure Vivian doesn’t even want to look at me right now. There has to be an explanation as to why the missing tennant never answered the door."

    "And if he’s missing, why was someone banging on his door…"

    anita "Actually, there is something else that I feel like I need somebody to confide in."

    elleanor "What seems to be the trouble, dear?"

    anita "Do you know about the missing tenant from apartment 313?"

    elleanor "Do you mean Tom?"

    anita "Yes. I talked about him with Mr. Lamlor when I asked about Void. All I got out of him was that he was on vacation and that he is still paying rent."

    anita "How long has he been gone?"

    elleanor "He's been gone for at least a month now."

    elleanor "Now that I do think about it, he does have me worried. Especially to leave his kitty behind. Most of the time, she's his only companion."

    anita "What do you mean by that?"

    elleanor "Tom is... hmm..."

    elleanor "Well the nice way to put it is that he is a bit of a homebody. From the time I’ve known him, Tom doesn't go outside his apartment very often unless he needs to. "

    elleanor "But even when he does, that cat is always right beside him. So I was really confused when you brought her to me the first day you came here."

    anita "Hmm, are you a pretty therapy kitty, Void?"

    "Void's ears perked up once she heard her name. She looked up at me with that blank stare. Which doesn't really confirm or deny anything but it was still cute. Though by the way she would behave when I have my own episodes, it does start to make more sense."

    "Poor Tom..."

    "Once she loses interest in the topic, she lowers her head back down onto the cushion."

    elleanor "But if he is still somehow paying rent, then he must be away for personal matters rather than just a vacation."

    elleanor "Lord knows that man needs some time away. Not sure why he wouldn’t take his kitty though, that’s what gets me."

    elleanor "Or that is what I believe. Either way, I hope he is doing alright."

    anita "I don't know him. But I hope he is doing alright too."

    elleanor "I think you would get along very well with him."

    elleanor "..."

    elleanor "If he would even give you the chance to even say hi, that is."

    "Elleanor giggles awkwardly to herself as she brushes stray hairs out of her face. It leaves me more confused about what she means."

    "I know absolutely nothing about this man, but yet his name keeps haunting me. I wish I knew why but there is always the sense of unease crawling up my spine when he’s the topic of discussion."

    "For a brief moment, I peer down at Void sleeping soundly right by my side. She deserves to at least know what happened to her possible owner so this wild goose chase can come to an end."

    elleanor "Anita?"

    "I snap out of my own derailed train of thought. Feeling bad for possibly not listening to Elleanor, I clear my throat as I turn my attention back to her."

    anita "Huh?! Yes?"

    elleanor "Maybe it might be best to move on from this whole 'finding Void’s owner' thing?"

    elleanor "You are obviously losing sleep over something that is taking you everywhere but getting you nowhere."

    elleanor "Who knows? Maybe Tom will come back sometime soon?"

    elleanor "If not, Void seems to have already taken a fondness to you. Either way, she seems to be happy and comfortable. Maybe she knows that she’s found a good home with you."

    anita "I just don't want to give up yet. If Tom really is her owner and he really is gone, then I would still need to budget in all the supplies it takes to maintain a good life for Void."

    elleanor "The Furry Friends employee discount still stands for you guys if you ever need it."

    anita "It's still sweet of you to do that for me. Someone you just met the other day."

    elleanor "If I were in your shoes, I would want someone to give me a lending hand too."

    elleanor "I'm also always here with an open ear too if you ever need one."

    anita "Thank you Elly. You are too sweet sometimes."

    elleanor "I try my best to treat people the way I would like to be treated. Now please don’t stay up on my account, both of you should be heading off to bed."

    elleanor "And remember, if you ever need an exorcism, I have no idea how to do it, but will be there in a heartbeat to help."

    anita "Heh yeah, I’ll…think about that."

    "Gently picking up Void, trying my best not to disturb her but ended up doing so anyways, I journey down the possibly unsafe hallway to make it back to my apartment."

    jump scene_205

label scene_205: 
    "I knock on Vivian’s door."

    "I’m worried about her. I know she’ll be safe in Mory’s care, but I still want to confirm that she’s okay. I need the assurance for myself."

    "I couldn’t do anything earlier to help her sober up. I even bothered Mory because of my inability to help. I want to check on her and ease my worries, even though I know how selfish it is to disturb her rest. "

    "It’ll be alright if she hates me for pestering her like this. As long as I can see that she’s alright, I can bear the brunt of her hatred of me. I deserve it after all."

    mory "Anita! Are you here to see Vivian?"

    anita "Mory? Y-you’re still here?"

    mory "Oh, yes. I’ve been waiting for the effects of the herbs I gave her earlier to kick in. She’s still not all there, but it looks like she’s starting to come around."

    anita "So does that mean she’s alright?"

    mory "Give or take a few minutes."

    mory "Oh, where are my manners? Sorry, come in! Come in!"

    anita "Would she even want to see me after…you know?"

    mory "Don’t tell her I told you this but she was asking me about you too."

    "The fact that she was thinking about me when she was the one suffering brought a bit of hope for our budding friendship."

    anita "B-but that’s alright! I wouldn’t want to intrude! Besides, won’t you get into trouble with Vivian if you invite someone into her apartment without her knowledge?"

    mory "If it was a stranger? Sure. But Vivian and I know you, so it’s fine. I could use another pair of eyes to make sure our resident drunk doesn’t accidentally wander into the hallway."

    anita "Oh! In that case, pardon me."

    "Mory moves aside to let me into the apartment and closes the door softly after me."

    "Vivian was lounging across the couch with an arm slung over her eyes, groaning in agony. She changed out of her costume sometime earlier for her usual outfit."

    "Mory hands her a glass of water. From there, Vivian shuffles against the cushions until she’s sitting upright. She knocks back the entire glass, draining it dry with an exhausted sigh. "

    mory "Feeling better?"

    vivian "It tastes like something died in my mouth and invited the rest of its extended family to die there with it. What the hell did you make me shove down my throat?"

    mory "The usual natural remedy. It’s as effective as it is nasty."

    vivian "Are you sure about that? Because my stomach says otherwise."

    mory "Well, it seems you’re able to speak properly again. Welcome back to sobriety."

    vivian "Keep acting all cheeky, and we’ll see who can speak properly in the next five seconds."

    mory "Hey, you wouldn’t hurt me in front of a guest now, would you?"

    vivian "I’d say you’ve overstayed your welcome, Mory."

    mory "I wasn’t talking about me, I was talking about Anita."

    vivian "Hm? Oh, you’re here."

    anita "Um, I can leave if you want."

    vivian "Geez, relax. You look like I’m about to break your jaw or something!"

    "Would it be wrong to say I wasn’t?"

    vivian "Look, you don’t have to worry about it so much. Besides, it looks like your little guard dog has you covered."

    "Vivian says this while pointing at Void as she nestles into my arms. I feel like I spoil her at times. That’s not changing anytime soon though."

    vivian "In any case, I wanted to say I’m sorry to you for kicking you out of my apartment earlier."

    anita "Oh no, it’s fine! I understand if I was bothering you—"

    vivian "That’s not it. It was—"

    vivian "..."

    mory "It was what?"

    vivian "Never mind."

    vivian "It's not important."

    mory "Vivian please-"

    vivian "Hey Anita, what made you move anyway?"

    anita "Um... I, uh... erm..."

    "The way Vivian shifted topics was very odd. I want to inquire further, but… it’s not my place to. "

    "Still, I feel an unsettling unease weighing upon my mind."

    jump scene205_choices 

label scene205_choices: 
    menu: 
        "Tell the full truth.": 
            jump scene205_label101
        "Tell a half truth.":
            jump scene205_label102
    
label scene205_label101: 
    "You don’t make friends by keeping secrets, right? Besides, I like to think what happened wasn’t my fault. That’s what my therapist says at least."

    anita "…My boyfriend cheated on me and kicked me out of the apartment."

    vivian "..."

    mory "..."

    anita "Please don’t see me any differently! I know I could have done better in the relationship. It’s my fault that he was lead astray, I should have-"

    vivian "Why…are you trying to stick up for someone that hurt you?"

    anita "B-because even my parents rationalized that-"

    mory "Your parents defended the guy that hurt their daughter?"

    vivian "Dude…this is so fucked up that they’re having you believe that this is normal."

    mory "You have someone to talk to about this, right?"

    vivian "Also do you have the address for your old place? I’m asking for a friend."

    mory "I’m sure that’s not helping much."

    vivian "What? I’m just saying if she-"

    anita "I want to stop talking about it!"

    "As soon as my cries are heard, the pair stops and looks apologetically in my direction once again. But I can tell by the look in their eyes that this topic isn’t over with."

    anita "Thank you…"

    jump scene205_continues

label scene205_label102: 
    "I don’t think this is the time or place to tell them in on that side of my life. I only just met them and I don’t want them to pity me."

    anita "I wanted a change of pace. I thought it would be nice and exciting to live somewhere new for once."

    vivian "Huh. I never pegged you for the adventurous type."

    vivian "I guess you can’t judge a book by its cover, huh."

    anita "I suppose..."

    mory "I know exactly what you mean. Change can always bring a new peace of mind."

    mory "I miss my family a lot back home but I needed to get away from them at some point."

    vivian "Nah my grandma was just smothering me."

    "I allow myself to let out a small giggle as I try to continue on the positive atmosphere. Anything to make up for what happened earlier."

    jump scene205_continues

label scene205_continues: 
    anita "What about you and Mory? How did you two meet, if you don’t mind me asking?"

    vivian "We both moved in years ago. We kept running into each other in the hallway, and he eventually pestered me into becoming his friend."

    mory "You make it sound like I’m a colony of mold."

    vivian "You’re just as hard to be rid of, that’s for sure."

    mory "Ow, harsh!"

    mory "Well, if I’m a patch of mold, then I must be well-taken care of by you to have lasted this long."

    mory "Uh, wait, that came out wrong. I didn’t mean that you’re a mess or that you don’t keep your apartment clean! It’s—!"

    vivian "Wow. You really know how to dish out compliments, huh."

    mory "It sounded better in my head."

    vivian "You’re truly a world-class flatterer."

    mory "Please, have mercy. I can’t take much more!"

    "Vivian snorts at Mory’s misery. It was kind of nice to see."

    "Despite her biting retorts, there wasn’t any heat to them. Her words were almost… playful. Fond, even."

    "Is this how friends are to each other? Trading insults without hurt feelings?"

    "It’s a novel notion for Anita. Whenever her past friends tried to banter with her, she was left with her heart sliced into ribbons."

    "They teased her how no one was waiting for her at home, how slow she was in doing their homework, or how cheap the snacks she bought with her meager allowance were."

    "If only her heart was stronger… then maybe she wouldn’t be so sensitive and laugh it off like the jokes they were."

    anita "You both seem to be really close. It’s nice."

    vivian "H-hey! What’s that supposed to mean?!"

    "Her cheeks flush."

    "Did I say something to embarrass her? Or maybe she’s furious?"

    mory "You’re included in the fold too, you know! I still can’t wait to see your artwork!"

    vivian "Oh sick, you draw?"

    anita "A little. I want to be an artist, so…"

    vivian "Cool. If I ever need a portrait of Lovie done, I’ll know who to go to first. Or even a new tattoo idea! How much do you charge per commission?"

    anita "Oh, I don’t… It’s not really…"

    vivian "Hell no! You better not be saying that you’ll give a discount just because we’re friends. I’m paying full price and that’s final!"

    anita "F-Friends? We’re… friends?"

    vivian "Unless you’re saying that we’re not?"

    anita "No! That’s not it! I-I’m just surprised, is all."

    anita "We’re… friends."

    "Maybe. Temporarily. At least until they grow bored of me."

    anita "I’ve never really made friends this quickly before. Normally it takes a month before I find anyone willing to talk to me."

    mory "I feel you. I was slapped with the race card since primary school. Not a lot of love for Black Hispanic-speakers where I’m from."

    mory "That's why I stuck close to my neighborhood. At least people accept me there…"

    vivian "Dude you have no idea. Neither side of my family knew what to do with me. The white and the asian sides are stuck with a freak of nature. The only time I felt any kind of acceptance was with some of my classmates back in school."

    vivian "Can’t say I miss it anymore. At least at a costume party, no one cares whether your skin is black or yellow under the mask. Oh, speaking of which, I’ve got another party I’m heading to tomorrow. You guys wanna come with me?"

    mory "I wish I could but my boss has me scheduled to work tomorrow."

    vivian "Ugh dude lame. How about you Anita?"

    anita "Can I? It’s on such short notice though."

    vivian "No one gives a shit. This event isn’t the kind you RSVP to. You either show up or don’t!"

    vivian "So, which one will you be?"

    anita "I-I’ll come! It sounds fun."

    vivian "Good choice. You have a costume you can wear, or do we have to go shopping—?"

    "KNOCK! KNOCK! KNOCK!"

    #SFX: Knock on Door 
    play sound doorKnock2

    "I shiver. A chill abruptly settles in the room. Void stares at the door, hackles raised, hissing."

    "Is there… someone at the door?"

    jump scene_206

label scene_206: 
    #SFX: Knock on Door 
    play sound doorKnock1

    anita "Were you expecting anyone, Vivian?"

    vivian "Uhhhhhh no? Check the peephole. If it's someone I'm cool with, I'll let you know."

    "I hesitantly go up to answer the door while Mory and Vivian talk amongst themselves. No doubt about what the coin showed her earlier. "

    "Even with those holes filled, I don't know if they will ease my mind whatsoever. Especially considering the bits and pieces that Vivian was able to see. I anticipate what kind of theories the two of them are conspiring together in what may be the death of me."

    "Just like Vivian instructed, I bring my eye to the peephole to see which one of her friends may be here to make the party last longer."

    #SFX: Heartbeat
    play sound heartbeat

    "What I saw on the other side of the door made my blood turn cold. From the little bit of range I could get from my view, all I could see was a wide grin stretching from one ear to the other. Changing my position to get the best image I can possibly get, I saw the stranger's gnarly elongated neck."

    "If I am not mistaken, they may be looking straight back at me with eyes wide open."

    "Clearing my throat, I try to ease my paranoia by getting the answer I desperately need right that very moment."

    anita "Uhh…Vivian?"

    anita "Did any of your friends dress up as the Cheshire cat? Or the Joker? Just anything with a big smile?"

    vivian "No. My friends are lame, but not to that degree."

    "With that thought now weighing on my mind, I take another look back through the hole in the door. Unlike before, I got a close up of what appears to be the end of a bird's beak. This time around, this person can't seem to hold still long enough to get any other information."

    anita "What the h-"

    #SFX: Door Pounding, progressively getting louder 
    play sound doorPound volume 1.5

    "Before I could even mutter another sound, a harsh knocking sound came from the door. My first instinct told me to get as far away from the door as possible. Not knowing I backed right into Vivian."

    vivian "Ach! Watch it?!"

    mory "What's that?"

    #SFX: Door breaking 
    play sound doorbreak2
    
    "Without even a moment to breathe, whoever was on the other side of the door broke through it with no hesitation. The first thing that Vivian does was grab the closest statue to her to use as a blunt weapon."

    "All the while, Mory shields the both of us with his body. Looking between the two of them, I froze in fear right on the spot. As much as I want to help them make an effort to fend off whatever is in the hallway, my feet can barely even move an inch." 

    "They can’t interact with the real world. They never did it before. Why are they now physically able to break down a door? It doesn’t show any signs of easing up either. The crow had made a large enough for a long and thin arm to reach through the crevice in the door."

    "I know I have to make a run for it while I still can. But chances are, neither of them are seeing what I can. Would they even believe me if I dare say what is going on in my world?"

    "Then again, I don’t really have much of a choice now that it’s affecting their world too. Let’s just hope this isn’t all just inside of my head again. Or I don’t really know what to hope for now."

    anita "I-it’s reaching for the lock…"

    vivian "Wait. What’s reaching for the-"

    anita "JUST HIT THE DAMN THING ALREADY?!?!"

    #SFX: Creature Growl

    "Before it could unlock the door, Vivian hit the creature’s arm with as much force as she could muster. As she swings her arms back to take another go at it, the lengthy thin appendage grabs her by the throat."

    "Still putting up a fight, Vivian drops the statue to use both of her hands to punch and bite at her aggressor. Mory made a mad dash right behind Vivian to pull at her waist to free her."

    "I can tell by the look on his face that he is beyond confused about the situation at hand but more scared about some unseen force choking Vivian. He can’t see what is forcing its way inside the apartment."

    astaroth "Tell your companions that it is not wise to keep us out here."

    anita "Huh?"

    astaroth "Do please let us inside for a quick chat, my dear."

    "I stare blankly at the large hole in the door trying to look for who is talking to me. This is so fucking weird."

    "I have never had any of my hallucinations ask for a conversation with me before. The most I have ever gotten were inhuman screeches or gurgling sounds from these creatures or the occasional short sentence."

    mory "Anita?! Who is that?"

    anita "You can hear it?"

    vivian "WHO THE FUCK CARES?! JUST LET IT IN SO IT CAN LET GO?!"

    #SFX: Door open
    play sound doorOpen

    "In a panicked state, I rush to the door to unlock it for them. The moment I hear the click from the lock, Vivian drops to the ground to take in air like she’s never learned how to. Mory instantly crouches down to her side to help her catch her breath. My eyes stay glued to the door anticipating the worst to come."

    "What steps through the door were two creatures that both towered all three of us. One resembling that of a crow with proportions like a man aside from its head and legs."

    "It didn’t take long for it to take its attention to Vivian's belongings. With every swipe of its massive beak, everything on her shelves came tumbling down. It had no target in particular, just anything that grabbed its attention."

    #SFX: Parakeet chirp
    play sound parakeet

    "Lovey sure didn’t like this new feathered intruder one bit. But she was the only living being that was grabbing its full attention for the time being. Vivian tries her best to keep a close eye on Lovey in case anything bad happens to her."

    "Unlike the bird, the other creature kept its composure in a civil state. It was standing straight and tall, like it was trying to present itself in the best possible way. Which is something I can’t say is achievable in this situation. "

    "It doesn’t help that this other thing was just as bad if not worse. This creature more resembled a scratched out human that died of severe frostbite but it’s feet were more like talons than toes. What disturbs me the most is it’s face is entirely blacked out aside from it’s facial features. What stood out about his is the dark crown that sat on top of it’s head. "

    "I’m having a mental debate now on which one looks worse."

    astaroth "Pardon the mess my companion is making. He gets excited around others of his kind. Isn’t it precious? "

    vivian "Where the fuck is that voice coming from, Anita?"

    anita "It’s a long story that I don't know how to tell right now."

    "I try my best to keep Mory and Vivian calm while keeping my eyes glued to the crowned figure standing before me. He mirrors my actions at my eye level from an uncomfortably close distance. "

    anita "Umm… How do you do on this fine night, gentlemen?"

    "I extend my hand for the figure to shake in a hopefully polite manner."

    vivian "Are you fucking kid-"

    mory "Shhh."

    "It completely dismisses Mory and Vivian by taking my hand. Shaking it to the point where my arm nearly pops out of its socket. Once I finally have my hand back, I rub my sore arm as I look back at it. "

    astaroth "I must say, I am quite charmed by such a polite young lady. We are both having an eventful evening. "

    anita "It’s a pleasure to hear of your splendid time. But I must inquire about the purpose of your visit to this humble abode."

    astaroth "Ahh yes, we are in search of our most gracious host for this night."

    anita "So someone within this manor invited you and your companion?"

    astaroth "Oh perish the thought, my dear. It is not only the two of us. The warlock called upon us to strike a bargain. "

    "The warlock? So someone here is calling these creatures."

    anita "What kind of a bargain did your host propose to you… all?"

    astaroth "Well, the warlock offered a rather splendid offering for our services. "

    anita "What exactly may that offering be, sir?"

    astaroth "My dear sweet child, you should already be familiar with what we want. They are already in those pretty little sockets of yours."

    "The crowned creature points its darkened fingers right in front of my eyes. My world is standing still for a moment as I try to collect what exactly to say about such a thing. Someone is offering my eyes to otherworldly beings."

    "Who would be calm in a time like this?I could feel my heartbeat quicken in my chest. Along with that, my breathing gets more shallow with each intake of air."

    anita "..."

    anita "I-I..."

    #SFX: Cat Hiss
    play sound hiss

    void "Meow."

    "The two of us now stare down at my feet where Void now resides. She is staring daggers right at this being who is at least fifty times her size like she has an even chance to go against it. She takes a few steps closer to it without any hint of fear in her eyes."

    anita "Void, no!"

    "As Void steps even the tiniest bit closer to the towering figure, it shuffles its feet back away from her and me. Not knowing what kind of danger she may put herself in, I scoop her up in my arms to keep her safe from this threat waiting to happen."

    astaroth "Ah yes, keep that Demon Ward close to you for in due time, it will serve no use to you. Once the veil between the living and the dead are paper thin, you and all of your friends are our main event."

    "The words are caught in my throat again. I still have so many questions floating around in my head. What is a demon ward? When will it stop being useful to me? What does it all have to do with Void?"

    "I know these questions are dire in my situation. But the words just simply can’t come out anymore. Having a prestigious sounding conversation with a blood hungry beast that is only here for my eyes is impossible at this point. The only words that can easily slip out out of my lips are-"

    anita "Why are you telling us all of this?"

    astaroth "That answer I shall gleefully serve to you on a silver dish. Which is, the fear that I am supplying to you lot will make the feast all the more sweet on the tongue."

    vivian "Alright asshole, we have been waiting here all this time going around in circles talking like you are sucking off Charles Dickens b-"

    anita "Wait, does that mean you guys can see it?"

    mory "No but let me try something. Where is it?"

    anita "Right there."

    "Mory pulled out his cell phone to point it in the same direction my finger is leading to. He snaps a picture with it. "

    anita "What are you doing?"

    mory "Taking a picture of it. Maybe it’s like the spirit orbs that show up in photos whenever ghosts are around."

    vivian "That's actually a really good idea, Mory. Let me see."

    "The three of us huddle around Mory’s phone to see what he captured on camera. What was in the picture made all of us stand ice cold in absolute dread. The only one moving out of us was Mory’s unsteady hand holding the phone, making the image harder to see clearly. But all of us already knew what was in the picture."

    "It was nothing like we had ever seen before. A collection of eyes all staring in different directions amongst a mass of what appears to be tar. Yet every single one of those eyes all looked ready to feast on every living being in this room. "

    vivian "We have to get the fuck out of here."

    mory "And go where?"

    vivian "Anywhere but here!"

    "The three of us make an exit into the hallway with the animals to think of a course of action in a calmer environment. Before making our leave, I heard that same smarmy voice call out from behind us."

    astaroth "Twas a pleasure conversing with my next meal. We shall meet again at the stroke of midnight."

    "Fear overtook our decision making skills as all three of us are trying to come to some kind of conclusion. All we know is that the hallways are no longer safe."

    #SFX: Gross Gargling
    play sound grossGargle

    "Although the disgusting gargling of some otherworldly beast could be heard by all of us, they can't see how close to death we're all about to be. I turn to see it's the same thing that was stalking me earlier."

    "And it's hungry …Oh god, I need to come up with something!"

    "Wait! My apartment! The door is unlocked. Maybe we can-"

    #SFX: Feet stomping
    play sound footstepsWood
    #SFX: Gross Gargling
    play audio grossGargle

    vivian "Oh god, I didn't think this through."

    mory "Maybe we can-"

    "Making a running start, I use my shoulder to push both of them through my doorway and slam it shut. With one hand, I hold the knob in place so they can be safe inside. In the other I cradle Void close to my body. "

    "Please…if you’re going to devour me just leave them alone. They’ve done nothing wrong so they don’t deserve it."

    #SFX: Bash over head
    play sound headBump

    "..."

    "It stops?"

    "Daring to peek behind me, the well spoken monster from earlier has a statue in hand with a scowl. My pursuer halts as blood trickles down it’s head and pools onto the floor, wincing in pain. "

    astaroth "No no no you imbecile. Your stomach will not ruin tonight’s festivities."

    "I don’t dare to move in fear of what could happen to Void if I did. As they tread away, the weight of gravity starts taking over my body as I plummet to the ground."

    jump scene_207

label scene_207: 
    "My heart is going completely haywire from all this paranormality going around me. I think I've finally met my wits end. I have always seen weird stuff since I was a child, but this…"

    "This is different."

    "Most of the time, the creatures I saw were in private, and they weren't actually there. They did not interact with the physical world in any way, but this time, they did."

    "They’re hurting me and they may hurt others."

    "I am not going mad. Not only were they manifested in flesh this time, they were interacting with things around them. With people around them."

    "This. Is. Real."

    "I feel like I'm going into cardiac arrest. My weak heart can't take all of this. I can't take this. I need to calm down. It’s like the stress is actually killing me."

    "INEEDTOCALMDOWNINEEDTOCALMDOWNINEEDTOCALMDOWN!"

    "I feel weak, on the verge of passing out again. I clench my chest so tightly it could have torn holes into my shirt. I feel myself start to control my breath."

    "I need to breathe."

    "Breathe in, breathe out."

    "Breathe slowly in."

    "Breathe slowly out."

    "I don't know if these creatures are even the same as the ones I usually see, but they are real, they exist. Despite everything, I cannot let them get the best of me again."

    "They will not take something else from me."

    "I never felt so afraid for my life, but I'll fight it with my lungs."

    "..."

    "..."

    "Breathe in."

    "Breathe out."

    "Now that they left, the shock of the situation got right to me. I'm simply having a panic attack, and this is my body reacting violently from a great deal of stress."

    "My breath doesn't seem to be stabilizing. Am I dying…?"

    "I need to calm down."

    "I need to calm down."

    "I NEED TO CALM DOWN!"

    "But… before I know it, I feel weak, dizzy. My chest hurts. I am a weakling and have always been. Maybe my parents were right about me. I am just a poor failure about to be done in by an anxiety attack when I'm barely twenty."

    "I hear muffled footsteps in my direction while vision becomes taken over by mud. I start hyperventilating."

    "THEYREBACKTHEYREBACKTHEYREBACK"

    "Disembodied Voice" "Anita!"

    "My heart skips multiple beats as I feel two creatures grab me from the front. A chill runs through my entire body, and my fight or flight response kicks in  but instead of doing anything, I paralyze."

    "It feels so warm..."

    "They are grabbing me..."

    "But… as if my most carnal instincts of humanity kicked in…"

    "I hug them back..."

    "And I feel the furriest of tails coiling around my stomach and something rubbing against me. It purrs. It purrs like it knew I needed it."

    "My heart beat slows down. My slumbering senses start coming back to me, and life breathes onto my soul once more."

    "..."

    "Disembodied Voice" "Are they gone?"

    "Disembodied Voice" "Hard to say. They're invisible, you know? But it seems like they left, I don't hear any footsteps or anything."

    "All my conscience drills it way back into my brain with relief, as my shoulders relax and leave their stiffness behind. My breathing stabilizes and my heart is slow."

    "Mory and Vivian are embracing me, both of them…"

    "And my tears of panic turn into tears of relief and happiness."

    "I don’t think I’ve felt this much warmth from another person, or persons, in so long…"

    "We have known each other for not even twenty four hours, but they are here, comforting me through the shock of seeing what should have been left unseen. It is hard for me to accept, but I accept it nonetheless. The seeds of doubt I had about their intention seem to vanish."

    "Void is also doing her best to give me a feline hug."

    "I don't feel like spilling my guts anymore. I feel like such a burden, but the pressure is being split through three friends. Friends…"

    "Hahaha…"

    "I wish Elly could be here as well…"

    "She is my friend. I'm gonna hug her too."

    anita "I… I’m so sorry… I'm such a burden…"

    vivian "It’s all good Anita. I'm scared shitless too, but we’ll protect us. If anything comes for us, I'll smash their skulls in."

    anita "I’m so sorry… I’m so sorry… All three of you are stronger than me…"

    mory "We aren’t any stronger than you, dear. Those things are gone. Just focus on breathing and calm your nerves."

    "Through this tight knit connection, I can feel both of their hearts. They are racing and beating as hard as mine was, just about to burst out from their thoraxes. This is comforting..."

    "Knowing they are feeling the same makes me sure I am in good arms…"

    "Heh, good one, Anita…I think."

    "Breathe in. Breathe out."

    #SFX: Cat Purring 
    play sound purr 

    void "Meow."

    anita "I-I’m sorry. I'll see what I can do to help."

    mory "You don't need to keep apologizing, dear. We are all the same here!"

    anita "Okay. I'm s–"

    "I remembered that interaction I had yesterday with Elly."

    "I shut my mouth before I can state that I feel sorry again. Not having to do it makes me a little… more powerful, in a way. Like I’m not in the wrong."

    "I keep hugging Mory, Vivian and Void for what felt like a while longer, but I’m not complaining. They’re not either. My spirit feels a little less jaded."

    "Vivian stood up from my side and made a dash across the hall to her apartment. I left Mory's embrace, instead picking up and petting Void. I breathe a relieving sigh and wipe the tears off my face."

    "They know I'm thankful for their help - and I promise to pay it back."

    "While that is going, Mory retracts and becomes pensive. While his smile is gone, his amicable aura stays and irradiates."

    "I look over to see what Vivian is doing as she quickly returns. Within her hands was the wooden box where her coin resides where she proceeds to stick it deep inside one of my cabinets. "

    mory "Anita. Those things were invisible to us, except you. What did you see?"

    "I breathe in deeply and start to detangle the vision burned on my retinas."

    anita "I-I saw two creatures. Both of them were tall and lanky. One of them was some kind of raven, and the other had a stretched out neck and a crown."

    mory "We didn't see anything, but we could clearly see them interacting with stuff and hear what they’re saying."

    vivian "Doesn't seem like we are the only ones. Lovie was freaking out on me too, and Void seemed to be scared too."

    vivian "Damn those pieces of shit. No one messes with my bird like that. No one!"

    vivian "And here's what is going to happen to them!"

    "I only just noticed that in her other hand was this enormous metal baseball bat. That thing looked like it needed inhuman amounts of strength to wield it properly."

    "Is that even legal to own?"

    "I think I already see dents in it."

    anita "Uhm… Are you sure that is a good idea?"

    vivian "Of course it is! I ain't letting some nobody demon taste my flesh without a concussion! I’m especially not letting anything touch that coin."

    mory "I'd like to say the same, but we don't know what they are capable of. Don't swing that without thinking first."

    vivian "Dude I thought you knew me long enough that I’m an action kind of girl. You clearly don't know me then."

    mory "I do, that's why I gave you the reminder."

    vivian "Hmph. Whatever."

    anita "Oh… Mory, one more thing."

    anita "Can I have another look at those photos… please?"

    "Hearing how desperate I was to see if I’ve truly lost it, Mory obliged by taking out his phone where we looked through the picture together."

    "In the image, both of the figures were a mass of flesh, tentacles and… crabs?"

    mory "Just what are these things…?"

    mory "Viv, take another look at this."

    "Diverting her attention from batting practice for a minute, Vivian looks over his shoulder to mimic the same awed reaction as before."

    vivian "Ew, they're gross!"

    vivian "I'm not sure if I want to coat my bat in their…feathers? Hm would they have blood or ink?"

    vivian "What in God's name are these things?"

    anita "I don't know why they showed up like this. I didn't see them like that."

    mory "Those things in the photo don't even take the same space as what they seemingly did inside here."

    #SFX: Knocking on Door 
    play audio doorKnock1

    "Voice from the Door" "Anita!! Open up, please!"

    "I'll have to admit I got a little scared for a moment from the knock. Made me jump, but it sounds like Elly. She is clearly very nervous and I can hear her fidgeting behind the door."

    "Vivian prepares her bat with her other hand on the knob. She twists it and is about to swing."

    "It's Elly."

    elleanor "Oh god! P-put it down, please! I'm not a monster!"

    "\"Monster\"? Did she get visited by some creature as well?"

    anita "Elly!"

    vivian "Oh…it’s you."

    mory "In the love of god, let her in!"

    vivian "Fine, come in. Or don’t that’s always an option. "

    elly "S-sorry to barge in like this, Anita. I knocked on a few doors, but no one answered. Glad to see you and Mory safe."

    vivian "Hmph."

    elleanor "I got a visit from t-this thing.."

    anita "What did you see?"

    elleanor "I can't tell you, it was invisible…"

    mory "We had the same. They left not too long ago."

    elleanor "What should we do? It garbled about devouring me by midnight."

    vivian "We gotta make a run for the exit, that is our best bet. If for some reason that doesn't work, I’ve got nothing."

    mory "Really? That’s all you can think of."

    vivian "What do you want me to say? Jump out a window?"

    anita "I… think I can pull through…"

    elleanor "Are you feeling good?"

    anita "Uhm… kinda…"

    "Elly rushed over and gave me a hug. It is comforting. I can feel her shaking too and I don’t blame her. While that goes on, Vivian puts Lovie in a smaller cage on her belt loop and carries her."

    elleanor "Are you going to take it too?"

    vivian "HER name is Lovie."

    elleanor "Oh… Are you taking Lovie as well?"

    vivian "Yes. Any complaints?"

    mory "None at all! Whatever gets all of us out of here safely."

    anita "I'll carry Void, so… no problem either…"

    elleanor "…No problems either."

    void "Meow."

    vivian "Good."

    vivian "Let's make a sprint for it, then assess."

    #SFX: Footsteps 
    play sound footstepsWood

    "All of us fled from my apartment. Vivian holds her metal bat tightly and is leading the charge, while we trail behind her slowly stacks. Mory volunteers to stay at the back. He doesn’t want us to get surprised."

    "I’ll admit that I’m still very much afraid, but being surrounded by people who I now consider friends makes everything much more bearable. I don’t know how I could survive this situation otherwise, especially walking down these completely pitch black halls."

    "All of us have our phones out, except Elly, and are using the flashlight function. It is somewhat blinding, but it is illuminating most of where we are looking. I don’t know why, but the lamps seem to be failing within the hallways and don’t stay on."

    vivian "See anything yet?"

    mory "No, I haven't heard anything yet either."

    elleanor "Yes, it is too quiet in here. It’s almost like we’re the only ones here."

    elleanor "But that would be silly, right?"

    #SFX: Footsteps 
    play sound footstepsWood

    "Now that she brought it up, the complex is… completely silent. Dead silent. We knock on a few doors, but no one answers, and most of them are locked. The apartments that aren’t locked are completely empty, and have no windows."

    "It is so silent I start to conjure up noises in the distance, all of them drawn out by our footsteps."

    "Lovie and Void are quiet, which is unusual for a parakeet and a cat together. They must be frightened as well."

    elleanor "Well I don’t mean to be a nosey nelly in such a tense situation but I must know. Is what both of you said true about having magical objects?"

    vivian "One, keep talking to me like a kindergartener and I will feed you to one of those things."

    vivian "And two yeah sure. It’s not like I exactly wanted to tell you but I had to. "

    elleanor "Well do you two have any idea how much this could mean to humanity? You can heal the sick! And you can predict world tragedies so we can fix them before it happens."

    vivian "Well I’m sorry for not predicting your dad’s condom breaking."

    vivian "And yeah that’s not how my coin works and even if it did, I would literally lose my mind. So let’s not and say we did Elleanor. "

    elleanor "…I’m going to pretend I didn’t hear that."

    mory "Actually I already do that. I’ve healed a lot of people in my family and community. "

    mory "I’m hoping to do it for more people one day."

    mory "…Also did you really have to go that far?"

    vivian "Yes, yes I did."

    vivian "I also want you to help out more people one day. If we make it out of here alive. That would be fantastic. "

    elleanor "B-but I don’t understand, how long have you both had these?"

    mory "I’ve had ol’ reliable since I was about thirteen."

    elleanor "What? That long? How come you never said anything to me about this? You know how deep of an interest I have in this."

    mory "Oh…I didn’t mean to hurt your-"

    vivian "Wow, it’s almost like OUR lives aren’t YOUR business."

    vivian "You’re not exactly entitled to details just because you have a hobby."

    elleanor "Well pardon me for being fascinated in actual proof that magic exists. "

    vivian "And shit like this is exactly why I don’t like talking about it with people."

    vivian "Now can you kindly shut up Ms. Frizzle. We’re here. "

    "We reached the entrance, the thick door had some small indications of mold infiltrating its hinges. It looks like the same kind of mold I saw earlier at Tom’s door."

    "I try opening it, but nothing happens. It is completely stuck and doesn’t move an inch. Mory steps in to try, but it does not budge. It feels like it suddenly weighs one hundred times more. "

    #SFX: Baseball bat smash door
    play sound batHit

    "Vivian tries bashing it with the bat, but aside from a lot of noise, nothing really happens."

    elleanor "W-what do we do now?"

    "Vivian ignores the questions and takes a peek through the small windows at the side of the door. We can’t go through it, they’re too small. The outside world is shrouded in a very thick fog and it is raining. We can barely see outside at all."

    vivian "I don’t think it’s very safe to go out anyway. Look at this fog…"

    vivian "Something is happening outside as well, we aren’t just trapped in here."

    mory "Hmm… Is there another exit anyway? We might need it."

    vivian "We got the roof, but that leads us to the, you know, the fucking roof. Unless you’re on board with jumping off a tall building, there’s no reason to go there."

    anita "W-what about the fire exit stairs?"

    vivian "Well…"

    mory "…Mr. Lamlor is getting chewed by the government because we don’t have any."

    vivian "I knew that asshole would be the death of me."

    anita "We’re done for!"

    elleanor "These windows are too small for us to pass through."

    "I start to feel more anxious again…"

    "I never felt physically trapped in a location before. What do we do? According to our phones, it is 10:16 PM."

    anita "We have to at least have a way out by midnight. Anyone have any ideas?"

    #SFX: Cat meow
    play sound meow2

    void "Meow."

    anita "I wish you had."

    vivian "Oh! Ahah!"

    "Vivian perked as an apparent light bulb formed above her head. Seems like something we said joggled up her brain."

    vivian "There’s a warlock somewhere that wants something from us, and we have until midnight to give them, right?"

    elleanor "Yes, but we don’t know what that “thing” is. For all we know, they might want all our organs."

    vivian "Let’s find them and cave their heads in."

    mory "That is… a violent, but sensible plan, I suppose?"

    mory "How are we gonna do that?"

    vivian "We should split up in pairs. We go back to my apartment, find another weapon like a knife or something, and we search every single door, nook and cranny of the entire complex. Shouldn’t take more than a little over an hour."
    
    vivian "I’ll be going with Anita."

    anita "Huh? Why with me?"

    vivian "Oh... uh..."

    "Vivian is emanating this feeling that she said something she should not have. Is this related to the vision she had in the coin?"

    mory "Vivian… what are you hiding?"

    mory "It has something to do with the coin, doesn’t it?"

    anita "You haven’t told us what you saw. What happened?"

    "Elly stayed quiet, only spectating the small altercation. I think she might just be a little confused, again."

    vivian "I… uhh…"

    vivian "Somewhat? Why does it matter so much who I pair up with?"

    "Mory sighed and put his hands on his forehead."

    mory "Vivian…Please, you’re hiding something and it’s obviously huge. We are in very serious danger so please tell us if it has to do with what’s going on."

    vivian "..."

    vivian "I panicked, okay?! That’s why I didn’t tell anyone! Is that what you wanna hear? "

    vivian "I didn’t write it down, I did nothing! I just told both of you to get out and hope to sort out this of my own!"

    "Vivian is screaming and hyperventilating."

    vivian "The coin shows me when my bike is gonna get stolen, or when a boy is gonna tell me he wants to hook up with me, or if there is going to be a discount at the supermarket. That’s it!"

    vivian "That is what it’s fucking supposed to do in my family line!"

    vivian "Not show me a fucking murder!"

    elleanor "M-murder?"

    mory "What do you mean murder? Who got murdered?"

    vivian "Her."

    "She pointed at…"

    "Me."

    jump scene_208

label scene_208:
    "My head grows pale as the realization dawns upon me that Vivian is hiding the fact that she saw me getting murdered through her coin. I don’t know if I should feel betrayed or not, but this is bad."

    "I do understand keeping it to herself in hopes of trying to fix it, I had my fair share of doing the same, but…"

    anita "Why would you ever hide that from me?"

    vivian "Cause I fucking care about you, that’s why! You’re a new person that just showed up in my life. We barely met and you’ve already been so friendly with me!"

    vivian "I meant no harm, I just… just got overwhelmed. I can get scared too, okay?"

    elleanor "If it were up to me, I wouldn’t exactly trust someone that was holding back such critical information. Unless you have something else in mind, Vivian."

    vivian "What are you trying to fucking imply?"

    "Vivian strides right up to Elly, standing an inch away from her face with eyes glaring at her like she was about to bite it clean off."

    elleanor "I-I’m not implying anything. I just think it’s strange timing for that to happen is all."

    vivian "Listen to me and listen good. I ain’t no killer, and I don't want to hear one more vowel coming out of your mouth, got it? I haven’t had a single ounce of trust since you moved here and even less since what happened to him."

    mory "Hey, Vivian, back off from Elly."

    "Vivian stared at Mory for a second before sighing deeply. Seems like him speaking up made Vivian recover some of her wits. I’m not sure how to feel about this, it is weird that Vivian wants to take me with her, but I don’t want to doubt her intentions…"

    "She left Elly’s personal space and walked a few steps towards the wall."

    vivian "Sorry."

    