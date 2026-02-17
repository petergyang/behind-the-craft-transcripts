---
title: "Inside How the Claude Code Team Ships at Lightning Speed | Cat Wu"
guest: Cat Wu
publish_date: 2025-09-14
youtube_url: https://youtube.com/watch?v=jmHBMtpR36M
channel: Behind the Craft
keywords:
- coding
- leadership
- design
- execution
- ai
---

We don't use many Google Docs for quad code. A lot of our best features was like an engineer prototyping an idea, shipping it to dog fooding, and we just hear what the feedback is. Like, do people immediately understand it? Are people confused? Is it buggy?

Or do people just like love it? How do you guys think about you? If you see a change in the Sweet Bench score, it's not always obvious what caused the change, and you actually have to read through these pretty gnarly transcripts. And a lot of them we get a new piece of feedback every I want to say like 10 minutes or so. We love negative feedback.

Like we don't want platitudes. We want to hear what doesn't work. Do you have like a vision doc or something for clock or like what do you think the product will look like a year or two from from now? A year or two is a really long time. I can talk about the next few months.

Okay. Welcome everyone. My guest today is Cat the product lead for clock code. Uh, Cloud Code is my favorite AI agent. So, I'm really excited to talk to Cat about how the team ships so fast, how she uses cloud code personally to do product work, and what her vision is for the product.

So, welcome, Cat. Thank you so much, Peter. Excited to share more about cloud code with your audience. All right. So, um, why don't we start with the vision story for cloud code and how you kind of got involved.

Yeah. So um quad code started as a project that uh Boris was tinkering with to better understand our APIs and to see how much of software engineering he could augment and at the time I was I was spending 20% time adding RL environments and I found that cloud code could make me a lot more efficient at it and that it was really good at integrating with all the tools um that we have internally and So, I was sending him a bunch of product feedback, um, things that I wanted to change in the tool, and when we made the decision to ship it externally, I was so so stoked to work on it full-time. And since then, it's been pretty widely adopted um, externally as well. And so, we're really excited to uh, continue to invest in it, make it more featureful, make it work across heterogeneous developer environments, and to make it more accessible. Awesome.

So, so it wasn't like some part of a grand strategy. It just kind of he built a little tool that he tinker with and then he got involved. So, what happened? Yeah. Yeah.

Exactly. Like he built the tool and other people on his team started using it and then the rest of the org started using it and then it crossed over into research and then it actually started to cross over into tech adjacent roles like data science and product management and product design. So, it had a very high viral factor internally before we launched it. Okay. So, you know, when I first started playing with Clockode, I installed in the terminal and then I was like, what is is this it?

This is the product. And uh but as I started using it more and more, I discovered more and more features and it kind of felt like uh kind of mastering a video game. It kind of felt like it doesn't kind of explain everything to you right off the bat, but like the more I got into it, the more I felt like more powerful, like you know, kind of kind of power user. So I I I guess was this like kind of intentional and do you and the team have any of the product principles in building this tool? The beauty of the terminal is that it can through the terminal cloud code can access almost everything a developer can and this is what makes the onboarding so smooth to the tool.

If you're used to calling like the GitHub CLI or the data dog CLI or literally any CLI tool, you immediately know that cloud code can do it. And so this just makes it really fast to get started. The terminal is also a very minimalist form factor. So unlike a web app, you can only use ASI. So you can only fit as many characters are available on the screen.

You don't have the option to add any buttons. And as a result, we've been very um pragmatic and very almost like brutal about what features we decide to showcase and what features we don't because there's such minimal screen real estate. Mhm. As a result of this, the app form factor is very light and so it means that you don't get overwhelmed when you first start, but it also mean but because we've built it to be very extensible. There's a kind of like arbitrary depth as you get started.

Our design philosophy is to make sure the CLI is very very simple to on board to. We have this philosophy that for new features there should be no onboarding UX. It should just it should be intuitive via the feature name via like a oneliner description what it does and you should be able to just get started. And then we also think that the CLI need to be very extensible because developer environments are very different and we want to expose tools so that every engineer every developer productivity team can customize it for their own setup. Got it.

And so that's why we have things like hooks and custom slash commands and sub aents and stuff like that. Okay. So kind of like um do the simple thing first. No no no like you know crazy onboarding flows and also making it composable and extensible. Yeah definitely make it very simple to get started but able to handle complexity over time.

