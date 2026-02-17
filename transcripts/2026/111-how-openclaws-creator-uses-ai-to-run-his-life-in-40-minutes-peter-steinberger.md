---
title: "How OpenClaw's Creator Uses AI to Run His Life in 40 Minutes | Peter Steinberger"
guest: Peter Steinberger
publish_date: 2026-02-01
youtube_url: https://youtube.com/watch?v=AcwK1Uuwc0U
channel: Behind the Craft
keywords:
- coding
- leadership
- ai
- execution
- growth
---

It's just like having a new weird friend that is also really smart and resourceful that lives on your computer. I was still in Morocco and someone sent me a tweet of a bug and I literally just made a picture of the tweet, posted on WhatsApp. It read the tweet, it understood that there was a bug. It checked out the Git repository, it fixed it, it did a commit and then it replied to the person on Twitter that it's fixed now. This will blend away probably 80% of the apps that you have on your phone.

Why should I use my fitness pal to track food when I have an infinitely resourceful assistant that already knows I'm making bad decisions and I'm Kentucky Fried Chicken? Those things are so resourceful, although in a scary way. It's like unshackled JGBT. A lot of people don't realize that if you give an AI access to your computer, they can basically do anything that you can do. All right, welcome everyone.

My guest today is Peter, creator of Claude, an AI assistant that you can just chat with in your messaging apps to get stuff done. And today is Peter is going to show us how to use cloud. And also Peter has a lot of really great hot takes about AI coding that I'm really excited to dig into. So welcome the other Peter. Peter, thanks for having me.

Great to see you. So why don't we start by talking about cla. So what exactly does cloud do at a high level and uh why why is it a lobster? [laughter] Yeah. So, so maybe I have a little bit of a backstory like when I when I came back from my retirement, let's say it like that.

I kind of wanted wanted a way to just check up on my computer from my phone cuz I I fully jumped on this on this V boarding trend and then you know like your agents might run for half an hour while you while you eat or they stop after 2 minutes because they have another question and then and then you go back and you're like annoyed. But I kind of I kind of didn't build it because I assumed all the big labs would do that anyhow. it felt like such an obvious thing like like something where like kind of a new new kind of operating system almost um but didn't happen and then it was like November and it still didn't happen. I'm like okay I'll try something small and and the small thing was basically hooking up WhatsApp to cloud code. So, so, so you send a WhatsApp message and it would literally open the binary like with the the prompt and like return you this thing like very simple was like built in one hour and it kind of got a life of its own and now here we are.

It's like I think 300,000 lines of code. It does every messaging platform on Earth. Not everyone, but like we're getting there. And I think it it's kind of where things are going in the future. like everybody will have an AI that is like super powerful and like follows them through their life.

Um, turns out if if you give an AI access to your computer, they can basically do anything that you can do on your computer. Yeah. And it's got to a point where like you don't have to sit there and babysit it, right? You can just give it some, you know, prompts and commands and it will do it thing for you and you can check it work and then that that's it. You know, you have to set a computer.

Yeah. So when I when I built it, I I feel I feel this project is like as much exploration as it is like technology because it's it's a little bit of a new category and then I was on a birthday trip for one of my friends in Morocco and I I catch myself using this thing all the time. It's like, hey, where are we going? like asking for directions or like or like tips for for restaurants or I don't know there was like one morning where someone sent me a tweet of a bug and I just literally just made a picture of the tweet posted on WhatsApp. It it read the tweet.

It understood that there was a bug in one of my repositories. It checked out the git repository. It fixed it. It did a commit and then it replied to the person on Twitter uh that it's fixed now. And I'm like really this is nice.

And then one day I was I was walking around and I didn't sync and I just sended a voice message, you know. I didn't I didn't I didn't build in support for voice message and I was like it showed me a typing indicate. I'm like oh I wonder what's happening now. And then it just replied to me as if nothing would have happened and I'm like wow how the f did you do that? And it was like yeah I saw a file but there was no file ending because I didn't build it.

Mhm. So I looked I looked at the at the header of the file and it was like ous uh some some audio file format. So I found ffmpeg on your computer and I converted it to wave and then I looked for visper.cpp but you didn't have it installed but I found this openi key and then I used curl to send it to openai's API uh and it got the transcript back and I replied to you. I'm like wow that's amazing. Yeah, like those things are so resourceful although in a scary way.

