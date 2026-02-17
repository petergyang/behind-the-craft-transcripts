---
title: "Master Google AI Studio in 40 Minutes | Logan Kilpatrick"
guest: Logan Kilpatrick
publish_date: 2026-01-25
youtube_url: https://youtube.com/watch?v=lbESr58-7DQ
channel: Behind the Craft
keywords:
- ai-tools
- coding
- execution
- product-management
- culture
---

We use AI Studio to make AI studios. I clone the AI studio UI all the time and I ask for like adding features or modifying. Do you still do the PRD in the design or you can kind of skip that thing? We basically require now you go and build a functional prototype. So like it is a step part of the process.

68 seconds from an image to basically a fully functional version of the ASG UI. There's one mode and the mode is we ship fast. There is no other option. There is no other alternative. How do you get it to show you defined?

You just make a bunch of tabs and then give it different directions. Yeah, that's a good question. One of the things that I do is um All right, everyone. I'm super excited to have Logan here today, the one only Logan uh who's product lead for Google AI Studio and uh really excited to get Logan to give us an inside look at how he actually vibe codes apps using AI Studio and all the amazing things that Gemini 3 can do and also how he and team actually ships at startup speed inside Google. So, welcome Logan.

Thank you, Peter. I'm excited. It's been a long time coming for us to sit down and do something like this. So, I'm excited. Yeah, super excited.

So, why don't we just get right into it? Uh, do you want to like kind of give us a quick tour of AI Studio and maybe show building something? So, folks might have used AI Studio in the past. Uh, the sort of historical context is AI Studio as our platform for builders. If you use the Gemini API, if you want to try our latest models, um, and now actually if you want to vibe code, all of those things, uh, sort of you start in AI Studio.

On the lefth hand side, we're in the build mode right now, which is I think what we'll focus. Um, but there is like a playground and you can manage your usage and billing and a bunch of other stuff. Your quota page um is in the rest of AI Studio. But in build mode, um you're sort of dropped into this uh this place to start building whatever your idea is. And my favorite thing right now about build mode is you can just go and click like I'm feeling lucky.

Um and we'll see what it comes up with. create a crossplatform social media content generator um etc etc. I like this idea. Let's kick this off and then in the meantime I'll actually go back and we can look at that example in a second. I'll go back to the main page.

Um so you have this way to kick off building apps. You can sort of click through some of these different chips um to add different capabilities. is like if I wanted to infuse Google search with a real live uh audio conversation with V3, I could then put in my idea um of like what brings those things together. Um you can also go and discover a bunch of things that we've pre-built. So if we go to the app gallery, you can see a bunch of ideas.

Everything from landing pages to apps built on Nano Banana. Here's Amomar on my team as a he built this comic book app that brings him and our one of our designers Chanel into a comic book together which is really cool using Nanto Banana Pro um to being able to build games and voxil art and interactive 3D experiences to just some of these like goofy uh things like the ball bouncing demos and SVG art generators and everything in between. So if you need inspiration, you want to see what the models are possible of beyond just actually Gemini 3. This is like our whole suite of models, um you can come to AI Studio, you can go to the gallery uh and look through a bunch of ideas. And the fun part is that you can actually fork any of these ideas.

So if we let me choose one that seems reasonable. We'll see. We'll make this ball bouncing one and see whether or not this works. Uh but I'll try to be uh ambitious with this. So, I'll say instead of it being a ball bouncing simulation, make it a water dropping into a or make it make it water.

Mhm. Instead of a ball. So, it should have fluid dynamics. No idea whether or not this will work. Um, but we'll kick that off.

Um, and we'll come back to this example. Hopefully, it'll all be working. Um, but I think that the point of the the point of me doing this is like any of these ideas or actually any app that like if your friend uses AI studio and they build something, they can send that app to you. Um, and you can actually remix it. So, if you have ideas of like, oh, I wish I could do X, Y, and Z thing.

Um, all that's possible uh just directly by remixing it. So, I'll go to Yeah. And also I I think AI studio like building these apps is is free, right? Like are you turning your money for this or No, it's it's Exactly. No, so it is free.

Um, so there are certain parts of the experience that require a paid API key. Let me find the other example that I I kicked off. What did I kick off before? Um, oh, the cross-platform social media content generator. Um, so we kicked this off.

