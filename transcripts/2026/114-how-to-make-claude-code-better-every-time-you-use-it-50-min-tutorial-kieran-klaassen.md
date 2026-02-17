---
title: "How to Make Claude Code Better Every Time You Use It (50 Min Tutorial) | Kieran Klaassen"
guest: Kieran Klaassen
publish_date: 2026-02-08
youtube_url: https://youtube.com/watch?v=g6z_4TMDiaE
channel: Behind the Craft
keywords:
- leadership
- ai-tools
- ai
- execution
- culture
---

AI can learn, which is really cool. So, if you invest time to have the AI learn what you like and learn what it does wrong, it won't do it the next time. The beauty is that all these things together are synthesized into kind of a story to me. Making sure those learnings are captured and then the next time you create a plan, it's there. It learns.

So, that isn't a compound play, right? It's like a QA team. Basically, you don't even need to write the test. You just say, "Yo, just test [music] it." So if something breaks, it can fix it immediately and immediately validate whether it fixed it. The LFG command.

So I have this command now. Everything we just did, testing and creating a video and creating a pull request and it just runs for an hour and it does it. Hey everyone, I'm really excited to welcome back Kieran today. Karen is a CTO for Kora at every and also my favorite clock code power user. So Kieran is going to show us how to do compound engineering so that cloud code gets better each time you use it and he'll also show us his exact clock code setup to manage multiple agents and a lot more.

I'm basically going to pick pick his brain a lot in this episode. So welcome Karen. Thank you so much. I know last time uh I really enjoyed talking to you and I'm very excited to show and share with everyone what I learned uh because close code is picking up. Lots of people are using it now.

Yeah. It feels like half the conversation on social media is about clock these days. So yeah. Yeah. We're like we're in a bubble but like I think the bubble is expanding a little bit which I love because more people can create which is amazing.

All right. So I'm going to share this slide. Okay. Okay. So I I made this [laughter] I I made this janky slide on compound engineering based on what you wrote and uh do you want do you want to just cover this thing at the high level and then we can get into like the actual clock code?

Yeah. Yeah. Absolutely. So compound engineering is uh it's a philosophy really that I invented when I was building Kora and it's just best practices that I just learned from using AI and especially this started with uh cloth code when cloth code launched a year ago um cuz there were things that worked and didn't work and they were frustrating so I built a philosophy and what I really figured out very quickly was like AI can learn uh which is be cool. So if you invest time to have the AI learn what you like and learn what it does wrong, it won't do it the next time.

So that's the seed for compound engineering. Um yeah, and there are four steps in the compound engineering philosophy, uh which is planning first, um working, which is just doing the work from the plan. Then it's assessing and reviewing, making sure the work that's done is correct. and then taking the learnings from that process uh and codify it. So this is the compound aspect.

So the point is for example if you make a plan do the work and then assess whether it's good. It's never completely exactly the right thing. There's always feedback or things that weren't exactly or you learn something. So making sure those learnings are captured and then the next time you create a plan it's there. It learned.

So that's really the the philosophy of the loop and I have a plugin as well for that and we'll go into that. So it's a philosophy. It's also a plugin that I built that you can use and yeah that's the high level of uh of everything. Awesome. Let me show you what a flow like this looks like.

So the four steps. So first if you want to follow along you can do that yourself as well. Mhm. I have my terminal open here. It's warp.

I have cl code running in bypass permissions. So, skip dangerously. That's how I like to go. [laughter] If you Yeah, we'll we'll we can go into like when to use what. Uh that's how I run it.

I'm just pushing things to go as fast as possible. If you want to follow along, this is the repo. So, you run these commands. Uh the compound engineering plugin, you need to add it and then install it. And then you have the exact same flow as I have.

So, you can just do this in your own project and follow along. So the first thing is what are we building and I am on this quest of making Kora agent native and yeah Kora is my product. It's a email assistant that screens your inbox and briefs twice a day and there's a assistant as well inside the product and the idea of agent native is that the assistant or the agent within the app can do exactly the same thing as the user can do. So like if you can go to settings for example in your app then if you talk to the agent and say can you change these settings the agent should be able to do exactly the same. So I'm trying to get to par there because uh like it's a very important thing because it enables agents to come up with new ways of working and it's really inspired by how cloth code works like cloth code has access to your computer and can just do anything on your computer and we figure out all these cool flows and things we can do suddenly with cloth and it's similar you can bring that same spirit to your app.

So what we're going to do is we're going to plan and uh it's called workflows plan since plan is now taken by the internal systems of cl code. So workflows plan and you give a description of what you want to do and I will use a monologue which is voicetoext app. Uh I don't like typing too much so we'll we'll we'll do that. Um and I'm going to explain what I want. I want to create um feature parity with all of the things we can do in settings.

