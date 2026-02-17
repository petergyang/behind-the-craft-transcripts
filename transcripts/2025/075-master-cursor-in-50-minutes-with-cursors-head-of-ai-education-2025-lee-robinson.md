---
title: "Master Cursor in 50 Minutes with Cursor's Head of AI Education (2025) | Lee Robinson"
guest: Lee Robinson
publish_date: 2025-08-17
youtube_url: https://youtube.com/watch?v=mm8cn53_pdU
channel: Behind the Craft
keywords:
- coding
- ai-tools
- product-management
- ai
- leadership
---

The way that we build software is going to change. The AI is going to write a better commit than I ever would. The agent can check its outputs. It can run a test. If the test fails, it can just read the output of the failed test and kind of continue going until the test passed.

Do you have some advice for like the, you know, the product managers or folks out there who want to learn this stuff? There's no way that AI can just magically think for you and make all the decisions for you. You have to bring some amount of context on the type of product that you want to build. Some people who've started to use some of these newer tools, they build the first version and they get something out there and then they have to like go back and kind of buy a textbook and learn the fundamentals before they can take things any further. How to build an app with AI from 0 to one.

So, there's a couple things here. Okay, welcome everyone. My guest today is Lee Robinson who is now at Cursor. Lee previously led developer experience at Verscell uh where he helped build Vzero and you know frankly he's a kind of like a legend in the in the developer relations field. So uh really excited to get him to talk about um you know how to build an app with AI from 0ero to one and also how you know existing engineers can uh get better use of these AI tools.

So welcome Lee. Thank you. Yeah I'm really excited to talk through this. Yeah. All right.

So uh before we get to the building part, let's talk about you know can you share like why you decided to leave Verscell and join cursor? Yeah. So probably maybe a year and a half ago I really started to code with AI more and at the time it was mostly autocomplete. You know I'd used GitHub Copilot and I thought that was pretty good. Um, but it started to get quite a bit better, not only in cursor, but in other tools for kind of the next generation or the next action completion in autocomplete and that was definitely helpful, but I still was I wasn't totally bought in yet.

Then about six months ago, I started to really take this seriously, try out a bunch of editors, uh, and really kind of get my feet wet with the AI space for coding because I'd heard a lot of people talk about it, but I was I was still skeptical. And as I started to learn more about AI agents and actually allowing agents to write code and gave them a shot, I was pretty surprised that both the quality of the models had caught up, but also the tools had gotten much better to the point where I was very surprised the amount of code that was able to be first kind of written by the AI, but I still had to review it and kind of make sure it was correct. But even that was enough to kind of shock me into I should probably take this a little bit more seriously. And then I started to use background agents kicked off from Slack when it was a docs typo or a UI bug or like these very very small things that I could have context switched in to do, but I could just ask, you know, through a Slack message to kick something off. And that really made me step back and think, okay, the way that we build software is going to change.

And I want to help teach people, especially existing developers, how to navigate that journey in the same way that I was navigating the journey. And that's what led me to your cursor. Yeah. It almost feels like uh every developer now has a team of I don't know, junior engineers or like it's kind of like a engineering manager who can kind of guide AI, right? Yeah.

Exactly. Okay. So, let's kind of get really practical here. So, maybe let's talk about uh building a app from scratch first, right? Mhm.

And you know, I think nowadays all the roles are kind of blending together. Like I'm a PM, but I think now engineers can be their own PMs. I think what a lot of people don't realize is how important the initial setup phase is to to kind of like building a good app. So maybe you can like kind of uh show how you use cursor to set this stuff up. Yeah.

So there's a couple things here. One is that I feel like for newer people into software engineering, they can get a lot of conflicting advice about the right way to start and build apps because AI can make it seem easy, but in reality, there's a lot of scope and there's a lot of technical knowledge needed to build quality software. And sometimes if you ask an AI model for a plan, if you haven't yet spent a little bit of time kind of learning some of the fundamentals, it's going to output stuff and you're going to kind of nod your head and say, "Yeah, okay. Postgress database, I think I know what that is." And then it like describes the schema and you're like, "Yeah, okay." Like that that kind of makes sense. Um, so I always want to stress that it's really important even as we talk through this zero to one phase to understand and ask questions on the plan like what is that thing?

Why why do we need that bit? Um for people who are just starting their coding journeys or maybe in the first couple years of their coding journeys u because you're you're taking something from zero to one as a solo person which means you're wearing the hat of multiple people. There was the front end, the backend, the devops, the PM, the designer. Like there's a lot of roles to build quality software and you want to make sure you can do a good job at at least parts of those. So, what I'm going to do is I'll pull up cursor and I've got a prompt that I've been working on for an app that we can build.

I want to talk through kind of how I structured it and then we'll see we'll see what happens. That sounds great. Yeah. Cool. All right.