Got it. you guys have been have been shipping a lot like there's new features coming out all the time and I'm just wondering how the claw code team actually works like you know on a given week like like do the engineers like basically ship features end to end themselves and if that's the case then what's your role as the PM you know how do how do you guys work our team is very strong um a lot of very strong product engineers who love to have endto-end ownership over features the the way that things normally work is there's some like high higher level design principles that we want to follow. Like we always want the tool to be customizable, but within that there's a lot that you can build. And a lot of our best features was like an engineer prototyping an idea, shipping it to dog fooding, which is so that hundreds at this point maybe like a thousand internal employees can try it out. And we just hear what the feedback is like.

Do people immediately understand it? Are people confused? Is it buggy? or do people just like love it? And for the features that people love, that that's a really strong signal that we should fast track it to um sharing it with the public.

And so a lot of the features that you've seen that we have shipped, a lot of times we've gone through two or three iterations of it internally before we made it public. And there's a lot of features that we've played around with internally and just like decided not to ship. I think as a PM it's tricky to be a PM for a developer product because at the end of the day the developer is the end user and so I see the role of the PM as one setting like the broader direction of okay how much how much customizability do we expose what is like what is the minimum bar or what is the like aspirational bar that we want our product features to fall between and shephering it through the process. It also in the age of AI tools, a lot of the PM role is around pricing and packaging as well. So just making sure that uh developers can focus on making the best coding experience possible and then the PM's role is to make sure that it's accessible for the world.

Okay. So is there like even like a product review process or you just kind of they they prototype something and then it gets traction internally and then it's like okay let us do it. Is that how it works? Yeah. Yeah.

For our larger projects there's a product review process and so if you if you look back at cloud 4 we've released ID integrations with VS code and intelligj. And so for those it was a very clear decision that we wanted quad code to meet people where they worked and have more context about their tools and so made a decision worked on it for a few months and then shipped it. But for smaller features such as a to-do list or plan mode, these are ideas that we've talked about internally. And they didn't require PRD because the hard thing is actually to figure out the right form factor. It's not like an integration challenge.

It's a design the tool the right way with the right prompt challenge. Got it. Okay. Here's a quick note from our sponsor, Laura Keat. Now, one of my biggest pet peeves is sitting on hold with customer support or mashing buttons just to get to a real person.

That's why businesses are turning to Laura Keat, an AI customer support concierge that works 24/7 across chat, email, and voice. Doesn't just point to help articles. It actually resolves issues. Loret knows your company systems, policies, and workflows to solve problems end to end with 99% accuracy. And when a real person is needed, it knows exactly when to hand things off.

Some of the biggest names in fintech, healthcare, and energy are already using Luret, and they've seen customer satisfaction jump by 30 points. Switch by October 31st, and Lori will even buy out your existing support contract. So, check them out now at litcx.ai/pater. Now, back to the episode. I think Boris tweeted something about, well, not three, he posted on threads about how he designed a to-do list, and it was just like him prototyping clock and trying different form factors, right?

And then you guys all tried it. Is that how it went? Yeah. Yeah. There's a long history for to-do list.

So Sid actually was the first person on our team to start experimenting with to-do list. And the problem he was trying to solve is we noticed that a lot of people use quad code to refactor or to rename variables or these like other larger tasks. And these tasks often involve making 20 or 30 changes. and cloud code would sometimes do the first five and then forget to do the rest. And so we were we were trying to figure out how do we force the model to actually complete these tasks.

And so Sid came up with this great idea to actually just force the model to write down its task kind of like what a human does as they go about their day. And we were totally blown away because actually just by forcing the model to write down its tasks and reminding it, hey, you can't stop until the tasks are done, this actually forced the model to go through and do all 20 or 30 items without any early stopping. And so this was like bottoms up uh by SID. And then the to-do list has now been augmented quite a lot. We've in the past it was just quad code would write the to-do list in the transcript and so you would see it fly past your screen but it wasn't persistent and then a lot of people we noticed that a lot of people were actually just using a to-do list to track the model's progress and this is actually this actually meant that you actually want it to be stickier like you don't want it to fly off the screen because otherwise users who happen to look at the terminal don't what the agent's working on, they have to like scroll up a lot.

