---
title: "Full Tutorial: Build with Multiple AI Agents using Claude Code in 40 Minutes | Kieran Klaassen"
guest: Kieran Klaassen
publish_date: 2025-07-20
youtube_url: https://youtube.com/watch?v=Z_iWe6dyGzs
channel: Behind the Craft
keywords:
- coding
- ai
- ai-tools
- execution
- leadership
---

While we've all been doing Vibe coding, Kieran has gone to the next level to manage multiple AI agents to code for him at the same time. It's like I'm a manager and I have like a team of people that are very capable. The work when doing software or building stuff is not code. It's way more. It's research.

It's product marketing. It's even understanding what you should build. Coding with agents is super helpful for people that actually build software. If your directions are good, if you're clear in your communication about what problem needs to be solved and how to go about it, they can deliver results to you. Running parallel is a good trick where you can run three things at the same time.

Let's get right into then. Let's go. Okay, welcome everyone. My guest today is Kieran, the lead engineer and general manager of Kora, a beautiful AI email assistant. And uh you know, while we've all been doing Vibe coding, Kieran has gone to the next level to manage multiple AI agents to code for him at the same time.

So I'm really excited to get him to show us exactly how this works uh by using cloud code and AI agents. So welcome, Karen. Thank you. Yeah, I'm really excited. I love everything related to agents.

I love everything related to AI and I love building things and I've been building this product Kora for almost a year now. We just launched two weeks ago uh to general public which is really cool and we have had many people say I love this product and a few that say I hate this which I think is the best product. Yeah, you want to have an opinion. And what I've learned is like I I really pushed myself to build alone. Like I've done VC backed uh like VP of engineering companies before where I was the VP of engineering just did the team and all the things.

And there's a time now where you can build stuff in a smaller team and that's really cool and I'm very excited about what you can do and like I've been pushing myself how far can you go like when does it break? Where does it work? And especially in the last weeks, it's really special. There's another step up again, which is like working in parallel and using agents to do long running tasks. And yeah, like let's talk about it.

Let's see what that means. And uh yeah, hopefully we can show some code as well uh like how to do that and share some workflows. So, you know, I've been doing a lot of quoteunquote vibe coding of cursor and just like watching it generate code and you know, debugging stuff, but I think I I think what you're doing is a little bit different, right? So, maybe you can just talk a little about that at a high level first. Yeah.

So, yeah, like vibe coding, this is something that started maybe a year ago like or like I was vibe coding a year ago and then it got maybe the name vibe coding started this year. But it's like you you have an idea and you say, "Oh, I have this idea like can you start it?" And you see something and you get feedback and there's this feedback loop where you kind of collaborate with the AI in like a tight feedback loop and create stuff that you you would take like that would take weeks or months before you would not even be able to do because you don't have the coding skills. So that was like the first step where and and that's yeah that's the vibe coding. what agentic coding is like it's kind of more like having a colleague like it's like I I'm a manager and I have like a team of people that are very capable and like I give a spec or I give a like a larger piece that needs to be completed and hand it off to an agent and the agent will actually complete that. So the feedback loop is less tight but if you do it well it can be very very powerful because imagine there are like five agents or people every two seconds say hey I did something what do you think like that doesn't work in parallel and the mind sh like the the the change with the new models with like clot 4 and opus is they're good at following directions so if your directions are good if you're clear in your communication about what problem needs to be solved and how to go about it.

They can deliver results to you. You're still giving feedback, but you're giving feedback on a pull request or on like a larger change. And you can also give feedback on the research. So like there's like these steps you need to go through. It's not like let's just go.

It's like you you actually need to think about what you want to build and that that is just like traditional software engineering like what problem are you solving and like if you don't know what you're solving like the AI doesn't know what to build. So it's like that's that's kind of the change. So uh coding with agents is super helpful for people that actually build software that want to get work done. And I would say this applies for everyone even like non-engineers. I have a friend and he's not a techie at all and not really an engineer but he's he's very interested in learning new things and I said just try cloth code.

He was like terminal what is that like like very scared. And I said no it's not too bad. It's just text and you speak to it or you type and it does stuff and like just see what you think what it does like do you like it or you don't and he was like holy [ __ ] this is like this is really cool like it does what I want it to do and that magic that's what agentic coding is it's like before you had to give feedback like oh no don't do that or like don't write like that agentic coding is more of like yeah it does what I want and yeah these magic moments. Yeah. It's kind of like a natural evolution if you think about it cuz like you know if if you're like a engineering manager, you're not going to look at your uh engineers computer the whole time, right?

Some do. Yeah. Terrible manager. Yeah. Yeah.

It's it's really like if you are a tech lead or an engineering manager, this is for you. Like this is your jam. This is exactly it. And the fun part is like if you are a very micromanager, nitpicky tech lead, it's also great because the AI doesn't care. They will happily do whatever you want.