So, I've got cursor open and I just pasted in a prompt into a readme so we can take a look at it before we actually ask the agent to do any work. Now, I want to step through each of these kind of bit by bit. And you're going to notice that I come in with some knowledge and an idea about how I already want the system to work. So, I want to build an app where we can track music listening and report stats on top artists and songs. So, back in the day, I used to use Last FM and you could like scubble your top artist and you could see your, you know, most played songs of all time.

So, I would love to rebuild something like that for fun. And what I want to do is work with the AI like a co-orker to help me make a plan. And you know, you're a PM. Our product uh folks watching know all about PRDS and kind of structuring your product requirements into something that's coherent. I will say that in the AI world with you as the driver of commanding AI agents, there are parts of the PRD process that maybe aren't as relevant to this world.

And there are part new parts that you need to bring in like having a bit more of the technical foundation to understand exactly what requirements you want to ask for. So for example in requirements I already know that this app is going to require some authentication and I have a general understanding of the types of authentication. So I know about OOTH. So I'm going to say let's just do Google OOTH or sign in with Google. Um they're going to connect to their Spotify account.

We're going to use the Spotify API. So, I need to know what APIs are. Uh, and then we're going to take that and store that information in a database. So, a little bit of a I've built an app before, you know, type of understanding here of I talk to the API, I get some data back, I need to store that data and do something with it in the future. So, we need a database.

Um, critically, I also want to use tests. So, for my business logic or how the application works, uh, end toend tests which can run over the entire app and test user flows. The reason this is important is because it allows the agent to have a selfverifying loop. The agent can check its outputs. It can run a test.

If the test fails, it can just read the output of the failed test and kind of continue going until the test passed. So tests might have been out in the past, but they're still back. Uh, and then a few more tech, you know, technology choices. I want to use git so we can take kind of snapshots over time. and I have an opinion about my package manager and I want to make descriptive commits as I go.

Then, you know, it's helpful to have some ideas of the stuff that you want to use ahead of time and how you want the application to feel. I'm coming from an engineering background, so I already have an idea of some of the tech stack that I want to choose, but if I didn't, I could ask the AI and go back and forth and try to understand some of those things. But this is one of those places where as you get more experience, it's going to help you a lot with knowing which tools work for you and and which tools are also good for the AI models to understand. So I have a little bit of an idea of what I want the design to look like. You know, minimal functional uh intentional use of color.

Our designers watching, they can probably give much better tokens here to the models, much better prompts. Uh then frontend wise, I know some of the text stack that I already want to use. Um I want to use React. I want to use Tailwind for styling. Shads UI and then ESLint in the same way that tests allow you to give feedback back to the agent.

Llinters can also give feedback to the agent on something that might not work well in the React world. If the AI generates wrong code, the llinter can say, "Hey, by the way, that might not work on the back end. Um, here's what I want to use for our database. Here are some of the tools that I want to use for infrastructure." And then what I want to do is have this plan. But this plan can kind of be a living document.

So we can put to-dos in here. It is kind of a extremely lightweight task management system. Now you could also integrate with external systems through something like MCP model context protocol. Go talk to linear. Go talk to notion.

That's more of the advanced mode if you want. But you can go pretty far actually with just a markdown file and some to-dos, especially if you're operating in single player mode. Um, and this last line I think is really important. Like if the model has questions, keep the human in the loop. Ask for my input.

Ask when I didn't give enough clarity. I'm sure that I missed things here. So let's actually take this. Just gonna cut this out. I'm going to open up the sidebar for the agent inside of cursor.

We'll make this a little big. And I'll drop this in here and we'll hit enter. Uh make my plan. Yeah. And just just to kind of like coming from uh someone who's like a little less technical than you, maybe a little bit more.

Yeah. Like you can also ask AI to obviously come with the requirements and tech tech stack and then you can review it and then if you don't understand something like you can just highlight the text and be like hey does this make sense or is like what what does this even mean? Right. Like there's a way to do that too. Exactly.

Yes. Exactly. So, we can see now uh it's kind of started to to go and started to work. And one of the things that the cursor agent can do for you is it can internally manage a to-do list as it's stepping through your task. So, you kind of have the local to-do list which is what the agent is managing.

And then you have the global to-do list which can be your markdown file or it can be an external task management system. And uh we can also see the files that have changed. So, we've got our plan. So, while this is kind of going, I can go open up the plan and we can kind of take a look at this. Uh, and if I wanted, so it says, "Hey, by the way, we've got your plan.

We have a bunch of other to-dos that we want to do, but before we go further, let's review and make sure that this plan looks correct." So, this single chat in our history here has finished. And it's worth just revisiting some of the kind of foundations here, which is I have this chat with an agent. I'm talking to an AI model. That AI model I've picked down here, which you can just use the automatic mode or you can pick a specific model once you start to get a feel for what works best for you. And as I'm adding more content into this conversation with the AI, all of the messages are kind of an append history.

