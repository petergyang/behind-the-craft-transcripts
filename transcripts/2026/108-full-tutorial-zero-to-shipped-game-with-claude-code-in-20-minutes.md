---
title: "Full Tutorial: Zero to Shipped Game with Claude Code in 20 Minutes"
guest: Peter Yang
publish_date: 2026-01-21
youtube_url: https://youtube.com/watch?v=247Z3jdw_hs
channel: Behind the Craft
keywords:
- ai
- ai-tools
- coding
- startups
---

Hey everyone. So today I'm going to show you how to build a really fun retro space shooter game using clock code. Building games with my seven-year-old and Clock code is one of my favorite weekend activities. So I want you to learn how to do this, too. Okay, so first of all, here are some games that I built with my kid.

I built a sidescrolling underwater shooter where you play a swimmer shooting against a shark. My kid and I also built an animal hospital game where you have to cure different animals and then we use Nano Banana to generate the images. But in this tutorial, I want to show you exactly how to build a retro 2D space shooter in five steps. So, step one, set up the project. Two, find game assets.

Three, draft the spec. Four, build the MEP and iterate. And finally, clean up and ship the game. And you know, clock code can be pretty intimidating, but I promise you that this is a tutorial that anyone can try. My seven-year-old doesn't even know how to type right now, and she knows how to build games.

So, don't get intimidated and let's get straight into it. Okay, so here I have an empty folder called Space Shooter Game. And this software if you don't know is cursor which you can download for free and you can talk to clock code uh using a terminal or something else too but I just prefer cursor because I can actually see the files that clock code is making. So how do you actually load clock code in here? You go to terminal and you have to make sure that clock code is actually installed.

All right, so quick recap. To install clock code, just search for clock code and all you got to do is just copy this link and just paste it into terminal to install it. And by the way, terminal is kind of like an intimidating thing, but it really isn't that intimidating. It's basically just talking to an AI agent and going back and forth with it. So the default way to start cloud code in terminal after you install it is just type claude, right?

and you press yes and then it starts clock code. But the way I like to use clock code is I type claude dash dangerously skip permissions. Got to make sure I spell it properly. And what this does is it loads claw code and lets it work in your new folder without asking you for permission each time it wants to do something. So you can see here that it has bypass permissions on, right?

And trust me when I say this, for stuff that you're viing, for stuff that you're building for fun, this just makes it way more fun. And Claude is generally smart enough not to screw up your files. Okay, so that's the setup. Now, let's move on to step two, which is finding the game art. So, what you can do, and this is how I build games for my kid, is I have a voice dictation app installed called Whisper Flow.

You can also use other ones, but basically um I just kind of give Claude an idea of what we want to do. And my kid can talk to Claude, too. So, here we go. I want to build a retro 2D space shooter. You know, where can I find some free pixel art assets for this game?

And there you go. It's pasted directly in here. And let's just go ahead and get Claude to execute on this prompt. So, Claude has, you know, web search capabilities built in. So, it can actually do research for you.

and it's going to find a bunch of interesting links up here, uh, open game art, itch.io, and so on so forth that you can either browse yourself or get claw to browse. But just to make this tutorial as simple as possible for you guys, I actually found a really great pixel pack already. Uh, it's made by this awesome creator called Animus and uh, you can basically download it for free. I think I paid five bucks for him to download this. And it's got some pretty amazing pixel art.

You can make a Castlevania game. You can make different types of platformers. You can make a pixel girl dance and uh you can even make like um cyber punk stuff and so on and so forth. And in here there is also a pack for making space shooters. So all you got to do is uh go ahead and download this pack and I'll include a link to this pack in the description of this video.

Okay, let's come back into cursor and I've already downloaded the pixel pack and let's actually go to finder right now and open our space shooter folder and let's just drag and drop this pixel pack into our space shooter game folder. So there it is. So if it work properly, it should appear here. And if you open this, there's a bunch of characters, aliens, and so on, environments, and all the great things that we can use to build our space shooter game. All right.

So, now let's go back to clock code and say, "Hey, I just added some pixel art. Why don't you look through the folder and list the ones that we can use for retro 2D space shooter?" All right. So, now uh Claude is going to go ahead and browse this new folder and hopefully find a bunch of art that's relevant for the game that we want to build. All right. It looks like there actually is a spaceship shooter folder that has a bunch of stuff.

