---
title: "Inside Gemini and NotebookLM: How Google is Shipping Non-Stop | Josh Woodward"
guest: Josh Woodward
publish_date: 2025-10-12
youtube_url: https://youtube.com/watch?v=r-xjo7MYc18
channel: Behind the Craft
keywords:
- ai-tools
- big-tech
- ai
- execution
- leadership
---

We put a huge premium on how fast you can go from idea to in people's hands. We get really excited when we get like our first 10,000 weekly active users or daily active users. And a lot of Google teams, we joke it's like dashboards may not count that low. It's going to make like this 20 30 slide deck that's kind of an overview of this entire set of 70 sources. You can have a whole team's knowledge base with one button turned into one of these like video overview talking slide explainers.

You also want to go out and just be with people because often when you build something really amazing, you see it in people's eyes when they use it. People who like to tinker, people who like to build, they express themselves through prototypes, not docs. You mentioned like you have to hire the right people. So like what kind of people do you look for? All right.

Hey everyone, I'm really excited for today's guest, Josh, uh VP at Google Labs and also Gemini app. Uh Josh is widely loved inside Google, I think. So I'm really excited to get him to demo a bunch of new Gemini features, notebook LM and even flow and also talk about how he's kind of built this shipping culture inside Google. All right, so welcome Josh. Awesome.

Thanks for having me. Great to see you. Yeah, I'm like super impressed by uh you and the team, man. So why don't we just start by doing some live demos for fun, you know? Let's let's show all the cool stuff that you guys are working on.

All right, sounds good. Let me uh project my screen here. Uh I'm going to go over and Okay, we'll just do like a whistle stop tour through some tabs here, Peter. and jump in at any point I guess. Um, so I thought maybe where we could start is maybe nano banana maybe.

So we've seen we've added the banana emoji in many places in the app and uh one of the things that's been just so fun to see is um how creative people have gotten. And um this first one here on the home screen, Peter, this is um this custom mini figurine. I don't know if you've ever heard the backstory on this, but this actually started in Thailand. It was uh something that went viral in Thailand and then spread to Indonesia and Vietnam and then just like the rest of the world. Uh and so we've tried to make it really easy today.

If you go to Gemini in the home screen, you can tap one of these, upload an image, and we've got this is the prompt. If you see, it's a 17th scale uh figurine. Um and then it kind of breaks it down. I'm sure a lot of people have seen this online. It puts you on the desk.

And uh anyway, this has gone incredibly viral. At one point in some countries this was as much as 30 or 40% of the queries we were seeing um and sort of like the peak moment. So it's very fun. And um one of the things that's been interesting too is like I'll just show you a couple things that stood out to me. This is just stuff people are posting.

So one very common thing we're seeing is people doing kind of style transfers on images. So this is a watercolor. It's kind of nice. Um this one is super cool. A lot of people have been doing interior design, but what's a little different about this is you see the picture on the wall uh behind the couch.

These are like artists putting their own pictures in these scenes and then selling them. So, it's kind of like you put that picture in and you can go black and white if you want and then it's like sold. So, this is kind of an interesting case. We saw one wave of people doing interior design. you know, put this couch in this room.

And now we're starting to see these almost like, you know, placements of certain things, which is kind of interesting. Yeah, this one's kind of fun, too. This is someone, we're seeing this a lot, too. They may take like a picture or an illustration in this case, and then like turn it into like embroidery or something. So, there's a whole bunch of like manov banana inspired merch that's happening around, you know, stickers or buttons.

People are making all kinds of physical world things. And I think that's pretty cool because this is stuff again we never really could have dreamt up, but you put this kind of tool in people's hands and they they go wild with it. Yeah, it's kind of great to just observe what your users are doing and then just like add a default prompt on the home screen to make it easier, right? Like the miniature figurine stuff. It's great.

Yeah. And it's it's interesting. It's some cases it's things like that figurines. You saw also on the home screen, you know, there's lots of things here of just like head shot. Even things of like youth through the decades, you know, the 80s style, the 90s, the 2000, like all of this is very very popular and kind of global globally interesting to people.

That's amazing. Yeah. And like Gemini really took off right after Nano Banana Long, right? People love pictures. Yeah, that's right.

And pictures is kind of universal language in a lot of ways. Uh yeah, there were definitely points I was trying to tweet about kind of trying to keep the status of things going because it was um just really melting TPUs. It's still like you know all kinds of new new highs and new records and things. So it's been it's been really fun. We've tried to hold on keep it going.

Amazing job. So it's called Nano Banana. So is there going to be like a big banana coming soon or like a better banana? This is one of the top questions. Yeah.

