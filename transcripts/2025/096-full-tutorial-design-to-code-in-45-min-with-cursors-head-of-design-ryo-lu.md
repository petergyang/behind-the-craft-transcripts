---
title: "Full Tutorial: Design to Code in 45 Min with Cursor's Head of Design | Ryo Lu"
guest: Ryo Lu
publish_date: 2025-11-16
youtube_url: https://youtube.com/watch?v=bdh8k6DyKxE
channel: Behind the Craft
keywords:
- ai-tools
- coding
- product-management
- design
- execution
---

I think the designer will start revoling as they gain these skills. They will realize, oh [ __ ] what were we doing? We're doing a lot of the designs. We will just maybe prototype in cursor because that kind of lets us really interact with, you know, the live states of the app. It just feels a lot more real than some pictures in Sigma.

All this back and forth of like, uh, the engineer built something, but it's like, I don't know, 50 pixels off and it's like, here's wrong, here's wrong, here's wrong, here's the spec, here's my like red line. back to the engineer. You just built this through like prompting cursor. Yeah. I think when I started doing these, it really required like say more technical knowledge.

But now it's like with the newer models and new like cursor features, you can almost like do anything like one shot get something really close. Most of designers in the industry are still just in Figma, right? They're just like making mocks. How do they become more like a real de cursor and then try to start something? Okay, welcome everyone.

My guest today is Rio, head of design at Cursor. Uh Rio has built a pretty amazing personal operating system that's feels very retro and honestly blew me away. He built it completely using cursor and AI. So he's going to do a walkthrough of it and also uh use cursor to add a new feature to his operating system without using Figma at all. And then hopefully we have some time to talk about how the cursor team builds products.

So welcome sir. Hey everyone, I'm Rio. I do design at Cursor. I was the first designer there. How I started there was really because I found the agent back in November last year and I got hooked and I kept making stuff.

Yeah. Let me share my screen. All right. Well, why don't we see this in action, man? I mean, you already built a lot of stuff on here.

Maybe we can add something new to this thing. Cool. You know, what do you want to add? Uh, I was thinking maybe like a I don't know. We saw like a calculator.

Maybe we can add a snake game. Um, what if we ask the agent to think about it? Okay, let's have Asia. Okay. Yeah, let's try this voice thing, too.

I'm not sure if like I'm recording with you if this will work, but we'll try this. Okay. Can we make something really cool like add a new app to the OS? Something that stuck with us through time. Let's see what happens.

And um dude, you so you actually use cursor in light mode. I never seen one use cursor light mode before. So, we actually have like a new theme that that is made by one of our uh designers. It's called cursor light. It's really nice.

Nice. I think as I got older, like my eyes just, you know, in the day, I just want something with more contrast. Okay, got it. Cool. It's kind of like doing some research.

Um, yeah. Huh. Whoa, whoa, whoa, whoa, whoa. Yes. Yeah.

I told you it's going to make a my my calculator appision for me. Interesting. Okay. So, I want to kind of show something like another way to do this. Um, so like what we just did is almost like you just ask something pretty vague, right?

Like I didn't say like which app I want. Uh, but it kind of did it for me. What if like the agent kind of help you, you know, think and plan and ideulate. So we built this new thing called plan mode. If you uh switch to plan mode and then hit this button again, let's see what happens.

So the same kind of research will be done, but it will maybe like do it uh for longer. Yeah. And it's going to like kind of do the research and then think of some questions uh to to ask uh if it's like something really ambiguous. Oh, it's already cool. So, calculator solitaire clock.

It's all really classic. Let's do the calculator, I guess. Do the calculator. Let's go. Let's see what happens.

And and plan mode. Uh I mean there's a lot of thought that went into it, but like basically the idea is to tell it not to code, right? Sure. Or I think it's more like you're still coding um but you you kind of do it at a higher level. Okay.