Yeah, this looks great. It looks like we have the art that we need to build our game. So, let's go ahead and move on to step three, which is to draft a spec or the plan. Okay, so now I'm going to tell Clockode write a spec with requirements, three milestones, and links to all the pixel art assets that we're going to use. And each milestone should be playable.

And by the way, use ask user question if you have any questions. So before we execute this command, let let's take a look at some best practices that we just covered in here. Right? So first of all, write a spec with the requirements. You should always write the spec first before you get claw to build anything.

Always plan first before building. And we broke the project into three milestones so that we can test it along the way. You don't want to try to get claw to build too much at once. And we also asked it to link all the pixel art so that claw knows where to find each art asset. And finally, ask user question.

This is my default way to write specs. Now, it's a new tool that Anthropic introduced that gets Claw to ask you a series of questions to flesh out the spec together. It's absolutely brilliant and I'll show you how it works. All right, so let's execute the command. And I don't think we're going to use this dancing girl, so let's get rid of this.

Okay, so here we go. So Claw is going to ask us some questions. So which technology platform should we build this with? We can use basically HTML. We can use Phaser.

For games like this, I prefer to use Phaser. And if you don't know what Phaser is, you can always like ask Claw some more questions or open up a web cloud to ask this question. But Phaser from my experience is great for building games. Let's use Phaser. What scrolling direction and gameplay style?

I like top down vertical shooters personally. So I'm going to pick one. What features do you want? And this is actually a multiple choice. So let's actually pick all these features.

We have powerup system, boss battle, score, and let's do multiple waves too, right? So let's actually pick all these at once and uh submit. And there you go. Let's go ahead and submit the answers. And now Claude is going to write our spec for us based on our guidance.

So I'm going to quickly skip ahead until Claude generates a spec. Okay. So you see here that Claude actually wrote the spec for us. You know, I as a PM, I don't have the right specs anymore. And uh usually what I do now is I take a look at the spec together with my daughter, right?

So, what we're building is a classic vertical scrolling 2D space shooter. Makes sense. Core gameplay, smooth 60 frame per second. Okay, sure. Let's go down like a powerup system and so on so forth.

And what I'm looking for is actually the milestones because I want to make sure that it's building the right playable experience each time. So milestone one is a player prototype with some basic shooting mechanics. So it's going to set up the project. It's going to have the background. It's going to have the player ship and there's going to be some enemies from the top and moving downwards.

Okay, that sounds good. And then milestone two is the progression of power-ups and milestone 3 is the boss battles and polish. Now Claude has also linked all the pixel art assets that we're going to use which is going to be super useful. And yeah, overall this spec looks pretty good, right? Uh, usually when claw generates spec, it tends to want to build too many things at once.

So, usually I like to cut stuff out. So, for example, like smooth 60 frame per second. Who who cares? I think it's going to be smooth in anyway. But, uh, Opus and the latest models are so good that clock can actually frequently oneshot things.

All right, so let's actually just go ahead and get Cloud to build milestone one. Build Milestone one. And let's just say remember to use all the pixel art that you linked. All right. So again, I'm going to skip ahead to when milestone one is done.

Okay, we're back. That took maybe about 2 minutes. And uh when I'm doing this on my daughter while we wait for claw to work, usually what I do is, you know, I try to get her to look at some of the code, see how it all works behind the scenes, but usually she tunes out and does not pay attention until the game actually works. All right, so now Claude is saying, "Go to this link to play the game." So, let's actually go ahead and just paste this leg in right here. Local host.

And here we have our game. And let's see. I can move it over. I can shoot. The airplanes are coming.

Things seems to be working very well. Like some of the background seems kind of weird, but overall, we have a basic game working already in just three minutes of planning and two minutes of actually getting cloud to build. All right. So, let's go back to cursor and cloud code and let's ask it to now build milestone 2, which let's go ahead take a look at milestone 2. Milestone one core combat milestone 2's progression and powerup system.