Uh so yeah, like for sure and uh let's talk a little about cuz uh you know, cursor has been growing like crazy crazy, but it seems like the people like like yourself who are like the most savvy of this stuff are moving to cloud code, right? So maybe talk about so like the thing is there's no right tool. Uh currently there are lots of teams uh like AMP or Klein or like even co-pilot like there they're all interesting teams doing interesting things and they all have their own take and you as a builder or you as someone that are experimenting with these things. You should try them out because one works great for someone and the other doesn't work great for someone and you should experiment and push yourself and in two weeks it might be different. So like we're going show to show cl code now but it's not about the tool cl.

It's about like how do you reset and rethink how you work with these tools? Makes sense. So so let's get right into that. Can you give us a tour of cloud code first? Let's go.

Yeah. Okay. What you see is warp which is my terminal but it could be any terminal. Uh you can get the terminal by just typing this and say terminal if if you're not used to this. Um and you install cloth code go to their website.

You just paste one thing and and it's there. And you started by just running cloth and this is it. Like it it kind of looks weird. The first time I started this, I was like, well, is this really going to like change my IDE? I'm a very visual thinker, so I love to see visual things.

But I I like it now because this gives me peace because there's just one thing I can do here really, which is type what I want it to do. And if you compare that with cursor for example like uh yeah which do you select like auto mode uh many buttons many things there there is a way to also still have it in uh in c uh cursor or other places but like it's it invites you to do something and like the blank slate is nice but basically what you can do you can just say type in something and it will start doing stuff for use. So um for example so so what I use I use uh monologue which is a text to uh or a speech to text app we built internally as well. Uh I can share the the link if anyone wants to try it out. It's very early on but it's it's really good for for using cloth code.

I don't like to type. I stopped typing like more than a year or maybe two years ago whenever whisper launched. Uh I stopped typing. So, okay, can you show me what the app we're in does? Like very high level.

This is a great use case you can use close code for, which is just teach me stuff. So, that's really helpful if you're like in a new code base or if you're uh yeah, not very familiar with it. It will like ask you uh uh yeah, it will ask ask some things. Okay, it's going to Okay, it's going to do a cloth code. So, it's going to say uh what cloth code does.

So, um actually can you look at the code and say what this project does like what language what what what's up here? So, my speech tool it reads also context. So, it sees cloth code and uh and like rewrites part of it. So, it's now doing stuff and you can see it keeps to-dos and to-dos are kind of a way to keep the keep it on the leash. So, it will not do random stuff and you can tell it like hey I want to do five things create todos out of that which is a very helpful thing and it will just go one by one h until it uh did everything and it's very good at finding files and gathering information.

So this is like number one that I always do is research. It's really good at research. It can search the web. It can you can connect MCPS like context 7 which I like. It's it's very good for putting in information.

Uh it can look on your file system. It can do anything in your in your CLI which is basically everything. So okay now so this is this is like a demo app. It's a Ruby rules 8. Uh, this is the text tag.

There's this already set up and I already added some Gmail fake Gmail clients that we might use and already an LM library. Uh, like it's very good at already existing code bases. It's it's also good for creating new ones, but like that's how it's different than VIP coding. I think most people use this stuff at work or for actual products to ship actual code more than like vibe coding. It breaks down at some point and you're like this doesn't work.

You delete everything and start over. Like this is like for sustainable uh apps and things like that. Got it. Okay. It is pretty bare bones in that you see text but the fun part is you can also work with GitHub.

So like you can uh do research and then say create GitHub issues. So let me show you like um for example you want to like do some research and like see if we can create some issues here and uh start building some or do you do you want to do something else? Yeah, let let's build something like a demo or something. Yeah. So, I thought it was fun to like kind of show like a very stripped down version of Kora uh which which looks at your email and then like kind of summarizes it and makes like the most important things uh uh like prioritizes those.

And so, I have a fake Gmail client that kind of fetches uh fake information. So, uh we're going into the mode, the plan mode. You can shift tab into that and what that's enabled is like it will start getting information and thinking without coding and this is something like cursor loves to like start coding and uh and and this is a best practice like it's better to have very good research up front because it is like easier down the line and I'll I'll show you a few things. Okay, so I'll also just start talking. I want to research a feature um and use the Gmail client and RubyM gem.

I want to add models um database models for emails that will store the emails from the Gmail client. Then I want a service that will take an email and summarize the email for me. Yeah, you can use the Ruby LM gem. And then third, I want a UI that I can read through these emails. Um, can you do research on what you would recommend and maybe you can make these three separate issues and you can do them in parallel using sub agents so I don't have to wait too long.