Um instead of you know kind of uh doing the low level like coding each file type of thing you kind of just think about the architecture or what do you want in it? How do you kind of you know specify the things you want out in the most clear way possible for the agent and look at this as like the agent can kind of help you kind of do the first draft of the plan. Yeah. Um and as it kind of think about um all the things that it wants to add, it will kind of you know think about a lot of the implementation details where to put things and at the end it's going to think uh what are the individual steps I need to do to kind of do this and all I need to do is like to review and if it's it's good I can just hit build and let's actually like read it a little bit here. Uh okay add a calculator icon.

Okay. So, what if we, you know, so I don't really have a icon yet. So, what if we just say like uh use a placeholder where now you can search in the icons folder and that's it. Like I can almost like write my own spec too uh or make modifications almost like in a Google doc. Yeah.

Where like PMS do like parodies. Um and okay, great. I just hit build and it's going to flip into this mode where it's going to start building. I like how the the MD files like you know markdown formatted and stuff. You know it kind of looks like so so so I feel like people are actually going to start using cursor to make documents like why not it's not just for writing code right?

Yes. Yeah. I think a lot of people are already doing that like we notice say like I want to update the change log or want to do some documentations. Um, people just use the cursor agents and if it knows your code base, it can even like, you know, give you better, more real results. Oh, nice.

Okay. All right. So, now it's making everything making the main app components. And do you always like to get it just running locally? Yeah.

First see it changing real time. Yeah. I still prefer like kind of being in the driver's seat like I want to look at everything and Yeah. see it happen. But like you could imagine like similar workflows work for say like our background agent um or like for say like a more um defined problem say like a bug to fix uh you can just send it out say through Slack or or web agent.

And I I noticed that like your view here is basically just the agent and I guess the local host. Uh like that's not the default view, right? The default view has all the files and like the the code and everything. Yeah. So um cursor used to like have this um what we call like the IDE layout kind of borrowed from VS Code.

That's right. But we kind of start noticing like people start to like look at code less and less and the main thing they're focusing on is actually the agents and then maybe the list of agents maybe they're running multiple agents. they want see review, you know, things um or spin or like just quickly flip between them, see the states, uh preview things in the browser or making plans at a high level. But you know, like if you want you can still look at the code like you can just click and see what happens and then you like make modifications yourself uh if you Okay. Okay.

So it ran into a bug and it's fixing the bug now, right? Yes. And um are you uh do you do like the fancy stuff where you have multiple stuff, multiple agents working at once or try to stick to one at a time? Yeah. Um I usually like spin stuff to the background more.

Okay. Um versus say like it's almost like my workflow is I usually have one main agent uh locally and then maybe spin spin like you know little tasks to the back. Um we're working on a new feature called like it's like making the agent work really well for like work trees uh so that like uh you can run multiple local agents in parallel um and they will not like overwrite each other or like you can kind of review all of them at once. Okay. Yeah.

Oh no, something's wrong. Let's try fixing this. Can you fix this for me by reading what's going on in the browser? Do you have some MCP installed or cursor already can read them the browser? We built like a internal browser automation thing.

Um, it works for uh Oh, shoot. It works for um wait, let me fix this first. go to uh I think I know what what it did is like it kind of opened like another web server I think. Okay. Haha.

We need to fix this. Yeah. So we have like two types of browser integrations. You can do this like internal browser tab. You can also talk to Chrome.

Okay. Uh if you use it let's see what to do here. This episode is brought to you by Reforge Build. You know, I took Reforge's first growth class 5 years ago, so I'm really excited to see Brian and the team expand into AI prototyping. Most prototyping tools make you start from scratch each time and produce the same purple-looking AI slop.

Reforge Build learns from your design guidelines to generate prototypes that actually look like your product. You can even generate multiple variants to compare approaches side by side and collaborate with your team directly in the product. Reforge understands how product teams actually prototype better than most other companies. So check out their new product at reforge.com/peter. Use the code build for 1 month free of premium.

That's reforge.com/peter. Now back to our episode. Nice. My states are back. Great.

Okay. Yeah, there's like a lot of little fixes we're doing right now, but I really wanted to show like the new stuff. So let's do 1 A and 2B. Make the calculator design match each system themes. That will make it more interesting.