Okay, that sounds good to me. Let's go ahead and build milestone 2. Now, let's skip ahead a few minutes and let's come back once milestone 2 is done as well. All right, so uh Claude has finished Mountain Bounce on 2 and there are some bugs here with the ships, but you can see there's more ship variety. There's screen shakes.

There's a health bar at the bottom. You know, things look pretty decent. And let's go back to cursor now and let's go ahead and ask to finish the game with mouse 3. So milestone 3 is going to add boss battles. I'm just going to make sure and double check.

What sprites are you going to use for the boss battles? just to make sure that it actually uh has art for that stuff. So, let's see what it comes up with. Okay, interesting enough, it's asking me some questions. So, let's take a look.

Use big name sprite. Why don't I say like uh search the legacy collection to see if you can find relevant art. Okay, because there just like a lot of uh art in here, and I'm surprised I cannot find other things for boss battles. All right. All right.

So, looks like it found a top-down boss folder. You know, sometimes you just have to remind Claude to look harder, right? So, it found a top down boss folder and uh it wants to proceed with milestone 3. So, let's go ahead and get it to do it. So, proceed with milestone 3.

All right. And let's see what it comes up with for the final game. Hopefully, there's no bugs. All right. So, it built milestone 3 now.

Took about 4 minutes. and let's play the game. So, wave one. Let's see. There's uh enemies to shoot.

There's powerups. Weapon up. All right. Now, we have a dual shooter. You know, I think there's like a problem, right?

The game is kind of boring. It's like too easy, right? There isn't really um that much challenge. The enemies appear one at a time. So, why don't we give Claude some feedback saying, you know, game is too boring, man.

Make the enemy numbers higher. make it more frantic. Also make the boss appear faster in level one and also fix some of the pixel art seems off. Okay, so this is not exactly super precise instructions, right? Like imagine basically you have a junior engineer or someone who's trying to build this game for you and you just kind of give me a feedback and let's see if it can actually fix everything based on this vague feedback that I gave it.

Okay, claw tells me it's all done. So let's play the game again. All right, so we have our level one and let's see if this is more challenging now. There's still some issues with the art that we can fix later, but you can see a lot more enemies are appearing. It's hopefully a little bit more frantic.

Let's get all the power ups. Shield. Great. What else is there? Speed boost.

Weapon up. Shield. Shield. Okay, we're uh in pretty good shape now. And I actually want to see if the boss even appears or not.

Okay, so I'm just going to keep playing for a little bit longer and let's see if the boss even appears. Oh, there we go. Warning boss approaching. Let's see if the boss and um you know what? I actually do not see the boss at all.

There actually is no boss. So, why don't we actually fix this? Here's what I'm going to do. I'm going to take a screenshot of this, copy it, and put it into clock hole. Just paste it here and say the boss doesn't actually appear and seems to have zero HP.

All right. and let's see based on that feedback if it can fix this bug. Guys, fixing this boss is more painful than I thought it' be, but let's see if it actually works. Now, let's actually uh So, what I did was I added a hotkey to just load the boss, right? Boss approaching.

There we go. So, here's the boss. There's the health points. And uh let's Yeah, looks like the HP decreases now. Oh, this boss is pretty hard, man.

I'm like dying. Uh, let's see if I can get it down to zero before I die. All right, lost the ship there. All right, but it's almost dead, I think. Let's see.

I wish there was some power-ups here. Okay, now it's getting really hard. Okay. Oh my god. Okay, I think I made this boss way too hard.

Okay, there we go. I managed to kill it before it killed me. But that was pretty fun. But I want to show you guys this. Okay, so this is the actual conversation I had with it to try to fix the boss.

And you can see here it's a pretty long conversation, right? And honestly with you guys, it probably took me like 10 minutes to fix this. And um if you burn this with your kid, they're not going to have the patience to fix bugs. So maybe get them to watch YouTube or something while you fix the bug. But what was the bug?

Right? So it's important to actually learn why you're vi stuff even for yourself, right? So I asked it like what was the bug? And the bug was they were storing the boss HP directly on the phaser object. And um yeah, phaser sprites can have their stuff modified by the phaser engine.

