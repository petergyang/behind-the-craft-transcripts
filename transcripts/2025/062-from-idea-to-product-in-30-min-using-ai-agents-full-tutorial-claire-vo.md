---
title: "From Idea to Product in 30 Min Using AI Agents (Full Tutorial) | Claire Vo"
guest: Claire Vo
publish_date: 2025-05-18
youtube_url: https://youtube.com/watch?v=ikyxK6i0AL0
channel: Behind the Craft
keywords:
- product-management
- strategy
- ai
- leadership
- culture
---

I don't say product management is dead because of doom and gloom. I say it's dead because I think you're going to be in a world of pain if you're not prepared for a shift in the next 18 months. I know lots of startups that have gone many, many years before hiring their first PM and kind of don't want to hire many. If you look at something like Devon, it is a language-based interface. You are telling a system what to do.

your ability to clearly articulate what to do in a way that a system can appropriately interpret it, access its set of tools and get the job done correctly is actually a really important skill. I tell all my engineering managers when they use Devon, I say, "Congratulations. I just gave you 10 interns." I would screenshot this. This looks great. Write me a purity I can send to my engineering team.

Boom. Nice. It worked. It's there. Okay.

Welcome everyone. My guest today is the one and only Claire Vo. Uh Claire is the chief product officer of Launch Darkly, founder of Chat PRD and also host of the brand new How I AI podcast. So, no product leader uses AI as much as Claire. So, I'm really excited to get a demo of her favorite AI workflows and discuss how AI will change product management forever.

Welcome, Claire. Oh, thanks for having me. I'm really excited to be here. Yeah. So So I think you're like the first person that I actually interviewed.

So So it's great to have you back. Oh, good. So we're we're back at it. So maybe we can get right into it. Like maybe you can show us how you build new products with AI.

Sure. Let's do it. Okay. We're doing the reverse how I AI move here. And I'm going to show you how I AI.

So I'm going to share my screen. I'll just walk you through how I think about building products and how we might build something actually how we do build things at chat prd. So this is chatpd AI co c co-pilot for product managers and it helps you write and draft product documents and do other product work more efficiently and with better quality. And you know, one of the uh features of chat prd is that there's a chat and then there's a a document mode. And the way we tune and improve the core experience is very similar to a chat GPT.

We have, you know, little user user ratings here. And so when somebody chats with chat PRD and has, you know, a good response either from a document or message perspective, they hit the thumbs up, thumbs down um button. We actually run a lot of AB tests and experiments on different models, different prompts, different configurations. It helps us figure out how to build these great experiences. And one of the things that I do is when you hit me with a a thumbs down um I ask specifically what we could improve.

So these are some common common um you know feedback that we get from users. It's too long. It's too short. It's inaccurate. And so we built this modal every time you hit the thumbs down button to say what we can improve.

Now I have a problem which is actually chatard gets a lot of thumbs up and I actually don't know what people like. So when you hit a heart or a thumbs up I just say thank you. I don't bother you and all I just all I know is that you liked it. I don't know what you liked about it or um how you know how you how you liked it. So I am going to actually build a PRD for you know thumbs up and then show you how we might flow that into a prototyping tool or to Devon to actually build this feature.

So, what I Yeah, what I would typically do, you know, I'm a lazy PM. So, I would screenshot this and I would probably because I'm a PM, I'm always in Slack. So, I would go in Slack and I would actually ask chat purity in Slack because I don't like to change um models and I say, "Hey, help me build a PRD for giving uh sorry, receiving um positive feedback, comments, and reasons for when people like a chat PRD chat response. We do this for negative feedback, but I want to do it for positive feedback as well. Okay.

So, I would like ask it's not super detailed, but I would ask chat pierd as sort of like my inslack um product manager to just write me PRD for this and it'll go off. It'll think through all it knows about chat pierd. it'll probably force me to be a better product manager here by saying, you know, Claire, this is just an idea. We don't have a why. We don't have a business reason.

Why why should we build this? Um, so it's going to ask me, you know, here are some sections I might improve, context, what's the problem statement, which is actually right. I have an imbalance in understanding user satisfaction, seamless integration into current workflow, etc., etc. I think this looks fine. We're a small team.

I don't need to go into it too too much detail. So, I'm going to say, "This looks great. Write me a purity I can send to my engineering team." Spoiler alert, my engineering team is is is AI, too. Yeah. Um, and and this is one of the prompting tricks I I do in uh a lot of how I use AI is I give it the context of what kind of team member it's going to go to next, even if that team member is an AI.

So, I often say like, "This is great. Write me a PRD." So I can send it to design. That's the PRDS that I would build to send something to like Vzero. Um sometimes if I'm going to send it straight to Devon, I'm going to say, "This looks great. Write me a PRD I can send to my engineering team." And what I found is that it will tune the content of the document to what they anticipate that sort of uh persona might.