Um, but that was kind of like the the the moment where it clicked for me is like, oh yeah, this is really powerful. This is much more interesting than using JGBT on on the web because it's like it's like unshackled chbt and I think a lot of people don't realize that that those things like cloud code, they're not just good for programming, they are very resourceful for any kind of problem. Yeah. You just got to give it access to like, you know, your computer and like, you know, be able to find stuff, right? So, you just have to give it tools.

They'll become very resourceful. Yeah. So, so, so over the last few months, I I kind of built up my my CLI army because what are what are agents good with? Calling CLIs because that's what they train for. So, I've built like CLI for accessing all of Google, including like the Google Places API.

I built one that that that makes it very easy to look up memes and gifts. So you can also like reply with some memes. [snorts] I did I did a bunch of experiment. I even built one that visualizes sound because I wanted it to like experience music. Um that that goes a little bit more into the art direction.

I don't know if that makes any sense, but anyhow, it's a lot of fun. Like like I have like a whole list. I built one that that that hacked into my the food delivery here. So So it actually tell me how long it takes until my food's there. I have one that that that reverse engineered the the eight sleep uh API so it actually can control the temperature of my bed really and real quick like when you build all this stuff you just you're just getting AI to build this stuff or what's going on the funniest thing is I I was in my my old company um I was very very good at iOS and and Mac OS like the whole Apple ecosystem I did it for 20 years I'm like very much an expert in there but also when I came back I I I built a project where I'm like I'm kind of sick of Apple gating everything and it also would make a lot more sense to build it as a web app because it's kind of a thing that it should be in a browser and and should be accessible and if I do it as a Macup again it's like we'll have a very limited set of people that can use it but you notice I see this with a lot of engineers where you're really good at one thing and then moving to another technology is just so painful because then you feel like you feel like a sorry for the word an idiot and [snorts] and you have you look up every little things like what's a prop or like how do I split an array cuz because you understand all the concepts but you don't necessarily like know the syntax.

So that that's kind of like how I felt when I moved from from Objective C and Swift to to JavaScript. Like I know JavaScript a little bit, but I never really built something big in Typescript. And then it's just it's not even that it's hard, it's just painful because you have to look up all those things and you're just so slow. And then and then with AI all that all that melts away like you can you can still apply your system level thinking your like how do I build and structure bigger projects and your taste may I say or like your which dependencies do I build on um all those things all these things is still valuable and you can like much easier move that from one domain to the other. Yeah.

And and that felt like a superpower. Suddenly like I I feel like I could build anything. Languages don't matter anymore. My my my engineering thinking matters. Yeah.

Because like I was trying to worry about like whether you have a parenthesis here and there is is lame, right? You don't have to worry about that kind of stuff anymore. This episode is brought to you by Granola. If you're in backtoback meetings, you know how much work it is to take notes [music] live and clean them up afterwards. That's why I love Granola, the best AI meeting notes app in the market.

Here's how I use it. Granola automatically takes [music] notes during a meeting and I can add my own notes too. After the meeting ends, I use a Granola recipe to extract clear takeaways and next [music] steps in the exact format that I want. Then I can just share notes directly in Slack with my colleagues or even get Granola to share her notes automatically. Honestly, of all the AI apps that I use, Granola is the one that saves me the most time.

Try it now at granola.ai/pater and use the code Peter to sign up and get three months free. That's granola.ai/pater. Now, back to our episode. But, but dude, let's let's go back to Claude like like the the thing that you built. Maybe you can um screen share, maybe you can show like maybe you can show like how people can install the thing first like it like do you have to be super technical to use cloud or no?

Right. You can just install it and then get it to work. Yeah. Um yes, yes and no. So fortunately and also unfortunately this project attracts a lot of uh people that don't have a lot of clue about technology because it it lends away all these all these layers that make it complicated, right?

You if you use cloud code, you work in a terminal, you you kind of have to think about the context space and what folder you're in and like it feels very techy. like talking to a thing on on iMessage or WhatsApp or Telegram. You do it with your friends and now it's just like having a new weird friend that is also really smart and resourceful that lives on your computer. Yeah. That makes the whole technology very approachable.

You don't think about, oh, what model do I pick or what? It just works. Mhm. And then that's that's that's kind of the idea. It's also like that good and bad part because of course with a lot of power comes a lot of risk which is also unsolved like this thing is access to your computer.