Okay. Um yeah, I don't know about the sounds when you drag the Windows man. Maybe that's too much. So these are actually from like the old days. Um, so when we started on computers, I think a lot of people really need more feedback.

Like they don't really know like if things are moving, how to do things, if I click a button, what happened? So back in the days, like when you do like stuff, um, it will like make a lot of sounds. But as we kind of grew out of it, you know, there's like less sounds, there's like less Yeah. Yeah. big things.

Um, big feedback. Cool. So plan mode. will do some research and make a plan for you. That is pretty detailed.

Um, you can have a review if it's doing the right thing, things are the things you want. Um, oh, Fisher price style. That will be very interesting. Uh, maybe we can just ask it to use the XP themed buttons instead. That will be easier.

Cool. Um, and for the icons for now, use a placeholder in the icons folder. Okay, once we're ready, let's hit build. Awesome. Okay.

And how how do you and the team um like uh build cursor these days? Like do you guys mostly get the agent to make PRs or or do you do you watch him make stuff live? Um I think we we basically do like a mix of things. Um it's like cursor is kind of everywhere now. Um I still like the local ID to make like really quick changes.

Uh where say like it's it's like visual. I need to see the thing. I need to tweak all the details myself. Um, but for things like um if you're just fixing some bugs uh that are more defined or maybe there are just like tickets in in linear um you can just kind of send them over to the clear background agent um they're going to do stuff in the cloud fix those things for you um and once they're um done you can kind of review them in the list of agents uh or they will just kind of ping you in Slack you can make a PR see it Um the bug bot even sometimes can maybe find some issues and once they're done like you can just hit merge. Got it.

Awesome. And and what what what kind of features do you work on in cursor? Like like uh do you mostly work on like front end features or like you actually build like entire features with the team? Ah so like at cursor I see say like the roles between designers, PMs, um engineers like are really muddy. Yeah, we kind of just do the part that um kind of makes our like that does our unique strength.

Um use the agent to kind of tie everything. Um and when we need help, we can kind of assemble like people together to work on the thing. Maybe some of them focus more on the visuals on interactions, some of them focus more on say the infra side of things where how do you design like a really robust architecture to to scale the thing. Um so yeah like like there is a lot less um separation between roles and teams or even like tools that we use. Um so like for doing a lot of the designs um if they are not individual space we will just maybe prototype in cursor.

Um okay because that kind of lets us really interact with you know the live states of the app. Um it just feels a lot more real than some pictures in Figma. Yeah. Yeah. Yeah.

Okay. Got it. Got it. So Figma doesn't get much use in a company. Yeah.

uh or like I think we're still using it a lot sometimes like it's like in the initial phases of like exploring something or maybe is like defining some new visual patterns or like kind of exploring like layouts of things like that's still like I think pretty quick because we still used to doing it yeah in Figma. Yeah. Is it working now? I think so. Did you actually actually hire a PM because last time I talked to lead there was like no PMs.

So did not hire a PM yet, but we do have a So we have an engineer who used to be a founder. Um he kind of took a lot of like the more PME side of the job and then he kind of got it became the first PM of the company, but I would still say like a lot of the PM jobs are kind of spread across the builders in the team. Yeah, makes sense. Let's see if it's actually them. Um there it is.

is the mind sweeper. I have Oh, cool. Oh, wow. Look at this. Yeah, it works.

Cool. So funny. Nice. But uh but dude, make make sure the math works. Does the math work?

Like do do like a two plus two. Yeah. Wait. Oh, nice. Keyboard works too.

Yeah. Boom. Okay. Nice. Not bad.

Nice. Okay. So, so yeah. So it basically did it in one shot because uh it did plan mode and wrote the spec and you modified it and then Oh great fixed scientific coming soon. Do you have like a bunch of tests running for this thing so that you know no like in case it screws something up that you can't see.

It does do like say you know it it reads the lint errors build errors console logs. Um I don't really do tests. Um, yeah, I I mostly vibe and look at things. Got it. Okay.

