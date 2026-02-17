---
title: "Complete Vibe Coding Tutorial: Build a Full Stack App in 30 Min with AI | Matt Palmer (Replit)"
guest: Matt Palmer
publish_date: 2025-06-08
youtube_url: https://youtube.com/watch?v=2HK9Th7GDiU
channel: Behind the Craft
keywords:
- coding
- ai
- ai-tools
- storytelling
- leadership
---

You can be a domain expert with AI with the power of like asking flawed things, right? And the other thing I want to talk about is like what it means to vibe code and all people see on Twitter are like the demos that they're like, "Oh, look at this thing I built in 15 minutes. It works. It does all this amazing stuff, right? They don't see the failure and the learning." A lot of people ask like what makes a successful vibe coder like how do I get good at this thing?

I think courage. the courage to fail, the courage to start over, the courage to again feel like, oh, I just spent two hours and I didn't actually create anything that worked. But you know what? I'm gonna roll up my sleeves and figure out how to do it the right way and I'm going to try again. When agent's building, what you'll notice is that it's like editing these files, debugging on its own.

And so when it built that first app, we were talking about like prompting best practices, but it actually like made some edits. It took a screenshot of our app to make sure things were working properly. um it'll run test commands and scripts to make sure that it's building the way it should be building. Maybe we'll see some of that in a second. And that's fundamentally different from how a lot of other tools work.

All right, welcome everyone. My guest today is Matt Palmer, head of developer relations at Replet. Uh Matt is a VIP coding expert and a real engineer. And today we are I'm going to ask him to build an app to help busy parents find kid-friendly places nearby like playgrounds, hikes, and more. something I could personally use every weekend.

Uh, and we're going to do this step by step to teach you how to build this app yourself. So, welcome, Matt. Thank you for the introduction, Peter. Really grateful to be here. A little nervous anytime anybody introduces me as an expert and a real engineer, but let's uh hopefully we'll have some fun.

We'll build something cool. We'll build something useful and learn a bit along the way. Um, so we can just yeah, we can jump right into it. I'll share uh my screen here and uh we'll get started. Um, one second.

Perfect. Uh so um today the goal is to build a family activity finder using Replet. We're going to talk about best practices in prompting, best practices in vibe coding, what makes a good vibe coder. Um and we're going to talk a little bit about the landscape of the tools out there because I know it can be confusing as well. Um most importantly, hopefully we'll have have some fun and we'll build something cool.

Uh so we're going to talk a little bit about the prompt and then just get started building in Replet. The way I like to structure these demos, because as most of you probably know, AI takes a little while to write code, um, is that I like to jump right into it and, uh, talk about building the prompts and then take a step back while we're building to kind of discuss the tool, discuss the landscape, and some of those other conceptual things I mentioned. Um, so, you know, one of the ways I like to approach building things like this, uh, is to think a little bit like a PM. Let's think about like the problem that we're solving. Let's think about what we want the solution to look like.

Let's start to think about this like problem space, right? And so when I think about like finding activities, I really want kind of like a map first interface. I want something that looks maybe a little bit like this. Something like a Google Maps or an Airbnb search experience. Um, and you know, some of the skills we're going to talk through when we build this are prompting, processing, analyzing external data because these places that we want to find on our map, they have to come from somewhere, right?

Uh, debugging. Uh, we'll talk a lot more about that as we go on. Um, but if I think about what I want to build, it looks probably something like this. And if I start to break down that problem, might look like, hey, I want an interactive map interface that shows these locations. I want filters or, you know, some other location based features that show nearby activities.

Uh, and then maybe I want to get to the point where I have a favorite system with like user login so I can log in, save things, or mark them as done. Um, and most importantly, we want this to be mobile friendly because, you know, parents are going to be on the go using this with one hand, right? Um, and so, you know, when we start to think about these things, this can be daunting. Um, it can be intimidating to think, well, where do I get this data from? How do I figure out if that even exists?

And, you know, here's where I'd like to add a plug for using AI tools, using web search, using tools that have access to web search. You know, maybe open up claude and say, help me understand this space. What uh open source data exists that might be able to give me this location uh these locations, right? And basically what I did was just that and I found out about this thing called open street map. So if you're unfamiliar Open Street Map big open source data set lets you query basically all of these different types of data.

And so like here are some examples. If we were going to call the Open Street Map API, this is like what that data would look like. Now how did I find this? Again, just doing like some search, finding some docs, etc. And and this really is domain specific knowledge, right?

Unless you're a maps expert, you might not know about these things. But what I want the the point I really want to elaborate on is that you can be a domain expert with AI with the power of like asking clawed things, right? And the power of AI is in product like understanding these domains. So hopefully what we're going to do today is going to show you that, right? And we're going to walk through this example.

So crafting kind of like my prompt on replet. I'm going to say, "Hey, help me create this simple minimalist maps application to visualize our kid-friendly places. This is some of the other research I'm talking about. I looked up some framework." So I prompted Claude, "Hey, what are some good maps frameworks? Let's use leap leaflet for the map visualization and open street uh map for that data." What I did was in this prompt box I just pasted in that uh mockup that I created and then I said hey like let's use these open street map data types and again I found these by asking claude.

So I said I've attached a mockup and some docs. Now you'll notice that when I paste this link that we pasted in here it pulled it into our sort of like scraping modal here. I could take a screenshot of that or get the text content. So now what I'm doing is I'm saying okay here's what I want my app to look like. here are some actual like documentation on the way that this uh framework that I found online works.