So let's see. So what I what I'm doing here is like um I already have in my head kind of what I want. I I want to give direction but I don't want to be too specific because I still want it to be creative at this stage because if you say all the details like it should have all these things in the data maybe I miss something like LM are really good at like filling in things I missed. So you want at this stage to be not too precise like we're exploring and you can see here I set in parallel uh because sometimes these things go on for like 25 minutes. My record is I think 25 minutes.

We have like a competition internally with people like how long can you have cloth run and I I might I win at 25 minutes still. Um but it's like still like we're on a podcast and we're like actually doing stuff here. So running parallel is a good trick where you can run three things at the same time in a sub agent and the the added benefit is like it won't cost you tokens in the context window of the main conversation. Basically it means at some point it did too much and it gets worse and doing it like this it like does a task summarizes or takes something and then only has a summary in there. So you can like reduce tokens on the main context window.

So it's basically like three separate cloud chats with like some yeah this this is basically like I'm opening three separate chats here and then copy paste this instruction and then say for this one do that for that one and this automatically does that like it orchestrates the sub agents and like brings it back and synthesizes it. So it's a good tool to know. Just note that sometimes uh so sometimes you have to say yes, which is good otherwise uh yeah it's not as safe. So yes. Yeah.

Um yeah. So so that's that's basically what it is. Yeah. Yeah. Yeah.

I think there's also a way to just get it to yolo like instead of you have to say yes all the time. Yes. Yeah. That's how I actually use it. like uh like like I would start using it like this but at some point you trust it and you can like it will save all these yes in in a config file as well but I just run it yolo which is like dangerously skip everything which is a mode that just like it just goes I I wouldn't run that without being here like that is a little bit dangerous because you need some containers but if you have containers set up and stuff like that just think about it.

Okay. Uh yeah, but but yeah, like experiment like if it's if it's a project and you feel safe, do that. Like there's the magic for sure because saying yes yes yes if you do sub agents like this we'll show the the just running without saying yes yes yes with these three tasks. So it has a plan um let's see so it has a plan the core models uh the structure where it's a service and this is going to do that um and there will be some components uh which is like an emails controller so yeah like I I I I think let's go um yeah let's do it yeah I say okay can you create three different markdown files uh for issues and yeah for all these three issues with uh with the plan so I want to store this plan somewhere and normally I do it on GitHub and the GitHub CLI is also there but like for now let's make it simple you can say create three different issues on GitHub for this what I like about that is that other engineers can pick it up even or an agent can pick it up or like there there is some visibility in why it went that way because sometimes with vibe coding it's like yeah there is like some command that you say yes sounds good or something and that is like the only place and you have to go back to through history and this way you can also say hey let me try codeex let me try amp let me try client let me like and like just see which one is the best and go with the best which is also very Uh, interesting. So, I would always like document things like this and use them then to kick off another agent.

So, here it made the first one. Let's pick this one. So, what I'm going to do now is I want to like implement these three features at the same time because why would we do one at a time if you can do all three? So um there's this feature in git called work trees which is uh so git is a way to check in your code and there's version control for the for the nontechnical people is basically if you make a change you say this is a change where I do this and this and this and your name is connected to it and you can reference like the versions you can see what happened use if you don't like and if you don't know what git is or how it works, just tell cloud code to commit it or use git for uh for everything. Um or teach teach me git like it it will teach you.

But git has work trees which are basically you create a new branch but it's in a different folder. Uh so that means you can have different um agents or different cloth codes running at the same time because the issue is if there's one changing a file and the other one is changing the same file they that will be messy. It will mess up. It's basically having three developers using the same system or something at the same time. And this is like separating that out even though it is on one system which is a very cool feature.

So I have this uh command here uh WT which is just make your own but basically what it does it just creates a work tree for me uh based off main here you can look what I what I have but like make it however you want it uh you can do that in cloth as well so work three um and we'll do we'll just call this because it's feature one Okay. And and then I do CC and then you can see now s c s c s c s c s c s c s c s c s c s c suddenly it says bypassing permissions and cc is the one I use and it just runs cloth and says dangerously skip permissions. Okay. So CC is just your own function to it's my own function that I use and uh I I don't like typing a lot so I I just use aliases and functions uh to just make it go faster. Um, okay.

So, we have this one. So, you can reference files with a add sign. So, it knows it's a file. Like, it doesn't really need to, but um, okay. Can you start implementing this feature?

And before you do that, think ultra hard about all the to-dos you need to take to get this done. So, I use some trigger words. So, one is to-dos. create to-dos, which is like that list that um we talked about. Yeah.

And the other one is think ultra hard. Um Oh, yeah. So, okay. So, this file doesn't exist um because we didn't check it in. So, let's let's do that.

Okay. You got to commit. Yeah. Can you commit these files? And you can see already like if you have this on GitHub, like that's not an issue.