So, now let me ask you the let me ask the million dollar qu question. So, so ba b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b basically whenever I vibe code something, it always use it. Yeah, it always does a chassis and crap like So, how did you actually get it to look like this? Like you you just prompt pro prompted it. You share some screenshots or Well, if you look at um the files here um so let's go to source.

Yeah. components. So all a lot of these components are actually shenan components. Okay. So in real like all the standard controls, menus, uh buttons, even tabs, um drop downs, uh dialogues, they're all chassen.

Okay. But because Jassian is like you know it kind of duplicates the components to your uh work working tree um it can also do like a lot of the theming um variables like I kind of like a theming thingy where like I define a lot of different themes and then I kind of override some of the styles by hand. Um, okay. Then you can kind of, you know, it's almost like I do this because the AI really knows these things well because it has seen it a lot around the internet um when they're used for training. So it is really good at composing patterns that exist and because a lot of these components are even like you know shien is a wrapper on uh uh reics um which like a really robust like UI library where like a lot of you have put a thought thought in it um they handle say like keyboard navigation accessibility uh a lot of things for you then you don't have to like let the AI you know start from scratch which is you know more errorprone It's kind of building patterns on top and then your job becomes like in like instead of making the thing look like AI slop, how do I almost like paint it in a way that you know fits the thing I want, but underneath there are still like these pretty standard share components.

Okay. So basically you build some standard chassen components and then you tweak the theme CSS or like some of the CSS files. Yes. or it's almost like I built like a theming thing on top of it. Yeah.

Um where you can kind of swap different styles. Um but like fundamentally they are just you know Yeah. I mean I guess I guess we're just talking about like you know you know uh more retro fonts and you know Yeah. So for those things are like you need to kind of really look at history. Got it.

what things like how things were made like um I think a lot of the details really matter um for you to kind of fit all the vibes together. Yeah. Okay. Yeah. Like I could say send you some pictures like what this first shot looked like versus now.

Like you can kind of maybe see the difference. Oh yeah. Yeah. When you got started. Yeah.

That that would be useful. Yeah. Um, and and all these different backgrounds and icons, you just kind of use that website and drag stuff into your cursor project, right? Or like it's more like a almost like a research project. So like like um I would say like UI archaeology basic like I got some really old Macs.

Um I have them at home. Um I looked at them a lot and like as you try to recreate these patterns you kind of realize like you know what kind of constraints or philosophies they were thinking about. Got it. Yeah. So this is real OS.

It is almost like my personal playground. I kind of use this to test cursor all the features we make all the different models that are available. So how I started this whole thing was I started from making this soundboard app when I was leaving notion joining cursor because when I'm in meeting rooms I make a lot of noises. Oh no not horrible. And I made a little app for the notion friends so that they can remember me.

But how this started was this looked nothing like this. It started it was only this app. It was like in the tailwind like default styles with chassis in it's like really bare and also I started from kind of like a I was just asking um the agent instead of like this really boring neutral style can you make it more retro Mac OSy? Yeah. and kind of did say without this window part, it kind of applied some like Google font that looks pixely and I I was like this is getting interesting.

Um what if we added a window and then I put in a window and then we added the menu bar. Then I was like what if we just make more apps and we started making the apps in this order. Um I made like a chats app with like a fake Rio in it. Yeah, I made a browser. I made an iPod um that actually works like a real iPod.

Like it kind of completely replicates the UI and UX. Um but it's a little special because it it can also show you like lyrics and like the music video. Yeah. Um and there's like more things and more things. So yeah, that's how kind of you know how so so you kind of just built it over time and I guess this real chat is is using some API like a open API to chat with real or yeah so real is actually like a multi- modal agent.

Um, if you go to the system all closed, clean slate now. Oh, sorry. Uh, turn on debug mode and then you scroll down and you actually see like it's like it's plugged into all of these models. Oh, wow. Okay.

Um, so I can kind of test different like it's almost like you can kind of start tasting the different flavors of like how the models behave or there's like really drastic differences in how they respond to you with the same prompts. Yeah. Yeah. And uh why don't why don't you just show like I I think I was pretty impressed by the virtual PC thing. Can can you quickly show that?