And then what I could also do is come in and say, "Oh, well, I was on this Overpass API site. You know, I don't work with APIs. Maybe this is a little too technical for me, but like this is a quick start for 60 seconds for like a developer." And you can think about replet agent replet as a junior developer. So, if this is just like a snippet of code that we could run, well, I bet if I give agent this sample of request and response data, that's a little too long. We'll trim that up a little bit.

We'll actually only just take most of this. Maybe if I give agent this request and response data, right, it'll help me um build out that application. And so, um, what we're starting to do here is, uh, build the context for our model that we're going to use in this prompt. So, now we're going to click start building. We're going to talk about what's going on.

We're going to talk about why we're doing all this, right? And the context of of what we're building here. Um, but the first thing that agent is going to do here with our prompt is come up with a plan. So, it's going to say, "Hey, based on all this input you gave me, let me propose a plan for what I want to build for you." Um, and that's the first step on Replet. and then we'll move into the actual building.

Yeah, I think that's really important. I usually uh when I you know do the co-pilot PM stage with cloud or you know even with replet itself I ask you to give me the simplest text stack possible and also maybe use like free APIs like try to keep that as simple as possible so I don't have to pay for anything you know 100% yeah we're not trying to get anyone to anyone to pay anymore these tools can uh you know start to add up on us right but um what we're what we're doing here you know we'll note that based on the original kind of spec What I was talking about here is is we selected some subset of these features and we said okay like how can we make this as simple as possible to get to something that works and then start to build on that and that's going to be a theme throughout this uh this tutorial. But the other thing I want to call out is that the first thing agent's going to do is design a little visual preview for us. Um, often when we build with maps, it doesn't actually show us um like the the map because that's rendered with uh React. This is just um HTML and CSS.

But this definitely conceptualizes like what we want to build and it looks like it's going to be on track. Um so the first thing agent does is build this v visual preview and then it's going to start writing code for our app. Now this um what you're seeing in front of us is the replet workspace. I think I'd be remiss if I didn't talk a little bit about what this is or why it's different from some other tools out there. So, when you go to replet.com, kind of taking a step back, you're getting an entire code editor and development environment.

Now, we're actually taking that and giving the environment to our agent, which is like our junior software developer to use. It has access to all those tools. But the really cool thing about this is that it runs entirely in the cloud. You don't have to install anything on your laptop. And what we'll see is that Replet has access to all these services and tools that it's going to integrate into your app in real time.

So very powerful, you know, like agent is building out this app in the background. You see all these files starting to pop up as it starts to work on that prototype. Um it builds full stack applications. So we have a client and a server. What that means is that we're going to have a front end and a backend.

And the back end will build APIs and then communicate with that front end. Um, and it's a really powerful architecture because it's sort of standardized and easy to understand even for someone who might be new to this. Um, but also we have this entire environment that's running in this like little window without installing anything. We'll get more into those advantages, I'm sure, as we keep going. And I think having the visual element streaming is also pretty unique to Replet.

I I haven't really seen that anywhere else that I've tried. Yeah, it it makes it cool because you have to wait for a while for it to build everything, right? But it makes it you can kind of see what's happening. Exactly. And that was, you know, kind of what we were going for.

You know, it's a little less uh impressive in this example because there isn't a preview of the map, but for other things where you're like designing something that's a bit more visual and simple um that doesn't have like embedded map elements, it can be really useful. Uh and so, you know, if we're talking about uh vibe coding, right, we kind of went to our prompt here to get to an MVP. Um and there are some prompting tips I like to share with folks. We won't, you know, we'll talk about some of these. Uh, and you're going to see all of these as we build through this app.

Um, but what I've noticed when I'm teaching like, oh, you know, how to v vibe code or like how to build with these tools that a lot of people get kind of hung up on the experience of building and I think it's um, super common because a lot of the principles we're going to teach here actually are just principles of like software engineering or debugging or kind of like logical thinking. Um, and that's not intuitive for a lot of people and we take those for granted. I think a lot of people that have been building in the AI space for a while. So what we're going to see just to call out a couple of these as we start to build is that checkpointing is really important. It's kind of like version control for our app.

And what we'll see here we actually have our preview done here is that agent creates these checkpoints. Right? So when we're building can actually go to a history. Agent is going to save off versions of this application for us as it's building. And the really cool thing is that this is just under like behind the scenes.

This is just get, right? And so at any time we'll be able to go back to these checkpoints. And you can think about it kind of like playing a video game, right? Like if you get to a checkpoint, you don't have to worry about using your work. If something breaks, you don't have to worry about losing your work.

If something breaks, you can go back to it. You can kind of like save your progress there. Um, and you know, that leads into debugging, which I think should largely rely on that checkpointing functionality. like if we get to something that works, we can start there and then, you know, add on new features, debugging along the way to figure out what's going wrong. Um, but as I talk through these, I kind of want to actually implement them in parallel for you.

So, it looks like we have our map here. If I click on one of these, I mean, looks like real data. I don't think Coll just hallucinated this on us. Um, I think this is pulling from Open Street Map. But the first thing I always like to do is to check to make sure things are working because sometimes AI can hallucinate on us or like things might not work.

Uh but we want to make sure that they do. So I can click on these places. I actually can't click on the search um uh box here. So that's something to note. If I try the filters, looks like the filters are working for me.