It took in all the context that we put in. It spent, you know, it's been running for 190 seconds. A couple things that I'll I'll call out. So left chat panel, you can sort of continue to iterate on your app. You can see all the files that have been created.

can hover over and it'll give you like the quick tlddr of what's happening in the constants.ts file or what's happening in the app.tsx file. Um you can then preview your generation and then you can actually go in and see the underlying code. So if you're a developer or you sort of know how to code and you want to make manual modifications, you can actually do that if you want to. Though you could do everything without seeing any code. So for this one, we're using Nanoban Pro, which is why it's prompting me to put in an API key.

So, I'll go ahead and I'll do that and then we'll hopefully be able to build something and we'll see. What was this idea again? Create crossplatform social media content generator. Uh, so we'll see if this works. What's our idea, Peter?

You have anything? Let's do a rant about product management. I'm I'm glad that. Okay. Let's run about um uh you know, stop the cross functional meetings.

Let's actually just prototype and show it to users. Yeah, something like that. I like it. Um, so we're going to take this in and this is the post idea and we'll make it a witty tone. Um, and we'll do it 1K.

Sweet. I'll kick this off and we'll generate it and we'll see what happens. Um, so behind the scenes, this is using like the Nano Banana Pro model and it's I'm assuming it's actually going to use Gemini to then take in this input that we gave, put it into a format that Nano Banana Pro is going to actually be able to use. Um, and then it'll generate that image for us. So it might take a few seconds to first generate the actual like prompt for the model.

Um there I like this. Okay, so LinkedIn is I have a confession to make. I love a color-coded road map as much as the next manager. There's something deeply satisfying about moving a geo ticket from backlog to in progress. Let's be honest.

Yeah, this is interesting. You got to tell not to add the hashtags, you know, but you know I know I know. Well, this is this is too much in pre-training that uh everyone thinks there needs to be hashtags on on X, which is funny. Um but actually nice. So, we also have images that go with all these things.

I kind of like this one the most to be honest of all of all three. The one for X is is pretty engaging. So, um a good example of like this is like the fusion of three or four different things. And you can actually go in if you this is the one time where like the code is actually quite helpful. You go to the code, we have this Gemini services file which sometimes has the prompts like actually yeah this is what it has here like your professional social media manager the tone the requirements.

So here you can actually go in and like do a little prompt tuning if you want to. This seemingly works like reasonably well but here I could say like for ax never use hashtags they are lame. Um and then you'd be able to sort of make use of it. So, um, lots of cool customization and we can keep iterating. We can keep asking for additional features or customization in different ways.

Yeah. And I will say that like I I was playing with this the other day and, uh, you know, I I try to use like nano banana to build stuff in cursor too. And, uh, it's it just took more work. Like I think in AI studio you have all the Google stuff hooked up already, right? So like it just I literally just click a button like make me a nano banana app and add my prompt and it it'll just work.

Yeah, it does work. I mean, this is the magic for us. Like this is part of why we wanted to do this too is like we we have an interesting edge to be able to hook all the Google stuff up and you can also do things like deploy directly to uh Google cloud um so that you could like make this a production ready app if you wanted to. So there's there's lots of lots of interesting and unique things like that. But let me let me go back really quick just to follow up on our um the other example.

So I'd asked this to switch the ball bouncing example to more like water droplet fluid dynamics. Um, and it kind of is getting there, which is interesting. So, it seems like there's a lot more. Maybe each ball is a drop of water or something like that. Yeah.

Yeah. But gets very interesting to see like, you know, you can do a lot of remixing and refactoring of this stuff. Uh, which is super cool. Yeah. It's easy to remix stuff, man.

Like, if I want to build a beautiful landing page, it's easy just take an existing landing page and just re remix it. This episode is brought to you by Linear. Let's be honest, most project management tools suck. That's why I love working with Linear because they share my obsession for craft and quality. Linear is incredibly fast, beautifully designed, and comes with built-in support for AI agents like cursor.

As a PM, I love using linear to capture customer feedback, draft PRDs, and manage development and communicate across the organization. Product teams at OpenAI, Versel, BS, and Cash App all use linear to build complex products at lightning speed. See for yourself by visiting linear.app/behindthecraft. app/behindthecraft. That's linear.app/behindthecraft.