So any settings the user can do in any of the views. I want to make sure that the Kora assistant can change the same things as the user. So make sure we look first for everything we can do as a user and then make sure to uh see how the assistant can do that. So through tools through whatever we want and you can look at the agent native skill to uh learn how to best do this. So I give some direction here and it's going kick off here now and we can kind of uh see what it is going to do and why it's doing those things.

So any questions so far or this episode is brought to you by Granola. If you're in backtoback meetings, you know how much work it is to take notes live and clean them up afterwards. That's why I love Granola, the best AI meeting notes app in the market. Here's how I use it. Granola automatically takes notes during a meeting.

And I can add my own notes, too. After the meeting ends, I use a Granola recipe to extract [music] clear takeaways and next steps in the exact format that I want. Then I can just share notes directly in Slack with my colleagues or even get Granola to share notes automatically. Honestly, of all the AI apps that I use, Granola is the one that saves me the most time. Try it now at granola.ai/ AI/peter and use the code Peter to sign up and get three months free.

That's granola.ai/peter. Now back to our episode. I'm really curious what's doing behind the scenes like is it making a snip or looking through the code? Yeah. Yeah.

So so this is like you hear this in different places like you specdriven development, you have like taskmaster like like all these things you have planning mode and this is basically the planning mode from cloth but it it's a little bit beefier. it's a little bit more uh it will use more tokens but also it will do better research and really the points here is um it looks at your current code so it grounds itself in what you already did. So if there are patterns it will pick up those patterns. It will look online it will go search for articles that have been written about this and like what are the best practices. So this is what others say is good which is also very uh very handy and it goes look through frameworks you use.

So if you use specific frameworks or libraries it will go look up like also it will check what version you use. So it's also important to yeah use the correct versions because otherwise there might be a mismatch. So just making sure everything is correct. So those are the first three agents here and these agents run as sub agents which means the context will be separate from the main thread. And you can see it's already like 56,000 tokens, 77,000 tokens, [snorts] 35.

So it's like it's it's not cheap on the tokens, but that's not the point. The point is on the max plan. Yeah. Yeah. You have to be on the max plan to because otherwise you run a few and you're out.

Uh but also the max plan is not very expensive. If this is your job, if you make money doing code, yeah, this is clearly uh value for the money and also you if you want to experience what the future is going to be and really push yourself like, hey, how is it going to be? Um yeah, you should just push yourself because uh yeah, like our our CEO Dan at every he always pushes me a little bit because I'm like, "Yeah, but we need to look at the cost for this and it will cost us like hundreds of thousands of dollars if we just switch to the new model." and he says yeah but we should also know what we can do now and if we don't know we just get stuck in the past so this is also for you as a developer if you feel like I'm very scared I want to see what's happening here I want to feel what's going on I want to see the code um let it go a little bit and just experiment with like how does it feel if you don't see what's happening here because it is a complete mind shift as well I mean like Well, like how much does the average developer cost per hour? Like you know the the $200 $100 will pay for itself. It's nothing.

It's nothing. Yes. Yeah. Yeah. So exactly.

Yeah. So like the goal uh so the goal of this like is to get a really good plan and then we as humans look at the plan. Uh but obviously the goal long term is you just say one thing and it's done. So this is just getting getting towards a place where we know and trust certain steps and flows. Yeah.

Uh to get us to a goal. So yeah. So at the end I'll I'll share one other command I have that just does everything in one go. So you don't need to even understand what all the steps are. Uh because I think that's going to be interesting and very helpful soon as well.

But if you are a developer, you want to know what's going on here because you want to tweak this. You want to make your own. You can use my plugin obviously, but like even better is to use my plugin, see what works, what doesn't work, and make your own version of that or make your own flow so you really understand what's happening. And once you do, you can just let it go. Yeah.

Yeah. I love the I love the best practices researcher and framework researcher because I I think if you just use plan mode in clock code it's not it's going to look at your codebase but it's probably not going to do this other stuff right yeah it's like it's good for for like small things I I use plan mode and obus 4.5 is pretty good in doing things but this is just it's it's a little bit better but I hope like at some point uh Boris will just copy paste this into uh into cloth code and we'll have everything working well. So like like my goal is not to have a system like ideally I delete this entire flow and everything works already. But I mean Boris is basically copying man like he already copied your compound engineering so [laughter] and he's inspired. He is inspired.

Yes. He's not been paying attention. So yes. Yeah. Yeah.

Yeah. I I know he's inspired but also like I like um Yeah. But but he's do like he's letting people figure out what they should build and then they're like building it and and that's is really really nice. The funny thing about Boris is like he went on vacation for for like for like a week and then he shipped like 50 PRs or something right on Twitter. [laughter] So I'm I'm just wondering if he's actually working like how how much does he ship shipping?