Um and typically what I'll do here is I'll open the console. So the console shows us what's going on on the back end of our application. Now that can be a bit confusing because there's also uh the dev tools which some people refer to as a console multiple names and this shows us what's going on on the front end of our application right but what we're doing here is we're setting up our tools for debugging to check for messages or logs and what I noticed on the console is that we're getting IDs back and some data. So I think we're fetching these properly. Now, we won't get too hung up on design because what I want to focus on for this demo is building in features, but I think it's important to show you like how I would iterate on this application.

So, what are the things I noticed here? Well, first, sorry, real quick. Which one which one is the browser compos? Is it? So, this this icon here is the dev tools.

And the cool thing about Replet is that these every time we develop because it's in the cloud. You can think about with other tools you might build on local host, right? Um, here we're building in the cloud and so you have this live development URL, but that button I just clicked is the same thing as opening up your Chrome DevTools. We just provide a shortcut. And so you can look at this in the browser, which is what we're doing.

The cool thing about this URL, I don't have my phone handy on me, but you could go to this URL and you'd be able to see this application in real time, right? So, one of the cool things about prototyping on Replet is if you have your co-workers sitting next to you and you want to try and build something and do it interactively with them, they can also look at this app. You can look at it on your phone. Um, and we provide some handy shortcuts for doing that in the browser as well. For example, you can resize the screen to see what things might look like on mobile obviously.

Uh, we'll have to do some work to make this mobile friendly. Yeah, that's awesome because a lot of times I run into issues where it's working in a local host and not, you know, remotely and then or vice versa. So, I guess this avoids a lot of that. 100%. And that's the power of this kind of environment in the cloud.

If you're more technical, you can think about it like a container. If you're less technical, just think about it like its own computer. Now, the cool thing about it being its own computer is that you can just click deploy and we're going to deploy this entire environment. So, if it runs on Replet, you can deploy it. That's really powerful.

But I don't want to waste too much time here. Uh let's let's make some improvements to this map first. Um I don't uh let's say let's uh improve the icons. I'm a big emoji guy. Uh let's make them emojis in a circle with a blue outline.

Uh for uh emojis basically for each um activity activity type. So that'll be the first thing. And then sometimes as I'm building, I like to also take note of things that I'll fix next. So for example, uh we want to fix the search box. Like that's a pretty big one, I think.

Um, but off the bat, like I think the data is the hardest part um, of any app like this. So, fixing the search box, making this responsive, making it mobile friendly already. That looks like 10 times better. I already like this a little bit more. Um, search box.

I don't really like this map theme. Like, this is a little bit busy for me. So, maybe map theme is something to think about in the future. Um, responsiveness, right? Responsiveness also means mobile friendliness.

What is that? Uh what is that? Oh, it's playground that that that kid picture. Okay, the kind of it's a little creepy. Uh let's we'll change that.

So, one of the things uh change emoji uh or playground to uh slide like the slide emoji. Yeah, we'll do that first because that's a little weird. Uh, and then we can start working through some of these other things. Um, but already we're starting to get to something pretty cool. And you know, from from where we were, uh, you can see we're getting some good progress here.

Now, what does this directions do? I can see in the bottom left, what I'm going to do here to test this because I don't want to like, you know, reveal my address to everybody by clicking this and opening it on Google Maps is click it, open in a new tab. And you can see basically from that little preview, this would navigate to our direction. uh in Google Maps. So, we can be reasonably certain that that's that's working as I would expect.

Now, we have our playground icon. Um so, another cool thing about um we use relief leaflet, right, which is uh our framework for this map. We could say use the cardo. It's kind of like a little hack because I've used this before. Light theme for a leaflet.

Um and that's going to give us a bit more of a minimalist map theme here. Uh but what we have here is um our map. It's showing our locations. We can navigate to it quickly. So we're starting to get through our criteria, right, that we talked about.

We can filter on these locations. Um search isn't quite working, but now we have a bit more of a minimalist uh view here. Um a lot better. It it does, right? And we're getting there.

Uh but you know, if we tie this back to some of our um some of our prompting tips here, what am I doing? Well, I'm starting by uh we'll mark this up a little bit so it's a bit more clear to see. I'm starting by showing the AI what I want. So, I'm using images. I'm using code.

I'm using snippets and sample data to really illustrate what we're trying to build. I'm keeping my prompts concise. We're keeping it simple. And we're walking through these solutions one by one. We're defining our outputs really precisely.

We're considering some of those edge cases. Um and kind of throughout this whole process, we've been thinking like a PM and and an engineer. This actually I think vibe coding is harder in a lot of ways from just you know being told what to do and building something because we're figuring out what we're building as we go through these this exercise right like we're figuring out what this looks like. So now I'm going to say hey um the search isn't working. I can't click the search box.

I'll test one more time. Yeah, still can't do it. But, you know, step by step, we're making a lot of really good incremental progress here. This already looks a lot cleaner um than it did before. Search box is set as disabled.

Well, there's your there's your why it's not working. Yeah. And uh you know, that's kind of what that's what it's like to build with LLMs. And so, you know, we also asked, you know, we didn't do this in the demo, but we asked about tools, asked about frameworks, started to understand, you know, what we'd be building with, whether that's leaflet or open street map or these things that maybe we've never heard of before. Um, but we can actually unlock just by giving the right context that that uh thing about using like some light theme for leaflet, you can just search for leaflet and find online, right?