So yes it could do bad things on your computer. If you tell it to like I don't know delete all my files in my home directory. It would probably like ask you are you sure? But if you if you like if you like keep saying yes yes yes it will probably comply and probably also delete itself and crash. [laughter] Yeah you got to be careful.

Yeah I I'll let me share my screen so you see. So in it's written in in TypeScript. Mhm. So it runs it runs everywhere. Uh even on Windows you can just go on our website clogbot.

Yeah. And there's a handy oneliner. Looks very scary but it's every everything's open source. You can check everything including the website. Mhm.

So so this is the easiest way to install it. It works on Mac OS Linux. It also works on Windows. It's time to turn terminal right and then it'll start installing. Yeah.

You can also install the mpm for people who understand that ecosystem and I think something that that I did that I haven't seen in a lot of lot of project is also it has a hackable install again a simple way and like the more manual way where you basically check out the git repository and then and then launch it from the git repository which is to to be fair is like the most fun way to use it because if your agent can read its own source code of its harness it can literally reconfigure and reprogram itself and then restart and then either crash or have new powers. Um, [snorts] okay. Like this I think this is one of my my superpowers where I got a lot of people participate in the project and like send me pull requests that never did a pull request. I mean sometimes that also shows um but I but I see pull requests more often as a as a prompt request. Yeah, it's enough to like understand the intent and then and then and then a after we install it like do you like how do you hook it up to a messaging app?

The nicest way is probably right now just using this one lineup and then it will like greet you with some sassy stuff and and try to configure everything up. Got it. In install the package and then you and it just guides you through and you just you can hook it up to do any of the common messages. Okay, that that looks good. It's working.

Yeah. And then you can say plbot. It will do it automatically if it's a clean install. But now I have to type in on board. Got it.

And basically then you have like you can enter a model. You can Oops. All providers. Let's say we go with some tropic. Probably a new one.

Then you can set up Telegram, Discord and then it will guide you through the rest. You can like set up skills hooks and then do you have to give it your anthropic API key? It works with with any model. Yeah. Although you know they're in industry like Anthropic and Open are kind of like leading.

Yep. It works with API keys. It works with subscriptions. Okay. Although although there's been there's been a little we we we added support with it because it's kind of like what everyone does.

Yeah. But I don't think Entropic likes it anymore. So I would recommend using using an API key or going with another model. There's okay. Yeah.

The the main problem is like OpenI works well, but it's just not as funny. There's something special about Opus that makes it really really fun. Oh yeah. Like like the personality. Yeah.

Yeah. There's I don't know if if you've read this article about how they put a soul into the model. Yeah. And then people rediscovered it by like feeding it blocks of text and letting it like continue. And eventually they they re they they they squeezed out the the text of the soul that the model wasn't even aware it was being trained on.

Is is a really interesting story. I don't know. I feel that has has something to do. But this is the first model that is actually funny to use. Like I I built mine so that Yeah.

It can roast me and it probably doesn't know that it's on camera right now [laughter] and and it's it's going to roast you based on what it has access to all your computer stuff, right? So it's Yeah. Here. Yeah. All right.

You asked for it. You sold the wildlen world to find yourself did Sarah. We tried everything and your bigger relation was I should build more software. [laughter] You're so obsessed with the alto is that you literally built yourself a friend because debugging code is more fun than dating. And let's be honest, the only reason I existed because you needed someone who'd listen to your chainway hook takes at your Amazon judgment.

Wow. Yeah. Now go kill that podcast. So So I I hooked it up to pretty much everything on my computer. It it can read my emails.

It can read my calendar. It can access to all my files. It can control my lights. I I use Philips who? Yeah.

It it can control my sonos. So like I can I can tell to wake me up in the morning and I slowly like turn up the volume. It has access to my cameras. It was it was funny like I when I built access to the cameras I I told it like watch for strangers and then it told me in the morning like Peter there's someone and I like I watched in the whole night and it made like screenshots the whole night of like my couch because it was like there was like the camera is pretty blurry and it looked like someone was someone was sitting on the couch and it assumed there was a stranger sitting on my couch the whole night. Wow.

But yeah, I slowly it it has I'm just thinking like in my place in Vienn it also has access to my my kx so it can actually control every part it could literally lock me out of my house like in space they say it's like oh can't do that okay how did you hook all this stuff up you just ask cloud to do it or or what you just yeah yeah literally you know you know there's this thing where we have skills so usually you you talk to it will these things are really resourceful so it will like figure out an API Right? It can Google for it. It can find your keys on your system. You can give it keys. And people use it for everything.