Okay, now back to our episode to your question before of like how do we potentially use AI Studio inside of Google to like increase the product velocity overall from a Google perspective, but also from an AI Studio perspective. This is what we do. We use AI Studio to make AI Studio. So, I clone the AI Studio UI all the time and I ask for like adding features or modifying and we can actually do that live if that's helpful. Um, but it's one of my favorite it's one of my favorite use cases for product development or PMs to like take their existing product and like add features.

Do you have to give it some sort of a style guide or or something to make this work? Yeah. So, this is let me let me do it live and I'll move my tabs around. Um, so I literally am just going to go like this screenshot and capture and then I'm going to go start. I'm going to say clone this UI exactly use the same styles.

So we'll kick this off. We'll see how quickly like one of the things that I'm always impressed by is just like how fast it's able to make this product experience work. And again like our team is literally doing this like dozens or hundreds of times a day of just like taking the a studio product experience iterating on it and other teams across Google are doing this as well which is which is really really fun. So I think you're seeing like a real speed up in how quickly we can iterate on some of these ideas. while we're on this topic like you know like in the old days we used to write the PRD and the design and everything first right but I'm guessing now you just do the prototype first and then do you still do the PRD and the design or you kind of just skip skip that thing like yeah yeah it's a good question so I think for us right now the place that we're at is um there is some detail in it's like all three at the moment is basically the short answer so we do PMs at least on my team are still writing PRDS um we still have design like actually doing a lot of this work.

Um, and the last part is like we also basically require now you go and build a functional prototype. So like it is a step part of the process is to have that. Interesting. But this is pretty darn good. Um, I feel like it looks almost exactly like the AI studio UI.

Um and we got in 68 seconds uh from an image to basically a fully functional version of the AI Studio UI copying most of the details. And then the fun thing is like I can just iterate from here. I could be like so what would it be like if I had X Y and Z feature instead or this thing was collapsed in this way or we presented information in this different way and do that iteration really really quickly. That's awesome. do like uh you know like the planning and development stuff like do you ask it to write a plan first or like I think if you're just doing iteration you can just tell it to make updates right you don't have to make like a whole plan and spec or anything just yeah I don't I don't do that the only time that I do that that's like common in my workflow personally is like taking a PRD actually so oftentimes what I'll do is like I'll spend a little bit of time thinking about like what what should we actually build I'll write that as sort of requirements and a bunch of CJs and stuff like that um and then I'll dump that into AI studio with a screenshot of the UI and a bunch of information like that and I'll say like make me make me this product experience now.

And it depends on like if it's a brand new product experience like we were playing around with like what does design mode in AI studio look like because we're going to add that. Um that was one of the examples where like I wanted to let the model sort of make a bunch of decisions and like show me some different ideas based on like the requirements that I put together. So and I got some pretty good stuff which is pretty fun. And how do you get it to show you different ideas? You just you just just make a bunch of tabs and then give it different directions.

That's a good question. One of the things that I do is um I often say and I'll I'll do my favorite like yap to app feature. So I'll I'll talk to the models so that way you don't have to watch me type it. I'll show you here. Um all right, I really like what we have so far.

Um but I want to see maybe like five or six different styles of what the like, you know, design of this UI might look like. So make five or six different styles and then add a widget in the UI so that I can actually click through the different styles and see all of them um without needing to like reload my page or anything like that. So I I do this I always have to do this in a very verbose way. Um I don't know like what the like succinct way of saying this is but it's a super common workflow is like I want to literally just like have something in the UI where I click a button and then as I click that button it shows me five or six different UI options. Um yeah that that's very smart.

Yeah, I was thinking you would like open different tabs, but this is way easier. The the tabs works as well. I mean, it depends what like if I'm really getting like truly different options, then I will I'll use different tabs. So, it it helps from that perspective. Okay.

So, uh let me ask you this. So, you have So, when you go present to Josh or whoever, right? Like like your boss, do you um when you have a product review with him, do you guys look at the prototype first? You look at some Google doc first or like how does the product review actually work? Yeah.

Or is there even not a product review? you just send them the link and like, "Hey, play with this." Yeah, that's a good question. We don't do a lot of product reviews with Josh. Um, but maybe we should. So, Josh, if you're watching, you know, I would love to do more product reviews with you.

Um, Josh is very busy. He's got a lot of he's got a lot of stuff going on. Um, we do product reviews internally and the demo is is often like something we do. Sometimes people have slides and like the slides will just like give some random context and then we'll go in and look at a demo. But almost all the time we're looking at um like live demos that like actually the team can play around with.