Some documentation or something. Yeah, sure. Like if you do like leaflet themes. Yeah. like oh hey look we could actually okay this is not learn about the different themes that exist in leaflet got it so it's not just asking LLM sometimes it's literally just you know unpacking these frameworks unpacking these things that exist and then saying oh like well now that I know this thing exists I didn't know what I didn't know right and now I do and now I can ask AI to implement this thing for me um and you know I think the big the big thing here is that a lot of experimentation is necessary.

Um, what we're doing is we're building on the frontier of what's possible, right? These are all brand new tools and one of the most fun parts about my job as an educator is that we're discovering the best ways to prompt LLM. We're discovering the types of things that we can build. Nobody knows really what's possible. And so, as practitioners, yourselves, as builders, you get to explore that and you get to build things that people didn't know were possible before.

Um, and so let's see. Okay, looks like we have some search on our app now. So, yeah, it's coming along. Um, let's take a look. What were our criteria?

Uh, we were saying we got our category filters, we have our map interface, we have um we can get directions with Google. So, we'll also consider this one like partially done. Now, let's talk about some of the things that make Replet separate from some of these other tools. Hopefully, you've already been able to see, right? On the back end, we have an API.

This isn't just like a web app. That's just a client side app, just a front end. It's actually a full stack app with a front end and an API. Now, where this starts to get powerful is that Replet has added in a bunch of services that integrate directly into the platform rather than going out externally and adding in services. And that includes things like databases and off, right?

So when I'm prompt agent here, I'm going to be able to add databases and off, but like nobody really cares what databases or off are. They care about what they allow you to do. And what they allow us to do is add users and store data for application. So in this next prompt, sorry. Uh let's quickly define O basically means log logging, right?

That's basically what O means. Yeah. Yeah. Off like uh it'll be very clear, but like you know here you can see my profile icon in the top right. I think that's like the clearest way to show it.

It's like what we're going to do is we're going to do that for our app. And so we're going to do it in in a way that uses Replet's infrastructure. So when we add o we're saying okay I just want to add users and login and because replet can add databases to your app it can store those users it can store that login and it can actually integrate it in a way that's completely bundled in our replet app which makes it a little bit simpler. Mhm. So now what we want to do, this is going to be a bit more of a complicated step, is I want to be able to save and um let's say mark uh locations as done for um my user.

Add login. Uh we'll just you can just say add login or add off and we'll match that for you uh to my app and the ability to save locations. Um oh why don't we make it like uh favorites instead of done because you know I still might want to go back to it. Well so what I was thinking is we have favorites and then we have like visited right. So okay you have two different categories.

Yeah. Yeah. This is like you know I need to learn some PM skills to define these things a little bit better. Let's uh so we'll clear that up. If it was confusing to you, it's probably confusing to agent.

I want to be able to save favorites and mark my favored uh locations as visited. So, basically, this is like I go hiking a lot and this is what I want, right? Like I want to have a list of favorites, but then I want to know of those favorites which ones I've already done and maybe which ones I want to go back to again. Um, so yeah, we'll send that and we're going to observe what happens because I think this is going to be interesting and maybe um informative and then I'm going to talk a little bit more about how agent builds and we'll walk through some of these past chat messages um because there are some also important things to call out there. So what you'll see right if I open this up we're integrating with replet off and a database and so that database I showed you agent's going to create this database and attach it to our app.

It's going to implement off and attach that to our app as well. And yeah, like uh I I normally stay away from this stuff because it's it's actually like a huge pain in the ass if it's not built into the platform to do this stuff. Like it can get totally stuck, you know, right? And then you're creating multiple accounts. Um you're pulling in external APIs.

Uh you could be exposing sensitive information. The thing that we're really proud of and that we've been we recently released last week is uh some security scanning functionality which we'll talk about but also what we've always done is build these apps with a client and a server and then built the database in using best practices and what that means is that out of the box you get protected against things like SQL injection or like some malicious attacks on your database. Um the API calls are separated from the front end. So basically um we make it very difficult for like attackers to you know or or even people that just go and try to like mess around with your app to get information out because of the way that we build these apps. Um and that's also true of Yeah, exactly.

And that's also true of like O for example because we're using Replet's authentication service. It's protected by um you know a bunch of our authentication infrastructure. Uh, and your app out of the box gets things like protection from DOS attacks and some of these other things because we're building with these sec this secure platform. Yeah. Because if people mess around with my app, I have not have no idea how to protect myself.

I don't know any of the stuff. So, exactly. Exactly. And I have some blog posts about that as well, like what we do and everyone can feel free to read more about that. Um, but the other thing I want to call out is that when agent's building, what you'll notice is that it's like editing these files, debugging on its own.

And so when it built that first app, we were talking about like prompting best practices, but it actually like made some edits. It took a screenshot of our app to make sure things were working properly. Um, it'll run test commands and scripts to make sure that it's building the way it should be building. Maybe we'll see some of that in a second. Um, and that's fundamentally different from how a lot of other tools work.

Um, and I found when I'm building these apps, it makes the process a bit easier. Even if this run is a little bit longer, I can come back to the app with more certainty and know that it's running. And so often my flow is I'll be building something. We can talk about these and I'll keep an eye on our little fabicon up here. It might be tough to see in the stream, but it's purple right now.

