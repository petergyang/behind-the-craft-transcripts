---
title: "Claude Opus 4.6 Is Here: Everything You Need to Know"
guest: Peter Yang
publish_date: 2026-02-05
youtube_url: https://youtube.com/watch?v=5z4StBj9qck
channel: Behind the Craft
keywords:
- coding
- ai
- execution
- startups
- storytelling
---

Hey everyone. So, I got to play with Anthropic's newest model, Opus 4.6, before it launched, and I want to share my first impressions with you all. In this quick video, I'm going to cover what makes Opus 4.6 different, and I'm going to test three use cases live. Using regular Claude for podcast postprouction, using claw code to generate a game, and using codework to generate a presentation. So, let's dive in.

Okay, so what's new with Opus 4.6? There are three things through my testing. First of all, it follows instructions much better in long threads. Previously, in long conversations with Claude, it can get lost and ignore your instructions, but with Opus 4.6, it remembers your initial prompt, even if you're deep into the thread. I'll demo this in the cloud use case next.

Number two, it gathers context before acting much more. So, one of the criticisms of anthropics models, especially for coding, is that they tend to just want to code. You have to use these hacks like plan mode to get it to think through things first before coding. But with Opus 4.6, this is much better. It read through the full picture before making any changes.

Now, this means that the initial response might take a much longer time, but the work that follows is much higher quality. Finally, it doesn't give up as easily on hard problems. it will try multiple approaches independently before checking in with you. So in some ways it's more agentic and can run longer independently. And just a few quick tips from using Opus 4.6.

When I use cloud models, I always have extended thinking turned on. But now extended thinking is adapted thinking. So the model is smart enough if you give a simple math question to just answer the question without thinking too much and it can think longer for more complex tasks. And number two, because Opus 4.6 gathers more context by default, now you don't have to prompt it to be detailed or, you know, don't be lazy or just check everything. In fact, if you prompt it like that, it can actually lead to worse results because it could just overthink things.

Okay, so now let's put Opus 4.6 to the test first inside regular claude with my podcast postp production project. So, what this project does is it takes a raw interview transcript and it turns it into YouTube titles and thumbnails, show notes, key takeaways, and social posts all in one shot. It probably saves me at least one or two hours every week in podcast postprouction. So, let me show you what the project looks like. Okay, so here's my project and let's take a look at the prompt.

And you can see here that it's a very, very long prompt that I worked on over a very long period of time. It has instructions and the best practices for making YouTube titles and thumbnails. It has stuff around moments to cut, intro to make, keep going down. It has a show note format that I like. It has key takeaways and it even has social posts.

All just coming from a raw transcript, right? So, you can see here I put Opus 4.6 here. And let's take this transcript right here from an interview that I did with Kieran that's coming up soon. Let's copy this whole thing. So, I'm going to select and copy this whole thing and let's go ahead and just paste this raw transcript into Opus 4.6 and see what it comes up with.

Okay, so you see that I thought for a little bit and now it's coming up with thumbnail and title combinations. Compan engineering so clock code can get smarter every time. Yep, makes sense. Make clock code learn. Why your AI code doesn't improve.

Zero to AI that learns. Yeah, these are pretty good combinations. I probably want to go back and forth through a little bit more. But you can see here it's still generating stuff. So, it's generating the intro reel that I can use for uh the beginning of the podcast.

It's generating a bunch of moments that I should cut. It wants me to cut the sponsor read, which I don't think is a good idea. No, I'm not going to cut that. But uh and then it goes down to generate show notes and newsletter post and everything else. Now, this is not something that I would just copy and paste in one shot.

I will go back and forth with it a lot, but just testing Opus 4.6 six on this long prompt. You can see that it's actually performing remarkably well. So yeah, so that's our first use case. Uh I'm definitely going to be using this every week to save a couple hours a week on post-production. But now let's move on to some of the more fun use cases.

Right. So next, let's test Opus 4.6 with clock code. And my favorite thing to do for vibe coding is just to build a game. So I'm going to use the same pixel pack that I used in my previous tutorial on how to build a game with clock code. you can check out in the description.

But this time I'm going to build it in a very lazy way to see what 4.6 is capable of. So I'm just going to give it this prompt. So let's actually open up clock code. So I've open up clock code here. Let me zoom in a little bit.

You can see it's on Opus 4.6 and I've already copied the pixel art assets into this folder. So the prompt is explore the folder for gaming art assets and then use ask user question to build a game together quickly. All right, so that's the entire prompt I'm going to give it and let's see what it comes up with. This might take a while, so I'm going to skip ahead. Okay, we're back.

I gave it a massive collection of 4,000 plus assets across four categories, right? and it scanned everything. And now it's asking me which game I want to build. So, space shooter, sidescroller, beat him up, top down RPG adventure, or something else. I feel like a beat him up could be fun.

I've already built too many space shooters, so why don't we just pick beat him up and let's use phaser 3. And let's go ahead and submit. And let's also say don't use playright MCP. Playright MCP is basically something where it can test the game itself in the browser. But just for lack of time, let's just say I'll test it manually.

Okay, there we go. Now, it's going to go ahead and build a game. And again, Opus 4.6 tends to, you know, work longer before it comes back to you. So, I'm going to go get some coffee and I'll come back once it's done. Okay, guys, we're back.