Uh but yeah, like so you can see it's committing now. It's uh adding these markdown files and it's pushing them. So we'll do the same here. I like how you've uh optimize your workflow to be maximally lazy, you know, like with the shortcuts and the voice. Yeah, you should because it's all about friction.

Like the less friction you have, the easier it is to do. So uh yeah if you can lower friction uh yeah do it uh but but you start yeah you you don't start here obviously you like you create your own way of working like start using cloth start then changing one thing and then like where where's the friction how can I automate that so now it goes here um I'm going to do the same with the others so let's see this on. Uh you can do cool stuff in in here as well where you like split screen in warp and you can use t-mucks and whatever you want. But I'm uh I'm a classically trained composer. That's my background.

Okay. So I I'll just I'll just make this work for however I do. And you can see here the to-dos are already generating which is cool. Okay. So we'll do this one here.

Uh yeah, there there are systems for doing this really smoothly, but for some reason I just like the simplicity of just like me doing it because I'm closer to what's happening instead of like using a framework and like doing all kinds of hard stuff. Yeah. So you can see two features running at the same time and they are on different branches here and also in different work trees. Um and we can do the third one as well like we'll Yeah. So but the two features are not like they don't they don't need code from the other feature right like like so yeah like yeah like dependencies obviously you need to think about uh yes they need code like this one needs code from the other feature but the beauty is we had research done as a holistic thing.

So you can say, "Hey, like assume this exists." Um, got it. So yeah, like yeah, it's it's like like this is a pretty big feature to build in like 20 minutes, but like it's showing how it how it works and what it does. And normally what I do uh going through this is uh so so these two will will work uh without each other. The third actually needs the the models being done. But you can see it's going step by step and it's uh thinking ultra hard which means it will take some more tokens and more time.

But when you do that it gets better output. And just think about like when would you think hard about something? Will you think hard about something if if you say oh yeah can you change this line to that line? No, you don't need to think ultra hard. That's easy.

But I if it's about uh what can go wrong deploying this to production uh if I have 20 million rows here like might maybe like I I will need to think harder. So then you can trigger you say think hard think ultra hard or think deeply like those words will increase the the thinking levels in in cold as well. Yeah. And you're not you're not paying by the token, right? You have the $100 plan or something.

Yeah, I got the $200 plan. Okay. But you can get the $20 plan, which this includes also the $100 plan. I barely hit any limits, but like I did hit limits once in a while. And I'm just like this is so much value that it doesn't make.

Like I like I think I'm now at like I checked yesterday $1,800 in token usage in the last month. So like that's $200. So, it's worth it for sure. And and there I know there are people that have like way more uh like thousands like four, five, $6,000. So, yeah, like but but subscribe and since yesterday the this plan is also included in the CI version.

So, you can actually run these not on your own computer, but you can run them on GitHub and you can do atclient running on GitHub. So, Oh, wow. you don't need to use work trees which is really cool. Yeah, that's awesome. Yeah.

So, uh it's doing things here. The nice part is like it's not just code like it's going to do migrations. It's going to um add tests. It's going to run the tests and it it's pretty good in like not going crazy. Like it's good at course correcting when it does something wrong which is really nice.

And do you usually like uh watch this happen or do you like go get a coffee or something or normally? Normally I go Yeah, I go on X obviously. No, I get a coffee. Yeah, like I I normally do something else but a lot of the time the time when this is running I'm already starting to think what is next like if these things are done what is the next step I should be working on? And that could be already researching the next step or uh so so let's let's do that.

Let's say uh we have this clothes code here. Um or we can do one more here. Let's do that. Let's we can see everything. Mhm.

So let's do the UI and we can say actually the the models are not there yet but like we can see uh something because it would be nice to have something. Um okay so we'll have this one. Okay I want you to implement the UI. Um currently the models are being worked on by a different developer. So just uh mock something up real quick.

Uh, but I want to see the UI already. There we go. Oh, and and sorry, what what is in those MD files? It's like the previous research that you did, right? Yeah.

So, let's open these. Um, yeah. Yeah. Normally, I I review these, but it's um Okay. It's like a spec basically.

Yeah. It's like a PRD. It's like what what what is the problem you're solving and uh and you can use uh yeah you so like it's it's fun because it's pulling in what kind of techniques it should use and like it it looked at the code base and like how how things work there. So um yeah it's it like for these we did some experiments like what is the like how do you get the best research done and the best research done is not using sub agents necessarily because they use a cheaper model they use sonet use opus and think ultra hard normally the more information in a plan the better as long as like it's correct and opus is really good in writing correct information and really grounding it in things and things you can use is uh like reference blog posts where you think I really like this style or this pattern or like what are best practices and context 7 is a MCP that has like that all curated for you which is really helpful but you can just do a web search and like say these or do deep research with chat GBT and say like what are the best practices for this kind of framework in 2025 and And if you agree, you you just say, "Yeah, it sounds good." And you can add that as uh context as well. So you were able to trigger Opus like you didn't actually pick the model, right?