Like how do you keep track of that? At least 100% is AI written by him now. So and and I agree uh like I think for me it's also 100% now and yeah I haven't opened cursor other than looking at text files in like the last 3 months I think. Yeah. Okay.

And while we wait like what what what terminal is what what terminal app is this? Yeah I use warp. I like warp since yeah warp and it's AI based uh terminal as well. um which is handy if you like do things like with git and it doesn't work you say just fix this and then it will also fix it. So I I like warp also I like that you can like split paints easily.

Um yeah it it's it's the one I like best. So okay so let's see um he did this uh is looking at the agent native architecture skill. So this is something I said to look at here. I said hey can you check the agent native skill because we have this like what we try to do if there are specific information that's important we try to distill it in skills and that means you can put a lot of information in one place uh so for example this one uh here let's open it here agent native architecture so this is a very extensive long document about how to build apps like this. And there are lots of references here as well.

And if you load all of this in context, you would just kill your context. But it's too much. It's too much. But it's also very good to have access to this. So a skill is this way uh like it's kind of just in time context.

So whenever you need it, it will like think like, oh, do I need it now? it will pull in that skill file and then if it needs even more it can look at the the resources inside there or you can run scripts. So this is way to put things like around a specific subject or a tool or a skill that it can use then. So I love that and you can like create your own skills that you reference and this is a way to make the compound engineering plug-in yours where you have your skills. For example, if you do iOS development or you have like a like a Go CLI thing going on, like I don't have any of that in in my plug-in, but you could have your skills and the compound engineering plugin will read your skills as well and we'll also apply these.

So, this is a way to make it your own. Uh, and yeah, I can advise that for sure. And and and you're basically uh you're obviously not handwriting the skills, right? like you're basically getting no no skills. No.

Yeah. So there is a there is a skill uh create agent skill uh in the combat engineering plugin as well. I think there are others but that's the one I have. I think there are some from anthropics themselves as well. So yeah don't write handwrite skills.

No but make sure to read them and review them and see if it makes sense and is if it's good. Okay. So it did that uh is now doing the spec flow analyzer. So I introduced this as I noticed that sometimes it zooms in on things a lot and it show yeah it it it like figures out I need this plugin and this page and it's so zoomed in that it forgets that it's part of a bigger picture and sometimes it just forgets a complete page or thing or it does it's not hooked up to a flow or something like that. So the specflow analyzer is like imagine you're a user with like specific uh personas and go through do you miss anything?

Do did we miss anything in the planning and that's very uh yeah very good to have uh like this. So that's the last step and then it writes the plan and then you can do other things. So let's let's see what it does here what the plan is. Okay so it is done with uh the writing of the plan which is great. Um, and it will ask me what to do next.

So, there are a few things we can do here. Can open the plan in editor, which means let's look at it. I like to use an editor or like a viewer because I like to feel really good about the design of whatever I'm reading. So, we're going to do that. But there's another option, deepen plan, which is like it just goes ham.

It loads everything. It can load and reviews the plan, does any like any skill you have every like it just goes wild. And this is just like if you v code, this is great. You can also trigger this uh like automatically uh from the start, but it just goes ham on tokens and does everything it wants. Uh and it's cool when you v code because like there's nothing to lose really and you have tokens left.

So yeah, why not? Yeah, why not? Yeah. So uh the next one is the plan review. If you want to review the plan not manually but you want like an agent to look at it this is handy.

So if if you don't want to read it or you can say yolo start work um let's normally I open plans and this is also good you can share it with your team with other people. You can ask for feedback like RFC however you want. Mhm. I use a an app uh to read my markdowns and I like it like this because it looks pretty instead of the terminal. It's It's just more pleasant to look at very boring plans and specs and things.

If it looks nicer, I'm just more like it's just nicer. So, I I have this app and I uh You vod? No, this is a typora, but I I already had people reach out that said they vioded a free version. This is 10 bucks or so, so it's not a lot, but okay. The theme is widy.

So, if people want to All right. Okay. witty witty or something. Uh so assistant feature parity enable core assist to modify all uh settings. So analysis it says hey uh okay so general um so addit user doesn't exist.

Um categories reordering doesn't exist but most of it brief settings is there subscriptions is not there and tokens also. So actually we're pretty good. We just need the general the user addit we need. Mhm. Um and okay so blah blah blah blah security.

So like these come from different places. There are different angles to a plan always. So briefs is one. It does like I like to have an example piece of code like pseudo codes because I can already feel or see if this is completely wrong if I see any red flags or not. But uh it it looks it looks pretty good.

So So up time zone. Okay. So it has different different tools. So I my question is now um so my like I'm an engineer. So if you're not an engineer, you could say yeah I have no idea what this is and just do it.