And the most fun part is like it's not just about the team playing around with it. Like everyone like 10 people in a meeting could start iterating on that idea because we all start from the same base level um and like add new features. So it is really really cool to see to see that play out which is fun. Oh yeah. Yeah.

You can you can basically 10 people can all remix this thing and just add their own stuff, right? Yeah. Exactly. Yeah. Yeah.

And this is maybe an example. Let's see. Let's see. Choose different styles. So when I click on them Yeah.

This is what I love to do. Like I'm just like I can't I could never imagine what a pink version of AI Studio looks like, but like now I can. Um and it's actually really helpful to be able to see these different styles show up. And the brutal. Let me see the brutal.

Oh, nice. Okay. Yeah. Yeah. This is I mean it doesn't even look that bad to be honest with you.

It kind of looks good. Um so it's nice. Yeah. And I I usually do this more for like different feature decisions and stuff like that. Less for style, but it actually is really helpful for style.

So we're also working on a way to like import your style guides and sort of like have that type of context uh in AI Studio itself. Got it. Yeah, this is awesome. And I think this this looks so good also because of Gemini 3. Like I I don't I don't think the previous versions could have done all these crazy styles like this, you know.

Yeah, I agree with you. Yeah, actually Gemini 2.5 Pro was pretty good at copying UIs. That was actually still one of like prior to three, that was the most common use case that I would use AI Studio for was just like clone the UI. It just it it sort of u it definitely wasn't as good, but it was it was still surprising how good it was in some cases. So, uh, so like, uh, so I guess you know there's no point to Amar's job anymore.

I'm just kidding. No, no. Amar is really So, here's here's the interesting thing is he is so talented that, um, it makes it it puts how good Gemini 3 is into perspective. Um, I see. And actually, even more so, the other designers we have on our team um, are also super talented.

So, it is um, I do very much appreciate it because they just think of things and there's like subtle details like I don't know. The limitation is I don't know how to instruct the model to even like do some of the the things that they do from a design perspective. Like I wouldn't have like thought about it that way. So the limitation is like if you have that knowledge like you can really wield these tools to do these things. But like I certainly don't have that knowledge.

So yeah, that makes sense. They're promptly a different way and like yeah it just just like if you're an engineer you can probably build better you know more robust apps, right? So 100%. Makes sense. 100%.

Should we try the floor plan one? Let's try the floor plan. We can do floor, man. Or I kicked off this other one before that you had suggested. Build an interactive mapbased chatbot that uses real-time Google Maps data to answer location specific questions.

Let's try this. Yeah, let's try it. Okay. Okay. Let me let me get it ready.

We'll see. So, allow this app to request my geographic location. Sure. Let's riff. I I think there's Do you have a suggestion of like how how do we evolve this example in the world where it can't see my location?

Uh do you have any suggestions because we can just iterate on it? Um, I I think it's just, you know, like just finding like uh, you know, hikes or finding restaurants nearby or like, you know, find finding the best, let's say, find the best uh, a Asian restaurant enrichment. Let me um, I like it. And did you have to set up the Google Maps API yourself or it just works? Nope.

That's the beauty. It just works. That's great, dude. Yeah. Yeah.

So we have and part of the the context of why it works is because we have this so I don't know I don't live in the Richmond district but if somebody does and fua dumplings um or dub or bow dumplings are good let us know in the comments. This is actually an an accurate suggestion. Um but yeah the reason that this works out of the box is because in the actual Gemini API we have this grounding with Google search tool uh grounding with Google search. We also have grounding with Google maps. Um, and so you can pull in a bunch of maps data without actually needing to like separately set up maps or separately set up the Google search API.

It's all just like baked in as a as a hosted tool, which is really cool. That's actually a big deal, man. I feel like a lot of new vibe coders like just the setup part is like the huge the biggest pain in the ass, you know? 100%. So yeah.

Yeah. And we're thinking about like how do we do this for more Google services where there's interesting data that folks might want to build on top of. Yeah. Um, so it's it's definitely a work in a work in progress. But search and maps uh works out of the box in AI Studio, which is really cool.

That's awesome. Yeah. And then you get citations, too. So, if you want to go and like look at the menu and be like, do I really want to go to Bow Bow Dumplings? You can click on it and hopefully see like what the menu looks like and all that stuff.

Got it. Yeah. Cool. We were looking at building something around this floor plan. So, let's go and let's go kick that off.