And so the the new form factor that Boris is experimenting with was actually showing like having the to-do be more persistent so that you can call slashtodo at any point. Yeah. Yeah. I I I I use that. Yeah.

I think there's like some some shortcut key to see it see how it's doing at any point, right? Yeah. Totally. And we've like experimented a lot of form factors along the way that we uh didn't end up keeping. So things like we have these like cute little thinking words and at some point we put the to-do list in there and then people weren't super happy with that and so it it's been a iterative process for sure.

How do you uh when you iterate you you have you have obviously the you know anthropic employees that you get feedback from but do you have a customer community too or you just look at Twitter or how do you how do you get feedback? Yeah, we're very lucky that Anthropic employees are extremely vocal about cloud code feedback. So, we have an internal chat with about a thousand maybe more anthropic employees who've opted to join. So, it's not people aren't in it by default. They've just decided to join.

And we get a new piece of feedback every I want to say like 10 minutes or so. And it's always really high quality. So we are very very very lucky that we get such a high volume of feedback before products even get out the door. Um once products are shipped we look at feedback from both our early enterprise adopters and also occasionally from Twitter. Um I I think our enterprise adopters are probably the highest signal for me right now.

There's about 10 companies that we work very closely with who are who we tell, hey, just be just be as loud as possible. Like if you run into any issue, please put it in the chat. We might not be able to fix it immediately, but we want to hear about it. We appreciate it. And please, please, please share negative feedback.

We're very insistent that we love negative feedback. Like, we don't want platitudes. We want to hear what doesn't work. And thankfully uh these users are both very engaged with cloud code and very happy to share what's not working for them and we've held ourselves to a pretty fast SLA for fixing a lot of um a lot of these issues. So, so for issues that we decide to prioritize and decide to fix, we'll turn it around in a week or two.

You know, like in a more traditional company like the PM has to maintain a bunch of artifacts, right? Like specs and road maps and maybe like the vision dock or something and and uh uh and also like keep track all the feedback. So, do you have any of those stuff or like do do you uh use cloud to summarize all the feedback or how do you Yeah. Yes. Um, it's an interesting question.

We actually get so much feedback that what we should prioritize becomes pretty clear because you'll hear it 10 times. I know this isn't a super satisfying answer. I wish I could just say, "Hey, we like rank, we track every single thing and we like rank it all." Yeah. But I think in practice what happens is we get someone posts a GitHub issue and they say that something's broken and then there's like a hundred thumbs ups on that GitHub issue and then our sales team DMs us and says hey like for these three customers this thing is broken. So normally when a big when something's a really high priority it's very very obvious.

Um there are a few ways in which I do use cloud code though to help me with this. So one is we've connected cloud code with slack. So it's really easy to synthesize feedback. So for example if one customer asks us for the ability to customize models by sub agent. I'll just ask cloud code hey which other customers have asked for this?

That way I know when it's built we're telling the right people that we've done it. And then I also can ask cloud code, hey, like also look at our GitHub issues and see if there's any GitHub issues about this. That way when it's built, we close out all the GitHub issues. We also use cloud code to automate as much of this handling as we can. So for example, cloud code will help us update the docs.

So it'll do a first pass at docs and then we'll clean up the remaining 10% to make sure it's very accurate so human still reviews it. And then we also use cloud code to dduplicate issues on GitHub. For a lot of issues, we see five or more cases of it being filed over and over again. And so this helps us just maintain the the backlog and make sure that our community is kept up state. You probably have all your documents in like MD files, right?

You don't have any like Google Docs. If I just have one there. Yeah, we don't use many Google Docs for quad code. No. Got it.

Okay. It's also nice because our codeface is actually pretty small and so even if like I think normally people use Google Docs to document functionality or why we built something and I think for a lot of quad code features the why we built it is sometimes it's just like in the PR and so if you ask it hey what was the original inspiration for to-do list? uh search GitHub, it will be able to just find the original PR and like tell you it. And because the code base is small, if you actually want to know exactly how something's implemented, it's actually a lot faster and more accurate to ask cloud code uh while it's in initialized in that repo rather than read a doc that um might be out of date. Yeah, that's a really good point because the source of truth is the codebase, right?