Which is perfectly fine. I think this is this is a good good thing to do. But if you are an engineer and have opinions, this is a point where you can compound or iterate. So let's try that. So because like I yeah I see all these tools but I also think these are a lot of tools.

Can we not somehow consolidate this? So so let's see. Okay, I see you create and add a lot of individual tools. Is there a way where we can create one tool that can do multiple settings so it's less heavy? What about that?

What do you think about that? Yeah. So, let's see what it does. So, like and it's it's important to do this here because if you already started implementing this and you're like an hour further, it's it's or half an hour further or more tokens further. like it's more hard it's harder to take take a step back and say no or rewrite or like you have all these things.

So like if you do it if you spend time uh it's better here. So okay so benefits uh yeah sure we can do update settings tool um and what I want to do is I want to compound this knowledge because I think this is like this is better. So I want to say compound boom. So I'm going to run the compound flow and it will understand from the context here what it is about and it will start to create some documentation about uh things like this. So next time when it starts uh writing a plan it will pull in that information and ideally never make this mistake anymore like like where is it going to write the instructions though like just the default?

Yeah. Yeah. So there there's a a docs directory um and it will organize learnings inside the docs directory and cloth in planning will then look for things that thinks might be relevant. So there's some front matter in the top so you can search on keywords as well. But it also has uh it also has the uh option to update your cloth MD file.

Like a very easy way of to do compound engineering is just saying can you update my my cloth MD file. So if you don't have the plugin and you want to compound it's just like hey don't make this mistake again add this to cloth MD. This is like the the easiest way to do it. But uh yeah, that that that's basically the prompt, right? You just update because that that thing gets inserted into the prompt each time.

Yeah, exactly. So anything that is in your cloth MD file will always be inside the prompt. So it will follow pretty directly. So if you want to start with a very light version of this, if you see it make a mistake, just say hey add this to cloth MD. And I do this all the time actually as well because sometimes it is something like a general knowledge not very specific.

It's like hey how do you start the server for example or like it tries to do something in a weird way and like it should just never do it and then I'll say just store it to clothd I don't use the compound flow. So so yeah it's not one or the other. You can use everything together. It's cloth code and it all works together. So got yeah you can see here it's storing it in architecture decisions uh in solutions and docs uh which is available then as well and it looped through other things I already have.

So if it's related it will uh append it there and it will consolidate it. So and the beauty is this is just files in your repo and cloth reads files in your repo and is really good at that. So yeah, uh yeah, I interviewed someone else who Yeah. who she has like extensive documentation for Claude and uh she doesn't sometimes doesn't even read what whatever Cloud updates. You just trust Cloud to update the docs for her.

Yeah. I I do the same. Yeah. I I like I Yeah. I I don't I don't Yeah.

So this is like this old versus new paradigm of engineering. Like yes, you have old school engineers that don't use AI, but let's talk about the engineers that use AI to write code in cursor or something like that, but they all want to see the code. Like if anything changes, they're like I better see the changes and approve every single change and and there's this new wave where like I'm at at least at and like lots of others too, but like it's it's a little bit more of like I trust you. I don't need to look at all the codes. I don't need to read all the code but I have systems and um ways I work with AI that I trust and through that I can let AI do things and I I think with documentation like that is is the same.

Yeah, documentation doesn't affect the product. So it's just docs. Yeah. So yeah, it's docs. But I I want to say I do the same for like even for product like I do look at all the code that I do for Kora for example because thousands of people use it but if I vibe code something myself or some something experimental or maybe a part in Kora that is just for me to experiment for now like I don't look at all the code all the time because that's not the point if you that ruins the vibes man if you keep looking at all the code.

I know it ruins the vibes and also that's the whole point of compound engineering is to make sure that if you look at the code and you find something that you make sure that you will teach it so that next time you don't have to look at the code. So it's capturing however you work really. Yeah. Uh and to make sure Yeah. that that is always working.

Okay. So now uh we compounded here and yeah we can we can do work. So we'll do that. So it compounded that. Um now the next step is to do the work uh which is just let letting it rip.

Um and obviously it changed the plan now with with the single uh the single tool call. So update settings is now uh you can do as many iterations here as you want obviously but I feel confident now that uh yeah this this is the way I want to go. Okay. So if you're very lazy like me, you don't even compact or create a new session. But probably that's better.

So let's just do the the better way. So let's do new here. So we clear our session. We have a clear uh clear context. Yeah, clear context because it's all captured in the plan really.

So uh we go workflows work and then we paste in the plan. And I use markdown, but uh you don't need to use markdown. Yeah. Yeah. You can use GitHub or linear or whatever you want.