So you just as think extra hard and then it's using Opus. Yes. Yeah. Like Yeah, you can actually pick the model. I never do, but yeah, it will pick the one like I think you can just do model.

Uh and then you can select something as well, but got it. It's going now. Yeah, you can select a model as well, but use Opus. Yeah, it's the best. And if you already have Unlimited and you're not throttled by anything, like there's no reason not to use Opus.

It's it's it's for sure the best. Yeah. Okay. Um Okay. So, these are still these are still going.

Mhm. What like normally what the next thing is like you have this code and Okay. Like I think I think this one is done because like it's doing test now and I think that's fine. So you can hit escape. So and any time and this one is also done.

It's also doing test like I think for the purpose now it's fine not to have tests. Yeah. Yeah. Um okay create PR. So I always use GitHub.

I love GitHub because that's just something I'm familiar with and like like it's something I'm used to and pull requests are great to review code. So I like to be old school and review code before merging. So I use that. So I just say create a pull request and look at the code. And I have other tools as well like automated testing and things like that.

So maybe we can do that uh with the pull request here if one is generated to have cloud code also reviewed. Um one other thing is like yeah like I'm talking lots of uh things here like oh do this and think ultra hard like I don't say all those things I just have slash commands uh created but it's good to understand what I'm saying and what the elements are but for example this one is the research example and how that works is I can just say slash I can just say slash issues and it will trigger that command and I can say issues um and then I can give information about what I want it to research. Um okay and that that is then passed in here as an argument. So the elements here in this command are first researching the repository. So like what are we in that's important to have in a context researching best practices and I liked web context 7 uh to do that it's like that grounding part where you wanted to like gather information ground it and then I go to present a plan and if I like the plan I say create a GitHub issue.

So this is uh your prompt or like class prompt. Yeah, this is my prompt and it's just like when when I do these prompts so like I just think like oh yeah this is a useful one I will use tomorrow again. Um okay and what I normally do is um I go to the anthropic console generate prompt and just like write stuff down. So, for example, I get a lot of podcast um requests in my email and I want uh like uh a way to uh look through my emails and see if there are any very very good proposals uh in there like top proposals and I want to use the Gmail MCP for that. Um, so it could be that basic.

So I imagine you have a Gmail MCP connected to CL code, which you can, and you have this business thing of like I I want to like have cloth code like find precious podcast things. Yeah. Yeah. And normally I copy this and just go here and create a new slash command. And and this is always pretty good.

Uh just make sure that um like emails you instruct um make sure to fetch the emails with the Gmail MCP. So if that's clear um cloth code will know that the MCP is available and you can use this and you can add your criteria here obviously and then you have a command and then it works a certain way or not and you can refine it and then sometimes you you look at another command like mine or like you're like oh that's an interesting way to think about it like let me add that as well and I'm very yeah I'm very much pushing to use this for other things than just coding like featurebased triage. I have one where I look at all featurebased posts and triage them and see if it makes sense and then I can create a GitHub issue or fix a bug really easily. So there are like other things that I'm trying to do now as well. Yeah.

Yeah. That's that's I I I wish they had this like slash command stuff in the just the regular chat interface for for cloud and they don't like they Yeah, they don't problems here. Like it's it's funny but now I just use cloth code for everything that I use cloth normally for and I use the file system kind of like projects as well and like that is fine like it's it is super flexible uh to do it. Yeah. Yeah.

That's brilliant. Yeah. Okay. So let's see we have a a pull request here. Let's um Okay.

GitHub is not linked but there there is a pull request now and what you can do is like there's a review command so you can use cloth to review itself and that's another thing like starting new agents to review itself is great because it will reflect and think and like have a different mode or different hat and different context window. So you can even do that five times and see if it's like coming up with new things or two times and you can even do it in sub agents where you say review this with three different hats on like uh like a business person or like a security researcher and and they will all bring out different things. Okay. Um but in the end it's like where and how how do you integrate this in your workflow? And I do that in GitHub uh where I just say okay add these all to GitHub.

This is currently one of the biggest bottlenecks uh I have is doing the research and it's doing the reviews which and and the coding is actually the easy part if you do good research because it's pretty good at writing code. Uh it's like the sheer amount of code you need to review. So like how to do that uh like what we've what we're trying out is like creating custom commands as well. So here we have one that is uh one is proofread. It's like hey if there's copy in in everywhere like we like good copy.

So there's like a very extensive list of uh how how we should write and this is style. So this this is one. So we run that one. um like fix critical is like this is a very important part like if it's like uh encryption like more security like run this to think ultra ultra think ultra hard while executing. So it's like really leaning into the uh security hat and like really activating that part.