People build like a a skill to so go shopping for them on Tesco. Um or buying stuff on Amazon. I I I let I let it check in my flight from British Airways. And this is actually I don't know if you've I mean you've used check in sites. This is I feel like this is almost like the hi test.

It was a touring test, but like steering a browser to check you in on an airline website is like the ultimate test and and and then the first time I my integration was pretty rough. So it took almost like 20 minutes that was still in Morocco and everything was very much hacked together. Mhm. And then it finally managed but it actually had to had to find my passport in my file system. It found it on Dropbox, extract a key, put everything in it correct and it finally checked me in and I was like watching it and sweating.

Wow. Yeah. Wow. But now it works much better. Now it's like it it does it within minutes.

So it can it also happily clicks the I'm a human checks on the browser because it literally just it it literally just controls a browser on it has its own little computer over there and and just kicks around. So So it's like really really difficult to detect from all those antibot systems because it it doesn't feel different from a human in in those patterns. Can you maybe like can you show us like just a couple more use cases like uh can you maybe have it turn on the light or show some use cases from other books? Yes. So I started collecting because I feel I'm so I'm so bogged down actually building it.

By far I'm no longer the the most creative one who actually use it. So people people hooked it up to their messaging system so can actually reply uh not just as not just to you but to everyone. Uh and you can also hook it up into group chat which is even more fun. There's a lot of people that use it as a as the family the family member almost. Um yeah, send me reminders, create GitHub issues, sync with Google Places, or every time you make a bookmark on on Twitter, it will like capture bookmark and add it to your to your to-do list.

Yeah. Keeping track of costs. Um some people I I I programmed something in to like remind people that they sleep enough. So like they always get like bitched it when they're up at night from their bot. So it can help you track your sleep.

It can access your your fitness watch. Uh it it has its own little one password vault. So if I want a password shared, I move it into its own vault and it can access that one. Um because it you still want to have some boundaries. I mean there people give it the credit card.

Yeah. I don't know about that. [laughter] Yeah. Um it can do all those things like research, creating invoices, managing managing your email. These people are like enthusiasts, right?

like they they've really customized it to do whatever they wanted to do. Like how about for like dude like how about for some just just download this thing just download for you know fresh fresh install and what are some like really common use cases that I can get get to do like just like manage my calendar or you know stuff that doesn't delete my computer what are some uh safe things to start with. It's funny because everybody takes a very different path. There's like people who like install it and immediately immediately build an iOS app with it because it's also it's also a coding agent. It can do anything.

It can spawn sub agents. It can it can either code yourself or it can like control cloud code or codex and ask them to code. Yeah, this guy started immediately like managing Cloudflare. This one was great. Week one set up for my family.

Week two, set it up for some non techy friends. Week three, we're building cloud for work. I hope I hooked up one of my my non- techy friends and like he started sending pull requests. He never did it in his life. Yeah, fitness is is is a big thing.

Okay. So, so basically it's it's kind of like u you really have to I guess way to use this thing is just to think about what's causing problems in your life and how you can get this personal assistant to help you to help you streamline everything. I don't know if this is the project that's going to be, but if you think about it, this will blend away probably 80% of the apps that you have on your phone. Why should I use my fitness pal to track food when I have an infinitely resourceful assistant that already knows I'm making bad decisions and I'm Kentucky Fried Chicken. So, so it will probably like remind me if I forget tracking the food.

I can just send a picture and it will store itself in the database and and calculate it and and and roast me that I should go to the gym because I'm like way over my calorie limit. Yeah. Why do I need an app to like set up when my my bad my ASIP should work or not? Because it just has API access. It can just do that for me.

Why do I need a to-do app when it just tracks my to-dos for me? Why do I need an app to like check in on my flights when it can just do that for me? And it's like such a more convenient interface because I just I just talk to a friend and because it has so much so much context, it doesn't need so much custom prompting. like why why do I need a a shopping app when it literally can like recommend me things and do all of that for me? So I feel I feel there's a whole layer of apps that will slowly melt away because if they have an API these are just services that your AI will do and in a year I don't know I think actually this year will be the year where a lot of people will explore it more and like get their uh AI assistance from all those big companies.