Is there going to be like a larger macro or XL banana or something? Uh you know funny the name of this all got started um one of our uh the product managers on the team actually came up with the name and we kind of fun it was you know it started showing up in uh some of the chatbot arenas and sort of and we just kind of ran with it. Um in fact even that banana emoji that shows up you know in the picker and things that was something one of the engineers just for fun you know landed that code uh one night probably after midnight or something. Um, but it's kind of its own little life to itself. Yeah, you gota you got to keep the memes.

The memes may make spread the word. Yeah. Yeah, that's right. That's right. Yeah.

No, we'll see. Um, we are uh, you know, we are starting to work right now already on some of the next generation of where this is going. We're hearing all your feedback out there of, um, you know, one of the things I'm very excited about this first Nano Banana model was a big leap forward obviously in kind of this conversational editing. So, expect more there. Uh we're we're really excited about what we can do with that.

Um I think the other connection we're starting to see more advanced users do right now is putting together Nana Banana and VO which again for insiders is like you know exactly what I'm saying but for the outside world it's just like I want to make my thing move and like animate it make it a video. So I think we're going to try to make that obviously really easy. People are already starting to do that naturally. Yeah. And then I think the other thing is kind of interesting, Peter, is like, you know, even a year or so ago, nine months ago maybe, these models weren't that great at text.

Um, and they've gotten way better at that. And so there's a whole bunch as we're thinking about Nano Banana 2 when it comes to like how to give you more control over generating things. In some cases, maybe it has a lot of text on it, which historically you never would have thought of as a maybe an output from an imagery model. Um, there's there's plenty to come here. We're very excited about it.

Yeah, the text one is actually really important because like you know I I still kind of make infographics by hand and like if you can you know satisfy a lot of the marketing use cases then I think like content creators like marketing agencies would would jump on this. Yeah. I mean it's one of the top feedback areas we hear from people is like how this is an unbelievable kind of like singleshot experience but I want to do more of this editing and kind of iterate with it and so um yeah watch this space. All right. All right.

You're shipping like 10 things every day, man. Okay. All right, let's talk about uh your other product, notebook alm. That's also really impressive. Yeah.

Yeah. Oh, thanks. No, this is um one of our original Google Labs projects. I I'll pull it up here, too. I've got some stuff I wanted to show you.

I mean, here the way to kind of think about notebook is um you know, it always started from this idea that how can we help you kind of understand anything? And you know, the feature that put it on the map almost a year ago in 10 days back was um uh the audio overviews and kind of the podcast. And really where this team has gone in the last year is super exciting. And kind of where it's going is even more exciting. So where it's been, obviously there's now a mobile app.

There's new ways you can transform this content. And one of the things I'm really excited about is right here at the top in this top row. These are called featured notebooks. And what we've done is we've gone out and we've kind of worked with different partners. You could see here there's folks like from the Atlantic or the Economist or certain authors like Eric.

And what's cool is if you tap in like say this economist one, this is a notebook that basically comes pre-bundled with 70 sources as you can see here. This is the economist's world head report. This awesome kind of annual report. And what we see here, Peter, is like a glimpse into the future of how the notebook itself is like a new container or a new format. And it comes with sources on the left.

You can obviously Q&A it in the middle like you always have been in notebook. And then all of these rich kind of studio or media outputs on the side. So it's got things like of course the mind maps you can expand and it's all based on this content like always. Oh, that's awesome. Yeah, this is actually the one I wanted to show you.

So this is an area we're super excited about. These are called video overviews. You can think of them almost as like talking slides where I'll just make this full screen for a second. And um this is you know the world aheads report and it's going to pull out like a seven minute clip. So, it'll go through as it's talking here and just pull out all these different interesting insights as it goes through and it's going to make like this, you know, 20 30 slide deck that's kind of an overview of this entire set of 70 sources.

Um, yeah. So, it's kind of unbelievable when you start to think about kind of these content transformations that we're right on the cusp of. And so, this one, of course, teachers love this, students love this. We're seeing a ton of enterprises pick this up too because you can imagine you can have a whole team's knowledge base with one button turned into one of these like video overview talking slide explainers. So it's quite powerful.

Yeah. No, nobody likes making slides manually, you know. Yeah. Well, I think this is actually kind of it's interesting you mentioned that, Peter, because this is where we're excited to kind of see where this goes because you imagine something like a nano banana model that can style slides and that consistency across maybe a whole deck with sources. You know, it reminds me like one of the things on the Google Labs team we've been thinking about for a while is like what's kind of this look like?

You know, we've seen like the rise of creators and that gave birth to like YouTube and other types of format. What does it look like for people who are curating in this case knowledge or in other cases like visual assets or you know things for a business or an entrepreneur that kind of thing. So there's a whole I think rich area stuff to explore when it comes to the like curation to output using AI to kind of help transform stuff. Yeah. Curation is kind of creation too.

So it's Yeah. Exactly. Exactly. Yeah. This episode is brought to you by Composio.