And it'll be green when agent's done done building this next step. Or you can just go on a hike, man, and like, you know, pull up rep on mobile and then This is true. If it's done. Yeah, I mean so I feel like you know a lot of people might say oh mobile you know that's great most mobile apps are kind of gimmicky you get the full functionality of replet on your phone and you can see the app that you're building you can see all the code I mean a lot of times if I'm going to an event I live in San Francisco which is why this map is of San Francisco I'll be like in the Whimo or in the lift or whatever like I need to finish this app you know I need to add more functionality I need to polish it up and it's like pretty good you know so maybe one day I can do my do my job out on a on a trail in Marin or something, you know. Yeah, that'll be amazing.

Yeah, baby steps. Baby steps. Uh we'll get there. So, where are we on our kind of journey here? Um we have our map, we have our category filters, we have our some location based features, and now we're working on our favorite system.

And then we might get to some mobile friendly design things. Um we're implementing our best practices and we're we're you know, uh learning a little bit about what it means to be a good vibe coder. And the other thing I want to talk about is like what it means to vibe code and what it means to use AI to generate outcomes. Now, if you're PM, if you're listening to this, if you've used Claude or Chad GBT, what you know is that the same prompt gets you different results. That's like a little disorienting and kind of scary because it means that sometimes you might get bad results and sometimes you might get good results.

And so I have a normal distribution here. Like if you've taken statistics, all this means is that like this very oversimplified model, this probably isn't what the variance looks like. Our quality of outputs are probably on a spectrum. Like sometimes we might prompt agent, we might get something that's over here that's like really good. Sometimes we might get something that's like subpar.

Sometimes we a majority of the time rather we might get something in the middle. And so what that means is that you know sometimes we might build apps, they might work really well. Sometimes they might not work really well. But there are things we can do to increase the likelihood and quality of the likelihood of success and the quality of the apps that we're building. And those are the prompting tips that I just talked about with you all.

Right. Yeah. And so yes, this is an oversimplification, but nothing is perfect and you will get errors. And that's a big part of vibe coding. And sometimes like uh you know, you have initial prompt and they build something that's like doesn't actually work and it you can get stuck, right?

And sometimes it's I won't talk about the details of this, but sometimes it's good to just start over again because like like I said, sometimes it's good and sometimes it's bad. Yeah, 100%. Right. If you find yourself in this in like a you're you're giving prompts, you're doing all of the things that we talked about and you still can't get it to work, sometimes you just got to start fresh and you know like actually right if we think about variance and what this means in terms of statistics, you know, we're too used to certainty, right? Everything we've built has been certain.

Normally you open up a tool and it's like press button get result. That's not true with AI. And so the two things I like to tell people are don't be afraid to fail. And to your point, Peter, don't be afraid to start over. And so, you know, the secret, quote unquote, I was talking to SM engineers about this a couple weeks ago.

The secret of being an engineer is just failing a lot, right? And nobody wants to see nobody wants to know about, you know, the hours you spend building something and breaking it and trying over again and looking like looking like an idiot. I say that because I do that all the time, right? Um, and all people see on Twitter are like the demos that they're like, "Oh, look at this thing I built in 15 minutes. It works.

It does all this amazing stuff." Right. They don't see the failure and the learning experiences and all the other stuff. Yeah. People don't tweet like, "This is wild. I built this in 15 minutes after two hours of trial and error." They don't they don't tweet that.

Doesn't Exactly. Exactly. And you know like this demo I've built similar demos and that's how I knew how to use certain features and I've built with replet before and that's how I knew to use replet off and that's really what I love about my job is that I do these things and then I say well now how do I go and show them to people in a way that you know they can kind of work around the mistakes or they can have shortcuts to building these things. Another another advanced tip, at least for me, is like after I get stuck in one of these like endless cycles, I ask AI like kind of like what what did we learn so far to avoid these mistakes? And then it tells me and I put that part of the prompt back into the initial prompt to start over again.

So then do the same [ __ ] all over again. Yeah. No, that's a great one. Um, sorry, I just got distracted by the prompt here. I agree with that totally.

Uh, we'll we'll talk through it. Um but I do use that with agent quite frequently. I think you know people forget they think they have to come up with all the things but you know you can ask AI what would you add next to this application? Help me understand what we just built. Help me understand how this thing works.

Um exactly and and you can actually learn that way. That's you know a lot of people say um hey you know like all this AI no one's going to learn how to build anything anymore. Well, I can tell you personally, I've learned so much about web development just by watching agent work and like digging into what a client is and how it's structured. Dig digging into what a server is and what these things are, what a route is, how this app is structured in terms of React and whatnot. Like I got my background in data, so I wrote a lot of Python, but you know, AI has really taught me a lot about webdev and how to how to build front-end applications in Typescript.

Um, so, uh, let's see what we got going on here. It looks like this is a sec. This is just a randomly generated string, so we don't have to worry too much about exposing that. Looks like agent might have done what we asked. I'm going to open this in a new tab.

We'll go over here. We'll close this guy. Um, so this is our preview of our app. Now, what we have is a login button. Let's see what happens if I click login.

So, this is going to say, hey, we'd like to access your replet account. There's my replet account. I'm going to click allow. And right when we say off, this is kind of like logging in with Google, right? So now I'm logged in and theoretically I my account now has access to the app.

What's going on on the back end, right? We have O um I have a user and you all you know maybe Peter can edit out my email from what I just showed you. Okay. Okay. Uh we have a database.

Um and in the database we have users. There's my email again. Yeah. Time time stamp. Don't worry.