And like you know, this model is really good at summarizing stuff in the codebase. So, totally. Yeah. And the code base is small. Do you check in code yourself?

Like make some copy tweaks or do you check in features? Yeah. Yeah, I do. Um, so I used to do this a lot more when I first joined as the PM and there's always like smaller features that are just faster for me to do than for someone else on the team to jump in on. So, like two months ago, we had this collaboration with Rick Rubin about vibe coding and he one of the ideas from our brand team is that we should have a vibe command that referenced some of Rick Rubin's writing about the topic.

And so, it was just much easier for me to add it than for someone on the team to add it. And so, just like take that on. And we've also seen this with other folks on our team like Megan who's our amazing designer. She used to never commit code which is very normal for a product designer. And when she started using quad code more she started making PRs to console which is the our management um it's our product for managing API keys and other API usage and she's also made PRs to quad code itself and so it definitely lowers quad code definitely lowers the barrier for everyone to make PRs especially for simple changes.

Yeah that that's amazing. I mean like that that that is a dream, right? To be able to for designers and PMs to be able to check in code directly make impact on the end user experience without just writing a bunch of Google Docs like that's a dream. Yeah, totally. And it also makes it easier to audit flows too because we have a lot of branching logic.

So, for example, if you're on a max plan, there's a lot of conditions where we'll like show you a rate limit warning or like show you an upgrade message or and this differs based on every plan that you might be on whether you're on one pi or 3P API or cloud for enterprise or proumer. And so, cloud code also makes it really easy to audit these flows because you can just ask it, okay, trace the code for each of these and tell me exactly what happens. And then you can got it. You can feel pretty good that it's accurate if um it comes back accurate. Got it.

Okay. Um so probably entire team talks the clock hole the the most during the day. Yeah. Um let let me ask you let let me ask you there's been a lot of hot takes about evals recently on Twitter. Some people say it's like you have to have like super robust evals before you launch anything.

Some people are like ah what whatever. like how do you guys think about eval and and and run stuff before you ship? Yeah, eval are really hard. Um, so there's two kinds of evals that we care about and they're both imperfect and we're both we're trying to get better at both. So the first is endtoend evals.

So you can think of this as running sweet bench on new quadcode harnesses to make sure that we're not degrading performance. And so this this is something that we regularly do both when we're making large changes to the harness and when we're testing out new models. This isn't that granular. So if you for example see a change in the SWEBench score, it's not always obvious what caused the change and you actually have to read through these pretty gnarly transcripts and a lot of them to be able to figure out themes and what went wrong. We want to make this better, but we don't have a silver bullet right now.

Um, the other kind of eval that we think is really important to make is triggering evals. So, what that means is there's a lot of situations where cloud code can decide whether or not to use a tool. And ideally, cloud code can make these decisions without the human. Um, that that way things just feel more magical to the human. So for example, uh claw code supports web search and we want to make sure that web search isn't overly eager.

Like if you ask it a question, you don't want it to like search the web 100% of the time. Yeah. But you want it to search it if you're saying, hey, what was the latest like what was the latest React release and what new functionality is available there? And so actually tuning this triggering is pretty hard to do. And so th this is a situation where both it's really straightforward to make an eval because you know you can clearly articulate when web search should and shouldn't happen and then it's also really easy to grade whether or not web search did happen.

Got it. The harder emails are capability ones like what what kind of capabilities like give me an example. Yeah. Yeah. So if you want to evaluate, hey, is this harness better at data science work than the last one, that is actually much harder to test because you would actually want something closer to a SWE like setup where the model has access to a really big underlying data set, has the ability to write queries against the data set, iterate on those queries, and you have a you need to have a gold standard answer and you need to make sure that there's no ambiguity in what the right answer is.

Yeah, got it. Okay. The the web search one um you just kind of look at the like maybe look at the past uh when the web search was triggered and see if it makes sense or not and maybe have a score or or something. Is that kind of how it goes? Yeah.

Yeah. So there's for web search there's a spectrum of when web search should never trigger and when it should always trigger. And so to start, I'd recommend codifying the black and white areas in an eval. There is always a gray area and I would probably just take care of those afterwards. Yeah.