This episode is brought to you by Vanta. Whether you're a startup founder navigating your first audit or a seasoned security professional scaling your GRC program, proving your commitment to security has never been more critical or more complex. That's where Vanta comes in. Businesses use Vanta to build trust by automating compliance for indemand frameworks like SOCK 2, ISO 2701, HIPPA, and more. And with automation AI throughout the platform, you can proactively manage vendor risk and complete security questionnaires up to five times faster, getting valuable time back.

Venta not only saves you time, it also saves you money. A new IDC white paper found that Vanta customers achieve $535,000 per year in benefits and the platform pays for itself in just 3 months. Go to vanta.com/peter to meet with the Vant expert about your business needs. That's vanta.com/peter. Neat.

So, it's going to go write the doc. It takes a little long to write the docs because we're now upgraded to GPT41 and it's just a real yapper. People love it. Product managers like to write but it takes a little bit longer time. So what I would do is I'm gonna wait for this to be written.

It'll come back and link me to the doc. What I would decide is if I need to send this to a prototyping tool and because the you know the modal already exists in my codebase because I already have sort of a component that I can reuse. I'm probably going to skip the prototyping step because it's like an unnecessary step in the workflow. Instead, what I'm very likely to do is take this PRD, export it. I'll show you how I do that and then send it directly to Devon who can actually write write the code for me.

Okay. Now, now it's writing the PRD here. Okay. So, you don't so you use Vzero for prototyping and you don't you don't actually use cursor or windsurf. You just go to Devon for coding for something like this.

Yeah. So don't don't tell my I love cursor. Um I've tried a lot of wind surf but actually since uh Devon has really improved over the past couple months and claude code came out I have dropped my cursor usage by like 70% or so. I still start fresh projects in cursor. sometimes things that I just want to explore or build myself or have an opinionated view on how to build.

But I would say seven out of ten times I'm going to Devon to start a PR for me. Um it's it's for me it's less about the technical capability of the codegen and it's actually more about the user experience. So, you know this, I'm very busy. Lady's busy. And so, I can't be synchronously working in an IDE all the time.

I'm actually not at my computer all the time. So, yesterday morning I went for a early morning walk. I'm not at my computer. I got like a ping from our support that there was a bug. I can't pull up an IDE on my phone.

I can't log into C even though it was a simple bug to fix. And so I but I can't at mention Devon and say go fix this bug for me and it happens elsewhere. And so it's really less about the quality of the code although I think the quality code is sufficient for most of the use cases. It really is about the synchronous asynchronous nature of how I can interact with the tool. Okay.

So I had this lovely PRD. Um I'm sure it's very very compelling. Yes. Uh I want to quickly indicate I liked a response. I want to specify what I liked.

I want to skip adding a comment if I'm busy, but still give feedback. That's pretty much that's pretty much it. So, what I would do here is actually export this as markdown. You know, RAI loves markdown. So, now I have a markdown file.

And I would actually go into my very long Devon thread. You can see what I've been working on. And I would say, Devin, um, I want to capture positive feedback commentary the same way we capture negative feedback commentary. Um, I'm going to pull up I have cursor. So this is the actual code for the um the negative feedback.

So I'll say we already have a component called shared feedback modal. We can use the same component for positive feedback as well. Love, like, and what else would I say here? You can make up the positive feedback categories. I don't want to think about that.

um review the attached PRD for other context. So I would attach this PRD and send it off and then what Devon Yep. Go ahead. It has so so you can read that component in your code, right? Yeah.

It has access to my repo. Okay. Okay. Yeah. Yeah.

So, uh Devon's friendly friendly. He wakes up. Um, and then what's really interesting about the um, the interface here for the product designers out there is it takes time. You saw my chat PRD. It t it takes a time to get a response and you know, you want to know that your message is acknowledged.

You want to know it's thinking. You're kind it's it's kind of like waiting for a colleague where you're like, are are you there? Do you have five minutes? And so you'll see here that pretty quickly it will come back with a plan and say, "Hey, here's my plan for implementing this." And then um it'll ask if I want to wait to confirm the plan or if it can just yolo go straight out and then um once it it continues, it will go ahead and build and issue the PR. So we'll wait for that to happen.

Wow. Okay, that's pretty cool. Let's see. and I'll pull up. There we go.

Okay. So, we can see here Devon's working on a plan. I can say wait for my approval. I don't want to wait for approval. So, it can just go and it'll actually build the plan.

And what it's doing behind the scenes is it's looking in the repo for the right um project. It's finding the code. It's designing a plan and then it's going to go ahead and make um make the experience. And what's really interesting here is I'll pull it over. I can also follow along here in the Devon console.

So, it's making it's making this plan. You can see uh it opened up the PRD and is looking through it. So, you can see it's working like an engineer would, right? It's like, okay, great. I'm going to look at the PRD and make sure I understand what it's achieving here.