Yeah, I love emails. Uh but uh it looks like right we have um we have the tables that we would need sessions, favorites, places uh to store our data. And I'm walking through this because you know sometimes this can be a bit tricky to configure. Now do we have somewhere where we can favorite these places? I I don't actually think we do.

Like I don't know where I would click favorite and it still says login save favorites. So, I guess what I kind of learned here is uh there's no place to favorite um a location and the app still still says log in to save favorites after I've logged in. However, right, still impressive. What we've done is we've laid the frown the groundwork rather for being able to save this in a relational database. And you know, again, relational databases are like kind of complicated.

it can get kind of scary. But what I found with using AI is if you really start high level like hey what's the best data structure for my application you can ask agent that what are some like ways that we can build this app that would simplify the data structure or make it faster or make it easier to um interact with and then from there you say sorry yeah getting there getting the database and login working in one prompt is pretty amazing I mean I mean it took two prompts so you know I can't take all the credit but um yeah no I like I'm blown away um when I use this tool and you know that's the power of having these um integrated uh this integrated functionality in the app and something I kind of breeze through is that we also have secrets right and you know if you've ever used a N file or you've tried to use secrets locally or you actually accidentally push secrets to GitHub you know I did that early on in my engineering career um this can be really useful if you've ever saved secrets somewhere in your computer then forgot where they were like API keys or stuff. We have account secrets. So like I could pull in um any of my account secrets into this application, right? And um you know the power in that is that you can just enter in API keys.

They pull through to your app. As you saw earlier, agent actually edited API keys and added one to my app. It created that random session secret for us. And so having all of the what you're starting to see is having all of these tools integrated into one experience um saves us time. We don't have to go to different providers.

we don't have to like break our flow state. Uh and it makes things easier and helps prevent mistakes. Um for example, you know, one of the things we did here is like we made it impossible. So the session secret is not a real secret. It's a random string for our app.

Um we're working on building in some uh like checks basically like so if you paste in an API key with agent, it actually should throw a warning. So I'm going to pass that to the team. Normally it alerts us that that uh that that would be an API key. So something's broken there. Um, yeah.

You don't want you don't want the LM to remember your API keys. Yeah, exactly. So, we're forcing people kind of into best practices that way. Um, now, okay, we have our app says save my favorite places. I'm logged in.

I can click my So, this is like I could see potentially my favorites. Um, see what happens when I click that. Did anything happen? Let's go over here. Nice.

Um, so copy the page. Yeah, we're uh we're learning about what what works and what doesn't. So, um what I usually like to do is check the console like what happened. Um you can see we're making all these requests and I'd say I get a 404 on the favorites page. 404 is just not found, which is what we saw when we clicked um here.

Yep. And you know, we can even add this context because I'm pretty sure that's the issue. Did you forget to add the page to the router? Should know what that means. And then, well, let's take a look.

When I click favorite, what happens? Um, you can actually see post API favorites 2011. Like, sounds good to me. Um, when I click favorite, I can see a 2011 in the console. But um Oh, and we get visual feedback.

It just took a second to come through there. Yeah, there you go. And I also don't think And now we have Mark visited as well. So um that's amazing. Yeah.

Yeah. Yeah. So it took uh a few seconds for the um favorite to populate on the front end. Can you make it instant? Um so we'll go after these one at a time.

We'll say this guy first and then we'll follow up with that. But this is getting much closer even if you know I care a lot about padding and spacing and UI and this this is driving me a little nuts right now but we'll get there. So let's test the mark visited functionality as well and see what happens. I click that um looks like it and and like po post just just to kind of explain to nonangle people post just means updating like updating some data in database right 100%. And you know I you again as as someone who's built with these tools I take that for granted but what what you will see just like if you're using a spreadsheet and you're learning formulas in a spreadsheet just like if you're learning a language um whether that's you know uh Latin or French or whatever or an actual programming language you'll start to understand oh a get request just means it's getting this thing.

A post request just means we're sending information. A patch request means we're updating something. Um, and again, we see our little check mark icon come through there. So, it's again, it's a little delayed, but you kind of learn how to speak the language of of web development, of building with these things. So, yeah, it's all a learning experience, and I would just say don't let it intimidate you really.

And and um, can you show us uh I know it's not fully complete yet, but can you show us how easy it is to deploy? 100%. Yeah. Yeah. So, the cool thing about deployments is that when you click deploy, it's just a snapshot of this environment.

Currently, one one thing a lot of people ask about is, well, can I have a database for development and a database for production? Currently, that's not possible. We're releasing that in the next couple weeks. So, maybe by the time this podcast comes out, the answer will be yes. Um, okay.

So, again, we're multitasking here. So, let's let's check this really quick and then we'll go through the deployment flow. My favorites. Okay. We got these things.

It says unnamed location. So, we'll uh we'll make that adjustment. So, we're saying, hey, this is what I see when I go to this page, right? We'll get working on that next. Um, and the great thing about this environment, as I was kind of mentioning, we're going to have is that, you know, we're going to have those database features, as I mentioned, is that I can take a snapshot of what I just built and deploy it live to the internet.

So this preview link is temporary, but if we want to make that permanent, we go to the deploy tab. Again, this is where you could see, you know, maybe a little bit of scary stuff if you don't know what these things mean. We're going to kind of select the best configuration for you. So, we're not going to worry about that too much right now. But if you want to go back and understand more about these things, you can kind of go back and start to dig into them.