So it builds up more context as it's called as you continue chatting with the AI. And I can see here with this percentage gauge, I've used about 2% of my available context or kind of the working memory of the AI. So we've got our plan. Okay, we're going to build this web app. It's got our text stack.

That looks good. Infrastructure package manager. Okay, so let's see how it decided to take my requirements and break them down into chunks. So the first one is setting up the project. That seems okay.

setting up the database, getting the tables right and you know it makes sense we have to set up the project first before we go and set up the database. Okay, that all makes sense. Oh, we even have deliverables of what we can verify that this step is working correctly. Set up authentication so we can log in with Google uh integrate with Spotify through their API and then start to add some of the features. Now, some of these features we might need to break these down even further.

They're they're pretty wide. Um testing, we might want to add tests a little bit earlier so that as we add features, for example, we can use the test to verify that things are working correctly. Uh deployment somewhat similar. We can wait until the end if we want, but we could also deploy earlier and often and try to get uh a URL live. And then as you remember, I asked for feedback.

So, here's some open questions like how often does the data sync? What statistics do we really care about all of this context I didn't provide to the AI model, which is why it's good for it to ask questions because it helps you reason through what do I actually want this application to do? What do I actually want to build? There's no way the AI can just magically think for you and make all the decisions for you. You have to bring some amount of context on the type of product that you want to build.

Let's see. And then you would basically give it some feedback to update the plan, right? Like to add testing throughout and so on and so forth. Yeah. And like success criteria.

I think that makes sense. Uh I might want to move the success criteria to the individual iteration. So let's make these changes. Let's move the success criteria into each iteration. Um, let's set up tests earlier so we can verify each step and um maybe we can answer some of those questions.

The data should sync uh let's do daily. And it's funny like you can have typos. It's fine. Like the AI model understands if you have typos. You don't have to type in perfect grammatical sense or have perfect spelling like it'll figure it out.

Yeah, you can go through plan based on some of those things I suggested. Great. And uh we get this kind of diff view here inside of cursor where we can say, "Yep, we're going to keep these changes. That looks great." And uh it's going to keep going and adding more of the deliverables and success criteria to each part of the plan. And then once that finishes, we can actually have it go kick off and work on the first step or the first iteration.

So right now we only have the plan in our app. We have no code yet. We haven't actually started on that. But this is where we'll start to get to the interesting bit where we feel pretty pretty decent about this plan. We like the way it's kind of broken out.

We can start to ask the agent now um to actually go kick off this process. Now, it's worth pausing for a second and talking about foreground agents and background agents. So, the foreground agent is what I'm working with right now where I'm watching the output. I'm kind of reviewing what it's doing. And as you're going to see here in a minute, I can approve or deny specific things that the agent does.

There's also a world where you can start agents in the background. So, as we get a little bit further into this project, for example, you might see in phase two, once we've got the app working and there's kind of multiple to-do lists here, maybe we decide that one of these we can just go run in the background and we can do multiple things in parallel. Now, this is a little bit more of an advanced thing to manage and get used to, but as you get used to that, it can help you kind of break up different tasks. Now you can also do multiple foreground agents but then you have multiple AI agents trying to update the same codebase. So you have to be kind of intentional about how you do that.

So it looks like it finished. Um cursor suggested a memory for me. So it's like a long-term memory for how we might want to steer this project which says that the success criteria should be moved into each iteration of the plan which we could keep this if we wanted to keep updating the plan. For now I'll just discard it. Um the thing with the memories is they will be injected into the context of your conversation.

So if you put into memory, you know, I prefer responses to be very concise, it's going to remember that for future conversations like uh across projects too or just in the same project. So it's just for this kind of workspace that I'm in right now. Um there there might be a case where you would want something across all of your projects. Yeah, that could be interesting. Okay, so looks like it's done.

Um, we still only have the plan, but we have multiple to-dos kind of drafted and ready, and it wants to do the next one. So, uh, let's go ahead and do the next to-do. So, we have a plan. Seems fine. It's going to now start to actually go through this list and kick things off.

And then we'll be able to verify along the way if things are working or not. Now, what you're going to notice is the agent, and I'll just zoom out here for a second so we can make this a little bit bigger. The agent is just going and running things for me. And part of the reason this has happened is because I've already had an allow list where I've said that is okay for the agent to run specific commands. So, on my machine, the agent is using the terminal and it's running a command to go talk to the internet and download things and install things.

Now, if this was a command that I didn't want, I might have to manually allow that every single time, but I've already made the the case in my global settings. Actually, it's fine. If you run npx, you know, that's totally fine. Mhm. Um, so it's going to go through, it's going to make this app great.

