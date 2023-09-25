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

    question "...exitium...potentia...mors..."

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

    