Um, and what was the idea was take in. So I have the floor plan image that Nanobanana generated for me. The idea was to make it either either get them to generate a 3D image or or maybe even have it like build like some sort of 3D like I don't know using 3JS or something to build some sort of 3D. Yeah, I like it. Okay.

Okay. Let me see. Um, I'll I'll yap to app and we'll we'll try to make it happen. All right. I have this image of a floor plan.

I want to build an app where I can upload a floor plan like the one that's in this image. And I want it to then take that image and turn it into an interactive floor plan. Maybe we have a couple of options for that. Like we can use for one, let's use 3JS 3.js to visualize that floor plan in 3D. But I'm also open to like an open or like some other interactive way of sort of looking at the floor plan and remixing it or something like that.

So, come up with a few ideas of how I can bring this floor plan to life. Uh, build a bunch of features around it and let me know when it's done. We'll see what this one comes up with. And I I'll make just a couple of other random comments. Like, if you're um if you're a developer and actually I think one of the use cases folks like the most right now is they start in AI Studio, they build something, they then go to to Google's anti-gravity and like continue to develop whatever they build because it's a little bit richer of a development environment.

Um, we're working on a way to like let people port over that stuff automatically, but you can download your code. You can uh save it to GitHub, whatever you want to do. And again, you can also like share the app and that's where you and me or you and a team could go in and iterate and fork and remix. Um, which is a ton of fun. Yeah, that's awesome.

Yeah. One of the other things, and we should do this with this one, is we built this annotate feature, which which folks have really resonated with. Uh, maybe while this is building, I can show it on this example. So, we'll do something like I'll look at this example and I'll say I'll open up annotate mode. And let's see.

I hate this recently viewed section. So, I'm going to say I would like to get rid of this. I'll just add my comment. I'll say I really don't like this. Can we make it collapsible by default?

And then I'll say add to chat. It should pop over. You can just send the prompt. And it just says the prompt is apply the edit shown in the screenshot and it literally just takes it. Um and hopefully we'll get an updated version of that.

Uh and our other app is cooking at the moment as well. So yeah. Oh, so it just took the screenshot of the thing with your annotation on it, right? Exactly. Yeah.

Got it. Yeah. And it works like a charm. This is like the multimodal as we as we sort of build AI Studio. One of the things that is like always top of mind is what is like where can we bet on the model basically and like this is a great example where like there's probably ways that you could build this that like don't bet on the model but the multimodal understanding is so good with actually we I just posted some blog post in the last couple of days that shows like the the benchmark chart was just Gemini 3 pro state-of-the-art I'm basically like every multimodal benchmark that exists which is really cool um and like you you sort of feel that come to life in a bunch of these examples which is which is really cool.

So we're constantly pushing on that. Yeah, this is why I'm buying Google Stockman. Like uh the first reason is because you and Josh work work there. That's the first reason. But uh second reason, yeah, I feel like the multimodal stuff for Gemini is just like unmatched.

Like it's like and also like uh if you think about like social media like you know Instagram is more popular than Twi Twitter. So like everything's going to be multimodal eventually. That's going to be the predominant format, right? Yeah, it is interesting. I think there's uh everything's going to be multimodal and everything's going to be code which I think is also fascinating.

Like I think the code as this sort of main scaffolding I think will be interesting. Okay, so this was a small feature. Um but I like this way more to be honest. I'm going to send this to our team after this because I hate every time I open up AI Studio. I hate seeing all of my like recently promps.

It's just clutter. I'm like I never click on any of them anyway. So I'd much rather have this collapse. So Amomar, if you're watching this, uh we need things collapsible by default. So, all right, we got that.

And let's go back and look at the floor plan. So, we ran for 159 seconds. There was 42 errors. Uh, and thank goodness for Gemini, it thought for 38 seconds and hopefully fixed all 42 errors. Um, so we have this, we have a little bit of an agent loop that sort of does some of this.

But I'm going to put in this floor plan and we'll see what it came up with. We kind of let Gemini take the reigns on this one. So, I don't know. Yeah, I don't know. But I like this.

I like this name architectural intelligence. That is interesting. Dude, wouldn't Wouldn't it be great if uh you know, cuz we're both PMs. Wouldn't it be great if our job was just to like just generate all these prototypes all day? You you need to become a prompt engineer.

That's what it is. Peter, that would be nice. No more meetings. Just prototyping. No more meetings.