And and and and I mean the truth is like you have such an engaged community that like your your users are keeping you honest all the time, right? Like so you can look at some scores but like your users are just keeping you honest about what is working and what is not working. Yeah, that's true. Yeah. Like even for to-do list, we spent quite a bit of time making sure that it was triggering well because sometimes cloud code would want to write a to-do list for one item and then check it off.

And this is a clear case where a to-do list shouldn't have been used because you don't really need this form factor to track getting done one task. Just do the task. Got it. This is a situation where an EVA would have been really helpful. Like you can make sure that you can take the trajectory where the agent um create a to-do list for one task, put it into your eval suite, and then make sure that either the agent doesn't make a to-do list item or if it does make a to-do list item that it's like three or five items.

K, can you tell me some interesting stories? I mean, you've been on this journey of CLCO team, right? Is there any like interesting stories that the team laughs about? you know, like, you know, I think I heard a story about you guys shipping a feature during a me meeting. Tell tell me some fun fun stories on the cloud cloud team.

Yeah. Yeah. When I think about the team, I think of just like just people who absolutely love developers. Um, some of our some of our favorite memories are when we first launched. We wanted to thank our earliest users.

And so if anyone accidentally mentioned the word swag or stickers while they were using cloud code, we would send them Sid built this. We would send them to like a sticker portal where they could enter their address and we would actually mail them a sticker uh a set of stickers and someone actually reverse engineered the code or like looked at our source maps or something and found this and as a result we got like 500 or so inquiries where people were like submitting their addresses and it was just like a cute little thing that a cute little Easter egg that we wanted to embed into the like for no other reason than to just like thank our earliest, most engaged users. Yeah. We thought that it would only take an hour for 12 of us to send 500 stickers, but instead it actually probably took us eight hours. Wow.

Okay. And then we just we we were originally going to make dumplings and we ended up just ordering takeout and mailing stickers the whole time. Wow. Okay. It's probably have to remove the feature afterwards because you don't want to be sending stickers all day.

Yeah, we we thankfully did cap it at I think around 500 or so. Well, send send me a sticker after this. I I I want a sticker. Yeah. Oh, we have a lot.

We've been iterating on them. Now we have think harder stickers and Ultra Think and there's there's a bunch of memes, right? Like for example, Cloud Cole will will be like they'll make it make a to-do list and they'll be like, "Oh, it'll take it'll take an engineer. It'll take me like two weeks to do this and I just d in like 10 minutes. Yeah, I've seen that happen before.

Yeah. Yeah. We need to teach it a better sense of time. I think it's quoting human hours and then it just doesn't cuz I think it's only seen human hours on the internet. So, um I mean sounds like there's some pretty good vibes on the team and um I know you're hiring a PM for the cloud team.

Uh you know, what kind of person is looking for and what does the interview process look like? We're looking for someone who loves developers, just like loves like ideally has been a developer before or has worked on developer tools for a while. Ideally, we'd love to have someone who wants to make sure the SDK, the cloud code SDK is the best way to build agents. We want to create more agents in the world and we think the cloud code SDK is the fastest way to prototype an agent and bring it to production. And we're also looking for someone who wants to grow the ecosystem.

So we've noticed a lot of developers are customizing their setups. They're building custom slash commands and custom hooks and status lines. And we want to have like a hub where people can share all of this, where people can review each other's customizations, where someone can oneclick install it to their own quad code instance. So I I would say we're looking for someone who's both able to steward the SDK as the best way to build agents and two to grow the community to make it to make these customizations easily sharable. So probably someone who's already pretty like into cloud code then.

Yeah, we're definitely super power user. Yeah. Yeah. And do you guys uh maybe for cloud code or just anthropic in general? Um is there like a like during interview process there like hey can can you build something here or like you know can you add a fee feature using cloud code or is there some live demonstrations involved?

Ooh maybe we should do that. We do ask folks to spend a bit of time in the products and give a critique of what they would like to see improved. Okay. I think normally we can get a pretty good sense for how engaged someone really is in the tool uh based on that. But that would be fun.

Yeah. Or we're or we're looking for people who are like making tutorials on YouTube, you know. Just kidding. Yeah, totally. Yeah.

Okay. So, uh let let's kind of let's do a lightning round. I want to hear kind of like uh some some tips on how to get the most out of cloud code, right? And maybe how you use it per personally. Yeah.