uh and if you have a GitHub CLI installed, it will pull from GitHub if you have the the linear integration somehow like it will pull from there. So you can you can find a place wherever you want to live. So if you're more if you're a GitHub focused shop or engineer or whatever, then just do it there. So what's the difference between like the this this work step versus just you saying let it rip or like go build it? [laughter] Yeah.

You ask you a few questions? Yeah. Yeah. Yeah. Yeah.

So, so yeah, like clearly you can say just do it or something like that. But there is one thing in the beginning here, especially since you have a new fresh uh context here. It will like figure out um if anything is missing because sometimes things are missing. So now it it says I have a few questions. So the plan shows updating user and account in a transaction.

uh if only name or time has changed should still wrap a transaction or is it also changed? Well, that's I mean that's a good question and we didn't really answer it in the research. Yeah, like sometimes there are good questions um where it's not super well defined. you miss something or it it removes something but generally uh it yeah it just goes but it does make it does make a plan now how to tackle this so it is a little bit more than just do it it does build a plan how to do this uh let's go I'll I'll just say let's go you figure it out just do the best and that is fine sometimes and just having these questions here is good for context because it will start thinking about these things and why it is best. So, uh that's why like this is kind of like thinking mode basically but it's like us pushing it to think or like what could go wrong and then it will think oh that could go wrong and then it starts thinking about how it could go right.

So it's like traditional prompt engineering uh here that just works for you if you yeah have these tokens. Dude, it really feels like Yeah, it really feels like you're like a tech lead or like a EM managing like this engineer and you're just having like meetings with it, right? You're just like reviewing his plans. Yeah, absolutely. Directions.

Yeah. Yeah. Yeah. Yeah, I I I think last time we talked about it as well, but like like skills you need are like tech lead skills and like uh management skills. Uh because you're managing these agents and this actually feels like feels very hands-on still.

We have to still do all of these things. Yeah, I think the future uh and we're very near is where you just do one thing at the start and you get the end result and it's pretty good. And obviously you need to do the compound loop for a little bit. So you need to train it and but it's similar to onboarding a person on on your team. You need to like get them on board, get them used to your code.

But once that is done, uh yeah, you can let them go and really uh yeah, really just run with it and uh do more end to end. Okay, so looks like it's almost done. It's running test already. Yeah, like this is it. It did the feature and it's writing the test.

So uh that's really cool. and and and after that uh one of the coolest things of Opus 4.5 is the testing because it's really good at using playrights and really good at understanding flows. Uh, so this [snorts] I love like before I still had to go in and manually test things. Uh, like clicking on things like obviously writing test it was good at but now we can have playright work. Like it never worked really well but with Opus 4.5 is the first model where I think playright really works.

It's not super fast but it works well. And uh, playright just for audience is like basically like a MCP to have Claude see the browser right? See the browser. Yes. Yeah.

It's just a Chrome uh like you link Chrome to CL code and like it can control your Chrome window. There is a Chrome plugin for CL code as well which you can use too and that's pretty good. But for me I I like playright a little bit more since yeah you can record the screen you can take screensh I do things like that where I record the whole video of the whole flow and put it to the pull request automatically as well. So I just like playright a little bit more but whatever works for you if if you like uh to use something else that's so so basically so basically to use playright you just type one line to install it right and then you just do playright test and what what it's doing right now is uh is loading a browser behind the scenes and playing with the product. Yeah.

So it's now it's still actually it's it's fixing the test still but uh after we can just yeah okay let's say the feature is done uh these I I think it will work because these are just tests it writing for specific use cases but yeah we don't who needs it I I I need test but just for like us we're very uh we want to see it we're too excited um So you run playright test and what this command will do this is also part of the combat engineering plug-in. It will write a plan of like what are the features introduced in in here just keeps going. Okay. Well that's good. Yeah.

Writes a plan like what to test, what is new, what is introduced. And then um here let's let's just say for now skip the test and go test and play. Right. We'll get back to that after. So you can see how good Opus is with following directions like the we have the Rolf Wigum loop thingy go viral but I haven't seen it to be very very needed because it's pretty good at following directions.

Okay, so here we go. Uh it's funny because it's now on deaf please. Okay, so yeah, so we're here and now it's going to control the screen. So, I will just move this a little bit. Yeah, it's going.

So, it's controlling it. It's taking screenshots and it can do all of this. No hands here. Look, it's not me. And it's just testing the feature.

Okay. So, it's kind of like a it's kind of like a browser use thing, right? It's kind of it's a browser use thing. But the beauty is that this was kind of a missing piece. Like you have system or integration tests obviously, but this is like the ultimate test whether something works.

uh- which is like does it work? And it's very easy. You don't even need to write a test and it's not no overhead in like your CI or anything. You just say yo just test it. It's like a QA team basically.