Exactly. All right, let's go back to this image. So, we have a kitchen, primary bed, walk-in closet, bathroom, garage, and another bedroom. Okay, let's look at the three schematic. And does this seem correct?

walk-in closet. I like need them side by side. It kind of seems like it's Oh, okay. Oh, okay. There.

There we go. Okay. Yeah. Twocar garage. Let me switch.

Okay. Two car garage is there. Let me see. Two car garage is there. Let me switch it.

Wow. This is kind of fun. Um, this is this is probably the 3JS version, I'm guessing. This is definitely the 3JS version. Uh, but it looks roughly right.

Garage, kitchen, stuff. Yeah, garage. I think it has it the garage and this flipped or maybe I was looking at it flipped but it seems reasonable. Um and then we have remix. So this will now take in that image that I said and we can use Nano Banana Pro to actually change the image in some way.

So we'll say maybe make it modern minimalist and we'll see we'll see what it does. This one it looks like it's going to use Nano Banana by default and not Nano Banana Pro. So it might not be as good. We might need pro to No, that's pretty good. Yeah.

Yeah. It just like animated it which is interesting. switch it to a blueprint schematic and see what it looks like. I think it's so the the thing every time I do this I'm like I should just go and make businesses all day because I feel like this is like 50% of what people actually want. Um which is so funny.

Like you're you're actually like really close to actually working product which is really interesting. It looks like it's actually doing some uh room composition. The primary suite seems interesting. 10 rooms. One, two, three, four, five.

Yeah, I I totally agree. I think there's like so many businesses that can just build off Nano Banana Pro like cuz I don't think people want to prompt the stuff. They just want to like click a button and have it generate what they want. So 100%. Yeah, there's so many businesses.

Yeah, this one is awesome. I think there's like a lot of room design stuff that I think uh feels feels super natural that Yeah, there there's there's Yeah, there's so many cool companies to build. Do you have any uh like quick tips for prompting that Nano Pro? Because like sometimes it doesn't you know like do you have any tips for that? give it like a example or something or Yeah.

Yeah, that's a good question. We actually have this nano banana um prompting guide which we can put in the show notes potentially or folks if you go online just search up nano banana prompting guide. We our team spend a bunch of time on this. Um we're also trying to like part of one of the fun things about launching these models is like you sort of learn a lot from customers and the creativity of what people are doing. So, we also have this nano banana account on X where we're sort of like daily posting new examples of like cool things and the prompts that get you to generate those cool things.

Yeah. Um, so we're sort of we're figuring a lot of these like new use cases out in real time. Like the weather one, I don't know if folks saw this, but like there's a way that that folks were taking in like weather data and building this like really rich visualization of the city that you're in and the weather forecast and all this stuff. And it's like taking something that's really boring that like you regularly look at the weather and bringing it to life in a really exciting and fun way I think is uh was super cool to see. Yeah.

And and this stuff can go like super viral and help grow uh Gemini and Nano Banana. So yeah. Yeah, for sure. It's great. I mean it it really is already happening like that.

Um I think there's there's let's see if there's any other good examples. Um yeah, the infographics I think is another one that folks are really interested in. This like product mockup composition I think is another one that we've seen a ton of use cases like people want to visualize product ideas and merge their brand with some physical thing. Um so it was really cool to see yeah folks from from our team and others built these uh built some of these demos. All right, dude.

Well uh I want to ask you some questions about just like working at Google now. So I guess my first question is like you know a couple years ago was it maybe like one or two years ago like uh Google had barred and people were making fun of Google right like it's like this stuff is not good and then maybe it's because you joined the company I I don't know what happened but like now now you guys are firing on all cylinders and what do you think has there been like a culture shift internally to actually like prioritize ship shipping or what's your observation internally? Yeah, that's a good question. I I think some of this is just like the you know part of the advantage that startups have is you're able to sort of like adapt to the trend quickly. Um and like that is like a that's a a foundational advantage of being a startup.

And I think if you look at like what are the foundational advantages of being Google, I wouldn't describe one of them as like you know we can move on a dime as a company in order to like adopt some new trend. Um, and I think if I look back like two years ago, you know, putting the right pieces in place and getting the right shots on goal I do think was important. But another thing is like it just takes time. Um, and this has been one of my realizations in the last uh in the last six months is like it really does take a long time to build a great product. Um, and to build great models, it takes a long time and to build a team that sort of is is rowing together in a sort of coherent direction takes time.