I the three tips I would share are one demos not docs. Quad code makes it so easy to make prototypes that if you're thinking about hey should we build this feature I I would actually ask hey is there a way like for quad code to prototype that feature for you so that you can get a feel for how useful it is before writing a multi-page doc on it. The second thing is I would treat cloud code as an eager new grad software engineer. So I would think of it as something quad code as a tool that's very responsive to feedback. I sometimes see people give quad code a really ambitious prompt and then when quad code makes wrong assumptions they kind of give up.

But instead, I would say if you notice cloud code's doing something wrong, just tell it that it's doing it wrong the same way that you would give feedback to to a human. And it's really receptive and it'll normally um change its direction and incorporate that feedback. And then the third thing is there's a ton of value in investing in your CloudMD file. CloudMD is the equivalent of memory for cloud code. Every time you start a cloud code instance, the cloud MD is included in it.

So you can kind of think about it as edge onboarding. It's everything that you would tell someone who's new to your codebase and who you want to be productive off the bat. So it's great place to mention the architecture of your app, any gotchas, how you like to test and verify work, anything that you would tell a new hire. There's kind of like two approaches to cloud MD, right? You can just type slashinit and it'll like scan the codebase for you and add a bunch of stuff.

But uh I I kind of like how Megan uses it. She she has like a she's like I'm a product designer. You got to like overexlain everything to me. Like it's kind of like a more per personal like style kind of cloud MD. Yeah.

Yeah. Yeah. Totally. So the whole system is very configurable and so you can have uh a quad MD for the entire repo and then you can also have your fully individual cloud MD and in Megan's case for for a cloud MD that describes who you are and your role at the company and that applies to all projects. You can also have a global personal cloud MD so that cloud code has this context no matter what repo it's working in.

Got it. Got it. Okay. And in terms of the in terms of like the the second tip that you shared about treating as an overyear engineer, I I found that like the more time you do planning actually the better the results are. So like so like actually making it write like a pretty detailed spec about what you want to build and like looking over it and then also like asking it to like make a to-do list and then looking over that.

Totally, you know, that that's that's been super helpful for me. Yeah, totally. Our users love plan mode. So, actually, yeah, maybe a funny story is we originally knew that people wanted plan mode because people kept saying, "Hey, just like tell me what you're going to do, but don't write code yet." And we kept being resistant to adding plan mode because we wanted to teach users to express what they wanted in natural language. And when you do express in natural language, COD will make a plan for you even outside of plan mode.

Over the course of one or two months, enough users said that they just wanted to be really explicit, that they wanted a shortcut to it that we caved and said, "Okay, okay, we'll we'll add an explicit plan mode." But we were really hoping that we could teach users to directly ask the model to plan. And maybe maybe in the future when the model is better at following these kinds of user directions, we might we might remove it. Uh yeah, I mean it's just like the models these days are just too eager to code. Like it's like even even in plan mode when I'm like, "Hey, can you make a plan for me?" And then it'll make a plan. They'll be like, "Oh, by the way, I can start coding right now.

Do you want to start coding?" Like, "No, stop coding. I got to review your plan first." Yeah. So it's just too eager, I think. Yeah. Yeah, totally.

Do you have like a vision doc or something for cloud code or like what do you think the product will look like a year or two from from now? A year or two is a really long time. I can talk about the next few months. So we we want to make sure that the CLI continues to be the most powerful coding agent and we also want it to be incredibly customizable so that it can work in any developer environment. it can integrate with all your existing tools and you can and that we create an ecosystem around the customizations.

The second pillar is we care a lot about growing the SDK. So in general we would love for there to be more agents in the world. not just coding agents but legal assistants, EA assist like personal assistant AIS, uh, health health assistant AIs, financial assistance, stuff like this. And we hope that the cloud code SDK actually makes it easier for all the companies building general agents to get started. And we're seeing the initial signs of this.

There's many companies that we're working closely with who are building non-coding agents on the SDK. We want to make sure these companies are incredibly successful and and will tell their stories as their products come to market. Yeah. And the third bucket which is the most amorphous is bringing cloud code out of the terminal and making it more accessible to more audiences. So right now we primarily target professional developers.