I'm going to go ahead and search the codebase for that um component that it referenced. All that kind of stuff, which I think is really um really neat. And but I prefer to stay in Slack because I'm product manager. I don't know. I'm in Slack.

I'm on my phone all the time. So, all this stuff is happening behind the scenes while I'm just sitting here waiting for Slack to happen doing a fun podcast with with my friend uh Peter. So, so it should come back and what it will say is basically I've done the work or I have a question and it'll issue a PR with the code change and then I'll show you how I kind of go through the the code change process. Do you actually review the PR or of course of course I review the PR. I mean we're you're required to review the PR and have an approval in our codebase.

We don't deploy anything without review including AI stuff. So, we enforce approvals. So, it has to have an approval. Um, so once we get the PR, I'll show you how I do the code review. That's where where cursor maybe sometimes comes into play.

Um, and then I ship it. And and let let me while we wait, let let me ask you like I I noticed your Slack channel is is only like a bunch of apps and bots. Like, do you have like real humans working for I do. I actually closed them out so you wouldn't be distracted by uh by the real humans. So, for chat PRD, I still by far ship the most code.

If if you haven't guessed, we have um one and a half sort of like one full-time, one part-time engineer global that works with me on chat PRD. And then I have um a part-time growth person, although she's on uh leave right now. She just had a baby. And then I have a friend that's doing fractional enterprise sales for me. That's awesome.

Yeah. Let let me ask you this. Like I think a lot of PMs want to, you know, build something on the side, have a side hustle. Like how do you find people these people to help help you? Oh, how do I find people to help me?

Yeah. So, I actually found them all different ways, which is kind of fun. So, the um engineers, I use a service top called Top Tall. I used Top Tall when I ran my last startup about 10 years ago. Had a really really great experience.

So it allows you to hire engineering talent globally and the I would say from a product perspective I think their onboarding is pretty amazing. It actually I I um hired these engineers July 4th last year. Maybe you can empathize with this because it was like July 4th weekend. I was with my kids in Santa Cruz and I was like coding because we had this major bump in users and there was all this stuff I had to handle and it was a holiday and I needed to spend time with my kids. I was like what am I doing?

This is bonkers. This product is profitable. Claire, you're allowed to hire people. And so I submitted sort of a request for engineers that were comfortable in our stack. same day had interviews and next day hired them and they've been working with with me for about a year.

So I hired engineers through sort of a a talent connection marketplace. The growth person that I work with, Alisa, you may have seen her on our YouTube. Alisa made a YouTube video about chat PRD. Oh. About a year ago and somebody sent it to me.

It was like somebody made this amazing YouTube video about how great chat PRD is. And so I just emailed her and and thanked her for making the video. It was very very good and very nice. And she said, "Well, if there's anything you ever need, let me know." And I said, "Yes, can you teach me how to be a YouTube influencer and help me with some of my marketing?" And so she's been helping with our newsletters, our social and growth, and our our video marketing ever since. So that was sort of an organic user.

And then uh my buddy Travis and I used to work together at Optimizely. He ran sales. I ran product and I grabbed coffee with him and I said, "Dude, I think we can get this thing to like a million in ARR." Yeah. With just us. And he found that very interesting, an interesting problem to solve.

And I said, "I have too much enterprise inbound to manage. I can't do it during the day. I have work to do." And so he helps manage um my my customer relationships, including enterprise prospects and onboardings and all that kind of stuff. Wow. Yeah.

I I I love the Elisa's example in particular because like she just made a video and kind of like didn't ask for any new permission and then you found her just through proof of work. I didn't ask for I didn't you know ask for permission asking her to do stuff and you know I get a lot of people reaching out and saying if there's anything I can do with chat purity I'd love to be involved. Two things that I think Alisa did differently is she gave me very specific things she could do for me. like it was very obvious the particular value she would bring to the product. Not like if you think of something let me know.

It was like yeah this is what I can do for you. And two I only hire people that I'm going to pay. Like I'm not going to hire unpaid interns. I don't do volunteers. Like I only hire people that pay and so I want those people to be incredibly high leverage in the business and they have to be able to add something I don't have and I certainly think Alisa does that.

Okay. Awesome. All right. Let's let's go back to the Slack. It looks like it did something.

Yeah. So, it made this nice little plan here. Let's look at it. Um, so it's going Oh, it's like a 14step plan. Very good.

I would have just yoloed in the code. Um, so it's going to create a new branch, update, positive feedback options. I like these. It was clear, actionable, concise, relevant examples, good tone. So, it gives me a good sense of why somebody would like something.

It's going to modify to have a positive or negative feedback type. That's smart. Extensible works for my use cases. Don't have to create a new component. And then it's going to update it uh to accept the rating parameter.