Most of the pain in shipping AI features doesn't come from the model, but from the integrations. You're dealing with messy APIs, fragile tool calls, and hours lost to debugging and figuring out why something broke in Slack or Salesforce. Composio gives you one SDK to connect to 800 plus apps like Slack, GitHub, Gmail, Jira, and they built the Rube app that plugs all of those apps straight into an AI chat. So you can just ask pull me the latest metrics from Mix Panel and update linear. Now, instead of fighting with APIs, you can focus on actually shipping faster.

Check it out at get rube.link/pater or the link in the video description. Now, back to the episode. And another thing that comes to mind is like um like I feel like AI often get get you like 90% of the way there, but like you know it would be even better if this thing was actually like I can actually edit a Google slide with this thing and then like finish the last 10% like I want to tweak some text or something. You know, that would be really amazing. You're uh you're reading the road map.

That seems like okay. All right. Yeah, this is one of the top requests. You know, another request we get too, Peter, is like, okay, slides are one format, podcasts are another format. There's lots of things people are interested in of like you mentioned infographics earlier to think of the bar either in terms of time or cost or expertise to make an awesome infographic.

Trying to figure out like how do we make tools that help the very best people do that maybe faster or more creatively, but for all the people who never could do it, that's also a huge opportunity. And so that a lot of our projects have that kind of dual focused often times. Yeah. It's going to lead to an explosion in creation. I'm really excited about it.

Yeah. Well, we you'll have to give early feedback here on stuff. Well, I mean uh Okay. So, like you know, in my opinion, there's a lot of competition in the space, but like Google is like by far ahead on multimodal AI and uh you know, I think we saved the best for last the the v the video part, right? Like do you want you want to show the Yeah.

Yeah. I'll show something on this real quick. Yeah. Yeah. So I'll flip over.

So this is flow. Um this is a project that just came out at Google IO. Really interesting backstory on this project. A lot of our Google labs products. We work with teams around Google and in this case was very close collaboration with Google Deep Mind.

Obviously they built the VI3 model that was the breakthrough that brought not only this incredible quality you can see on the screen, but sound effects. So, it was the first time you could kind of have the silent picture era ended and we moved to kind of sound effects and dialogue and things like that. Um, but this project went from idea to in people's hands in IO in less than a 100 days. Um, and it's like a really good example of kind of the kind of phase we're in right now at Google where people are just so energized and the tech's amazing, but it's also how do you package it in kind of a way where people can really get the most out of it. So, here's what's kind of fun about this.

So, flow is the tool. You can make stuff with it. 8-second clips. You can stitch them together, export it out with what's going on with kind of flow TV. And it's just going to kind of rotate through just like it sounds like.

This is kind of like a gallery of all the different stuff, you know, that you can make with this tool. So whether it's like interviewing an owl here or you have like these talking skunks like u these are kind of designed to be and I can kind of flip through this gallery so you can see these are like fake infomercials underwater just this incredible set of stuff that you can kind of play with and one of the big trends we're seeing right now Peter is people want to go in and kind of remix things so they may be like oh hey this like bubble thing is kind of cool so they may click on that and then you can see here at the bottom we've got like the whole prompt that you can kind of play with. And then what's really amazing about Flow, not only does it bring kind of audio for the first time, this remixability and the ability to bring in reference images. So you can bring in like, okay, I'm in this whatever pyramid looking scene, you know, kind of in this dark area. You can bring in certain objects that you want to insert into the scene.

And I think this is again this next stage of really video generation. It gets kind of that same nano banana editing feel. Yeah. And so much control this gives kind of creators which we're really excited about. So So I can bring my face in here like to be the actor.

That's but like and I think interesting is people start mashing up different things. So you might go in and say like okay let me go back to like the gallery view here. You could go in here and say like okay here's a Christmas tree and it's got the reindeer and Santa running through it right? And then it's like, oh no, no, make them take off and go over the tree. So you can really direct these scenes in like a very interesting way.

Bring yourself into it, too. Yeah, there's going to be a lot of really cool YouTube videos coming out of this, I'm sure. Like people scenes together. That's right. Well, there's already tons of them.

And so, you know, flows a product. What's really cool about this is it's not something you just ship at IO and you're done. Literally, this team is like every week, every other week, shipping new things. So, just in the last three weeks, you can now make videos not just in landscape mode, but also portrait mode, which is awesome for shorts or other things you want to do that are more mobile optimized. We've also made it now, we've made some amazing improvements in the efficiency to serve the models.

We have an unbelievable serving team at Google. And so, by making these models cheaper, we can give away more credit. So now if you're part of the AI ultra plan for example, you basically have unlimited generations. And so what we're seeing is people will go do a bunch of quick kind of fast generations, create almost like a story board and then you can kind of put together the best, you know, cherry pick your best ones and turn that into actually a final final production. Yeah.