Um so it is uh I think people have high expectations for Google which is why I think they hold they hold us to a high standard but I think some of it is it just takes time to do a lot of these things. Um I also think there's like lots of like structural things that have happened. Um, you know, one of them is like bringing the Deep Mind team and the Google brain team and folks from Google research together into a single organization, Google DeepMind. Um, and actually principally also having products in that portfolio as well. Historically, DeepMind, this is one of the things that gets me excited about the direction that we're going with AI Studio, the Gemini API, the Gemini app, um, etc.

is that it's like actually inside of DeepMind. It's not like someone's throwing some model over the wall to us and we're building a product around it. It's like we're we're co-building the model uh with the research teams to make it really great for all these use cases that our customers, developers, builders care about. Um and that's such a unique advantage that I think Google has with these products which gets me excited. That's awesome.

And and and you being like kind of at the forefront of engaging customers on Twitter, Twitter, and other platforms. And tell me about these like feedback loops internally and externally. internally like uh you work with the researchers every day you kind of feed them information and like externally you know have you encouraged other PMs to talk to customers more or Yeah for sure I think this is one of the and so this you know I talked to internal teams about this sometimes as well this is not without challenge um like it's it's there are there are very real downsides we don't need to spend the time talking about the downsides we'll talk about all the positives on this podcast but um I really do think as a as a PM it's like the most competitive advantage differentiator that I could possibly have. Like I think normally you sort of have to fight to like get feedback from users and in my job like and this is I think a privilege of Google and you know thankfully folks on the internet care about what we're building like I get so much good feedback. Um and like seeing what the ecosystem is saying and seeing what people you know think about AI Studio and Gemini and our models like very genuinely makes my job easier.

Um, it would be harder if I had to sort of figure out like I wonder what people think about Gemini or I wonder what they think about AI Studio or I wonder what bugs they're running into. Like having to search for that data and that information would take a lot of cycles and time and I don't have that problem right now which is really nice. Um, so yeah, that flywheel spins and I think more and more of our team and actually more and more folks across Google and you actually see like Demis and Sundar and others doing this as well like they're showing up uh for customers, they're doing it in public, they're fixing these problems. Um, which I think is like a a great trend line. Yeah, that's the way to do it, man.

People don't want to hear from some corporate brand account. They want like the the person and and talk to the person. I 100% agree. Yeah. Yeah.

I think the brand accounts are actually really useful in telling the story, but like my personal my personal opinion and I've sort of I've given this comment to lots of folks is like I don't think the brand account should ever respond to people on the internet. I think it just it feels kind of weird. Um, if you have real humans, like have real humans talk to real humans. Like that's what I want as a user. Mhm.

I'm sure there's cases where that doesn't scale and doesn't make sense, but um I do think it's it's sort of the the golden path if you can do it. Okay. And another question like internally has has has Josh or other folks really empowered you guys to just to just ship, right? Because like I I think you know in these big companies there there's like a lot of approvals and like check all the boxes and like do all this stuff like you have do like two-year planning and blah blah blah. So like shipping is learn learning man like and like you know has the culture changed where you can just like ship ship stuff to a certain extent.

We do ship stuff. Um so I I think the the guard rails around shipping depends on what you're trying to ship. Um so like the like the core product velocity is exceptionally fast. Um models there's like a bunch of like legal and regulatory infrastructure around like shipping new models. So they're actually there it is like slightly more heavy weight in that sense.

Um, and we've actually done a lot to like make that streamlined and and sort of, you know, do the do the right diligence, but also be able to get models out the door. Um, and then there's very specific features that do require like you need to, you know, go and meet with security and privacy teams and stuff like that to to understand, but by and large, I think like the default is we ship stuff. Um, which is really fun. I think it's not just like I think Josh has done a great job of this across all of his teams. Um, but I think this comes from like Demis and Sundar and this like at the at the top level this sense of urgency of like how we need to be showing up and moving quickly.

Um, and my my personal worldview is like I don't even know how you would do this if you weren't moving quickly. Like I don't think it doesn't feel like it's a like I don't wake up being like ah we got to ship fast today. It is just the there's one there's one mode and the mode is we ship fast. Um there is no other option. there is no other alternative to what we're doing.