And it's very nice and and you can say just do this for an hour. Think of everything that can go wrong and really kick the tires and like try to break it and it will try to do it. And the beauty is it is in cold code. So if something breaks, it can fix it immediately and immediately validate whether it fixed it. So it's like this iteration loop using this is very very cool and very very powerful and and if something uh if something like breaks can can also inspect and see all the console er errors and stuff.

Yes. Yeah. It can control the entire browser. So it can click on elements, it can run JavaScript, it can read the console log. So basically you as an engineer in Chrome it can do everything.

So it's it's really cool and also one added thing is like Kora connects to Gmail and and I was doing a feature where uh I just I just launched it where we do email signatures and drafts and to see if that works you need to go to Gmail and how do you write a system integration test to go to Gmail? You're not doing that. But with Payrite, I could just log in with my Gmail account and say, "Hey, I'm logged in with my Gmail account. Just see if it works." And it went to Gmail like it's just a browser. So it's it's it's magical to see it work.

Well, it works. Our feature works. Yeah. Um which is cool. Um so this is a good state but what I always do after that is uh making sure there are no security risks or if there's no slop or if it looks can be done more simple like there are all these things that can always be better and uh the review command which is the the last command or it's the it's it's the command we didn't use yet we used the compound already this is the assess stage right yeah is the assess state.

Yeah. [snorts] stage and it's running reviews from certain perspectives and it's my perspective. So I have an agent that has my like way of working. I added a security person architecture code simplicity reviewer which is also a very good one. uh which like uh yeah Boris has the has one too and he shared it uh I think this morning on X so Anthropic does it too um like there's also one that reviews whether this is agent native enough dhh is the creator of reals and he will just like he has a very opinionated uh view on things which is hilarious always uh and the beauty is that all these things together are synthesized into like uh kind of a story to me.

They're like priority things that come out of this and they're not being fixed immediately, but I'm asked to say what I want and say, "Yeah, this sounds good. This sounds good. This doesn't sound good." So, let's let's finish these and Yeah. Because otherwise, if you just say like uh just like, you know, clean up the AI slop code, it's going to do it's going to start just like change the code, right? But this one.

Yeah. Exactly. Yeah. Yeah. Yeah, because we like the point of like we are at a stage where we tested everything.

We reviewed the plan like and it's too easy to now like go into a direction where it increases scope or delete stuff and like you need to be careful and you're not going to change too much now but you want uh like very knowledgeable people or agents or things to look at it from a certain perspective. Uh amazing. Yeah. which is like this is the point where like before we we had like very wide brought it back to a plan narrow plan that's very focused and we had that focus plan being worked on and since it was focused it kept to that plan but now we need to make sure that we didn't miss anything so we're wide again so there's like going in and out from from looking different perspectives which works yeah so it compiled everything into like it has things. What it's doing now is creating a to-do directory.

So great, we don't have any P1s, which is great. P1's are like you should never never merge this because you have security flaws. We have P2, which sometimes are important and P3 is like you can kind of ignore, but yeah, nice to have. And what it's doing is writing it to my to-do. I have a folder to-dos and it's writing them there.

Um, and you can see also I have this status line here where I can see how many to-dos are pending. Um, but what I like to do, I don't like to read a lot of stuff. I want to like kind of the AI to walk me through what to do or like how to go think about it. So I have a command called triage and triage will just in a sort sort of conversational way walk me through all the all the findings and then ask me what what do I want to do and then it uh makes the decision and then yeah after that I just run one command to resolve everything and a PR is created and so yeah so for example this is add name length validation I mean okay sure let's do it it's it's like small things but like like that is fine so it will crash because it's it's database backed but this is good okay so we do that so I just take us just real quick like um like for me to build all these sub agents that you have for each step of this comp engineering will take forever man so like the fact that you're making this available on GitHub for for free is is great like I I basically take Kieran's stuff and build my own it took me a year so yeah like Uh yeah, it takes a long time. But I do realize some people want their own and they they are more inspired and you can pick one of these.

But the beauty is you don't need to use this whole system. Yeah. Um you can just say I use the plan phase and then I go manually code everything because I love to write code. Sure. Or it's all it's all triggered by slash commands, right?

Like all it's all slash commands. So you don't need to use all of this. So yeah. So it's marking these as ready. And then uh now I'm happy for example and then say resolve uh to-do parallel and that's it.

It's going to pick up all these things. It creates like a dependency graph and how it thinks it can resolve it and then sub agents will pick up all the to-dos and push everything and yeah then we have uh then create PR and then we're done. And and this whole flow like how like how long did it take? It's it's it's very quick and yeah, very cool. So yeah, one one thing I want to show like what if all of this was just one command.