Yeah. You can probably build a product around there, right? Just like a storyboard product where like each one has a prompt and you just cut the ones that you like. You can probably work on that. Yeah.

Yeah. Yeah. Well, and that's kind of how Flow works today. We're we're optimizing that more, too, because I think what we're finding is is so interesting to co-create. You know, we're doing this project with folks.

Some of them are down in Hollywood. They're bigname directors, but we're also doing it with a lot of what we call like AI filmmakers. They're people that are kind of building stuff AI first. They're AI native when it comes to kind of creation flows. And so, getting to study their workflows and try to build products for that is um is a lot of fun.

It teaches you stuff every week, too. That's very exciting. like that. That's probably like one of the new jobs that AI can create like AI AI filmmaker. Yeah.

Yeah, that's right. That's right. Okay, so let let's uh switch gears a little bit. I think uh these are all like super cool demos and you know like before I started talking to you and the team like my impression of Google was like this big bureaucracy where you know you have to like get approval and like it takes forever to ship anything. Maybe in some parts of Google that's still true, but like you know really impressed by how you kind of build a shipping culture inside Google.

So maybe you can talk about how this happened. Yeah. Uh well, I would say um it's funny. I started at Google as an intern almost 16 years ago and uh in a lot of the things we've tried to do in whether it's Google Labs or now the Gemini app or even like the AI studio team, these are all very fastmoving teams. I think one of the ingredients is um the type of people we try to bring onto the team and I'm happy to talk more about that if you want at some point but it's I think we're seeing it now across different parts of Google and to me that's what's really exciting is it reminds me like when I started at Google um you know you look at the velocity and the progress out of like AI mode and search all of Google deep mine parts of Chrome and workspace it's just like it's spreading cool around uh and I would say we you know we play a small part in that but we're trying to do our part in it Um but what are the ingredients?

Let's see. Very small teams. Um most of our Google Labs teams start with like five to seven people. It's usually like PM, some engineers, UXer, uh go. Um we put a huge premium on how fast you can go from idea to in people's hands.

And so I me we talked about flow. I mentioned you know less than 100 days. I think that one was like 86 days or something like that. But um we're really trying to optimize kind of the whole thing towards put it in people's hands and then I mean you know you've been around a lot of products too like that's when you really realize how far off you are in terms of building something. So uh we put a lot of focus on that.

We put a ton of focus also I would say on trying to um predict different scenarios of like future outcomes. So I'll give you an example. We're um really obsessed right now about what's the future of software development going to look like. And so we may take several different product bets. Sometimes they're conflicting honestly about what that might look like.

And I think that's a big other kind of part of it is like you're trying to stay on the frontier of where the model is, the capabilities, the raw power, but you're also trying to keep a pulse on like where the user needs are and try to connect those two. Um, and that's something I think our team tries to do a lot. And we talk a lot about co-creating with people in the different industries, whether it's filmmakers or musicians or artists or teachers or all these different sort of professions. Yeah. I think that feedback loop with the user is like really important, right?

Cuz like, you know, you don't really know what they want until you actually put it out out there, like they start playing with it. Yeah. Yeah. Usually when we're talking to people, we're trying to figure out like what's a big pain point or something that makes them grumpy is kind of the way I think about it. And it's like those are usually good products if you can find something around that.

So like um you don't actually do you spend a lot of time on like planning and like you know internal alignment stuff or you just like hey let's let's get out there like do you have to go through you and demi and everyone has to approve the product before you ship it or how does that work? Oh yeah good question. I mean we I guess we still have like annual planning at Google in that sense but it's not um it's funny the way we've set ours up right now is it's kind of uh we kind of come back when we have like kind of a hit on our hands then we try to staff it quickly. So I what I found over time is it uh one of the mistakes I made early on in my product career is you would hire too big of a team too early and it kind of creates you know work and you're trying to come up with the right thing but you're really not sure even what the product is yet and so one of the things we've done here has been a little bit more like reactive to that market pull and that demand so when something like for example notebook LM took off a lot of people are like well where's the mobile app and we're like we don't even have a mobile team yet. So you so it's like we're trying to think through like is there something here before you actually kind of staff it up and then you then you kind of get that obviously people want to join and it's part of the exciting part.

Um but that's one way about it. Yeah, that makes sense. Yeah, like there's Yeah, there's so many benefits to having a small teams. Uh like people feel more autonomy, you feel more owner ownership, there's less coordination tax. Like it's like it just makes you know it's so much more fun.

Yeah, that's right. That's great. Yeah. You mentioned like you have to hire the right people. So like what what kind of people do you look for to bring on these small teams?

Oh yeah. Yeah. This is this is a one of the number one things. Um it's funny. We when we started up Google Labs we kind of wrote this doc called Labs in a nutshell.