That all looks fine. It installed all of the dependencies for me. It's uh it kind of made it in a sub app and then it moved it back into the main app. It used to install it like this. So much better than the This is so much better than the pre-AII days, right?

Like just installing those dependencies takes for forever, man. Like you know. Yeah. And like especially when something goes wrong, the agent can just fix it. Um so there are cons to that, right?

Where you have to kind of jump in and steer the agent. But sometimes when you're adding dependencies and you get this like weird error because you know you were supposed to use some CLI argument that you didn't know about, it can just do that for you, which is really nice. So, it installed all of these dependencies. It's setting up testing for me early. It's setting up um Shaden for me.

Now, what you're going to notice is we got to a spot where it actually required user input. So, it's kind of waiting for me. So, I'm going to say that looks good. Um I like that color. Sure.

And that kind of subterminal finished. And it kicked back out to the agent and said, great. That looks good. Like, keep on going. Keep on going.

Uh, so it's just installing and setting up a bunch of things for me. Now, while this is going, just pull this back over here for a second. Uh, we can start to see we have a project that's kind of coming to life. And if you're a newer developer, this might look kind of intimidating. So, this is also the time where as this is kind of working here, I could go back into my agent.

I can do uh command T. I can open a new chat or a new tab and maybe I want this tab, maybe I don't want this tab. This is like additional files to include in the context when I'm asking a question. But I could say like explain the files uh in the root of this project. What are they and why are they even needed?

So this is just like a question that we're asking to try to gain more knowledge about how the system works. It's gonna go read all these things and kind of come back. So, we're still cooking over here. Like the agent is still going and setting up things. And you just saw something that was really interesting, which is it had set up and installed all of the tests and then it knows how to run the test.

So, it made a test that the page rendered without crashing and it confirmed that the test worked. It ran the server and it made sure that the server worked and now there's a test that's failing which is good. That means that something was not working right and the agent is going and kind of fixing things along the way. Oh, you see what it said? It said I can see the issue.

The default page doesn't have a main element so it couldn't be found. Uh all of this is kind of just happening for you which is really really nice but also it's a lot of code being generated. So, we're really going to want to make sure we step back and understand uh what's happening here. Of course, there will be a summary of all these changes because it's just spitting out a lot of stuff which can feel a bit overwhelming. But like let's go back here and see what it says.

Okay, so we have a package json that defines dependencies. We have a lock file. Okay, we have the next.js configuration file, how we configure TypeScript and etc. And like this will help you as you're kind of gaining familiarity and context with some of these things also help make better technical decisions for the type of tools that you want to use or the type of tools that you don't want to use. For example, you might say, "No, I've used Playright before and I actually want to use a different testing library." Great.

That's fine. But you'll get those reps in so that you can determine what you want to use and what you prefer. Yeah. I mean, that's kind of how you become more technical and learn this stuff, right? So, Yep.

Yeah. So, it's still going. Um, it looks like that worked. Um, and now my end to-end tests actually work. So, it opened up a browser.

It confirmed that the browser could render the page and then gave those results back. And then because I told it in the plan to make commits, the AI is going to write a better commit than I ever would, which is here's the commit of everything that it got set up. Great. That looks awesome. It commits all those changes.

Uh and then it also goes and updates the plan. So it got everything in phase one done. App runs locally. Linting passes. Basic test structure.

Uh basic test suite exceeds. So now we have a summary at the end here. Phase one, what did we do? We set up the app. We installed the package manager.

We got all the plumbing for the test setup. We got git working. Awesome. And we have a server that runs. Linting passes.

Test pass. Now we're ready to move on to phase two if we would like. So if I'm happy with this, I can go ahead and keep all the changes or I could also step through every single file. uh and kind of verify them manually and understand a bit more of what I'm working with. So, because I have familiarity with these tools, I can kind of step through here, kind of verify and kind of spot check and make sure that things look okay.

Um so, let's let's check this one out for example. Uh here's our homepage. We got this React component. Uh it's a music tracker. Awesome.

Sign in with Google. Connect Spotify. And then here's our test. So, does the page render without crashing? Um, does it display the music tracker heading?

Does it show the sign and connect? Like that seems seems like good test to have. Um, that seems right. Yeah, I think there's like kind of like two differences between how you did this with how I typically like try to vibe some of this stuff. I don't include the instruction to get it to write tests, which is like which is what an experienced engineer would do.

So, seems like just the fact that I wrote test means that it can actually fix a bunch of stuff and like test a bunch of stuff, right? Yes, 100%. Like we can let me try to find a good example. Now, by the way, you can see that the cursor agent is able to spin up and run a terminal. And the terminal can be used to start the application locally.