So I have this command now that I [laughter] tried out yesterday is the the LFG command and basically everything we just did. I just say in a command, can you just do all of this? And I have the Ralph Wigum loop in the start and basically it just does everything we did plus a little bit more. and testing and creating a video and creating a pull request and and it just runs for an hour and it does it. So you can what do you mean?

It creates a marketing video or or something. Yeah. Yeah. Marketing video product marketing details change log everything. So it's just like this LFG at brief to CLI or whatever you want and then it goes.

So and I think we're very close to that. You see a lot of people with like agent orchestration stuff like that and I think to get agent orchestration very yeah to get it right you need a system like a combat engineering or whatever you have because you need to make sure yeah it's it's like the the harness plus your own harness like all because you set you set up all this [ __ ] over here so now it's making your life a lot easier basically. That's what it is. Yeah. All right dude.

Let me ask you some rapid fire questions. Let's start with the permissions thing. So like one of my pet peeves is is just like super annoying. It keeps asking me for approval for permissions. So yes.

So basically um so maybe you can exit clock code and and like show us like um so you just type a CC and then dangerously skip permissions. Is that Yeah. So I have an alias for So I what I do is I do CC but what that means is just an alias for um Oh for all for the full thing. Got it. Yeah.

It's Yeah. So it's it's just uh called dangerously skip permission. So if you go in this mode, yeah, it will never ask you for anything. It will just keep going. Um that is good for certain flows like you like if you are uh like a system like this works better if it just goes because the checks are not in between.

The checks are when you do a pull request or when you merge code. So just make sure that if you do this, don't share like your SSH secrets with it that can delete your production data. Like just make sure like the sandbox or your computer where you work is safe because it could do anything you can do. Um but it won't do it. Like technically it can, but like it doesn't really do it.

But also you can start approving things. Uh so if you if you don't want to do that, you just use cloth and you say add this to permissions and it will remember it for next time and that's also perfectly fine. It will just be painful in the first week, but after that it will not be. Yeah. There's like a settings file or something, right?

Or you can add a bunch of permissions. Yeah. Yeah. It will add it to your repo or however you set it up. There's there's lots of flexibility there.

Yeah. But I think in practice like I think Opus is smart enough to not just like randomly delete folders. So like Oh yeah. Like Opus will not do stupid stuff. No, it will it will do smart stuff.

It's not doing anything it shouldn't do like like oh deleted my database stories [laughter] like it happens but I don't think it's Opus 4.5. Okay so let me ask you another question. So you just show the way to like LG and like you just have it work for an hour right so what what's your preferred flow to like do you give it instructions over the phone too and like which do you use the clock code app or which prefer flow? Um yeah, so I so one really cool thing like not a lot of people know about it actually is if you're in cloth code you can do the amp percent sign. Uhhuh.

And what that will do is it will do whatever you do here. So you can you can say workflows plan uh push to it pushes to background. Yeah. Okay. So if you uh if you install the for some reason I haven't installed it now but it will push it to the background and it will push it to uh clo code on the web.

So you can continue conversations on your phone. So here here you can see I have cloth the cloth app and and you can see the the repos here and I can even work on local here which is also cool but I use it in the terminal but what it does it like it pushes from the terminal and then you can pick it up here. So it will push the session whatever you had up to the cloud h which is really cool. Yeah. And also like you could continue.

So for example, we're here and here you can see the pull request is created. So we're successful. Um here like this is the feature and it looks great. Yeah. So that's a feature.

But if you if you're like in hurry uh uh continue the uh test here cuz we didn't finish the test and it will cuz this so it should go to the cloud app. Yeah. Yeah. So So now Yeah. So now it should start here.

Yeah. So here. There we go. Wow. So it continues here in the app.

And you can do that on your phone too. I have to say the cloth phone app is not the best and there are bugs here and there. But this is really cool. And you can do it the other way around where if you are here, you can say open in CLI here and you can continue a conversation from the web and keep going. Oh, so you just have to t type AMP a percent.

Oh, I had no idea, dude. Yeah, no one has that. Yeah, no one knows, but it's it's pretty [laughter] cool. You can do local host changes too from from this. It will create an entire new environment uh in in the cloud, but it will work like it will have all the nodes and the things.

So, yeah, it will it will work fine. Yeah. Okay. So, okay. So, let me ask you another question.

So, I think you showed us this a little bit, dude. Like I think all this [ __ ] about slash commands, sub aents, hooks, skills, it's like overwhelming, man. It's overwhelming for someone who's like trying to learn this stuff. So yeah, but I think your workflow is use slash commands to trigger these workflows that then call the sub agents, right? And then maybe those sub aents can call the skills.

Is that kind of how it works? Yeah, because they like the the confusing part. They're all the same but slightly different. And it's like like what when to use what um and and how so I'm triggering now to create a video to show how well this works and add that to the pull request as well. So if anyone uses that so we'll just leave that running.