And it's kind of like sort of the mission the charter. It's all in one place. It's like two pages. It's a very short concise thing. And my favorite section in that doc is called who thrives in labs.

And we tried to outline. We ended up writing I think it was like 15 or 16 or 17 bullets. We're like, okay, you don't have to have all these, but the more you have, the better. And it's things like one of the most interesting signals, especially interviewing really any any discipline at this point, product, UX, is kind of what are you building in your spare time? Yeah, exactly.

So much kind of just in like the people who like to tinker, people who like to build, they express themselves through prototypes, not docs or things. You know what I mean? Like that's a huge factor. Um, we're really interested in people that are just like incredible uh at their rate of learning. One of the things I'm finding right now and you know you you tweet about this all the time too is like the pace of change right now is so fast and like the ability to be able to kind of react but also learn and kind of dot connect across different things huge hugely important um in a team like Gemini or labs or AI studio.

Um, the other thing I always like to try to find people who are um, you know, they're kind, uh, they're humble, they work hard. Uh, I love being around people who kind of ooze energy. They're like high energy optimist type people. I found, you know, these early stage projects, it's so hard to like you always have these existential questions of like, is my thing even going to work? And so you you want to be around people who kind of have this like, you know, we can do this, we got a shot at this, we're going to go for it.

um kind of that underdog mentality a little bit. Yeah. I mean, and I also think it's like way more fun to go zero to one than trying to tweak a little button in like, you know, Gmail or something like this way more product surface area, right? Yeah. I mean, I think it's you we uh I'm very thankful for those people, too.

But I think for me, it's like trying to invent something from nothing is just the best. I just love it. So I think uh yeah this is kind of the maybe the theme across a lot of the stuff that that I get the chance to work on right now. And how do you think about like some common big company stuff that's you know you have to deal with which is like there's dependencies there's like you know tracking goals and this kind of stuff like like for example for VO right when I started playing with VO yeah it was in some random URL I was like why isn't this stuff in Gemini and and then and then eventually made it into a Gemini app. So like how do you guys think about yeah that yeah it's a good question.

And I mean I think in general um yeah sometimes we you know end up testing things on labs.google or may come to another product later or things like that. Um it's a bit chaotic for sure in terms we're trying to experiment and get stuff out and learn. Um here's how I think about it. I mean I think whether you're in startup you're starting yourself or you're in a company like Google or anywhere in between um you've always got like stakeholders and stuff and it might be the board it might honestly your your users and your customers are like the ones I always think about the most like as stakeholders and trying to please and delight. Um, but I think for us, you know, what we're trying to figure out, and hopefully you're seeing this over time, we got more to do, but is like how, you know, the Gemini app, we want that thing to really stand for something, which is a personal, proactive, powerful assistant.

It's a life assistant. And so that you can imagine over time that life assistant will do more and more stuff like it might today might only create 8-second videos. Maybe in the future you'll be able to do longer form things or something like that. But I think our current mental model and why we have Google labs even to begin with just to take that example there's so many of these you saw flow and like how dedicated and purpose-built that is for a certain type of user too and so we're in kind of the early days of all this and really trying to experiment widely and then figure out kind of where the traction is. Got it.

And and in terms of like just measuring how successful teams are like um do you care more about like just the craft of the product because a lot of this zero to one stuff might not find product market fit right or do you try to be like you you don't have some like growth on metric by 5% thing right like how how do you manage yeah oh this is a good question we joke on the team yeah for a lot of our products um you know we get really excited when we get like our first 10,000 uh weekly active users or daily active users it's like you know and a lot of Google teams we joke it's like dash boards may not count that low kind of thing. It's like um yeah, for us those milestones are really important and because it's starting to show, you know, the retention and sort of people coming back to a product which is kind of our best proxy that we're making something useful. That's right. Yeah. But I would also say dashboards can be very deceiving in the early days of product development.

Um I always like to talk about and kind of try to coach our teams on like you want to be looking at the dashboards. You want to develop an intuition for that, but you also want to go out and just be with people. Like get outside this building and go to a coffee shop, go to a university, you know, cafe campus and like because often when you build something really amazing, you see it in people's eyes when they use it and they may smile or it may surprise them in kind of an interesting like delightful way. And so those are some of the more qualitative things at least I'm always trying to look for in the early early days of something. Yeah.

Yeah. Like people get too scientific with this stuff like just like go talk to five you users like go. That's right. Five users. Yeah.

Yeah. That's a very common thing and I think especially at a place that's like very data driven which a lot of our tech companies are you can kind of overoptimize for that and sometimes it's literally it's yeah it's more art than science in those early days. That's amazing. That's amazing that you built it because it's very hard. It's very hard to build like a startup culture inside a big company man.