Go make sure it's updated everywhere and uh test it and push a PR. So I think it's going to do that. In a couple minutes, we'll get hey Claire, you have a PR waiting notification. Then then you can just test it test it locally and then you can merge it, right? And then I can just test it mo locally and merge it.

I I do look at the code. So, one of the things that I definitely do is I pull up the PR locally, I run it locally, I test it locally, and I actually do look at the code to see if things make sense. I would say with Devon I get 80% hit rate on good quality nailed the product requirements and uh does it the way I would do it in terms of extensibility but occasionally uh it does something that is incorrect and so I sort of have to give it feedback in the PR or you know probably one time out of 10 I just trash the branch and move on move on with my life. Oh and it's pushing it's pushing the PR right now I think. Okay.

So, so maybe we'll check in in a couple minutes, see what come comes up with. Great. Um, so let me ask you while we're waiting. Um, so like you know the reality is like a lot of PMs still have to make a bunch of internal documents like strategy and and like this kind of stuff, right? Like they're not like as much as we all want to just prototype all day like that's not the reality of the job right right now.

So I'm also curious how you like work on like something you know like I I I don't know. I I feel like PMs think like pro strategy is like this like you know holier than thou thing like I have to go to a room and think about it for two hours. Yeah. But like that's not how you would do it with AI, right? Like how how do you do with AI?

How do you come up with a product strategy or like a plan? Yeah. So I really think about product strategy as market strategy. At the end of the day, I'm trying to think about how we build something and solve customer problems in a way that has a unique market competiti like a unique market advantage that's margin accreative that compounds on the platform that we've built and um our our team has the technical ability to execute and so I think product strategy is a set of actions you take given a unique understanding of your marketing customer. And I like it's really how I how I define product management.

And so what I'm using AI for is not um necessarily to write down the things to do, but to make sure that I have a very strong understanding of what that market context is, what our um unique technical differentiators are, what might be coming. And so one of the additions to product strategy building that I found very useful is deep research because it has access to such upto-date rich information that would be difficult to aggregate or or timeconuming to aggregate at an individual level really allows me to have a much more broad and deep view of the market. So a good example of this is at launch darkly. There's been a lot of market consolidation in the product um in in the feature experiment or feature management and experimentation space. I think we have a lot of adjacencies that we're going into.

We've done two acquisitions just this year. We're expanding multi-product. And so as we expand our platform and portfolio, our um portfolio of competitors and partners also expand. And then there are a b bunch of macro um forces at play that could change how we might want to think about our product strategy. Yeah.

And it's hard to keep track of every competitor, what they're building, what features, what those features might indicate about their overall strategy, who they're hiring, why they're hiring them, all that kind of stuff. It just it takes time and it's easy to have a very shallow view of the market when you have to do that research yourself. And so one of the things that I find myself doing quite frequently is really uh looking at the market and taking a step back and saying okay if we looked at these three competitors over the last three months what are they shipping? Who are they hiring? What does that indicate about their product strategy?

How does that relate to our stated product strategy which is X, Y, and Z? And this is what we're building. what potential threats might emerge that we're not addressing in our strategy and where should we lean in harder that could create an edge for us and just being able to aggregate that information into a single place and really apply some critical thinking to that context allows I I think not necessarily for more interesting product ideas any of that it actually allows you to identify like higher leverage points in your business that you should invest or places where um you might want to divest from because the market just isn't doesn't have the pull there. So you so you first like maybe use chatb deep research to research the competitors and what they're doing and then do you give it context of your like old product strategy or like context of Yeah. of launch darkly, right?

Yeah. Yeah. Yeah. Yeah. Yeah.

I I think the key thing here is like it's kind of like a collaboration with the AI, right? like like I don't I don't do well just like thinking in my room for two hours by by myself like I need to talk to some someone. Well, and I think it's one of the really it's one of the really interesting design benefits of these agentic experiences like what you see with Devon like what you saw with chat purity is especially in a distributed or remote world synchronous collaboration feels very expensive. you have to hop into a meeting, you have to make sure that everybody that you want to talk to is available and because you have this kind of limitations of space and time, you actually drag out collaboration and it takes longer to get stuff done because people just simply aren't available. That's right.

And it so it makes, you know, great Rise of the Super IC, I can do it all myself, but it's very lonely, right? you're sitting there, you're like, I probably could write a pretty good product strategy by myself, but it's sure as heck not very fun to do that. And so even this kind of stuff where on the weekend, you know, the our our engineers are off on the weekend, but I'm working with something, but want somebody to collaborate with and partner with. Okay, well, at least I have good old Dev in here to hang with um and get some stuff done or give me feedback when I need it. And so I think that's a really um kind of interesting design um attribute of some of these agents that might make them, you know, might make organizations drive drive adoption.