Yeah, I think uh yeah, why why click on these little little self-contained little apps when like yeah, this assistant has a bunch of capabilities can just do everything, right? Just connect it to everything. And I guess the way you connect it to everything is just like you just you send it a text message or something and then it's like, oh, can you do this? And they're like, oh, I need to do some re research and then it just takes care. You just kind of go back and forth with it and and make it have happen, right?

Yeah. And and then and then it it writes a skill and it it remembers. So part of what makes it so interesting is that it has it has persistent memory. it will learn about you and it will update it yourself. So it it so you the more you use it, the more you customize it and the more powerful it gets because because okay maybe the first time you have to like guide it a little bit but then it will it will create a skill and then next time you can just mention it.

Next time it it I need to like check in my flight. It will take like two minutes because it it exactly knows all the quirks of the website. Yeah. Because it did it before and it made notes. Got it.

Yeah. Yeah. It's like teaching someone to just learn something and they can do it easily the ne the next time. Yeah. Yeah.

All right, man. Let's talk about another topic. Let's talk about, you know, you came back from retirement to build this thing and uh you have very strong opinions about AI co coding like some pretty hot hot takes. So, let's talk about let's talk about some of those. Like you wrote this post that I really like called just talk to it and then well like you know these days everyone on X is writing about like all this fancy [ __ ] right like all these like you know hook skills and all this kind of stuff.

So, what's the gist of that that post? [laughter] Is it just just talk talk to the AI and figure it out? No, but but I work a lot. I build a lot of things and I I love Twitter as well, so I'm very active there and I just see so much. I almost I I I kind of call it the agentic trap because people discover that, oh, those agents are amazing, but they would be better if they could do a little bit more.

And then they really fall deep into this rabbit hole. And I've been there myself where you build really sophisticated tools to like try to accelerate your your workflow, but in the end you're just building tools. You're not actually building something that really brings you forward. You just have this, you know, part of the problem is that it's so fun. Yeah.

like like when I when I started pretty early, I I worked on VIP tunnel to have access of my terminals on my phone and I I was in this rabbit hole for two months until I it was so good that I was out with my friends on and instead of like joining the conversation in the restaurant and I was just like vibe coding on my phone and I decided okay this I have to stop this just for my more for my mental health than for anything else. Um, [snorts] and these days you can build everything, but you still need ideas. So I see I see so many managers for cloud code or codecs or like orchestrators or other little things that have the illusion of making you more productive, but yeah, really aren't. I mean, like the the latest thing that that I just had I just cracked about is like like Gas Town. Um, it's like a really sophisticated orchestrator that is like also very broken and doesn't really work where you like run like run like tens or 20s of agents simultaneously and they all talk to each other and like try to split up and there's like there's like watchers and overseers and a mayor and pcats and I don't know what else really there's a mayor.

Yeah, in Gaston there's a mayor. I mean I call it slop town. Um or like or like this whole trend of Ralph thing where you just like you you give the AI one little thing and then like you write in a loop and then if one little thing is done you trash away all your context and you start again. Um like the ultimate token burn machine. Yeah.

And then and then and then can you can create code and run all night and then you have like the ultimate slop because what those what those agents don't really do yet is have taste. They they are really they are spiky smart and and and they're really good at things, but if you don't if you don't navigate them well, if you don't have a vision of what you're going to build, it's still going to be slop if you don't ask the right questions, it's still going to be slob. And I don't know how other people work, but when I start a project, I have like this this very rough idea what it could be. And as I built it and as I play with it and as I there is a feel it I my my vision gets more clear and like I I get like I try out things some things don't work and I evolve my idea into into what it will become and that's that's like my next prompt depends on what I see and feel and think about the current state of the project. Yeah, but if you if you try to put everything into a spec up front, you miss this kind of like human machine loop and then I don't know how something good can come out without having having feelings in the loop almost like like taste.

So, so it was like somebody somebody tweeted like, "Oh, look at this mech app. Like it was fully Ralph." And I replied, "Yeah, it looks Ralph." like no offense but it looks Ralph because like you could see clearly see that like no same person would design it that way. Yeah, it feels like it feels like some some people are just like uh actually building these things not for the apps themselves but to prove that they can get it to run for like 24 hours like get AI to run for 24 hours without intervention, right? It's like selfmastery kind of kind of thing, right? You're just trying to prove that you can get AI to run super long time.

It it's like a it's like a size comparison context without seeing the other word in a way. And I I've been guilty a little bit of that myself. Like I also had like a loop for 26 hours and I was very proud. But it's that's it's a vanity metric. It doesn't that makes no sense.