Yeah. Uh virtual PC. Let's ask the agent. Um boom. Yeah, this is like super easy.

Um boot it up. Oh, so this is really just like a DOS emulator. Um Okay. So when you click on it, it will like kind of run like a DOSS box uh in web sam. Got it.

Oh, okay. Okay. Yeah. Okay. like that.

Um, and you kind of like, so the idea behind all of this is um, I kind of want to show people that like all of these things are the same things. Like all the apps that we use, the patterns that we use, um, what we do on computers are almost like, you know, the same and it hasn't changed that much. And, uh, you just built this through like prompting cursor. Yeah. So I think when I started doing these um it it really required like say more technical like knowledge say like I need to instruct the agent like specifically ah you need to use bun you need to use chassen for the components and I need to mention a lot of like details in my codebase.

If you don't do that um it's not going to give you good results and it takes like a lot of turns to do things. Mhm. But now it's like with with the newer models and new like cursor features, you can almost like do anything like one shot get something really like close and all you need to do is like just tweak a little bit. But you did have to upload a do you have to upload a bunch of like pixel assets and stuff icons? I I did I did some research.

So there is this website uh let me show you. So, this is a really cool website where they kind of um have a library of patterns and like things from the past basically. Okay. And you can see um like pixel accurate screenshots and icons and stuff. So, I kind of base a lot of things on this.

Um I found a lot of like historical assets like they're fully accurate. Okay. But everything else say like the styles um on any UI controls I kind of made them with the agent. Wow. Okay.

Awesome dude. Oh, thanks thanks for a demo man. This is awesome. And and um for people who are watching this Ryu also has a public GitHub with all the files, right? So we we can link that in the description.

Now let's talk about like uh how you guys work at Cursor. I think we talked about it a little bit already but like you know like I guess for a feature like plan mode or any other feature you guys build, how does it start, right? Because like you know at like bigger companies you have to do like write a document you got to make a strategy and all this stuff like how how do how do you guys do it? I think how plan mode started with both say when I first started at cursor the thing I I did was back then cursor had chat computer um a lot of different tabs on top and all we did was let's merge them all and then make the default the agents. Yeah.

But the problem is like you know the default letting the model decide might not actually you know satisfy all the things people want. Sometimes you want to do some more specific workflow. So like uh I'm just asking questions. I don't want it to make any edits or maybe I'm like say when I'm doing planning I'm I want it to be me more questions. I want to maybe see some you know document artifacts dot dot dot dot dot.

um these are still like um fundamentally the agent the same agent but you're applying different sets of uh configurations on it um that maybe fits certain workflows or people better and we kind of see say for plan mode specifically like a lot of our users are already doing this in cursor manually u but it's like there's not a really easy way for say other people to do it because you They have to know like how to put this like plan prompt and then ah force you to write markdown in this folder and then always reference the right you know plan file d you just get it. So we built it and then we just kept you know playing with it and iterating on it like using it ourselves. So so I guess uh maybe just like one engineer built it and then uh you guys stock it internally. Yeah. Is that how it works?

A lot of things happen like that. Uh for this one is like I think came from multiple sources. Um there's like some early thinking when we did the de the most thing from me we did some like explorations on say like I want to explore like different kinds of like editors for cursor like say instead of just looking at code what else can you see so we did some playing there and then it's almost like a lot of these little ideas plus say user really likes doing certain things we're like maybe we should do this someone makes a prototype maybe it's a little janky but we can see like ah there's like maybe some promise here. Let's make it better. Okay.

What was the decision to make it like a markdown file that you know it's like well formatted and stuff. Did that come from my Yeah, that came from my mocks from like I think I made it even before I joined cursor um when we were just chatting cuz I think like the natural revolution or evolution of where we're going is we're kind of slowly ascending up or maybe even really quickly ascending in the levels of abstractions of how you interact with the codebase, how you build software. Um, and it could be like like a lot of people think about what is this new AI world interface? Is it just the chat? Is it just the agent?