So we should move HP to a scene level variable and so on so forth. And maybe I understand maybe like 30% of what they're saying here and I can always ask more questions. But again, if you encounter a gnarly bug, don't give up, okay? Just give it instructions. Try to fix it.

paste images into cloud code as examples and learn after you finally fix the bug why the bug happened in the first place. Okay, so we have a great game now and now our last step is to clean up and ship the game, right? So how are we going to actually ship the game? Here's the thing. You should have a GitHub repo and you should create a new one.

Let's go to repo and let's just create a new repo and let's call it space shooter game to match the same folder as our local folder. Right? And let's just hit create repo here. So now we have a brand new GitHub repo. And by the way, if GitHub is intimidating to you, it really isn't that intimidating.

Just like using clock code isn't intimidating. Like you can just set up a free GitHub account and just follow the steps I'm showing here to create a new GitHub repository. Okay, so basically just like a folder that lives on GitHub. All right, so now what's important here is we have this link here, right? So let's go ahead and copy this link and let's go back to Clock Hold and be like commit this to this link right here.

So now Clock Hold is going to do all the work for us. It's going to do the pull request. It's going to do everything here. And uh let's actually skip ahead and come back once Clost has finished uploading our files to GitHub. All right.

So, Clock host said it's done. Let's push it to GitHub. Let's take a look. Uh, let's go ahead and refresh this. And there we go.

Now, we have all of our files, right? So, we have our source code and we have our legacy collection here. Probably what we should have done was to actually only include the pixel art that we actually use in our game, right? But now, I want to show you how to actually get a link to play the game. So, you can use GitHub pages, but lately what I've been doing and the easiest way to do this is to make a Versal account, versal.com, and just sign up for a free account.

And let's go ahead and hit add new here. And let's go ahead and hit add new project. All right, so it's saying enter a Git URL to deploy, right? So, our get URL is right here. So, let's go ahead and copy right here and paste it and hit continue.

And uh there we go, our new project. And let's just hit deploy. Okay, so now Verscell is going to generate a URL where hopefully anyone can play our space shooter game. All right, so Versel has deployed a game and let's see if this link actually works. Click on this and there you go.

Now anyone can play our space shooter game and I can also link to it in the description. So let's go ahead and play it and see if it works. We got our wave. Still have to fix that ship. It looks kind of weird.

We got our weapon ups. And let me actually get some weapon ups. There we go. Let's trigger the boss. Remember, we still have our hotkey Z to trigger the boss.

So now I got three boys. Man, now you're going to die a lot faster than before. All right, it's getting hard. It's getting hard. Okay, but it's going to die soon.

There we go. We killed the boss. And uh level complete and the next wave will start. And you can see the backgrounds changed, too. So, we just built a retro pixel shooter with Claw Code in five steps.

First, we set up the project. We found the game assets. We drafted our spec with Claw's help using ask user question. We had three milestones for Claw to build. We built and iterated it.

We ran into some pretty gnarly bugs with the boss, but we got it working because we didn't give up. And finally, decided to ship it. And now anyone can play our game. And again, if you want to play it too, it's right in the description. So, here's the thing.

The pixel pack that I use has art for way more than space shooters. You can build Castlevania style platformers. You can build cyberpunk shooters, underwater adventure games like I showed you before with my kid. You can even build top down RPGs. And what's the takeaway from this tutorial?

Look, a lot of people feel intimidated by Clocko, by Terminal, by GitHub, by Versel and all this stuff. But it really just comes down to chatting with AI just like how you chat with AI in Chat GBT Claude or Gemini. Don't overthink it. You have this AI who's here to help you build a game. So pick a game idea, find some free pixel art or use the one that I'm using and just start prompting.

All right, I've linked the game and my GitHub repo below so you can fork it and continue to improve the space shooter. But I hope you get inspired from this tutorial to go build a game on the weekend with your kid or your spouse or anyone else. It's incredibly fun. And I'll leave you with this. Right now, we live in a world where creating is actually more fun than consuming.

You know, it's way more fun to vibe code this game than to watch some slob on Netflix or YouTube in my opinion. Uh except for my interviews, of course. So yeah, go ahead and build a game this weekend and be sure to like and subscribe to this channel for more practical, no [ __ ] AI tutorials and interviews.