But what we're going to do here is uh we'll call it kid-friendly maps. We'll shorten that a little bit. And we're pulling in all of our different secrets from our app as well as the database. And we'll note that we can also run a pre-eployment scan. So if you're concerned about security issues, we released this last week.

We have our security scanner. So clicking that button is going to run a scan on our environment to make sure that um it's not secure or it's secure rather. And so what we found actually were some user controlled data input methods in our front end uh that could be potentially vulnerable. So we could actually do is ask agent. Let's make sure agent's done.

It says it it says it fixed the favorites. I can get easily distracted. So like I have to make sure I don't get go down a rabbit hole. It doesn't look like it did that. But we're going to table that for later and we're gonna ask agent to fix these security vulnerabilities.

So what you see from our security scanner is that we're passing that information to agent and we're saying, "Hey, this component has some issues. Can you fix that for us?" Yeah, this is a great feature, man. This is great. Yeah, man. I think this every app should have this.

And and the the most important part I want to emphasize this is like really scanning over your code for real issues. Um, you know, the thing about AI generated code, uh, is we're going to get to a point where we just build these in, you know, but it's almost impossible to make sure that everything, um, is 100% secure and that's why we added this check. Uh, so we're kind of fixing them now and we're going to move more towards a framework where we proactively build without these these um these errors. But if you know if agent's able to catch it, just imagine all the AI generated code that's getting run written and run elsewhere where these haven't been haven't been found. You should just spin this out as a separate product for all the other AI coding tools that exactly this is like required.

This is like P0 for all the coding tools. We fixed it, right? And you know, shout out to our partners at Sam GRP for helping us with this one. Um, but what we just did was fix these these security issues. Uh, and so you know, just like that, we patched it.

The other thing I was, you know, the other it encompasses a broad range of issues. So like the demo I had I think we can skip because it caught a few other issues is like you can paste in a SQL injection vulnerability in your app and it will detect that as well. But we fixed our security issues. Let's just click deploy again. What's going to happen here is that we're taking a snapshot of our app as it exists right now and we're pushing we're publishing it live to the internet.

So, in a couple minutes, that's that'll be out. And then what we can do is come back over here typically and I'll be like, okay, well, like I now have my defunct favorites page. That's like a little unnamed location is a little depressing. Let's see if we can figure out what's going on here. So, we're getting the favorites.

What we can do here is we have our element selector. So, I'm going to select this div and or this card title and I'm going to say this still says unnamed uh location. Um, and so we're passing additional context. The element selector is hopefully going to help agent debug the fact that this should not say unload unnamed location. Also kind of nice is that we get a little notes um, you know, functionality in here.

So like maybe we want to uh save some notes. Yeah, that's great. You didn't didn't ask for that. You just Yeah. Yeah.

Okay. So like look at this. Um, this is working as designed. There's no name available for a location. That's interesting.

Well, what's going on on our uh favorites um thing here? Looks like what are we storing? Interesting. It looks like right we might be pulling in uh either we're not one storing the data in the database in the first place. Um or number two uh we're trying to access what agent just said is it's looking for favorite.place.name.

I don't actually see a place column in the database. So like there might be an error uh sort of in our implementation. But we you can see both the favorites are in OSM places. So what I'll do for agent also is I'll say I see the favorites table favorites table favorites table and the OSM places table but the name is in OSM places. It looks like you're not pulling it through.

I I think may maybe another good best practice here is like before you actually build database maybe just like explore with it a few times what the data table should look look like and like give some fe feedback that might help too. Yeah. um you know like data structures and data you know that is its own profession right you know like it's it's it's hard to change but like there are entire you know data architects is a job of people that just design databases so I don't want to trivialize that especially as you start building out like really complicated applications um it can be very easy to create confusing interfaces that is another place though where as you build you actually learn um the way you want your data structure to to to live or look. And so, you know, maybe I build this app out and I'm like, man, I think we really messed up the architecture. That's where I would go back.

I would start uh changing the schema, maybe trying some new things out. That's vibe coding, right? And um it looks like the thing deployed, man. You want to check it out? Yeah, let's take a look.

Uh thanks for catching that. So, we have our link here. What we should see is the exact same thing. So, we're loading all those places. Um I can come up here again.

It'll be a new login. Uh I can log into my application kid-friendly maps.repit.app and I see my saved because we're using the same data uh database. I see my saved location with my favorites and and of course uh the O also supports like Google login, you know, just an email login too, right? Yeah. Yeah.

Yeah. That's so um what I can do here is well I don't want to log out of replet and I think I'm sharing uh I would I want to show you kind of um maybe what this login screen looks like. Um, but you can configure your app icon here. You can also choose login providers. What's going on here?

A lot of people ask this question, so this is good to talk about is we're creating if you don't have one, a replet account for the user, unsubscribing them from all marketing materials, so you won't get like annoying emails. If you have users for your apps, don't worry about it. Unless they want to learn about Replet, mostly because I'm sending those emails, so I don't I don't really think they're annoying, but you know, uh, I get it. Um, so we're using all of our infrastructure to create accounts for these users, but then passing that through to your application. So out of the box, you get all the benefits of our authentication infrastructure.

Um, which is actually pretty useful as it would turn out because O is really hard. So we want to save you the hassle of building out that O product and make it as easy as possible for you to build. That's awesome. So um, I think we got like five minutes left and it's good that you build a full app that mo mostly works. I think I'll use it this weekend.