It's like very hard. So the fact that you have this going on and I I I know some of your reports and they they love it volumes. Oh yeah, it it's a lot of fun. I mean in the whole in the whole industry right now, but I think especially this part, I mean, like I said, I've been Google a while and um I'm definitely having just tons of fun. This is one of the best times for sure.

Let's like a look towards the future a little bit more and um uh you talk about building a personal assistant. That's It's funny because I I have a gem where I've given me I have I have this Google doc and hopefully it never leaks anywhere, but I have this Google doc where it has all my personal information. It has like you know what gives me energy, what doesn't give me energy, what I'm working on right now, you know what I'm uh you know what I'm afraid of blah blah blah and even some like financial information and and then I I I give it to Gemini and then using that is able to give me like way more personal advice and I check in with it maybe like every quarter. Give me a pep talk. Yeah.

But but like you know, have you thought about this? Like how do you scale this thing to more people because like Yeah. I think right now these LMS are like pretty knowledgeable, but like they don't they don't know too much about you, right? I mean there's Yeah, it's one of the biggest areas we're excited about in Gemini right now. When I talked about those three Ps like personal, proactive, powerful, there's a reason personal is the first one.

Um and I think one of the things, you know, we're testing it internally right now. hopefully will be coming soon to you and others. But we're really interested in, you know, one of the top requests we get from people is I just want to hook my Gmail or my Google photos or like other parts of my Google life into Gemini and be able to use it for things like you're saying, whether it's your I guess you call it a quarterly pet talk or something, you're like quarterly, but it's um that's something of course there's a lot we have to get right with, you know, it has to be very clear what data is coming in. you have control over it, privacy, security, all of that, which we will. Um, but I think one of the things that is so kind of amazing about it as I've been using it internally now is the types of questions you can ask.

So, you can ask very specific things like you want to retrieve some piece of information maybe, you know, deep in your inbox or something. Um, the questions that I'm finding more interesting are some of the ones maybe it's how you're using your gym and that life dock you have is like how should I be thinking about like the next few years of our family life or what are certain ways that I can be a better dad or they're kind of more these like big open-ended questions that if you imagine something like Gemini has this understanding of you with your permission of course the the kind of ability for these models to work through all that context and the multimodal context, too, cuz remember it's photos, it's videos, it's it's all kinds of text, documents, and things. Um, it's really amazing. Um, and we've still got to improve it before we actually ship it out, but it's like there's the promising signs are there for sure. They got to put you in charge of the the Google workplace, man.

That team needs to move faster with all the AI features and Gemini integration. Oh, wow. But, you know, there's a lot there's a lot coming there. So, be uh be ready. Yeah, it'll be good.

It should be good. Yeah, cuz cuz Yeah, if you have my calendar, my Gmail, like just those two things alone, that that's like a ton of context to make it super personal. Well, from our earlier point too, Peter, remember we were talking about like curating stuff. Yeah. At the end of the day, a lot of this stuff is context engineering, right?

And making it easy for people to be able to point the model at certain kind of pools of information that they want the model to kind of work on. And so I think that's that's another thing to me is very interesting about these Gemini models have always been multimodal since the very first Gemini 1.0 release is very different than some of the other models in the market. But I think that deep kind of native multimodality. It's also what makes something like Nano Banana happen. It's like you can just talk to it or describe it and Gemini knows kind of what's in the scene and can make the edits.

Do you know what I mean? So it's it really shows the value of that like integrated multimodality. Yeah, that that that's like a huge differentiator for sure for for for Gemini. Um and actually on that topic like you mentioned somewhere that like you know like a year or two from now we're not going to be like typing little messages into the chat prompt. Yes.

Yeah. Yeah. Like so so what do you think like a year from now we're just going to be talking talking to Gemini like through voice or like using vision or like what would interaction model be be like? Yeah. Oh any of these predictions are always dangerous but I will say this.

I think like club the uh it's hard for me to believe a year from now we will still be relying so much on kind of the chatbot back and forth interface. I I think there will always be a place for that. you may always be in like, I don't know, a busy bus or subway or something where you don't want to just like talk out, you want to type or whatever. But I think the um at least inside Google, the leaps we're starting to see in sort of voice both understanding and generation, you're seeing Nano Banana with like the imagery side. You've seen VO at the V like video side.

There there's so much here I think we have to go in terms of just UX and UI innovation. And um yeah, I mean we see this all the time like our Gemini live conversations are like five times longer cuz people will turn it on in the car or they'll turn it on on a walk around their neighborhood or something. They'll just be talking to it. Um so I do think like you know anytime you've had these big tech shifts there's often kind of an input output shift that comes along with it and kind of an interface design type shift. And um I actually think we're in just like the early innings of this.

I think there's tons of innovation and really for a lot of our UXers on the team. I mean, they just love this is like such an exciting moment um because you're kind of breaking out of these very rigid kind of input output to something that could be way more dynamic and fluid. Yeah. Yeah. You're not like trying to hit buttons and stuff.