Okay, there is the uh best practices. So if you think like hey this stinks a little bit like maybe there are like better ways to do it like catching issues and this is also good for people that are new to a framework. For example, if you come from Python and suddenly you're working Ruby or if you're TypeScript and you do Django things are different and it's good to ground it in best practices for a framework like that. So there are different SL commands that you can run and uh use then as well. Yeah.

You you run this on the PRs like to review the PR. Yeah. Yeah. So it yeah like let me show you here. So basically this this is in Kora but basically it has access to my PR.

So um okay load the last uh newest PR please. So it can look at GitHub and just uh pull in the PR and you can say I want to work on this PR and it will check it out and pull in the comments. Uh the PR comments is the slash command to get comments from the GitHub pull request. Um this one is built into cloud and yeah the beauty is it is like it's all connected with MCPS and you can add everything you want. So like if there are to-dos here I can add it to my to-do list as well.

So here here it pulled it and this is the newest one. revamped memories index UI to match something and you can just hit review and and and this is a good start like it will like the the weird things that are just easy to catch that normally with linting clearly you have linting and stuff scan scans set up but like sometimes there's taste or there's like like it feels wrong and now the those things can be reviewed as well which is really cool and it's about distilling that style and that uh got it into a prompt or a review or a slash command. And yeah, so that command is a clock native command. Yeah, this is a native command. There's nothing special.

There's the the review and the the the PR comments are built in. So yeah. Okay. So it says it looks pretty good. Yeah.

Uh yeah. So it goes here and it says, "Oh, this is not good. We should fix these." Uh okay. memory leak things great and normally I look at it and like it's not always correct but it's it's good for me to say oh yeah actually it's incorrect like I rather say no this is not correct and I'm fine with these things than not even knowing about it so it's like I ship more confidently having the these reviews also if you have tests obviously uh but yeah like that that's that's kind of the workflow but but but but dude like when when do actually look at the code in the review like um Oh yeah. So that's all after this.

Yeah. So like like I try to automate as much as possible. So uh so there Got it. Yeah. So yeah.

So we're so I I I look at this. I can say um you can say add these as comments. Uh which is kind of fun because then Oh, it's in the code then. Yeah. Yeah.

And and maybe at this point I'm like okay let me let me actually uh like let me look at the code and and normally I do that in batch and I just do it old school where I just go here and like uh add comments. Um yeah. So I like like I I would say uh yeah so let's say like can we move these in uh inside the view instead of a helper? Is there a better way to do it? So I can say something like that and you see it rewrites it to like certain thing and I can even say cla what do you think?

What do you think? Sorry. Yeah. Okay. You gota type.

Yeah. I got to type bug early version. So if you do this um and you submit the review, cloth will actually pick it up and work in GitHub. So it's like it it's really cool to have it both like in a like execution mode locally but also having it here to finish things up. Yeah, it it Yeah, that's really cool.

and and if the code looks good and you can see here also we have Charlie which is another AI bot like we just add everything and they have different opinions and different angles that they come from like this more of a TypeScript heavy uh bot which is really cool because you have like a TypeScript bot reviewing Ruby code which there are different like it's nice there are different perspectives so like adding different perspectives uh yeah is is always good and you can I said like can you add these comments as well? So it added the comments as well here from uh cloth and the beauty is like I could take the reviewer role using cloth code and someone else could use cloth code to implement this like in this case it's nesh and the beauty is like this is more of a traditional workflow but it's heavily enhanced and accelerated because we use AI and if there are comments it's just easy to resolve them. Yeah, because you have like AI reviewing and AI implementing. Yes. Yeah, absolutely.

Yeah, that's well, man. That's well done. Did the UI generate yet or? H Yeah, let's look look at the UI. Okay, so uh okay, merge this to main or let's run it here.

Let's let's look at what the UI was like. Yeah, there's lots of code here. You can already see like from doing this like there's too much stuff to review to even like there's so much generated in the time we talked uh that it's hard to even show everything. So let me just show the UI. See if we see something nice.

Yeah, man. I'm not I'm not an engineer, but like I think the classic junior engineer thing is just like you just like submit a PR with like a thousand lines of code, right? Yeah. Is that why I'm doing this? See email like it did so much that I so let's see account ID emails see.

Okay. So so here we have something. So normally I kind of know what it's going to do but uh so let's do account ID. Okay. that well like there is always like so there is always um a use for like more old school stuff as well like AI agents are not perfect and they make mistakes and it's perfectly fine to run into mistakes and just go in and edit things or copy paste stuff like that is also something like it's very early we're still figuring this out Um and also like there were lots like this is also it crashes because it doesn't have the like this is a versioning thing.

It was always part of the library and this is like an LM is not up to date enough with this bleeding as version and you'll see that like if you use like later versions or like frameworks that change a lot you'll feel the pain more. Oh yeah that even by coding that's like very common pinpoint. Yeah exactly. Yeah it's like it like things Yeah. That was like two years ago.