I'm I'm I'm glad they didn't call it kid-friendly maps Matt Palmer because that that would kind of weird. So, you know, I was like this whole demo I was like, please don't make anything like weird with my name and like, you know, kid-friendly or whatever. So, uh we're doing our best. But, uh I I guess let me ask you one last question, man. Um well, let me ask you two questions.

One is like where do you think this vibe coding stuff is going to go? because we're seeing like uh OpenAI launch codeex. Do you think the stuff is going to become more async like you just kind of like tell do stuff and you just kind of go away for a while and then come back or how do you think this thing will evolve? Yeah, I mean that's a complicated question, right? Um yeah, to your point we have codeex, we have cloud code, we have all these other tools those are targeted more at devs, right?

What I just showed you today is more for prototyping internal tools uh maybe less technical users, but it does seem like we're moving to that async um that async model. And here's like my theory about that, right? Every uh you know, as time passes, the building blocks that AI can write reliably get bigger, right? So it used to be tab autocomplete. Everybody was like, "Oh man, AI can tab autocomplete.

This is crazy." Like a year ago, right? And then it was like AI can write functions. And now we're getting to the point with agents. AI can write entire applications. Now to your to what you just saw, there was a lot of human in the loop, a lot of manual intervention that was required, but that's less than it was five or six months ago.

And so the amount of time that AI can work uninterrupted is increasing exponentially. You know, it used to be 5 seconds, now it's 10 minutes, 15 minutes. And so what I think we're going to see is this human in the loop kind of pair programmer model where I'm watching AI, I'm supervising, and then it'll say, "Hey, Matt, I need I need help with this thing." And then I come in and I debug and I help it get around an issue or I give it an architectural decision or make a change to the plan that I had. Um, and that's what I've seen. That's how we've seen things develop.

Seems like that's the way um AI is moving. Yeah. I mean the ultimate vibe coding is like I watch some Netflix and then I get notification on my phone and then give them some input and then keep going. You know that's one day. Yeah.

There you go. And and and uh you actually didn't cover like you had like a general tip that I really like for vibe coding which is you know the core themes of vibe coding include agency, curiosity and courage. So why don't we why don't we end on that man? like um what do those three things mean to you and why do you think that's really important? Yeah, you know a lot of people ask like what makes a successful vibe coder like how do I get good at this thing?

Um you know it boils down to I think the first thing agency having sort of uh the motivation to take action and the motivation to say this thing doesn't work and I'm going to figure out why and I'm going to make it work. You know, in the same way that I kind of used this analogy earlier, if you have a Google spreadsheet in front of you, like it's just a blank canvas. And a lot of times spreadsheets break. They're actually really annoying. I've spent most of my career trying to spend less time in spreadsheets.

But they're also really cool and really powerful. So writing code, being an engineer, being someone who builds stuff. It's the same thing as being a product builder. You have to be willing to take action without someone feeding you, you know, sort of like what to do. And you know, with AI, with agent, we get this blank canvas.

We can create whatever we want. That can be intimidating, but it means we have to come up with what we want to build. We have to define the requirements and then we have to go tackle those problems that pop up. You know, we have to have uh I think courage. The courage to fail, the courage to start over, the courage to again feel like, oh, I just spent two hours and I didn't actually create anything that worked.

And that's really like kind of embarrassing for me. But you know what? I'm going to roll up my sleeves and figure out how to do it the right way and I'm going to try again. Um, and I'm going to learn about the tools. And, you know, that's part of being a professional and part of being a builder.

Uh, and I think, you know, that courage ties directly into curiosity of saying, well, how do I make this product better? And a lot of these skills are the same skills that you have if you're a good PM, good designer, good engineer, all of these things. Um, and I think that also ties into agency. It's good to hear that from you because, you know, you're like head of the rail at Rapid. And I feel like a lot of people like who maybe are not engineers just take themselves out of the game.

They think like, "Oh, I can't do this. This is too hard for me." And just don't. And now and now I think I want people to realize that you have all these like, you know, you have all these AI tools that will actually be a co-pilot with you will help you through these steps, you know? So like you shouldn't give up. Just keep trying.

Yeah. Yeah. And you know, maybe in your own life you've seen this where you knew somebody and they would always say, "Well, I'm bad at math." And so they never got good at math, you know? And it's like if you tell yourself that, well, yeah, no, you're you're not going to try and you're not going to put in the effort to learn it. And you know, my belief I'm a really optimistic guy.

I think anybody can do what I'm doing today. Um, you know, it might take a little while. It might take some some trial and error, but I think you all can get there. And, uh, to your point, Peter, some of these projects I used to say, oh, well, like I can get to that with a weekend or in two weeks or like whatever. I just don't have the time.

Today, you can get to it like in a morning or in an hour. Figure it out and get a lot of really cool stuff done. Awesome, dude. So, so like where can people find you online? Is it just like repetit.com or Yeah, me specifically.

I'm big on X. I love X. you know, you can follow along with me there. I'm also on LinkedIn and I have a personal YouTube channel where I put out videos all the time. I'll give those links to Peter.

Uh I'll give it to you well to share in the in the footnotes, right? Um and then all of the Replet content comes uh from the Replet YouTube channel on replet.com. I send out a lot of emails. I send out, you know, uh kind of monthly recap uh some user showcases for good apps people have built. So, if you're into Replet, you can follow along with those there as well.

Okay. Thanks so much, Matt. This is awesome. I'm going to play with this app uh myself and try to build it myself. Amazing.

Yeah. Thank you.