And my my answer is it's probably not because there's I think more say specific um forms of interaction that is maybe like just a lot easier and this very familiar for certain people. Um then the problem becomes uh identifying what are the most universal patterns that you might or that we might need uh but kind of pointing them to the same thing like underneath it's the same agents doing the same things but maybe depending on who you are the interface start changing or like you can set your own priorities and then um maybe based on where you are in the workflow if you're planning versus building versus testing um it can fit you better instead of saying just a chat where like you're kind of throwing everything into this little box and then it's like a black hole. Yeah. Like chat is kind of you can can't like I think the spec makes makes a lot of sense, right? Like having having cursor working with cursor to write the spec and then reviewing that because like that that that's like where a lot of the product decisions get made, you know, like what you include and not include.

Yes. Uh and then Yeah. Like people say like the spec is dead because people start coding. I I don't think it's dead. It's just like now it's like AI assisted and now you have to review it and then now you get the agent to do the actual work afterwards.

I feel like maybe specing will become even more important. Yeah, it's almost like as the models get better they will be really good at implementing like exact you know prompts or like specifications. Um, and then what we're good at is maybe without a lot of specifications, the model will only make you something mediocre, like something really generic, but like focus your thing on say I'm specking it out like by thinking about it, writing it down or maybe I'm doing something more visual or, you know, something that fits me better when I think. Yeah, but you use that and use that as input, put it to the agent, then they can do something better. And um like I I I think one of the best ways to build like products people want is like is just to kind of see how your users are trying to hack around your product, right?

Like you know before I was using cursor, I always told it not to code like hey just tell me what you plan to do first. So so like um you guys probably have some sort of beta group or something where you can see what people are doing. So we have a group of ambassadors and a group of like what we call like night nightly users. So every build goes out at night. They can see the latest thing that we're working on every day.

There's maybe a lot of bugs but like surprise good surprises. Um, and I think we still have like we have a lot of like people really vocal on Twitter where like Reddit um complaining but also loving certain things so we can kind of gauge what people want. Okay. But what about like uh longer term planning, right? Because like now basically everyone on the team can basically just vibe cool stuff in cursor, right?

Like they can use plan mode and start ship shipping stuff. But like do you guys have a like some sort of like spreadsheet or road map or something of what you guys want to do or Yeah. Uh we don't really Yeah. Um and I think so I I think of it as um because the world is changing faster and faster. There's like say new models dropping every day with like new capabilities and people's like mindset changing to what they prioritize how they work.

I think it's actually more important to um be a little more be a little bit more flexible and not prescriptive of each thing you're gonna do, but you build something that kind of lasts or like the concepts or the foundations of everything lasts and you kind of gradually evolve them and make them better, make them more cohesive. Um and like you know as things shift you can start changing you know what are the defaults people get maybe they get some new modes um maybe like we start expanding this concept to work better for like a team or like a big company. Um maybe it's like from extending from one agent to multiple agents uh running in parallel or sequentially in the background or locally. Um dot dot dot dot but it's like almost still rooted from the same concept or the same I mean but there there is kind of like a vision to basically I don't know to like let anyone build anything right or is that vision or like I think that is at least my personal like why I joined cursor basically it's like I saw a path where it's like as the models get better we need to build the right tools for people to kind of take away all the things the models are good at plus what they are good at in the way that they're really familiar in flow. Yeah.

Then they can do it just maybe just by themselves as one person but also as you add more people with others who are maybe specialized in different areas together as a whole you can make so so many like amazing things. Yeah. I mean that that that's amazing. if people can start creating by default instead of just like watching Netflix or consuming like that that that would be the world will be a much better place. Yeah.

But um but I do want to say um like I I I do think what you just said is very important because um like a lot of companies they do this kind of like planning the theater where they they pretend to have like a one-year road map or like you know like a a northstar Figma, right? Like a Northstar Figma that's been like three months on. And um I don't know. I just feel like the more the more experience I I get working this companies and like the more I just feel like that kind of stuff is kind of like a way waste of time, man. Like right I I don't know how you feel, but I I I just feel like you just have to like talk to users, have fast feedback loops.