You're actually like using all the Yeah. I go on walks in my neighborhood a lot and talk to AI and maybe my neighbor think I'm weird but if you're up for sharing like what kinds of things are you talking to it about or are you kind of thinking through things with it or what like you know I have like a like a problem at work or like some sort of document I'm trying to figure out and then I'm like and okay I just copy the whole document into yeah conversation and then I turn on voice and be like hey you know let's work on this problem together and then I kind of go back and forth with it and like you know I I feel like my brain works a lot on a walk outside and like sitting at my desk. Yeah. So, I much prefer to go out. Yeah.

No, I do the same. I do a very similar thing where you're kind of almost like you want a thought partner. Um and it it doesn't necessarily fit when you're like in front of your your laptop or your desktop. You want to kind of be out on the go or something. Yeah.

Like, you know, um I joke that like sometimes, you know, some days I talk to more than my wife. I mean, for better for worse. Oh, interesting. you know, like uh it's it's hard to load, you know, thousands of tokens of context into my spouse. Like they're not going to listen for that long.

They're they're going to get bored. Well, it is interesting. Yeah, it's kind of interesting when you think about the that again that same comment or that same theme of like how do you curate the context and sort of bring that there? Uh that's interesting. I mean, I guess we have like 10 years of context, so maybe that that that be Gemini on that, but yeah, definitely.

Well, it's funny when you think of people in your life that you do kind of have that much shared context. It is like spouses or maybe parents, siblings or best friends from like childhood and things, but it um yeah, these are kind of and you think about those interactions. I don't know about you and in your situation, but like if my wife and I are at a party or something, you know that there's like usually a lot of context where it might be like, "Okay, it's time to go." Yeah. Like, you know, she never has to say anything or I don't have to say anything. You just kind of know cuz you're in sync with the person.

So, uh, yeah. Yeah, that's a good point. You have to use shorthand for conversations, right? Exactly. Yeah.

Exactly. Exactly. Okay. So, like one final topic. Um, I just want to get into the nitty-gritty of how you and your teams actually work with Gemini.

Like, do you do you use uh Gemini? Like, do you prototype stuff first or how do you guys actually build build stuff? Oh, yeah. Yeah. Um, we're using it.

I feel like the tipping point for us internally was Gemini 2.5 Pro when it came out in the spring. Uh that model still is one is like top model on a lot of the leaderboards. It's even six months, seven months on. Um we use it a ton. One of the things I'm really excited about that kind of tipping point.

Um, even say like AI Studio, we have people that'll go in, here's a great example, one of the designers on our flow team went into AI Studio a couple weeks ago, basically rebuilt flow, vi coded flow, and has done all kinds of kind of next iteration features. Um, took him a week. Uh, and we think it's probably going to save somewhere on the order of six weeks of time um to get those next set of features out. uh just because he can take that, hand it off to the team, we immediately can start doing user research. It's just so much faster.

And so that's something we do a lot. Um we have another labs project we put out uh called Opel about a month or so ago. The idea behind that, it's kind of a a visual like nodebased tool where you can kind of chain together certain kind of calls. There's all kinds of agent frameworks obviously spawning everywhere, but we thought what would it look like if you made kind of a visual editor or something like this. So this one's kind of interesting, Peter, because internally all kinds of people now are creating these opals, as we call them.

A good example like one of our lawyers on the team, he created one that will like pre-review a lot of product documentation and look for very specific legal things as like a first pass um and sort of flag things um that are like deeper with you. So there's um both on like the kind of creative side, the process kind of side and then another one is super exciting we're starting to use a lot internally. We have this coding product called jewels where it's sort of this coding agent. One of the things that makes it really cool is it works in the cloud asynchronously. So we'll do a bug bash on the team file bugs and then we just kind of put jewels on it and it'll just start fixing fix.

So like so there's like a whole loop of these things that are happening even on like the kind of software development side that are also really really exciting. Yeah. you just give uh Jules a task and then it'll have a PR ready for it to review or something, right? Is that Yeah, that's how that's how it's working right now. And I think what's really interesting is like where does it go next?

And I think there it's like could you imagine something like Jules monitoring feedback on your app or your product or whatever and it's almost like helping curate the list of like here are the top 10 customer issues. I've been able to work on like four or five of them and you're going to have to focus on you know these three or four or something like that. Uh but it really starts to show like I think a vision or a picture of like co-creating co-developing with AI in that case. Yeah, I'm already using like in terms of agentic workflows. I'm using it for you know live coding.