It can also be used to run tests. So, it can kind of run those two things in parallel. Um, but I also want to mention we've got this kind of long change. We used up kind of 24% of the 200,000 token context window right now. Yeah.

And it's helpful to remember that this working memory of the agent, like everything in this chat, if I were to ask it to do, okay, now do the next thing. It's going to take all of this context that I had before and bring that into the next conversation. And we have to decide, do we want that or is that potentially distracting and unhelpful for the agent? Now, you might think, I mean, I've only used 24%. But even once you get up towards the top of the context limit, there's been some really good studies and kind of early research that's came out that have shown that once you get up to the top, you kind of have this like needle in a haststack problem where when you're at 95% of context use, you're giving the AI model all of this stuff and you're trying to tell it to find this one little bit of relevant information in the middle.

It's hard to do. I mean, my analogy I like is if we talk at the water cooler for 30 minutes and then at the end you're like, "Oh, by the way, what was the first thing I said?" I'm like, "Uh, I already forgot. What did you say again?" You know, like it's it's kind of similar to the way humans operate as well. So, for example, we've already made a commit. I can see in the source control panel here, I don't have all those changes.

Actually, I'm going to update uh the plan since we committed those things. Uh, so I'm in this kind of fresh state. So, actually what I'm going to do is I'm going to hit command N and I'm gonna start a new chat. Um, because I don't need all of that previous context. So, let's go back to the plan and let's see if we could set something up that feels verifiable.

Uh, what would be a good thing here? If we do database, I'm going to have to like go get a database and and set that up. And that that could take a little bit longer than we have time for here. Maybe just like build the front end with like some dummy stuff on. Sorry, say that again.

May just ask you to build the front end with some like dummy data or something like you know. Yeah, let's do um let's add a settings page um to configure your Spotify account even though we haven't yet integrated the API and I want to ensure uh it works correctly. So add test. Yeah, maybe we should just put the maybe curs just put the add test stuff in the system prompt or you know Yeah. The way I like to operate is when I find myself starting to say the same things multiple times.

It's kind of a nudge to myself that, hey, actually this is probably something that I want to put into a cursor rule. The cursor rule is effectively a little note that you're including at the top of every single chat, every single conversation to put it into the context when talking to the AI model. So, for example, it might say, "Always use this package manager, always run tests, always use uh, you know, a specific style of commits and make sure you're committing early and often." Like those could all be ways of working that you're essentially encoding into the kind of rules that are applied to your project. Yep. And cursor rule just for people who are watching is just say headings, right?

Cursor say headings. That's what the rules are. Yeah. So, so I'll just say let's make running tests and using uh git some cursor rules in my project. And I can just go ahead and hit enter and it kind of throws it in the queue.

And if I was like, ah, actually I don't want to do that, I can delete it or I can also push it up and kind of interrupt the chat if I wanted to. So, we've got a few things happening right now. We made the page. We added tests. We're going to do some navigation.

Great. I'm I'm still going to let it do all that stuff because why not? And then we'll have it update the cursor rule. But now this is a good chance for me to show the review flow a little bit here. So I can kind of step through.

We've got four different files changed so far. And I can approve or deny things. Oh, by the way, on the right we saw the test just passed. So that's good. Progress.

We've got a link to settings. That looks fine. Uh I'll hit keep or I can use uh command Y. Let's go to the next file. We've got our settings page.

This is a React component. Um, since we're doesn't really matter what this is doing right now, so I'm kind of just going to gloss over this until we get more functionality. It's kind of just stubbed out right now where it's it's it's not actually doing anything. Sure. We'll keep this.

Go to the next one. We've got our test. That looks okay. So, we'll keep that. And it passed.

So, that's good. Oh, we have another test, too. Nice. Now I do see something else which is I see this squiggly line and the squiggly line is is giving me an error. It's saying hey it can't find this thing.

You might have missed installing the type definitions which is interesting because when I when I you know install all of that stuff at the start it looks like it just missed setting up some of these type definitions which give me more feedback locally when I'm working in the editor. So let's go ahead and do that. So, I'm going to add this into the chat and we can cue that up as well. And uh it looks like it might have got stuck here on this test. Didn't actually exit out.

So, we can just skip that. I think it looks like it works, but we didn't actually exit out or the test didn't the terminal command didn't have an exit signal. Great. The settings uh pages are passing. There's a lint error.

Okay, still going. Great. It's done. So, now that this is done, it can actually kind of pluck things off of the queue and keep going with the things that I had suggested. So, it's going to make some of these cursor rules.

I'll just review these changes. Those look fine. And then I'll pull up my code again, and you're going to see here's my kind of directory structure for my project. And it's going to go ahead and create some cursor rules. Now one interesting thing is it's a good time to talk about how AI models work which is they're trained on some data from the internet up to a certain point called the knowledge cutoff and then after that point they don't know about changes.