That makes no sense. And like just because you can build everything doesn't mean you should or that it's going to be good. But then again, this this face of I'm just playing. I'm just like literally I'm building for fun. It doesn't matter if it's going to be used is incredibly useful because that's how you learn, right?

That's how that's how we learn to program. And prompting is just a different skill. Sometimes I see people that they're like a little more on the on the AI skeptical side. So they ignore it for a year and then they spend one day where they they evaluate the models and then they do a blog post and then they write like a short prompt and feed it I don't know into claw web to to make him make him an make an iPhone app which like is completely underspec and the model does its best to deliver something and then like it doesn't compile because they they build it on the Linux machine where there's no compiler for that you know and then you're like oh AI is not good and then they dismiss the whole topic for a year. It's like that's that's not how it works.

Yeah. You need to play to to to understand how those little monsters work. You need to understand a little bit their language, their way of inference of thinking and then and then you get progressively better at it and and then your output will be better. Yeah. You have to uh you have to be persistent, right?

because sometimes it doesn't work properly and you have to fix all the bugs and then and then if if you just keep playing with it, you develop this like I guess product sense or whatever of actually learning how to talk to the models and learning what they can do. So I mean partly it's it's being really weird because they're adopting some of the language. It's like I'm I'm thinking of like or you weave a feature in kind of like you like a like a in German it's fen a twin a tw or you you run the gate which like a linting and testing and building and it looks like a a big line in the terminal which is like the gate. So so I'm like we didn't run full gate. Um [snorts] sometimes things doesn't work out and then you can just ask why did why did you not do and then it will tell you you said this and this and I assumed this and this and it's like oh yeah I I messed up on the language or I was unclear like if you just tell it build me a Mac app it will probably assume that you want you want to support a lot of old operating systems because the majority of software does so it will API I I found that asking it to like just ask a bunch of clarifying questions to then make you clarify stuff helps a lot.

Yeah, it's it's also funny because I'm I'm more I like Codex modern cloud code. I think it's it's the better model even though it's it's it's it's incredibly slow, but it's soro and things work. And people complain that there's no plan mode, right? Yeah. and and and and my joke is always plan mode was a hack that Entropic had to add because the model is so trigger friendly and would just run off and build code if [laughter] you use in in the in the latest models especially like like GBD 5.2 to I'm just having a conversation.

I'm like, "Hey, I want to build this and this feature. It should do this and this and this and maybe drag in this control tool like I like this. I like this design or this and this. Give me options. Just say let's discuss.

Give me options." Then they have a conversation with it and and then and then the model will propose something and they're like I mean I usually don't type I talk to it. Yeah. And staying on brand. Do you do anything to um manage the context? Once you have a conversion with it, it can get really long and it can get confused.

Do you try to like do you make it manually compact or summarize stuff? I feel that this is also like old old patterns. This this was a this was very much a problem with with cloud code still is to a point. Codex is so much more the context lasts so much longer. Even though like on paper it's maybe like 30% more but it feels more like two or 3x more.

I think I think a lot of it has to do with like the the internal thinking. the internal thinking of of GPD models is really effing weird. But yeah, like the for context management, I think this was much more a problem in the earlier models. Now most of my features fit into one window. So the whole discussion and building happens simultaneously.

Okay, got it. And that that works fine. Like sometimes if if it's a really long thing, I create a new one. You want to like codify it in a file. Mhm.

But this is much less of a problem than it than it was before. That's again like the space evolves so fast you just have to try things. Yeah. Got it. Okay.

Got it. So basically so just to summarize like basically when you add a new feature to cloud or what whatever you're building like maybe just walk through the steps like first you explore explore the problem and the solutions with the AI and then you do you actually make a plan at all or or just go it's even better like I you know I I built this project and which is kind of like a mix between Jarvis and her her. Okay. Okay. the movie.

Yeah. Yeah. Yeah. Um but it it's very difficult to convey how it makes you feel and how useful it is just by talking about it. Yeah.