I mean, you probably talk to the stuff as much as you talk to your co-workers, right? Like Oh. Oh, I mean I talk to I talk to this stuff way more than I I talk to chatardy eco-workers. That's for sure. Yeah.

Yeah. Um okay, I've got a PR. Look at this thing. Okay, so I have positive feedback C categories and support for love and like rating. So Devon has issued a PR here.

Uh what I really like is the PR description is very nice. Um it's not a thing engineers love to write in a lot of detail, but it's very nice. It's very good how it's tested. Okay. So what I would typically do is um one I would um look at the code.

So um I would say I'm just reading through. Okay, selected rating. If it's bad, it's a negative rating. Otherwise, if it's not bad, it's positive. That's correct.

I would read through show. Oh, there's not. They got rid of the the um the timeout, which is fine because we don't need to show the little confirmation message. It updated my analytics tracking, which is nice. I didn't explicitly ask it to do it, but it a you know, updated my analytics tracking to accommodate for the new thing.

So, a good a good citizen. I don't know if you've had this experience, but engineers will sometimes write the code and then you have to fire like another Jira ticket for the tracking. The tracking is always like a afterthought. Yeah. is an afterthought.

So that's good. And then this feedback modal, what is it doing? Okay, so it's adding a new feedback type here. And then it's going to say what did you like versus what did you not like? It gave me the feedback options.

Okay. So like code code generally looks pretty pretty good. So then I'm going to pull this branch locally. Let's just do this and local host. Let's see.

It's always thrilling to do this to do this live. Okay, so I'm going to pull up my local host. I'm going to go to a chat and we're just going to smash that heart button and see what comes up. Okay, boom. Nice.

It worked. It's there. clear explanation, actional advice, concise, helpful. I loved it. Submit feedback.

So, so that worked. And you know, I mean, you and I had recorded a whole podcast while while doing this. So, then what I would do next is make sure my my checks have passed. They have. I would approve the PR and then it would be ready to merge.

That's amazing. I I've been sleeping on Devon. I I could try it. You've been sleeping on Devon. I'm like Devon's reply guy at this.

But but you can see that. And what's nice for me just the shape of how I do things is I really can't sit and babysit an ID. Yeah. I just can't do it. And so, um, it's just when I have features well scoped, well understood, um, it gets it done.

And I actually wouldn't be sitting here waiting for it to to work. I would be going off doing something else and then it would send me the slack that it's ready. So, uh the the sense of waiting and time is just um it's compressed. Yeah. I mean like I tried vibe cursor and wind surfing.

Yeah. You have to sit there and like wait for it to respond and you know like it's like way way more step by step than than what we did here. Okay. So, let let's kind of like switch gears a little bit. Let's talk about um I'm I'm I'm curious uh how you balance everything.

Like someone was trying to balance stuff. How how how do you balance the CPO stuff with like chat PRD and the new podcast? Is is it just like doing more things as async or people really don't like to hear it? I work all the time. Like I get up at today I got up like 5:30 in the morning.

I do I check in on the support queue from Europe. I reply to a bunch of support stuff on my phone. Um, I send a note to the engineering team, uh, who's usually about halfway through their day, uh, early ear early morning on chat, just making sure that I'm not blocking anything and that I can do PR review if they need it. My kids get up at like 600 6:15. Um, my husband's amazing.

He does lunches and breakfast. I do getting the kids dressed and drop off. One of us gets a workout in and then I'm straight into launch darkly work. So then I work a very serious job and spend a lot of time on lunch darkly. And then after school I I pick up the kids most most days.

Sometimes my husband gets the kids. We come home, we do like homework. We all do our homework. So my kids do their homework and then I do my homework. Okay.

Whether that's like uh launch darkly homework, podcast homework, chat PRD homework. Um we hang out and read books and do bath time and family time. um you know until 8 or nine. I watch like one and a half episodes of television and then I'm asleep between 9:30 and 9:45 to just like do it all again. And then I work on the weekends.

Like I really do work on the weekends. So I have two jobs on the weekends. One is carting my kids around to sports and hanging out with them and making sure that they have fun. And the other is I catch up on a lot of of chat purd stuff. And you know I do have help.

So on chat PD I have these two engineers. So I've hired um because the business is profitable. I'm able to hire. So that's certainly helped. So I have a whole team that sort of works the business day for me.

So I can step away from stuff um during during the business day. And then podcast is a new thing. So it's a little bit more time inensive. Yeah. Right now.

But I've got a bunch of stuff queued up and hopefully it'll become more steady state moving forward. But it's it's super hard. Um, I've got a great partner, so that helps. Um, I like to work, so that helps. When When are you gonna hire a husband to help help you with all this stuff?

Are you gonna Oh, I mean, he's he's he's uh my my partner in all things. We have founded I don't know, six startups together. So, he's, you know, he's behind the sca for for Chat Purity. Got it. Taxes, legal, admin.