Mhm. So how I think about this slash commands are like you trigger things like do this or do that or like it's it's like commit this uh create a pull request or like whatever you do like it's something you want control over like it's you saying do something. Um and the beauty is it could also be the agent because my LFG is like a list of other SL commands. So it could be you instructing the agent to call commands as well which is also uh good. That is that is that and and it it works really well.

Sub agents are mostly if you want to run something or do something specialized where like you don't need the whole context, but you want like a result like like I just want someone to tell me or something to tell me what the answer is or like how good it is or what's wrong where you don't really care about the full thing which is uh like review agents are great or like research agents because you don't care about the 30 books it reads. you just care about what the answer is. So that's when I would go for agents. Also, if you want to do things in parallel, like if you can do 10 things at the same time, sub agents are the way to go because that's how it works. Um even though you can do task in in in uh you you can trigger and the confusing part is you can trigger sub agents as well manually and like you can all do these things but like that's not how they're made.

So basically you basically you don't really trigger sub agents manually, right? You trigger through like some slash command. Is that right? I never I Yeah. I never add a sub agent.

I never do that. No. No. Okay, makes sense. No, because I like to like the slash commands are kind of the business logic or something like this is how the agents should work together and I say now do this specific thing and then it will do the thing.

Um and then you have skills and we've touched on it already. skills is just like uh if if there is like something for example uh generating images on nano banana using the Gemini API like there's no image generation in cloth or cloth code but it would be cool why not so that's a perfect way to create a skill where you just have a skill that says hey if you want to generate an image I'm here uh load me and uh I have some scripts and it works great so then you can say I want to generate an image image and then cloth thinks oh I have a skill that knows how to generate image let me put put that stuff in and suddenly cloth knows how to generate an image and that's like just in time context yeah it's like injecting knowledge at that point uh so yeah that's that's when I use a skill yeah it you know honestly like the skills don't get triggered that well like when I use the cloud app it doesn't get triggered that well but maybe in cloud code it gets triggered H you just need to be very explicit like I literally say like use this skill for and then it does it okay yeah if you're very specific and also make sure that you follow the best practices writing the skills there are some like best what the description should be because there's some nuances in like you should say not like when to call it but like I can do this and this and this or something like that so it aligns better. Yeah. Okay. All right, dude.

Well, let's let's close it like let's close this v video that you're generating. So, how are you going to generate this marketing video? You're using playright or Yeah. So, it's uh Yeah, it's it's now using Playright and it's doing stuff. So, it's like screen recording.

Is that what Yeah, it's screen recording and then converting it to like a smaller size and it's uploading it. It's recorded and normally it uploads it. um open the video and then we'll assign it to the pull request. So I'll just show it here, but it made a video automatically showing the flow. Um that's great.

Yeah, which is really handy like if if you review code of someone else and you open a pull request with screenshots of the changes uh sometimes before, after and a video of the full flow. That is great. So let's go. So this is it the video. Oh, that's awesome.

They can share in Slack or like point your Yes, exactly. And it's uploaded. There's a Yeah. Ex. So interesting.

It's So it's not always Let's see. It started here, but you got to review it. Yeah, you got to review it. Okay. So it is Yeah.

So it is doing well. Got to review it. But it's recording a video and like nine out of 10 times this works great. and and also this feature normally would have had the review already and like some testing before. So it's like it's more smooth, but it's really cool that this is like an artifact you can create and you can do it however you want.

You can use it however you want and and just part of your this is part of your compound engineering GitHub or Yes, it's all it's all in the compound engineering uh plugin. You get access to all of it and that's great, dude. Yeah. Yeah. So, it's all here.

And if you want to only use a command, you just go in the commands and you can see uh yeah, you can see all the commands here. You can say, "Hey, the the v the feature video is an interesting one." Just copy this to your local directory. That works as well. You can read everything here. Okay.

So, yeah, that's that's about it. Yeah, this is this is amazing. I I I think the thing I'm most blown away by is actually the playright stuff. Like the fact that I can just start testing and like make a vid video that that's pretty amazing. Yeah.

Yeah. It's really cool because it's really like I'm just thinking like what do I do always manually and that's getting less and less and less because it's just taking over more which is great in my in my view at least. Yeah. Yeah. Awesome.

So so we'll put a link to the compound engineering plug-in in the description and uh Kieran if you want to find you just search on X. Yeah. Find me on X and also I write uh about all this stuff at every.2. Um also recommend checking that out. But yeah, pleasure.

Yeah, this is so much more fun than uh you know doing all the man manual stuff. So thanks so thanks. I know. I know. Yeah.

[laughter] Cheers. Cool. All right. Thanks, Karen. See you.