Uh but we use something new and uh so now it requires it. Let's see what we see. Okay. So it assumes here. Okay.

We'll we'll get some nice to see uh simplify it. Simplify. And then the classic is simplify or go to Jill. Oh yeah, you you say that. I mean you say or uh something terrible will happen or like that's like the old school GPT3 where you like it doesn't really work.

No, it's this is a joke. It doesn't really work anymore. But in the in the in the previous past uh it did work where uh okay accounts emails path. Uh so yeah like yeah like this this is just like it's a big feature but let's let's give it a few more minutes I feel confident. Yeah.

Yeah. So I guess the vibe coding best practices still apply like you know it's part of it like I think vibe coding is just a piece of a bigger thing and I think vibe coding is something we used to understand that it's very powerful but also it sucks because like sometimes you have no idea why something is not working and everything breaks and sometimes structure is nice to have. Um, let's see. Oh, we're not logged in. That's probably it.

Yeah, let's let's log in. I think that's the thing. Let's first log in and then we go. So, maybe it works. Sign up.

See, it's too it's too good. So, also I use starter projects because I think that makes it way easier to write good code. um undo last thing because it has already like a like a vision. It has a set of tools. It has like someone that actually knows what works because they have experience uh baked in.

So I I would recommend using like some kind of starter kit. Okay. Well, we have a beautiful vibe coded. Wow. This is like email management.

Yeah, I guess it made Gmail as well. Okay, summarize all emails. Batch summarization started for all emails. Well, hang on. What what let's go back to your previous point.

What is starter project like just Yeah. So, a starter project like there are these people that like for example, this one is called Jumpstart Pro from Chris Oliver. And there are others uh like there there there are projects where there is already like a stack selected like stripe for payments or superbase for hosting or Nex.js JS for this with uh shed CN or whatever the technology stack is because they know that works well and they have experience and um they made those decisions for you and then you can focus on your business logic like you you like what is built in here is sign up stripe payments account management like they're all the things everyone needs but they're not unique to anyone like everyone needs that So if you start with something like that, it also gives the AI already like a starting point and and like a opinion of like these are the tools you should use instead of it going with clerk and like something else the next time and like sometimes the grounding in in those decisions and libraries can work very well. Yeah. And and and where do you find get started projects?

just search on or just ask chatd or oh yeah I would I would do that. Yeah I I would totally so it is um it depends in what language you want to build as well but just like chat GBT deep research starter projects and just explain what kind of problems you're solving and what kind of things you should probably have included and some are like very bare bones and some are uh very build out. Um, yeah. But yeah, like yeah, it's funny. We rebuilt Gmail.

I'm I'm sure I hear I'm sure there is like now something running somewhere. Let Let me look at the routes. Let me do old school. Let's see what we have because uh uh so let's see. We have so Yeah.

Yeah. And and this is one thing I don't like about work trees. Um you're like now in here and like oh but I don't see anything because that's because we're not in the work tree. Um so here let's go here. So so you have this get work trees here as well.

So you can see uh see the work trees here as well. And let's see we're in 02 email summation empty. Yeah. So here let me open this. So now if you want to jump into a work tree using cursor or any other like this is how you can open it.

So now I am in this work tree and now I should see the rounds that were added technically. Um but but I don't but that doesn't matter because we can also go here and say routes. What I want to see is if there's any other if there's anything else cool we can look at. Um Oh, you mean like all the things this is? Yeah, like like now it's it Yeah, like I like I it did something but I I don't account.

So we have build a lot of stuff, man. Yeah. So yeah, it didn't build all of this but because some was included already but okay let's see like we have the accounts. Um let's grab for accounts and messages. Yeah.

So we have messages. Oh yeah, that's that's not it. See the here is like where I'm like visual would be great. Yeah, you're and you're Yeah, you're this also the screen is a little bit small but yeah I uh I think this is it for now. I I I cannot find uh or wait let me do Yeah, no worries.

Yeah, my goal was to um show like ways how this could work um and hopefully inspire some people. Okay, so summarize. Okay, so we have summarize batch email search new. I think there's no view for the summarization yet. And okay and and like okay another way like is there a view for the summarization at all like you could ask cloth also.

So there's always different ways uh to get answers here and lean into their old school ways to do this but also like experiment with new ways. Yeah. Got it. Okay. Yeah.

I mean it can basically play like multiple roles right like PM it can be design. Yeah. It's that's really the the mind shift is think of it like a colleague more than a coding assistant because that is just one thing it can do. It can be a PM, it can write product marketing like it can uh post a change log, it can write in your voice and all of that. So yeah, absolutely.