I'm using it for deep research right that's kind of outsourced to AI and I think in the future yeah like uh just getting inbound like one of your pillars is proactive right so like getting inbound customer feedback because right now I'm just like copy and pasting a bunch of stuff into Gemmaine try to get feedback you know. Yeah, I think that's another part you you had mentioned earlier about how a lot of our the AI products in the market today don't really understand you and that's like the personal side of it. The proactive side is a similar insight. Most of these AI products today, even ones from Google, you have to bring everything to it. You have to bring the context.

You have to bring the prompt. You have to do all this work. And I think what we're really excited about with Gemini is like how could Gemini actually like get to work for you like and sort of have your interests in mind, an understanding of what your goals are, what your projects are maybe for the week or whatever, and then kind of bring you suggestions or kind of move things forward in the background. Um, so I think that's a whole other frontier that we, you know, we're just starting to explore. Yeah, that'll be amazing.

Like if if he tells me like, you know, here's your upcoming week and here's kind of what to prep. like just it' be like a lot of moments of delight if you can do stuff like that. Oh yeah. I mean imagine you wake up in the morning and it's like hey Peter here's like your seven meetings you have today. Here's like two or three things in each meeting are really important.

Um and be sure to ask this question in this meeting so you get like a decision on this part or whatever. You know what I mean? It's like there's so many of these on like a like in the workplace that are really cool. And then I think on the consumer side, we also I don't mean I don't know about you, like it's a very full life outside of work too. You know, we have like young kids and we're running around from different things.

It's like if you had something like Gemini that could help organize some of that and be proactive about that, that's also we think just hugely valuable. Yeah. Like imagine a kid schedule is like a nightmare, man. I need AI's help. It's a lot of work.

It's like help, send help. Yeah. Yeah. And and real quick, just like the last one is powerful. So, so what does that mean?

Yeah. Yeah. Well, I think maybe um the most near-term example of this you're seeing is something like Nano Banana where we've taken kind of like a capability that would have taken either a lot of time or a lot of expertise or money and just making it available in like such a powerful way. And I think this is where we had I had to tweet a couple weeks ago. I felt so bad.

we had to kind of like temporarily cap the generations people were doing because we were literally about to tip over the whole service with the TP. Yeah, I think when when you kind of give someone that power and that ability to kind of make that kind of something from, you know, something from nothing, like some of those examples we showed, um there's a lot more of that coming. And I think that's one of the things is really exciting working at Google right now is of course there's all the cool product stuff and the scale and all of that, but there's an incredible team in Google DeepMind that are just dreaming up all kinds of new raw model capabilities. And so being able to kind of connect those to those product experiences um hopefully that can bring some more more power to people in their daily life. Yeah, that sounds fun, man.

Like you're just getting candy from you know getting candy every day from the deep mind team. It's like you know it's really really fun to work together with them for sure. So let's uh let's wrap this. Like it sounds like a great time to be at Google and you mentioned some of the traits that you look for like like how you know how can like if people want to join your team like how do people like prepare like just go v code a bunch of stuff or yeah I mean it's kind of funny right this I feel like started a few years back where people are like hey look at my GitHub don't worry about my resume kind of thing. So I think um yeah that's probably one of the clear signals we're looking for.

How what are what cool stuff are you building with AI? Um, I always love it when we interview people whatever their background and they come in and they've done deep analysis of our products and they have a lot of feedback about, hey, this is really good, this is really bad. This is where you're beating the competition. This is where you're getting smoked by the competition. Like, so like I think that shows like both critical thinking, but it also shows like product taste and like an ability to kind of form opinions about what matters to users.

Um, and then I think the other thing is like I mean we do a lot of stuff on X and Discord and others. I mean we've hired people out of those groups too that are you know our users that love the stuff. U because I think that's the other thing. I mean we're we're really interested in people who who care about the mission. And you know for us that goes all the way back to kind of I always think my so one of my favorite words in Google's mission statement is like how do you make all this technology kind of accessible and then useful.

And I think that's the interesting word is like we live in kind of this weird moment in time where even if you paused all the model development, there's probably still like five or 10 years worth of stuff you could build that's useful. Um, but it's like uh you know the model development is not slowing down. Uh so there's even more coming is like how do you kind of translate it into into useful stuff? Yeah. I mean that that's what uh yeah like I think Google's original mission was to organize the world's information and like AI is probably better at that than anything I've seen, you know?

Yeah. So that's right. That's right. Yeah. It's never been more relevant.

That's true. Yeah. Awesome. Josh, well, where can people find you online? Give you feedback about stuff.

Oh yeah. Um well, feel free at any point. Yeah. I guess probably I'm most on XJShwood. Um but yeah, I hang out in our labs Discord.

Uh we're always looking for feedback on the products and how to make them better. So keep keep it coming. Yeah. Yeah. I'm I'm very bullish at Google because you guys are getting feedback now.

You guys are iterating fast. It's really really good stuff. Yeah. So thanks for your hard work. Oh, thanks.

Well, thanks for having me here today. It was great great to see you.