So what you just saw is that it made a cursor rule but it did it in this cursor rules filecursor rules. Now, for my cursor users who are watching, you'll know that this is kind of the older way of doing cursor rules where you dumped everything into this one rule. Um, which is fine. It still works, still supported. There's actually a newer way where we can break it down into smaller bits and we can give feedback to say, do I want to include this in every single conversation or do I want to only include this in some conversations?

So I could actually go in here and say actually use the newer version of cursor rules uh where they can be in multiple files and we can even tag things here like web to go search the web if there's any confusion about hey I don't know exactly how that works or I can go tag in specific docs like the cursor docs. So let's do that instead of web. I'll put that into the queue as well. Now, while I'm yapping here, the agent is going doing things for me, which uh I mentioned that there was that error in the chat where it didn't know how to understand describe and it and it went and installed the dependencies for these things. And now when I hover over them, I get all of this information from the type definitions that help me understand kind of what I'm looking at here, which is nice.

Mhm. Um, so now it went and deleted that file and it's going to set up some new cursor rules for my app. So I have doc cursor, then a rules folder, and then I have different kind of files inside of here. So it's going to set up a couple for me. Great.

One is on general rules, the other was on git workflow, development workflow. Awesome. And I can kind of go through here and prune out what I like and what I don't like. I would say these are probably a little verbose for me right now. I would probably want to cut some stuff out.

But um yeah, that's just one kind of way of working through this workflow where we can test and make sure things work. Seems fine. And can you try to get the thing to like load like like the the actual app? Oh yeah, let's do that. Let me um let me open up I'll stop sharing and I'll open up a browser.

and we can take a look at what it built. Okay, so this is this is the hello world app that it made. You know, if your app doesn't look like this, you ship too late. Like this is the most uh barebones kind of Hello World page we have. We have buttons that don't do anything.

Yeah. Oh, the settings. Actually, this isn't that bad. Uh when I told it to make the settings page, this looks fine. Um, it hasn't really taken into account the design that I wanted, but it's it's I guess it's okay.

I I needed to be more specific on exactly what I'm looking for here. But one thing you're seeing, which is really nice, is because I told it to use Shad CN UI, which is my kind of design system and component library builder of choice, I'm able to get these pretty like decent components. Um, I'm not sure if it's using them fully yet, but I'll be able to drop in all of those components, which makes things, you know, just a little bit easier, a little bit more accessible, a little bit more customizable. So, yeah, it's pretty decent. I mean, you know, in fact, chassis and UI is like the the favorite UI that AI likes to building.

So, yes. Yeah, it's used by all of the kind of major AI models to generate UI. Mhm. So, let me kind of recap this uh this example you did, right? So just kind of uh number one you put a lot of time in uh the initial instructions and everything like the the the product spec is like also has like details about the technical stack and everything that you want right and also like crucially you included uh some lines about um you know including tests and and also may maybe this is obvious to you but like this this was kind of like a new learning for me is to just ask the AI to make commitments uh along the way like make commitments along the way.

Yeah. Yeah. It's it's one of those things where the historical best practices of software engineering that maybe were hidden away in some book or just learned on the job are now being expressed a little bit more clearly at the start for how you work because the agents actually work very well in that same way. They need feedback. They need the outputs to be piped back in so they can understand where they went wrong.

which is why you're seeing typed languages like TypeScript, llinters, compilers, uh you know, running tests into tests, all these things. They help the agent work better. And it's nice to set them up ahead of time so that you're not getting into a state where you ask the AI to do something, the agent go and write some code and then it doesn't work. So you prompt it with something like, hey, this doesn't work, right? Yeah.

Yeah. Yeah. But the agent doesn't know how to go kind of farm for more information, more signal to figure out what to put in the context on why it doesn't work. Type languages, tests, llinters, they give you that stuff which have been helpful for programmers writing code from by hand and they're also helpful for agents as you're paral parallelizing the work that you're doing. Yeah, it seems to have like because you as you write tests, it had the context to go just fix its own problem.

So you have to keep going saying it doesn't work right and right now the example I showed was nothing too wild but that really starts to pay off when you have runtime logic errors. So when you build your application when you compile your application you're going to get some feedback there. The trickier stuff is when your application is actually working and running and users are trying to use it and they run into some error and that error hopefully has an error message. Hopefully there's a stack trace which is like a specific point or a pointer to the part of code where the error was. And if you have that information and you can pipe it back into the agent, it definitely makes life a lot easier for trying to figure out what went wrong.