So why don't we uh I want to make sure we have time to show the the real product like the the Kora if if you're Cool. Yeah. So we were trying to kind of do Kora but yeah like let me show like a view that I hoped it would have created was something like this which um like Kora you connect to your Gmail it will look at all the emails that come in and everything that is not important or not urgent enough to immediately see we archive and that is a very scary thing but also an incredible feeling if you open your inbox and suddenly you only see stuff you need to look at which is very very nice and everything else is um archived and summarized for you and you receive it twice a day and we also make things important. So the the more important things are on the top. So you can see here more important messages for me uh newsletters uh summarize like what are the main points and sometimes like you have more than one which is really fun and like I have so many newsletters that I don't even read all of them and this way at least I can see if I want to read it because sometimes I read it and I'm like oh actually this one sounds nice and I want to read it and you can go here or open in Gmail and promotions like no one looks at promotions in in their email.

But now like I see $75 or 50 or like it's easier to scan these and sometimes like I find a coupon where like oh actually I want coffee from that roster and they have 20% off so why not? Like this is the time and I would have never done that before. If you don't want these you can always just not have them. Mhm. Um and also if there is something like uh like this and say hey this is actually this is under under other but it should be in journaling.

So you can just say oh can you make it journaling and you can talk with Kora and uh the assistant here can take action for you and learn how you want to do things. We also draft emails for you. Um, yeah, it's really fun like people saying like, "Oh man, like I feel so much calmer. Uh, like this works for me." And like just having those that feedback is great because that's what I feel and I just built this for myself really. Uh, because I think email is terrible.

Yeah. I mean, yeah, there's so much more uh craft to it than just like a very sterile Gmail inbox, right? So, yeah. Yeah. Absolutely.

Yeah. Yeah. And um behind the scenes is basically like the LM categorizing and summarizing stuff. Yeah, it's it's actually pretty complex. There are rules, there are many LM workflows, there are many different LMS, but the goal is for you to feel confident it does the right thing.

And that means a different thing for everyone because everyone has a different personality. So it's a lot about like understanding who you are and what you where your risk factor like like how risky are you because some some investors might want to read everything but like some engineers might not want to read anything. So it's like how do you find that for everyone and uh yeah lots of emails and uh prompting and fun things. Yeah. Yeah.

I think uh that that's actually one of the lessons I've learned from AI products like you got to give the human ability to provide input so that it becomes more valuable over time like like if I provide a bunch of input it becomes better right so yeah and and it's not only here it's also with if you do engineering like if you do something don't do it again tomorrow just make sure that whatever you did is a slash command so the AI can do it the next day yeah so yeah it applies like make sure everything you do is like compounding because it's better. Yeah, this is like you know I wanted to demo clock code but uh the MD file thing was like the slash command thing was kind of like a eye opener like for for me. Yeah, even if I want to in my blog post maybe I'll start using clock code to do that. Yeah, you can do everything. And also you can write custom scripts like if you have a very specific tool you have or use, you can just say, "Hey, is there an API for this?" And can you just write a little script and say, "Hey, there's this script that you can run in your cloth MD as well." Um, and yeah, that that works that works great as well.

And and you just put these MD files, these prompts into the command there's like a commands folder. Yeah, it's undercloud commands in in here. But you can also have them systemwide. Uh just read the anthropic documentation on it like there's or feed it to the to the AI like I'm still I'm still confused why they didn't have that baked into cloud code but someone like someone is already working on it I think uh to do that. Yeah dude.

Uh so last question man like I I feel like this is super awesome. I feel like for the for the non-engineers watching this they might feel a little bit intimidated by all the stuff they just showed. So like do you have any words of advice? Yeah. Yeah.

Yeah. Like just do it. Don't feel intimidated. But also like I I'm doing this for a while and now I'm very comfortable with it. But like when I started I was like a baby as well.

I was like like that's fine. And the the most important part is not to listen to the gurus and the people say this is how it works because that's not how it works for you. like you should figure out how it works for you but you should listen to other people that push the boundaries to see like hey maybe I should push more towards that and that could be like non-technical people just install cloth and like try it have it do one very simple thing and just see see that one simple thing uh like exceed or not and and experiment with it like I think the play aspect is just go play with it no like Don't say I want to redo how I write blog posts or an entire like workflow because it's hard. Just do one simple thing and see if it can do that and then build on top of that. I love it.

And and and where can people find uh Kora? Kora. You can try Kora.computer. We have 7-day free trial and either you love it and some people hate it. And uh yeah, more people love it uh lately.

So I'm very very glad with that. Um, I post lots of stuff on X, like very deep, nerdy coding stuff, but also just more philosophical takes. So, if you want to see any of those, uh, you can follow me there as well. All right, Karen. Well, thanks so much, man.

It was so great uh meeting you online and having you walk through all this. Uh, one one day if I stumble around enough, I'll become as good as you doing all this stuff. So, I I'm a beginner. Thank you. Yeah, thank you for having me on.

C.