You kind of want to know where you're going at at a fuzzy level, but like pretend you have a pretend you have a road map in this day and age is kind of like a just like a you're just lying lying to yourself. Yeah, I think so. or I think it's like there's like a a little ambiguous direction we want to go to. Yeah. And then there's like the present this present state of where we are.

You can maybe see a little bit like steps here. Yeah. And all you want to do is like you want the steps to kind of align to that place and that's it. The fing direction. Yeah.

And you just keep going. Yeah. Yeah. start thinking like ah what is the step here step here step here and then you spend a month meetings oh the step should be here no here here here what's the point yeah and you kind of just like evolved it like like you mentioned that interface started as just like a VS code fork with a bunch of files and now it's more like an agent and what the agent's building you just kind of you kind of see it right you see more people use it that way like they evolve the interface yeah and I think the key idea because it is still the same cursor underneath. Mhm.

But it can start kind of changing itself and fitting it better for anything like for the thing you're doing and for who you are and for your team. Got it. But do you guys have like some sort of check and balances in place because like you know curs is actually in a lot of big companies now, right? Like people are trying to use this to update their production code base. So I guess you can't just do cowboy and ship ship what whatever you have to we now have like different levels of releases.

The enterprise people get the slowest one. I see. Okay. Got it. Got it.

So So hopefully like you ship to the consumers where like all the bugs are iron basically. Okay. So So you ship Yeah, you ship to the consumers first and they complain on Twitter and then you iron out all the bugs. Got it. Got it.

Okay. Got it. Okay. So So then what do you guys use? Uh at cursor like you mostly use cursor right to to just like mix specs and plan mode and yep write code.

Do you use you probably use notion or linear like what do you guys use? Notion linear cursor figma. Okay that's pretty much it. Yeah. Yeah.

Got it. Okay. Why don't we close on a few like two more qu questions. Okay. So most of designers in the industry are still just in Figma, right?

They're just like making mocks in Figma and they hand off the mock to the engineer. So let let's say people want to become more like a real like h how do they become how do they become more like a real? Yeah, download cursor and then try to start something from like something simple. Yeah, there are ways to say plug your Figma workflow to cursor 2. You can say get the Figma NCP and like it will be able to read your Figma files.

But I actually recommend starting from say like a really simple base and then kind of exploring with the agent. then you start kind of learning about these concepts. Um, and I think it's actually like really good to learn these like software concepts. Um, maybe not like say how exactly like this TypeScript syntax works, but rather like how do I structure my components? How do the these things you know flow together?

The props and stuff like it really helps a designer. We're basically writing software in a proxy. Like the the end result of our work is still like code that gets changed. That's right. But maybe we're thinking about like more on the visual level.

Before it was like you do it through a another artifact is kind of in pixels is like layers. It's like completely visual versus now you get to do the whole thing like you get to interact with the material with the code. You can see it, you can poke at it, you can how things work. Yeah. Because uh yeah, like you have to interact with the prototype or the code to get a feel of how actually works.

Like you know there the other abstractions are just hard to tell like how actually works. Exactly. Like it's not real. Yeah. Got it.

So basically your advice for other designers just to like you know Yeah. download cursor and just start prototype typing start building little features. Yeah. Start prototyping and trying things and then don't be afraid. Uhhuh.

Because the agent can actually help you like if you run into a roadblocks just ask ah fix this for me or like copy paste the error. Oh, fix this for me. Ah, okay. What did you just do? Explain for me.

Got it. They will just tell you. Got it. And I think it's important to because if you're working on like one of these big companies, they probably won't let the designers even change the code base. So, you kind of have to just do it on on your own.

Like you do it do some personal projects, put it on your portfolio, like that kind of stuff, right? Yeah. I think starting from there is good, but at some point you like I think the designer will start revoling. Revolting? Yeah.

Like as they gain these skills, they will realize, oh [ __ ] what were we doing? It doesn't make sense. It's like all this back and forth of like uh the engineer builds something but it's like I don't know 50 pixels off and it's like all kind of weird and then the designer needs to take some screenshots like ah here's wrong here's wrong here's wrong here's the spec here's my like red line back to the engineer do this thing loop again again again versus the designer comes in they do the maybe the same like ah fix this fix this fix this send it to in slack at cur cursor. Boom. It's fixed.