Yeah. I'm I'm trying to get my wife to do all my finances and like you know do stuff. Yeah. I mean I have a accountant in some in some sense um you know I have to invest in the business and invest in my own scalability and we have you know we have househel too uh like I have somebody that picks up the kids two times a week. Yeah.

Uh but honestly the thing that I spend the most time on is is my kids when they're when when they can. I love dropping them off to school. We spend a lot of time together in the mornings. I try to pick them up from school every day. Um, yeah, we hang out together and so it's just you got a lot of hours in the week.

I just don't do much of any anything else other than family and this and like exercise, you know. I mean, I interviewed uh Sahil who said like something very true which is like um like when like our most busy professional time is also when our kids need us the most. So you kind of have to remind yourself to take a step back sometimes. Yeah. You know, and I think for me, like I had working parents and every time uh I feel like I'm working a lot.

One of the things to do is write down why it's great for my kids to see how much I love what I'm building and I built something myself and I'm having fun and I have interests and I vibe code with my seven-year-old. Um and my 5-year-old keeps me really humble. So, I think it's good to have a parent who really loves what they do um and inspires you to lean into your passions. And I hope, knock on wood, I mean, I ask my kids, I say, "I have too many jobs." And they all say, "But your number one job is being our mom." So, they they they know my priorities are straight and that's all that matters. Yeah.

And and and like Yeah. I work the weekends, too. I don't I don't mind it because it's like you're building something you're building something great, right? Like something fun. So, Yeah.

totally. Yeah. Um so then um let's talk about like product management a little bit. You know I I think you had a famous presentation saying product management is dead. I I I I think it's more like traditional product management is dead or or is dying, right?

Is that fair to say? Maybe. I mean let's see. Let's play it. Let's play it forward and see.

Um it certainly hasn't died yet in terms of like I'm still hiring a product manager. Great. At Launch Darkly we just hired a bunch of product managers. I just think the role, the expectations are really going to change in the role. Um, I think the tools and the hard skills you're going to need are going to change in the role.

And I know lots of startups that have gone many, many years before hiring their first PM and kind of don't want to hire many. And so, yeah, you know, it's it's hard to say how existing companies and teams will shift in the short and midterm. I'm actually really curious about how new teams start to form and what the sort of like new persona of a building team will look like and whether or not what we call a product manager has any role on that team. I mean, it's happening already, right? Like they're like I I think the designer is becoming like a design engineer.

Totally. And then maybe there's like someone who's like more backend focused who knows product too. Maybe that I mean at launch darkly we have this product called AI configs and lucky lucky team. I love this product so much that I'm PMing it right now and so I'm sort of the named product lead for this product. Guess what?

I have an executive job. I have lots of other things to work on. So they get like a partial product manager. And what I'm seeing is our design lead, who's amazing, is writing PRDs. Our engineering manager, who's amazing, is writing PRDs.

They're coming to me 80% formed. And I can say, "Oh, actually, I think this needs to tweak or this is how I measure it for the business or let's not forget this part, but they don't need a full-time me to make that that piece happen." Um, at least in in the short term. And so I do think people with the right hard skills and the right tools can step into step into the gap and and make something happen for a team that's, you know, flexible and adaptable. Yeah. And I think maybe the optimistic view of this thing is like the job will hopefully become more fun.

Like there's like a lot of parts of the job that's like not fun, right? Like like um I think so. I don't know. Going through a lot of re reviews or or like you know just having a lot of meetings all day. I totally think so.

And and what's so funny to me is I don't say product management is dead because of doom and gloom. I say it's dead because one I think you're going to be in a world of pain if you're not prepared for a shift in the next 18 months. Like I just think not being prepared is the worst thing you can do for your career. And so if I can be a little bit incendiary on how I get you to prepare, I will I feel like I've done some good for folks careers. Yeah.

And two, a lot of the job is not fun. Like a lot of the job is tedious. A lot of the job is not creative. A lot of the job is very disconnected from customer impact. And so if you can compress the parts of the job that are not high lever, not interesting, you can spend a lot more time in the space I like to spend, which is in being creative, in being generative, in building and collaborating with a team, in talking to customers.

Those are the in competing in the market. Those are the things that I think are fun about the role. Yeah. And I just want to spend more time on them. Yeah.

Same same here. I think every PM wants to spend more time on this stuff. Yeah. Yeah. Totally.

Real quick, I'm I'm curious uh at launch darkly, have you compressed the planning cycle of of of the pro road map or like you know because a lot of times what takes away from this customer iteration stuff is like you know making OKRs and like planning you know me and my OKR memes. Um yeah, which one of us has not been victimized by by an OKR? So this is how we do product planning. We do heavyish product planning about every six months. And so we set aside about three days to do product planning.