So, here's what happened. Claude took maybe 15 minutes or so to finish building the app and then it told me to run the game and the game didn't actually work. So I said the game doesn't even start when I press enter. Okay, I want to give you the real deal. And then uh it went off and tried to fix a bunch of bugs with um player HP bars and other stuff.

And now the game actually works here. So, we can move around. Can see the street bar. We can kick. We can jump.

We can punch these enemies. And yeah, overall the game seems to work. Uh, so this is pretty impressive, right? It took just like one little prompt and a little bug fix for me to get this street brawler game working. But you know what?

Just for fun, I asked it to add more enemy variety. And now it's looking for more sprite sheets. So, let's come back uh once it fixes that part, too. All right, everyone. We're back.

And uh it looks like clock code with Opus added uh a few more enemies. Probably took another six minutes to do. So now let's go play our game. All right, let's press enter. All right, so we have our punch, we have our kick, we have our jump.

So first round is still just the punks. So let's beat them up. It's kind of weird that they're coming at me backwards. Probably need to flip that. Round two.

Now there's hounds. All right, let's uh beat up the hounds, too. And let's see what happens in round three. Uh oh, now there's ogres in round three. So you can you can beat up the ogres.

Yeah. So uh I can keep playing this, but um you know, we basically built a basic version of Streets of Rage, a beat him up game. Oh my god, now there's horsees trying to shoot laser rays at me. But anyway, we built a basic version of a beat him up game in just what through two or three simple prompt prompts. So, if you want to try this yourself, I'm going to include a link to the pixel art pack again in the description.

And uh yeah, just building games with Opus 4.6 is super fun. But let's move on now to our very last use case, which is using co-work to make a presentation, right? So co-work, you can find it on the claw desktop app. And the way it works is it spins up a virtual machine to make presentations, to organize your computer files, and to do other things for you. In this case, I've asked it to create a presentation with claw code best practices.

Make it visually interesting, right? And it's almost like a easier to use and more beginner friendly version of claw code. You can see here it thought for a little bit and now it's asking me some questions. Very similar to how we were building a game and it started asking me questions, right? Using the ask user question tool.

So, who is the target audience for this presentation? I'm going to have to go with developers new to clock code. How long should the presentation be? Let's go for short. Any tips you want to cover?

Let's say all of the above. And there you go. So, now it's going to go off and actually build a presentation. Let's see what it actually does here. So, it opened a progress tracker.

It made a to-do list, right? So, it's going to make the PowerPoint. It's going to research some best practices. And it's going to make the presentation. And finally, it is going to share the PowerPoint with me.

Now, right now, co-work, I believe, is uh mostly PowerPoint focused. I'm not sure if we can actually make Google Slides yet. We have to test that later. But why don't we skip ahead and see what kind of PowerPoint presentation it comes up with for clock code best practices. Okay, everyone, we're back and let's see what codeork actually did to make the presentation, right?

So, let's scroll down here. So, it did a bunch of research on clock code best practices online and then it actually coded the PowerPoint. I didn't even know that you could actually code a PowerPoint, by the way, but apparently you can. And then it did a bunch of visual QA findings. So, it actually found a bunch of alignment issues, card spacing issues, and so on and so forth.

And now the presentation is ready. So, let's actually open the presentation in Keynote and take a look. All right. So, here we are. Clock code best practices.

So what is claw code? Runs in terminal. Yep, looks good. Getting started. Very clean.

Uh there's a bunch of commands you can run. Claw.md. What to include and not to include. How to prompt claude plan then build pattern. Verifying the code with tests hooks MCPS permission security context and common mistakes to avoid and key takeaways.

So this is a pretty good presentation, right? It's very clean. It covers the major topics. I kind of wish there were a little bit more pictures. Anthropic doesn't have an image model, but it's trying its best by using icons and emojis.

So overall, I think coldwork has actually improved a lot since it launched about a month ago. Uh I haven't really put it to a test too much, but the fact that it can make presentations, it can organize your files, it can write documents seems to be pretty useful, right? Especially with Opus 4.6. 6's planning and context abilities. All right, so there you have it.

I hope you enjoyed this no hype breakdown of Opus 4.6. I just want to say one more thing. On the one hand, anthropic I think is really firing on all cylinders lately. I love the models because they sound the most human and are also in my opinion the best for work and productivity. And in the coding space is actually very competitive.

So both Anthropic and OpenAI Codeex are going after the coding market, right? And it's pretty much head-to-head. In fact, today OpenAI launched Codeex 5.3 just about 20 minutes after Anthropic launched Opus 4.6. So they're really kind of going at each other. They're running ads against each other.

They're making fun of each other. And there's a whole bunch of other benchmarks and breakdowns. This particular one from my friend Kieran shows opus leading but there's other ones uh you know on Twitter that actually show codeex leading instead and I think the general sentiment from my developer friends at least is that opus has a lot of personality is good for building 0ero to one is good for everyday coding tasks but codeex is better if you have like a super nardy problem or a gnarly bug that you want to fix that's the honest sentiment that I get from my developer friends but you know With the pace of change, this could change very fast. So overall, I think at the rate that AI is accelerating, I'm sure Sonic 5 is coming very soon, too. So if you want me to make more real, no [ __ ] no hype breakdowns like this, please like and subscribe.

I hope you all enjoy Opus, and I'll see you all next time.