Awesome, dude. So now let's kind of talk a little about how like like real engineers can like uh use use cursor and AI tools for like a established code codebase, right? Because there's just way too many lines of code for it all to fit into context at the same time. I think for me the difference between vibe coding the first version of your application which is roughly what I was doing here but the difference is that I have built up the context and the knowledge to know what tools I'm working with and to know the right questions to ask. Um the big difference is what happens after day one because I might build this app and I'm just building it for myself.

It's just kind of a throwaway thing. I don't really care about the code that much, like I'm just doing it to try out some prototype. Vide coding is great for that. Just throw the code away, right? It's fine.

If this is something that I'm trying to build and maintain over time, it's a it's like a, you know, a business I want to build or it's code that I'm working on with my teammates or it's the production software I'm writing for my company. I can't vibe code that. I have to know what I'm working with. I have to just do normal software engineering. But that normal software engineering, you can augment yourself with AI.

And I think what we're seeing right now is there's a healthy skepticism around doing that. And I think a lot of engineers who have been writing code for a really long time are trying to figure out what this new brave world means for them. And my goal is to help show a lot of those people who are skeptical but maybe optimistic and cautiously optimistic about where we're going is that AI can be really useful for automating the boring stuff, the work they didn't want to do anyway. It doesn't have to always be generating a full app from scratch. Although you will do that at some point, right?

You're always going to be building new things. from day one to 100 or a thousand. There's also a lot of practical uses of AI for even small things like reformatting or kind of parsing through a bunch of data and trying to figure out uh you know a specific bit or summarizing long information kind of going one format to another format. It's little things like that can really help. Yeah.

Like you know like it's not only the dependencies like that that that AI can help with. Yes. So I guess your advice for experienced engineers is just to like don't forget all your knowledge that you already have like you know engineering is not dead as a practice or anything. In fact it's like more in demand than ever but maybe try to use AI to to try to streamline some of the boring stuff that you have to do right is that kind of advice. Yeah, there's a lot of noise out there about how engineering's over and you know the it's I I just think a lot of it is unhelpful because if you build an application and you don't have an understanding about how it actually works, it might work great for the first day or the first week, but you're going to reach a point where you're in a really bad spot.

And you're starting to see it right now where some people who've started to use some of these newer tools, they build the first version and they get something out there and then they have to like go back and kind of buy a textbook and learn the fundamentals before they can take things any further. And I feel kind of two ways about this. On one hand, I'm glad that it's making software more accessible to more people. Uh at the second hand, I want it to I want it to be people who are excited about actually building software and what that journey looks like. So for me, I actually fell in love with building software when I started doing web development because I could really see it.

And there's something beautiful about using AI models to generate code and get working applications that I can use and see that I think will inspire a lot more people to code. Uh so my goal is to help them learn what it takes after that first day, what it takes going to day 100, how you actually build real software and do software engineering. and AI can still be a good part of that. Do you have some advice for like the you know the the product managers or folks out there who want to learn this stuff like learn the principles? Uh yeah, is it just kind like work on small projects at a time or like how do you get started with stuff?

go read a book or Yeah, I think it's I think it's both learning by doing and then also learning the questions to ask because I think what an engineer gets trained to do is be skeptical of a lot of things and also know where they don't knowledge and ask the right questions. So, as you're trying to apply yourself to build things and experiment with the new technology, experiment with AI, you're most certainly going to run into things that you don't understand. And you can both kind of learn as you're building and hacking with the the vibe code where you're just throwing it away. You're just trying things, right? And at the same time, I would strongly recommend anyone who really wants to give this a shot to go learn about computer science, go learn about engineering.

Um, there's a lot of things that might not seem obvious at first, like understanding data structures and algorithms and the different kind of bits of code that get created that are just going to be helpful to know. Like if you don't really know what a loop is, that's probably going to be tough when you see the AI generate a for loop and you're not really sure what you're looking at. And again, if you have the mindset of knowing how to ask questions, the AI can help you understand what for loops are. can give you a road map to learn working with loops and working with conditional statements and understanding the different types of variables. All these like core bits of programming that you're going to want to stack and learn.

You just have to have that curiosity of it's not that I just want to use this tool like some getri quick scheme or build an app quick scheme. It doesn't really work like that. It needs to be I want to use these tools because I want to learn how to build software. Yeah. So, so is a bit of doing everything right.

is like you know building building the apps trying to ask AI what this this stuff is and also going to read tech textbooks to build your foundational knowledge that's kind of exactly yeah because otherwise you can just like build something you know like we we've seen examples of people v coding something and then their API key leaked or something it could be bad you know if you don't know what you're doing yeah I mean if you've never worked with any of this stuff well one you don't know what an API is so you definitely don't know what an API key is and you probably don't know the difference between client and server. So you don't know the question to ask for why is it bad that the API key is on the client. Like you just you wouldn't even know to ask that question. And I think there's a responsibility of people teaching newer developers or newer people building software to step back and learn these things before we put databasebacked applications into production. Uh and I think the tools will get better about building some of that stuff in.