It's really product strategy and it starts with what are our business goals for the next six months. And so it starts with what are we going to sell? How are we going to sell it? How is this going to acrue value to the business? What are our actual goals?

Do we agree those goals are achievable and important? We spend a lot of time with that. And then we go into product strategy. And we define product strategy as a combination of what and why we're going to build things and how we're going to commercialize those and bring them to market. So it is a much more comprehensive view of planning and then we spend probably like less than 10% of the time on the actual roadmap items.

like the roadmap items cascade down and do we believe that they're the right ones but really we spend the time on the product and commercial strategic planning about every six months and then between those times it really is I just think an always on roadmap is the best way to go. I know where to go inside the company to find everything every single team's working on. And we know from a technology perspective and from a business perspective what are like the five most important things to achieve in any quarter and we look at those on a regular basis. So we try to keep it really pretty simple. Um, I have I I along with the rest of my leadership team fight the good fight on like dumping a bunch of time into planning meetings and actually spend more time on tracking are we getting stuff done and being more reactive in the moment when we need to address something.

Makes sense. It sounds like you have the planning pretty compress compressed so it's like intensive three days but like it doesn't drag on too far beyond that. It probably takes teams you know two weeks to prep for it. They're not prepping for it full-time, but they do have to get get together with the team, make sure technical initiatives are accounted for, all that kind of stuff. Okay, great.

So, so when I hear um you got to get ready for like this new new era, like a lot of the advice is just like, hey, you got to go play with these AI tools and you got to get your hands dirty, right? But but like and I think that's good advice, but like how do you go beyond that? Like um like you know, when you evaluate PMs, this AI stuff, how do you what skills do you look for? Yeah, I mean I just think again I think it's pretty shortsighted to say vibe coding will be the differentiator or like prototyping skills will be the differentiator um because that only takes you so far. So what I really think about is how to cultivate attributes that futurep proof your career in this world of AI, not AI hard skills.

And so the attributes I think about cultivating are scrainess, how do I get something done with very little? If I need to solve a problem and I have zero resources, how do I get that done? Can I prove I can get things done in a very lean environment? Perhaps using a set of tools, but perhaps not. I think scrappiness is one one piece that I assess for.

The second thing I assess for is the ability to learn. So again, you could show that you're capable of learning tools or capable of learning new skills. That's one way to demonstrate learning. You can also demonstrate that you're capable of learning the market or capable of learning finance, any of those things. But I really think that ability to learn at this moment is a really important attribute for um for getting stuff done.

And then honestly I think the ability to clearly communicate is so critical right now. And this is where I think maybe like classic product managers have have the edge. Um us us yappers h have the edge which is if you look at something like Devon it is a language-based interface. You are telling a system what to do. your ability to clearly articulate what to do in a way that a system can appropriately interpret it, access its set of tools and get the job done correctly is actually a really important skill.

And so you can call that prompting, you can call that clear communication, but the ability to clearly uh articulate a set of outcomes and get a system whether that system is human or otherwise to do things I think is very very very important. So those are some of the things that I look like from an attribute perspective really like scrappiness, ability to learn and ability to communicate. You can demonstrate those through through these skills, but if you have those kind of attributes, you'll be successful in kind of any role. Yeah, that's a really good point. I I think um every time you're prompting, you're basically improving your written communication skills.

Yeah, totally. You're kind of for force, too. Yeah. Um Okay. And uh do do you like uh evaluate like in like for promotions and stuff do you evaluate PM separated from design or like you know you talk about this AI power triple threat.

Do you try to like people who can blend roles together? Is that something you try to encourage? Yeah. Um so we try to encourage it from a cultural perspective. So maybe the fourth attribute I would throw on that list is low ego.

Like you're just not going to survive in new orgs if you get territorial. Like what a what a waste of of effort and potential outcome for people to block progress based on being territorial. So you know a designer that says no one but me can design this or an engineer that says no one but an engineer can push code. I just think that mindset is very limiting in the face of what is pretty radical change. And so what we look like look for in promotions is one I think you do need AI fluency and this is probably even more impactful in the engineering track.

I run the engineering organ as well organization as well. Um fluency with these tools matters. You need to figure out how to use AI powered idees. You need to figure out how it's appropriate to use something like Devon inside your organization. You need to have an opinion on what models work for what.

you need to have the ability to architect uh a repo to be easier to use with these tools. All those things are hard skills that should be part of a promotion ladder or career path for software engineers and you can you can imagine the parallel on the product management or design side. So I think there's like tool fluency is one piece that's pretty important and then it's just leverage right as you become more and more senior in a product role. the expectation you have a higher impact on the business and my expectation is that you use all the tools available to you to have that impact. And so we certainly do look at leverage um especially in senior promotions of this individual is having a high impact on our business and they could do that a lot of different ways but often they're they're they're leveraging all the tools available to them.