So on on Twitter it got me very muted traction. I'm like I don't get it. Like everyone I show it in in person gets super excited because they see me interact with it and and like showing off all the cool things but it you you can't get across the same thing on a picture when I talk about it. So eventually I I created a Discord and I just hooked up my bot to Discord so that people could interact with my eye that has full access to everything on my system with my my private memory on a public display. the most nuts thing that I ever did I think and then people got hooked and now and now like people always ask me there oh can you build this feature or there this and this bug and most of the time I now approach it by making a literal screenshot of the conversation dragging it into the the terminal or just copying the text depending on how it is and just ask hey let's discuss this because I'm lazy I don't even have to type anymore I just like copy in Discord conversations um or the same also when people ask hey do you support this and this or how to do this this I'm just like can you read the code and write a new FAQ entry and it does that so that's so these days it's actually how I start building features most of the time but like reading on discord and and and and seeing where people have pain points [laughter] oh my god so you just paste the paste the conversation and you just talk to AI about it and you figure out what the right solution is partly that partly also I I have a have a scraper so every at least once a day I scrape the the help section and and ask the model what are biggest pain points and then we we fix them.

And and do you do all the fancy [ __ ] like do you have like multiple agents and like you know you have those crazy skills and stuff that you run or no you just go I have very I mean I most of my skills are actually personal life skills like food tracking or buying groceries or like that kind of stuff for coding very little cuz you you don't need that much. I don't use MCPS or or any of that crap. Um, I don't I don't believe in in this big orchestration systems because like we talked before, I I feel if I'm in the loop, I can build a product that feels better. Maybe there's maybe there's ways to like build it faster, but I'm already so fast. I'm mostly limited by thinking about it and sometimes a little bit by waiting for Codex, but mostly it's it's it's my thinking that's a limiting factor.

Um, I just I just used a bunch of terminals like split screen. Mhm. I don't use work trees because again I feel it's just like unneeded complexity. I just have like a few checkouts of the repository like cloud pot one 2 3 four five and [snorts] then like either they are free or they're working on something. either I'm like exploring something or like I'm building something or I'm fixing something and then when it's done I test it locally and then I just and then I push it to main and then I sync it up.

So this is it feels a little bit it also feels a bit like a factory if they're all busy. But if you only work on one, it's very hard to actually get into the zone because it's just too slow and you have to wait. Yeah, you have to wait for it to do you can only [ __ ] post on Twitter so much. Uh, [laughter] so I I feel I need multiple ones to to really keep me hooked and get into the same flow state that I had when coding just that I I'm like insanely more productive. D I don't know if you play like the real-time strategy games before, but like it's kind of like yeah, you you have like a squad of people attacking and then you kind you kind of have to monitor and manage them, right?

And that that has kind of taken it. my business partner from my my previous company. Yeah. Also totally got hooked on on Clubbot and he's he's more from the business side. He was a lawyer in a past life and he's now sending me pull requests which is like insane in its own way.

How AI made like gave people superpowers that are not that technical to still build things is amazing. I know I know there's a lot of push back because yes, this might not be perfect, but I treat pull requests more as prompt requests because they convey the idea and most people just don't have the same system understanding. So they not be able to like derive the the model in a way to give optimal results. So I just rather I just rather have the prompt like the intent and just do it myself or if they send the PR I will extract the the the the intent out of it and just rebuild it myself or sometimes I base it off. I I still mark them co out but very rare that they actually merge code directly.

Yeah, that makes sense. Okay. Um All right, man. Well, I mean like um I guess the take away from this conversation is like my take away at is like um yeah, don't don't get crazy with the slop generators. Just actually have the human in the loop because the human is still your brain, the taste and everything, right?

You have to guide it. Yeah. Or like don't find your own path, you know, like some people always ask me how do you do that? How do you do that? You got to you got to explore.

You're like Yeah. It will take you a while to be good. You have to make your own mistakes. That's that's how you learn with everything in life. And that's how also how to learn those things just that this space is evolving very fast.

And where can people find uh cloudbot? Yeah. Uh cloud.bot. Uh it's also on GitHub. It's a cloud with a W.

CL L A WD, right? Yeah. Yes. Yeah. Correct.

[laughter] Yeah. Like like the lobster claw. Yeah. Yeah. Got it.

Thanks so much, Peter. This is a super great conversation. Um I I need to give Claude a try myself because Yeah. I I don't like sitting on my computer to talk to the AI. I like to just like be on the go and just like give it instructions, make it do stuff while I'm out with my kids.

Like that would be the ideal way for me. So, it's great that you build something like that. I'm looking forward to to see what what you what your opinion is on that. I think you're gonna like it. All right, man.

Well, it's great chatting with you and uh I think we'll stop right