I think right now cursor is really focused on helping professional developers build software better. But I'm also really excited by a lot of the tools trying to build for product managers, build for other people who are kind of getting into coding for the first time. I would love to see them add more tools for the beginners um for the designers or for the product managers who are just trying to figure this stuff out where maybe it nudges you to learning in the product. I think that would be great. Let's wrap up by talking a little about your experience.

Uh there's a few questions about your experience of resell and also now at cursor like um how do you guys build products at these companies like is it um like you know do is there like very well defined functions do you just write the prd cursor or h how how do you guys build new features? Yeah. Yeah. I think Verscell and Curser are different in so far as they're much further along in the company life cycle. Verscell is a much more established company than Curser, you know, newer company, both in terms of how long they've been around, but also how established the product development process is and what it actually means to ship software.

So, Cursor moves really fast. I mean, we're trying a lot of things. We're seeing what sticks, what doesn't stick. And I think giving a lot of agency to engineers to own that process end to end like we don't have I think maybe one product manager or our first product manager is coming soon. So we're we're still kind of building up that muscle where we have engineers who are product-minded engineers and I kind of think this is um a way of the future where engineers are able to stretch into other dimensions.

You've seen this with design engineers. Uh I've I've kind of wrote about product engineering in the past. I think there's a healthy blend or mix of these type of people that can do some of the product work, do some of the design work, do some of the engineering work. With that being said, of course, there's great uh a great product manager can make a huge impact on a product, especially an established product where they kind of know the the levers and the knobs that they're optimizing for versus more of the the generalist at an earlier stage startup. Um, you know, both companies move really fast.

Both companies care about building great software. And, uh, I've I've learned a lot over five years at Verscell and I'm already learning a lot just a few weeks in at Cursor. Yeah. And I feel like the generalist now has like it used to be like when a startup scales a lot of employees and and first of all like a lot of startups don't have to hire that many people anymore, right? Because AI can do a lot of work.

Yeah. Yeah, but also feel like the people who can wear all hats at a startup, you know, for lack of better words, now have a much longer, you know, shelf life, right? They can they can scale themselves and still be super valuable even at like a anthropic or even like, you know, an open eye, right? Yeah. I have a a good story and anecdote from my first couple weeks at Cursor, which was we wanted to send a refund to a customer or a group of customers and send out an email.

So talk to Stripe, send out an email. And I almost had to delete the SAS software part of my brain for this because I sat down with one of our engineers, Eric. And I was watching him kind of go through this task and I was expecting, you know, he was going to log into some tool and the tool was going to help him kind of submit the refund or and go through and submit the email. And he was running a script and I thought, hm, there's no way that that's going to work, right? he's probably going to have to think about, you know, doing a dry run of the script so we can validate things.

What if there's a network issue and something fails? You're going to have to like log the state as you're going through the script so that if you've processed a hundred of the thousand records, you know, you don't repeat the 100 and oh, we got to make sure that there's not issues with the deliverability of the emails and we probably want to test what the email looks like. It sounded like a lot of stuff. And I just watched him kind of systematically address all of these things and think through these things with an engineer's mind and build a very robust piece of software. It seemed like a script to me, but really it was customtuned software for exactly what he needed that integrated with Stripe.

It integrated with uh an API to send emails. And it worked really well. He tested everything, did dry runs, tested it to himself, you know, tested the failure states, and then took that and committed it into a repository of other scripts of like custom software that had been built that he had used for these tasks. And it was like it's like giving an engineer these incredibly powerful tools to basically do any task and connect with any service. And I thought that was really interesting.

So he didn't have to click around any UI or anything. He just like ran the script and it's done. Yeah. Yeah. Wow.

Yeah. I mean I mean that that's what the world is moving to, right? Like a bunch of like uh scripts or sub agents that can just do specialized tasks for you and then you can just, you know, you can go drink a coffee or something while while they're doing it. Yeah. And like that whole example is only possible with a great engineer who knows how to use their tools, knows the right questions to ask, has a a great deal of care for how they use those tools together, and they can do amazing things.

like the agent is just multiplying their productivity. That's amazing, man. Uh I hope we all become like Eric. Yeah, same. I'm trying to I'm learning from him.

Yeah. So, uh so, uh where can people find your uh you know, new cursor teaching content or you know, is it coming out soon? Yep. My website's le.com. I post on xx.comrob.

Uh that's primarily where things will be at. I also do some stuff on YouTube. Awesome, Lee. It was so great to talk to you again, man. Like I I I think I I think you're actually like a renaissance man.

You know how to build stuff, but you also know the developer marketing side. So strong strong hire from Ker. They're lucky to have you. Thank you. I appreciate that.