Yeah. It's kind of like a no-brainer like you basically have like a AI team help you. Why why would you not use this stuff? Yeah, totally. I tell I tell all my engineering managers when they use when they uh you know use Devon, I say, "Congratulations, I just gave you 10 interns." Like, no one no you know no engineering manager turns their nose up at headcount.

So I'm trying to position it like congratulations you got overnight headcount. Is that your response when they ask for more like human headcount? You're like okay I'm gonna give you that. So I I I do when people ask for headcount I say is your team maximally efficient just like you know, is your team maximally efficient? Yeah.

Um, and have they experimented to know where they could get efficiencies? A lot of times the answer is yes, and I have a good sense of that. And sometimes the answer is no. And then they need to spend some time getting there. Okay.

So, um, last question and related to what we talked about like how do you drive uh, organizational adoption of AI? Like a lot of this stuff is just limited based on like security or like you know people are like like I a lot of companies you can't even use all the tools that you want to. I know it's so sad. Um, so I think a couple things you need to do. You need to figure out the finance and security framework for your company to enable experimentation.

So luckily we're relatively small company with a you know good mature security team and program and a good mature uh finance program. Finance is not a problem. I can make the uh case for high ROI of these tools all day and all night. ROI of the the spend is non-issue and then infosc we just had to build a framework by which they could quickly evaluate thumbs up and thumbs down use of tools in a particular context to make sure that we were meeting our requirements and obligations to our customers as well as internal security principles. Once we had that framework we could move very fast in terms of onboarding tools.

The other thing that you have to do from a cultural perspective is normalize AI tool use and give the happy path to adopting it because otherwise from a security perspective you're stuck with a bunch of shadow IT where people like hide the fact that they're using AI tools. They do it on like personal accounts. Yeah. They do it on uncontrolled licenses and that is actually the worst situation from a security perspective. So you kind of have to accept like people are going to do this so let's give them the clean path to do it and let's put it out in the open versus not.

So that's sort of the admin side of things. I think the real uh needle mover however is cultural and so what we've done is we have at launch darkly a slack channel called project building with AI and we throw you have to request AI tool access in that channel. So everybody who has AI tool access is in the same channel which is good. Okay. And then everybody shows off stuff that worked, stuff that didn't, stuff they tried, stuff they've learned in one single channel.

It creates a lot of momentum. And so people will post their cursor wins or people will co post their dev and fails or they'll post new prototyping tools. And so it gives it gives socialization to a lot of use cases. And then in technology we've named a single engineer Zach. He's amazing as sort of like the responsible party for AI engineering adoption.

And so what Zach does is he goes and evaluates tools for us. He makes sure that those tools are set up with our codebase and our team to be built into our systems and processes, you know, making recommendations on, for example, cursor rules or Devon environment set up. And then he runs, which he's running right now, I'm going to do it after this podcast. He runs a Friday AI power hour where it's like a Twitch stream of of Zach using AI. So, um he'll sit, he'll show off some stuff, he'll invite others to show off stuff and um we socialize it live as well.

And people show up for this. Oh, I had like 60 70 people every week. Wow. Like it's fun. Yeah, it's really fun.

Yeah. Um, any any uh closing words of advice for for folks or any hot like you're you're you're the queen of hot takes. Give me some give me some closing hot takes. Yeah, I think this is the year of the agent. I know it's been said, but I think this is the year where you go from sort of like co-pilot singleplayer experiences in AI to multiplayer agentic experiences that feel more like your colleague.

Again, get good at it. Like, get good at working with agents. Figure out which ones are out there that add value. Figure out how you prompt them correctly. Figure out how you orchestrate them together.

I think that's a hard skill that's going to really be um important in the next year. And so, um, I think I think this is the year where you get out of this like single player mode and you start getting your your team of AI AI interns. So, so you mean let's let's define what agent is real quick. Like agent is like someone who goes off and does work for you and collaborate with other AI, right? Is that what it is?

Yeah. Yep. Yeah, it makes sense. Yeah. Just just like what you demonstrated with Devon.

Like you don't have to babysit it with prompts all the time. They can just get it to do do stuff. Yep. Cool. All right.

Well, um, let's talk about where can people find How I AI podcast. So, you can find How I AI. I recommend Spotify or YouTube because our guests get on and screen share their AI use cases. It's also available wherever you want uh to get your podcasts, although I recommend the video aspects. And then you can find me on X at Clarvo or I might revive the Tik Tok.

So, the chief product officer Tik Tok might be coming back. Yeah, Tik Tok is perfect for your hot takes. You should definitely revive it. I just I can't take like a fifth or sixth job and Tik Tok feels like a fifth or sixth job. Yeah.

Yeah. True, true. Yeah. Cool. Well, thanks so much, Claire.

This is another amazing conversation. I definitely learned a lot. Oh, I really appreciate it. It was super fun. Yeah.