Yeah. And then maybe like they they come back, they look at it. Ah, it looks great. Or like, h, maybe it didn't work well. Okay.

Add this engineer. Can you continue that thing for me? And that's it. Yeah. Yeah.

Man, there's so much uh so much of this polish and the craft is just saying like, yeah, like editing copy and making some pixel changes and and yeah, like that that kind of stuff like you should be able to do like it's a waste of it's kind of like a waste of any time to like do all this stuff. Yeah. Or I would say it's like people care about different slices of the puzzle. Yeah. Some people have the eyes to say see the zero to one pixel offness and then some people like their range is like a 100.

Got it. But maybe they're really good at like I don't know the high level system architectures were like backend stuff. Yeah. Yeah. Yeah.

We can leave the back end stuff to the engineers. Yeah. Yeah. Got it. Okay.

Got it, dude. All right, dude. Well, this is awesome. Um and let's close with this dude. What are your top three product or operating principles that you really believe in?

I believe in uh I think it's like simplicity but it is not minim minimalism. It is more like at the core of what you're doing is really simple concepts where say the architecture of things are really simple. Okay. But each of them kind of combine and they're kind of like a layered experience. They multiply.

they they emerge in complexity um so it scales and it works better for more people for more kinds of things but the default state of the thing is still simple that's kind of like what I want to do so that you can kind of re uh reach to more people versus say you kind of constrain yourself into this little little box. Yeah. A lot of people say uh simplicity means like fewer options, fewer decisions, but like you you kind of isolate it to just this group of users, those sets of problems. You design like a perfect solution for those users, those problems in the most simple way, but it kind of gets stuck there versus say you have some you know really robust low-level concepts that are flexible. So like notion it is the blocks, the pages, the databases.

With all of these you can do whatever with cursor is really just say the code, the agent, the models, the tools. Yeah. And with all of these and you kind of give them form, put them in the right place, merge everything, then you can almost like serve anyone, do anything, build anything. Yeah, that's like really important, really hard to do, man. Like uh let's let's take like Figma as an example, man.

like um I feel like if I'm a PM, I'm trying to edit a Figma file. There's like so many uh constraints now like you know auto layout and everything, it just like just like difficult to use, man. I can't move a block box around. Yeah, it's like it's a constant fight between like say rigidity, complexity, flexibility, simplicity. You need to find a balance.

Yeah. um say like if you make the tool so pro like PMs like you you can't even do it. So they start trying to simplify it but then like maybe that actually makes the designers who are the pros like more angry then how do we solve that? Do we like say split into multiple products? Do we say merge into the same product but there's like different modes?

Is it like different configuration customization options? What is it? And I don't think there's one answer, right? I mean it really depends on what you're trying to do like how big is your ambition or what are the core ideas of the products. Got it.

Okay. Yeah. I mean I I I guess my refrain is maybe like um like I I think it's like a linear value actually. It's like it's called simple but powerful or something. So like you know at at a surface level simple but if you want to power user features you can you can use it still.

It's not right like Yeah. Yeah. So, I would make something that's that's more flexible than linear. Yeah, that's true. Linear is very opinionated.

Yeah. Cool. All right. Real. Well, uh, where can people find you and where can people find real OS?

People can go to real.loo. You can find me on X and Rios is just OS.real.loo, right? Yeah. OS.real.loo. Okay.

Well, I hope everyone is into this. Uh, may maybe people can fork your GitHub or something, but like I hope everyone builds their own OS, too. That's as fine as yours. It's going to get even easier as the models get better. Have you seen the Gemini 3 demo?

No, man. Is it coming out soon or I think like someone tested it and then they kind of oneshot it real OS. What? No way, dude. In one HTML file.

Well, that that's that's probably not coding best practice, but okay. That that's great. So, if you want to do the proper thing, you still need cursor. Okay. All right, dude.

Well, thanks so much for your time, man. This is this is awesome. Yeah. Cool. See you.

Take care. Peace.