Like it is literally the only path. Um and that's been my mindset since I joined Google. And I think um you need the right pieces in place to actually be able to materialize that that sort of mentality. But I think we have those pieces now which is really really fun. That's great.

Yeah, that's great. Yeah, it's it's definitely a very competitive environment. So you have to show up. Yeah, 100%. 100%.

And and it's like a it's an environment where there's so much opportunity. like the models are so powerful and people are building so much interesting stuff that like I think the competition piece aside like um it's exciting like I want to ship quickly because our customers are like pushing the frontier of what's possible with AI and like we want to be there along with them. Um so from that perspective it's uh it keeps me excited. Yeah, I feel like a lot of the stuff you ship can just be like what are my most power users doing and how do we make it easier for the you know beginners and people who are new to the product. That's like one avenue I found that always works.

So yeah. Yeah, I love that. We're thinking a lot about this for the vibe coding experience right now because we have um you know there's definitely like a barbell of who is vibe coding like in a lot of kid like I'm a I was trained as a professional software engineer like I was a software engineer um but like I don't actively like write a bunch of code anymore. And then you have on the other spectrum like people who actually are full-time software engineers doing this still. And then you even have the folks who like have never opened up code, don't know anything about coding.

They just have an idea of what they want to build and like how do you build a product for all of those people is like such a such an interesting uh challenging space. Yeah. Yeah. You got to figure out where to do different levels of exposure and simplify stuff. Okay, cool.

So, so last question. Um, so you know, Gemini seems very exciting. Working for Josh seems very exciting. If people want to join your team, what kind of traits do you look for uh for hires? Yeah, like 10 years of fan experience or no, what do you look for?

Yeah, that's a great question. Um, there definitely a couple of things like and and this is not an exhaustive or an exclusive list, but like I love folks who are building in public. Um, it actually makes it easier to just like assess work quality. Um, because part of what I enjoy and like uh developer relations is a good example of this. Like it's actually I know people talk about like it's hard to hire Devril people in some sense it's easy because you have this like exhaustive proof of work of like what are the like what are the outputs the types of things they do the quality at which they do it.

Um so I know that there's some jobs in some companies where that that type of stuff's not possible. Um so that's that's really helpful. We for everyone we interview and hire on the product side and also on Devrell and other functions, we do this exhaustive like friction logging exercise. Um, and to me it's one of the most helpful things with like what is your product taste and like how do you see problems that users have or you yourself have um and like what is your principally not just like what is the thing that you identify as a problem but like what is your your sort of like suggestion and take on that. Um, and like I I almost, you know, we don't do this, but like I almost I almost in some sense wish that I could just use those things as like the interview decision making criteria because like it really is so helpful to see in a written format like what people think and you know how they identify problems and all that stuff.

So it's been incredibly helpful and it's something that I I love to read. Interesting. Yeah, that that's that's I think that's like Stripe does that too like kind of detail like what your frustrations using AI studio and like what you're going to do about it, right? that that kind of thing. Yeah.

Yeah. So, if folks have these things, please send them to me. I would love to read through. It's it's super helpful to to see people's product opinions. Um Yeah.

And I think the last one is this like agency bit. And I think it's hard to that's one of the things that I found most difficult to like assess in a hiring process, but um I want to work with people who are high agency and they're just like going and solving problems proactively. like um that that is like my ideal outcome even if some of the stuff is wrong to be honest because like I can I can fix uh I can I can sort of fix that problem. It's hard to sort of instill agency in people. So yeah.

Yeah. People are so afraid of being wrong like PMs are still want to make the right choices each time. But if you move fast uh and like you know like if you make like nine wrong decisions but the ultimate one is right instead of someone like you know trying to plan for like you know three months to make the right decision the first person is going to win man. So so it's like it's totally fine to be wrong as long as you fix it. I love that.

There's a good there's a good Sam Alman quote that I used to have up on my wall about uh sort of the speed of iteration and like the cost of being wrong. And I I think it always ends up uh it always ends up being true. Cool. All right, dude. Well, uh I I think people know where to find you, so I think Yeah, you're you're X.

Yeah, I'm on the internet. So, if you if you need anything, if uh if our team can be helpful, please reach out. Always happy to help folks who are building on Gemini or just have comments or feedback. Um and Peter, thanks for thanks for having me on. Thanks for vibe coding and building a bunch of stuff.

Yeah, I love Gemini. Thanks for building a great product. Yeah, of course. Cheers. Thank you.