We will continue to focus on professional developers because that's the core market of quad code. But increasingly we find that it adds a lot of value to tech adjacent folks. So data science, product management, product design and we would ideally like a form factor where uh these folks can get value too and increasingly to expand another to expand out by another ring to folks in marketing, folks on sales who we think will also benefit. Yeah. Yeah, cuz like people in anthropic are all like designers, marketers are all using this stuff, right?

I mean, there's a few we want we want to onboard more. Right now, it's still really hard to explain a terminal interface to folks who haven't used it before, but I think the core primitives are very general. So, I'm very excited for the future. And doesn't requ like like, you know, I I just did a recording of uh Alex, right, who basically runs his life like he runs a bunch of tasks using cloud code. And you don't need to have like some crazy prompting.

You just have to talk to claw to figure stuff out. Yeah. Just like can't do you just tell it. And if if you're confused like I recently onboarded one of one of the folks on our marketing team onto cloud code and she was like you know I've never written code before. I don't even know I I don't know what I should ask.

And I was like okay just ask it to build an app. And then quadcode goes with like some purpose and quad goes off to build an app. She's like, "Okay, I have no idea how to run run this app." And so I told her like, "Hey, you can just ask Quad Code." And she did. And I told her how to run it. And she was like, "Whoa, you mean any question I have, I can just ask." And I'm like, "Yeah." And it's really cool because it kind of just works.

Yeah. Yeah. Yeah. And and I I I love how you guys uh shipped um explanatory style to kind of like help people become more technical too as as they're using this stuff. Um my my one feature request actually is like to be able to use cloud code from my phone cuz like like this this stuff is very agentic, right?

Like it will work for like 10 minutes and I can just go like play with my kids. So have some sort of like you know thing later on the phone would be really really cool. Totally. I I agree. This is also why we built our original inspiration for hooks is kind of related to this.

A lot of people wanted to get Slack notifications when Quad Code was waiting on their response. Yeah. So yeah. So Hooks made it customizable. So for example, if you wanted to get a text message every time Quad Code was waiting on you, you could configure a hook for that.

But I also hear you on the broader request to run it remotely. Yeah, I haven't I haven't played with hooks yet. I still have the list of features to dive into. But but yeah um you know I I love how you said like you know two or three years is too long. You know you know what's ironic just to close like I feel like the most innovative teams like like yours are just kind of iterating and then some of the more traditional teams are like oh we got to have like a three-ear vision and we got to go there.

It's feels like very you know that that that's just kind of the feeling that I get like just just put yourself out there and like you know iterate with your users like that's how you build innovative stuff. I agree. We're very pragmatic. So yeah, we we try to build the products that we wish we had today. And because the models are changing so quickly, we think that it's really hard to predict more than 6 months in the future.

We think it's really important to build products for the next generation of models. Yeah. But generation capabilities don't become obvious until a few months ahead of time. So I I don't know how people plan further than that. Yeah.

Yeah. Yeah. Okay. So, like any closing words or advice for the PMs out there, you know, trying to become AIPMs or like, you know, any any kind of advice do you have? Yeah.

The hardest thing to learn about being an AIPM is having a really good grasp of what the models are capable of. There's it's hard to build evals. At the end of the day, a lot of it comes down to intuition. Like if you want to build a feature, you should probably actually have a really good sense of intuition for whether or not the model is capable of supporting that feature. And if not, how far away is the model?

Is the model 80% there and you can prompt the last 20%. Or is the model only 10% of the way there? In which case, you should actually probably just check back in in three months or six months. Just three months. Yeah.

Yeah. This is the hardest skill and the rarest skill. And I think you have to have that curiosity to push the model, right? To try to make something happen that you know can't do this or or not. Just try to make make it work.

Yeah. Yeah. Exactly. Like you have to know if the model fails, is it because the context was wrong? Is it because you're not you're using maybe the wrong model for the task or is the model at the core un not capable of it?

Got it. Okay. That that's really good advice. Yeah. Um All right.

So, where can people find you online or do you want people to Yeah. Where can people give you feedback? about cloud hub. Yeah. So, two places either underscore catw on Twitter or if you have uh technical feedback, please feel free to open a GitHub issue and we'll we'll look into it.

Okay. All right, Cat, this is awesome. I I really learned a lot talking to you and I'll be using Cloud more and more, I'm sure. Thank you for your support and a as you have more feature requests, please let us
