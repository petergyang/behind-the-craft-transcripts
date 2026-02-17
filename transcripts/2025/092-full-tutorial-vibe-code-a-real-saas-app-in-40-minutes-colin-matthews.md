---
title: "Full Tutorial: Vibe Code a Real SaaS App in 40 Minutes | Colin Matthews"
guest: Colin Matthews
publish_date: 2025-11-02
youtube_url: https://youtube.com/watch?v=Llhno97FUmo
channel: Behind the Craft
keywords:
- ai-tools
- coding
- ai
- metrics
- pricing
---

Typically, when we're talking about prototyping, especially with AI tools, we're usually talking about building things that are just on the client. The main difference between that and you know like a full stack application is usually the combination of adding in like a server and a database. You're going to have things like your your email integration, file or blob storage as well, right? Payment is pretty typical with Stripe. You have to have OH of some kind and product analytics of some kind and then some type of log analytics.

That's like a lot of stuff to Vive Code, man. That's a lot. So, if you tried to deploy this app, it wouldn't work. you have a a request to the back end, right, from your client side to generate the image um to this endpoint that you made API transform, but it's sending it right to local host 3001. So, these are some good examples of like the types of things that AI can make mistakes on.

What I built is a little template um that has like what I think are the most common necessary features to build a SAS project. So, basically, let's recap the steps, okay, to build a real product. Okay, welcome everyone. Uh today, my guest is Colin Matthews, the one and only. Uh Colin is a good friend.

He's taught a lot of students how to build stuff with AI and and like build real [ __ ] not not just like random prototypes, like real real stuff, real apps that you can actually uh get paying customers for. So that's what we're going to talk about today. Like I vibe coded a pretty crappy um nano banana um image prototyper thing and then me and Colin are going to convert that into a real SAS app. Okay. So welcome Colin.

Yeah, happy to be back. I think it's my third time now. Yeah. Great. All right.

So um why don't you start by talking about what the difference between a vibe coded prototype and a app is. Sure. Yeah. So I actually have a quick visual to help us out here. Let me share my screen really quick.

So uh if you've heard me talk about software at all, you probably seen me talk about this before. Client servers and databases. So typically when we're talking about prototyping, especially with AI tools, we're usually talking about building things that are just on the client. So like this is what you see in the UI, right? So if I build something in like bolt or replet or or lovable, a lot of the time and the attention is actually spent on like getting it to look correct and making it like feel good and all that kind of stuff.

Um the main difference between that and you know like a full stack application is usually uh the combination of adding in like a server and a database. So something to handle like application logic things like how users log in and that kind of stuff as well as obviously storing data over time. And then the only other major thing that people like to add usually is like thirdparty integrations, right? So this would be things like you know your Gmail integration or something something similar and usually that's talking to your server. So these are kind of the main components like prototype really just a pretty picture right just the client uh full stack app client server database and then uh some thirdparty integrations typically.

But when it comes to like a SAS app there's usually it's like a set of common features that most of these apps have right like like Yeah, exactly. So we can kind of pull pull some of those in here. But uh typically you're going to have things like your your email integration, right? So that's going to be like a third party. So you can send transactional emails.

You might have like file or blob storage as well, right? Uh payment is pretty typical with Stripe. You have to have O of some kind. And usually you don't want to roll your own O, meaning like you don't build it yourself. You use pre-existing O tools.

And then kind of I would say a bare minimum in terms of like the product and engineering side, you want to have product analytics of some kind. So understand using us user behavior and then some type of log analytics and this is specific to errors. So like if you're familiar with the tool centry that's what I'm talking about but like capturing errors in the product. Got it. Okay.

Yeah that that that's like a lot of stuff to vive code man. That's a lot. Yeah. Can you actually show the vibe coder thing that I have? Sure.

Yeah. Right now we have uh like a well I guess you can explain it if you'd prefer. Yeah. This is my um really amazing headshot pro AI app. You can see it's very professional.

Um, basically you can upload a headsh shot and then it will use Google Nano Banana to generate a more professional looking headsh shot of yourself and hopefully it still works. Did you try it to make sure it works? Yeah. Yeah, it works. It works.

Okay, it still works. Okay, great. Yeah. And how did you build this? Just curious.

Oh, that was good, man. Yeah. Um, perfect. I How did I build this? I use uh clock code and just like by coded it and and then I had to give it like a bunch of instructions to use Gemini's APIs and like a bunch of documentation.

Yeah, I I was able to get it to work. There's actually a tutorial that I can link to uh if you want to vive coat this. Yes. Oh, perfect. Yeah.

Yeah. I was just going to comment like you can perfectly see why I no longer have hair based on this image. The hairline's pretty far back. I think the AI got that right. Um but so um yeah, so this this I would say is like closerish to a prototype um in that like you don't have all those extra things.

And then also just for fun, we'll do like a quick review of of your code. So you do have a front end and a back end, right? So you have you have a client and you have a server uh which is already like one step up because you don't necessarily need to have a server for this type of application if you're just running it locally. Um but you know you have that working which is great. Um and then there's just a couple of like things though we'll just try to point out a few on the back end here in terms of like how things are working.

So if we hop into like your your Gemini stuff you can see like here's your prompt and all that good stuff, right? So, you probably wrote Did you write this prompt manually or did did AI generate this for you? Uh, I worked with AI to write the prompt. Yeah. Yeah.

Cool. And then it's sending the request over to to Gemini and doing all this this good stuff. And honestly, like this is fine because this is just that kind of third party integration step that we talked about a second ago, right? Like sending a request over to Google and getting the results back. Not a huge deal in terms of like the overall setup.

So, there are some things that are like are are a little bit off. Uh, let's see if I can find a good example here. Let's go into this one here. So, one like good example is that your images are B 64 encoded text. Like usually you reference a file, but it's just a super long text string that like the preview images that you have or like mock images.

So, it's like kind of a weird AI thing. Um, not necessarily like super incorrect, but kind of like a an odd thing to do in terms of a decision to make. Um, and then another good one, let's see if I can find it in here. I think we have a local host somewhere. you actually have I believe the the local host URL um directly in the code somewhere see yeah so well basically yeah right here so what that means is like you have a a request to the back end right from your client side to generate the image um to this endpoint that you made API transform but it's sending it right to local host 3001 so if you tried to deploy this app it wouldn't work um and you mean local host doesn't work yeah yeah so these are some good examples of like the types of things that AI even when like you're building something that's a bit more complex, uh, can make mistakes on, right?

And like just some small small things that you you'd want to fix or change. Okay. Um, and then obviously like the big thing would be adding like off and stripe and all the other things you talked about, right? Um, yeah. Yeah.

All right. So, so you have this template, right, where you actually added all this stuff. Can you show show it to us? Yeah, for sure. So, what I built uh is a little a little template that has like what I think are the most common necessary features to build a SAS project.

So, the template itself is just a to-do list. Uh the intent would be that like, you know, you replace this page with whatever you're building. Um, but you can see that it has like pricing, right? And we can go and upgrade to pro. That'll send us over to Stripe uh to actually complete the purchase.

It comes with uh our obviously like login and stuff. Let me just hop back over here. Login. So, you can sign in and sign out. Right now, it's using Google O for that.

You can also set up with like GitHub off or really whatever you want. and then also comes with an AI chat. And actually, I'm in the process of swapping this over to the new agent kit from OpenAI as the back end. So, that'll be kind of fun. Uh, and then also on the settings side, you can, you know, like toggle your email preferences.

And it comes with an integration with Send Grid. Uh, and then also like the other stuff like I mentioned, so like Post Hog for product analytics and for error capture and some other like small things behind the scenes. Um, and sorry, did you mention there's a way to get paid like a pivot? Oh, yeah, for sure. Yeah.

So you basically you just set up whatever you want and you just prompt like change this text, right? But uh yeah, you'd prompt or you just throw in your Stripe ID and then you can collect payment from Stripe. Okay. All right, man. This episode is brought to you by Composeio.

Most of the paying shipping AI features doesn't come from the model, but from the integrations you're dealing with messy APIs, fragile tool calls, and hours lost to debugging and figuring out why something broke in Slack or Salesforce. Composio gives you one SDK to connect to 800 plus apps like Slack, GitHub, Gmail, Jira, and they built the Rube.app that plugs all of those apps straight into an AI chat. So you can just ask pull me the latest metrics from Mix Panel and update linear. Now instead of fighting with APIs, you can focus on actually shipping faster. Check it out at getrube.link/per or the link in the video description.

Now back to the episode. Why don't you start a process of putting this thing like putting my vibe coded thing in here and then we can talk about some other topics while while it's trying to program. Yeah, that sounds good. So, basically we're going to try to convert your prototype to a full stack app. Right.

That's right. Um, cool. So, I'm going to start by actually taking a look at what your code here and I just want to quickly break down uh what your code is so people have a general sense of like how this works. So, you can actually see you have these two folders, right? So, you have backend and front end code.

backend code. This is your server side code like we talked about, right? So, this is really just the integration with Gemini. There's really not much else going on here. We'll probably copy your prompts so that we maintain the prompts the same way.

Everything else I honestly will just have the AI regenerate this code because there's nothing like super useful. It's just a call to the LLM to Gemini to to generate the image. Okay. Um, and then on the front end, you can see in the front end you have different kind of like elements in here. One of those elements is components.

So you have like a style selector component, a result display, an image uploader, and a download button. And then you kind of have like this main file called app.jsx that just imports all these components and kind of puts them in the page. Kind of like Legos, right? So like we have all these individual Legos and you're assembling those Legos in the page. Uh so what I can really easily do and what anyone can do is take the components that you built and bring those with us into the full stack app if we want to.

So we can try to maintain like some of the visual styling of what you have in the prototype. Okay. I think it's up to I'm I'm not that proud of the V visual sliding, but yeah, that's up to you. Yeah, we'll we'll try to we'll try to keep it uh just for fun. So, um cool.

Let's go ahead and start kind of moving this over. And literally what I'm going to do is I'm going to go like this on this side, like go like this on this side. And you can see this is the template by the way that the code I have over here. And you'll see a very similar kind of structure. So, we have the client side code.

We have server code, right? Uh same as you client like front end and back end. And then in the client, if we go into here, we'll see a folder called components, right? So this this pattern will repeat itself all the time of like how your code is organized. So I'm going to create a new folder here called Peter components.

And I'm literally just going to drag over your files. Um and that's that's all we need to do. And you by the way you can do this also with like cloud-based tools. So like replet allows you to drag in files and like right into the the file system and you can just bring in your components maybe build the prototype in like v 0ero and you want to you know uh make it better in in replet. uh you can move stuff around in the in the same way.

Okay. So, uh what else? Yeah. Yeah. I did also ask it to build us a little spec based on uh your stuff here.

So, let me just close this down a little bit and see what we have. So, I just asked it to generate, you know, a MD file for rebuilding your thing. Uh just basically describing the requirements were so I didn't have to rewrite it all. So, this currently a prototype application. We're going to rebuild it.

I'm going to get rid of some of the um or like modify some of this. Specifically, I'm going to say that the components are in Peter components because we just made that folder. And yeah, I'm going to kind of get rid of a lot of the backend service stuff that you have already. Um, just because we can kind of clean up some of this ourselves. The rest of this looks fine.

Oh, yeah, and it automatically extracted your prompts, which is nice. And yeah, I think that's pretty much it. So, I'm going to again delete some of this. Yeah, we we'll get rid of a lot of this extra stuff. This is a lot of code and just stuff I don't really need.

I just really need this top part here. And this is going to become our prompt. So, I'm going to basically take this head over to our, you know, actual application uh and throw this into cloud. And I I mean I know you've done tutorials on cloud code so I probably won't spend a ridiculous amount of time on like explaining cloud code. But I am going to put it on plan mode first.

Um just so that I make sure that the result that we get you know aligns to what we're expecting before we kick it off. Okay that's awesome. Uh okay so so just to recap you drag and drop some component files into your temp template. Yep. And uh you in my original uh repository you ask claw to generate MD file and and the prompt is like hey you know if I want to rebuild this somewhere else like what do I need right?

Yeah exactly. Okay and then and then it magically included a prompts in the MD file. Yeah. Yeah. It just extracted all the well I would say all the important stuff and probably a lot of non-important stuff.

Um so you can see like I deleted it was 800 lines cuz Claude likes to talk. I think I got it down to 80 lines. Um it was just I just needed the spec. I didn't need the you know the whole thing all your existing code. Yeah.

Yeah. Got it. Got it. Okay. Cool.

So let's just do a quick read through. And actually I think this will be really interesting to kind of like illustrate the difference between um the prototype, right, and what we actually have in a production application. So the first thing it says is that we need to change the database schema, right? So this is how we're storing information inside the database. And let me just see if I can run something really quick to make this feel a little bit more real.

Uh give me one sec. Cool. So this is like a database explorer that you can run locally on your computer if you're using the template or the same kind of technology or you know tools that I'm using. And so when we talk about changing the schema what we're referring to is like right now in this database there is nowhere to store anything that is relevant to this these requirements right like we have uh items for the to-do list we have user information so like my email and my ID we have file storage and that's it. So the first thing Claude is telling us that we have to do and this is a very common thing that you need to do is to change the database.

So we need a saying we need a headshots table. We also need a credits table to track user credits. Um I'm probably going to modify the plan a little bit because I don't actually care about tracking user credits. So I'll say don't need to track user credits at least for now. And then let's see what else we got.

We have the backend routes that need to be built. And you're going to see a couple of good things here, right? So we're going to require authentication. This is one like critical thing whenever you're building a full stack app. Every backend endpoint should be checking is the user logged in and are they allowed to perform this action.

Yeah. Right. So this is another kind of main difference between just a vioded prototype and building something real. Uh and then it looks like everything else is pretty similar right like um all that stuff there. I am going to say like we don't need to upload the image to file firebase storage.

So don't store your files in Firebase storage just to keep things simpler for now. for file storage. Uh let's see what else here. And then front end integration. It's going to build a page for the head shot.

Uh it's going to use your existing components that we already have. Integrate authentication, all that good stuff. Credit checks. U payment integration. So we already have the payment plan.

It's going to put three head shot per month for free. That's fine. Um Gemini integration, the file storage integration to store the files over time. I'm gonna skip this one just for the sake of time, but obviously like we would want to store the images over time, right, for the user. Yeah.

Yeah. And then also really important unit tests. So just in case people aren't familiar, typically you'd want to write unit tests against code so that you can automatically run these tests and that way uh when the AI make changes makes changes, you can test if things are broken. So unit tests are a way to like avoid manual testing all the time, right? So it's going to write some unit test for us as well and then actually apply the database migration changes.

So what basically what this means is like we will have new code but we actually need to apply that code to the database to make the database have a different schema. We can't just like have the code be different than the real database. We need to apply that change. Got it. Yeah.

Um and yeah, that's pretty much it. So I'll go ahead and kick this off. Um and I'll just say give me back an updated plan and go from there. So, you're gonna you're gonna do all these steps at once or Well, I mean, I'm gonna try to let Claw do all these steps at once. Yeah.

Honestly, like this change seems kind of big, but it's really not. It's just a Gemini integration. Um, yeah. One of the cool things, by the way, about having a template like this, you don't have to use my template, just generally, is that Claude is making better decisions because of the existing patterns in the codebase on how things work, right? like it's not inferring how the back end should be set up or inferring how tests should be set up.

It's looking at examples of how things are set up already. And so it makes it a lot easier actually to do like changes like this where it feels complicated, but it's actually just copying existing patterns. Cool. Uh let me just give this a peruse. All right.

Well, I'm not going to read this whole thing. So hopefully hopefully this works. So we're going to say yes, and then it'll do its thing. And you're using uh VS Code, right? just because it has like a native integration of C call code.

Yeah, it's just a little bit nicer from like a UX perspective than the the terminal, right? So like you get this nice little markdown editor. Um and you can kind of scroll up and down with the text at the bottom there like the input. So it's just a little bit cleaner. Yeah, that that is cleaner.

Yeah. Um Okay, cool. So it's going to work for a while now, right? Yes. As you can see, we have uh about a dozen to-d doist uh to work through.

So this will probably take a minute. Okay. So, let's let's go talk about some other things while what this does its job. So, let's go back to your uh exact to draw thing. Yeah.

All right. So, let's talk about So, we did a previous uh video on like our favorite AI coding tools, right? Yeah. But, but now I think there's like a lot more out out there and and like I think you prepared some diagrams about the difference between some of these prototyping vibe coding tools. Yeah, exactly.

So um I guess to start with like some pretty popular ones, Lovable and Bolt are a few others actually nowadays too. They're all using Superbase on the back end. So even this is kind of fun for the folks who don't know is Lovable and Bolt just announced their own clouds, right? So like literally I think a week ago now or maybe two weeks they're like oh yeah you can integrate directly with our own backend services. What really happened is Superbase released a feature that allows companies to white label Superbase inside their products.

Uh, and so it's still it's still literally Subbase and even if you look at the code, it literally references Subase inside the code. Um, so so it's like a branding thing. It's 100% a branding thing. There is no there's literally no difference in the features, functionality or anything between the prior existence of, you know, Bolt integrating with Suabase or Lovable and what you have today. It is exactly the same.

Interesting. Yeah. It's kind of funny because like the the people that these these companies are targeting like they probably have no clue what the hell a cloud or superbase is. Yeah, it's kind of I agreed. I think it's just like um I think a lot of it is just competitiveness in terms of like oh this is the best tool cuz we have our own back end or this is the best tool because we have the best Figma integration.

Um but anyway, one of the things that's interesting about these tools so specifically using Superbase as a backend is that uh by default they actually don't have a server. So if we go back up to like this pattern that we talked about so far, the way that they work is basically Superbase controls the server for you. So there's kind of like this little thin layer at the back here where um every table that you have in your database automatically gets a corresponding API endpoint. Basically meaning they they autogenerate the server for you, but you don't control that server. And so on one hand that's really interesting and cool because that means that you don't have to write any of the server side code, right?

On the other hand, one of the downsides about that is that you don't have to you don't have the ability to modify any of the serverside code like it's autogenerated. Um, and so especially from a security perspective, this becomes a problem. And so they have this system called RLS, which is basically a configuration system for who should be able to access what. Uh, because the server would typically handle that in like the normal stack that we have. It would decide like is the user allowed to perform this action.

Uh, but that doesn't exist in this context. And one really interesting thing is that by default u the RLS rules for every superb based project you set up are completely open. So any user can access any information and and this is like the primary driver behind why you hear about like vibe coded tools being insecure is because people are building on top of this system and they have no idea that RS or any of this stuff even exists and that they've built on top of it or how to modify it or improve it, right? Like how to configure it correctly. And so they're building these systems that like are not secure because you know it's not that superbase is inherently bad.

It's just that like you don't know what's actually happening behind the scenes. Wait, wait, wait. So, so what is what what what does RLS stand for? Or is that like an acronym? Yeah.

Um, you know what? I can't remember off the top of my head, but it's something like a it's like rules and some type of rulebased access system. Um, okay. And then and then if I go like is there some sort of set settings or thing for me to change this stuff? Yeah, exactly.

So, inside of these tools, um, if you prompt them to like ask about your RLS rules, they will tell you what they are, but by def by default, it is completely open and then you have to configure it to to be correct. So, one like lovable did add a thing where like if you publish your application, they'll pop up a warning and say like, hey, anyone can access the data in your product right now. Do you want to do you want to change that? Um, and then you basically try to prompt your way to this these rules, but again, like you're reliant on the AI to configure it correctly. Um, which is a little bit scary.

That's kind of crazy. Crazy. So, okay. So, if I build a app using these tools and then uh like let's say I have a user table with like the user information, right? Because people sign up and stuff.

So, you're saying that anyone can just get the email for all the users? Yeah. Yeah. Yeah. By default.

Yeah. That's crazy, dude. So, it it requires the user to like the person authoring the the project like you know the user level or bolt to modify those rules and set them up correctly. Um, but I guess my point here is that like the vast majority of people using these tools don't know those rules even exist, right? But why why why doesn't Lovable and B fix the stuff?

They don't know which table's which or something. Uh, it's more so that like this is just how Superbase works that like because they're trying to make it simple by not having you have a server. You still have to have a server though in order to access the data in the database. And so this is the simple version which is like you use a rule system instead of actually having code. Um but again I think it's actually more complex or like more difficult to understand for the average person whereas I think like if you have this um it becomes a lot more clear like if there's issues in the server where those issues are.

Yeah. I mean like I I don't think it's too difficult to set up a server right like especially if you have like some very powerful model to do it for you. Yeah. No no it's not difficult at all. Um, okay.

And hosting is pretty straightforward and all that kind of stuff, right? You can host on like versel or render. Even Replet, like this is the stack replet uses as well behind the scenes. Um, so Replet I would say is like I that's one of the reasons I prefer Replet is because um not because of like the AI coding tools or anything like that. It's literally like what stack are they using and how how likely is it that someone's going to make a mistake that they're going to really regret, right?

Wow. Uh, this is very this is like new news to me. I I didn't know about any of this. Yeah. Yeah.

Yeah. It's pretty interesting. I mean like I built an app on lovable the other day and it did fine but like uh you know I had to go through and configure the ROS rules to make sure that everything was correct. So you know Wow. Okay.

All right. Well, maybe we should email the loable people. Oh, they all know. They all know. Um yeah, if you again if you've read anything online about like five coding tools being insecure.

Yeah. Um this this is the thing that is like the primary security vulnerability. There's lots of other stuff that people make mistakes with, but this is the primary one. Wow. Okay.

Okay. Okay. I have a hot hot take. Like I feel like even as complete nontechnical person like I I don't think like clock coder or cursor or whatever these these like more advanced tools are actually that hard to use. Like you're literally just like typing to chat, right?

Yep. I mean I don't actually think they're actually much more hard to use than uh some of this like web- based tools. Yeah, I would agree for sure. I think um again like part of the part of the job of like a level or something like that is to convince you that the complexity is low so you feel like you can do it. Yeah.

Right. But again, if we go back like kind of the image up above, at some point in time, like you will need to add payment and they have a Stripe integration, but like you still need to go into Stripe and set it all up. You'll have to add email. You have to add like and if you don't understand how these systems work, I think at the end of the day, like when you have a bug with your email system and the only thing you can do is like promptable to say fix my email system like that's that's the challenging part, right? And so like um not to try to dissuade anyone from doing this type of work because obviously I think everyone should try and learn but at the same time I think it's important to to not treat it as like I want to get to the outcome as fast as possible.

Yeah. And I don't care at all about how anything is working and more so to say like okay like how does this actually work behind the scenes and try to learn some of that stuff. Got it. Okay cool. Do you want to check VS Code see if things are generated?

Yeah. Um so let's see. We want to generate and apply database migration. So this is actually interesting. Uh we kind of got stuck here.

must have asked for permission a little bit while ago but um it's asking us to apply a change to the database. This is another really good thing uh in terms of a pattern because typically what happens is most AI coding tools will just modify your database directly which is terrifying. What this is doing is it's generating a file to basically tell us what it's going to change and then we apply that change and it makes it easy to make sure that our databases are always kind of like in sync and up to date. So this is something called migration. And again, this is like a pattern that you'd want to learn and and consistently do rather than just allowing like an AI agent to write SQL queries against your database and just change anything at any point in time.

That's a little bit terrifying. And again, that's the default pattern. Uh yeah, because if you scrub the UI, you can change it back pretty easy, but you scrub the database is harder, right, to Yeah. Yeah. And even like with undos, I know a lot of people are reliant on like trying stuff and undoing it.

Uh you can't undo a database change the same way you can undo a code change. Uhhuh. Right. So, generally speaking, you want to be like a little bit more certain that, you know, things are going to work. Yeah.

So, so, so you don't dangerously skip permissions. No, no, no, I don't. Um, cool. So, it's going to run through this. I'm going probably have to pay attention for a second as it installs some stuff.

Um, okay. And you have like a database. The reason it's doing this is because you already set up a database with your template that has like some basic tables. Yeah, exactly. Yeah.

So, we have a database that has like the user storage information that has the Stripe integration. So it stores like the relevant stripe IDs and stuff like that. So again like the template is there. It's not I'm not going to claim that it's like a prerequisite obviously like you don't need it. Um but the purpose of it is to like help people avoid common mistakes especially on the security front.

And maybe this is interesting while we're waiting. I actually had the the pentest or had the the template pentested by security firm um before you know I gave it to anyone just for fun. What is a pentest? Oh sure. Yeah great question.

So basically uh it is a it's like a security review where they attempt to extract information from your website or from your app and there's like a bunch of very common attack patterns that attackers use and so they run through all those attack patterns against your application and see what they can what basically what they can exploit. Um and then at the end they kind of give you a report on like what you need to update or modify in order to be secure. Is that like a lot of money to do a pent test? Uh it's like a couple thousand dollars. Okay.

Okay. Wow. Okay. So you gota be serious. Yeah.

Yeah. Yeah, for me like if I'm going to give the code to people then, you know, like it's my template multiplied by a,000 or 2,000 or 5,000 times, it's worth it to spend a couple thousand to make sure that I'm giving people secure code. Um, for the average person, probably a little bit out of reach. Got it. Okay.

All right. We are back and here's what we have. So, what it did is actually added it to the navbar, right? It didn't necessarily replace what we had. That's okay.

We could, you know, ask it to to take some stuff out later. Um, but theoretically, so let's just take a look quickly at the UI and then we'll try to see if it actually works. Um, so in pricing, it did not update our pricing page looks like. Um, so no no head shot. I don't see anything here.

That's okay. And then in the headshots here though, we do have like a counter for the number used this month. And let's give it a try. One thing you'll notice is like it's using your components, right? So that that part worked.

Um, so we'll click choose image. We'll grab our picture here. We have this guy here. Generate headsh shot. And we'll see if it works.

Cool. Okay. So, new error. Um, failed to generate not supported. So, this is likely an error because we didn't pass in the right documentation.

And again, this is where like some debugging is obviously helpful. So, if we just take a look at this, we can see it says Gemini 2.0 flash XP image preview. So, this is likely the the same issue that you had before, Peter, which is like it's not using the right model, right? And so, we're just going to go ahead and Yeah. Uh this is actually a really common painoint of LMS is like they don't have upto-date information, right?

Like the training cutoff and so they don't know how everything works. Um so we're going to have to go find the Gemini Nano Banana docs. Uh let's see this one here. And we're going to want to pass in the relevant documentation and just ask it to update it. So we're doing uh image to image editing.

And I'm just basically going to copy the docs here, paste this in, and say, uh, you're using the wrong model. And again, I'm going to turn on plan mode because honestly, I I pretty much never I don't know if you do, but I never kick it off without doing plan mode first. I always alternate between planning and implementation. Yeah. Um, I just don't like the idea of like letting it do a bunch of stuff on its own.

I have no idea what it's doing. Okay. Um, but does the rest of the the does the SAS stuff work like like the O and everything? It should be the same, right? Yep.

Yeah, it still works. So, we can we can hop back into that for a second. Um, so let's go to here. So, we can sign out. We can sign in.

We can hop into our pricing page in a second. Here we can open up. We can upgrade to pro. I won't actually obviously upgrade, but we have our our pricing set up here. If we wanted to change this, this would be just like a setting in Stripe that we change.

We don't actually change the code anywhere. Uh, and yes. Okay. But to make this payment thing work for for my stuff, I have to enter my own Stripe information. Exactly.

So, you would have to enter in your own Stripe keys, and that's just part of the ENV file, like similar to the API key that we have for Google. You just put in your own like environment variables, basically. Okay, got it. Yeah. Uh, cool.

All right. So, it's going to clean up our server basically. wrong package, wrong model, all this stuff. So, yeah, we could have probably avoided this issue if we had um given it the docs up front. But that's okay.

We'll clean up pretty quick. I don't know, man. It it took me like a good 20 minutes to get this thing to work, so maybe I have better luck. Yeah, I've I've also done this one before. Um kind of like the the headshot thing, and usually it just makes this mistake of like not using the the correct up-to-date information.

Um, I actually partially did this on purpose because I think it's useful for people to see like the loop of like we tried something, it broke, we read why it broke, right? It actually gave us like a very useful error message if you just read it. Um, immediately figured out what the problem is, grabbed the relevant information to fix it, pasted it in, and then did it again. Yeah, it's all this like installing stuff or like picking the right version that that's like a pain in the ass with these pointing tools. Yeah.

Yeah, for sure. As an aside, by the way, like some people might be watching this and thinking like, "Oh, wow. This is a lot more difficult than lovable or both or something similar." Um, and to that I would say like generally I agree it's it's more challenging, but I also think that like one is you're learning how things actually work. Uh, which is good. And then two is like I do think those tools have kind of a bar that that is, let's say, lower.

So, you can't get as far as you can with some of these more like power tools. I mean, you're going to run into the same API issue using level one bolt, right? Because they have the same model behind it. Yeah. Exactly.

Yeah. Yeah. Yeah. Yeah. Um I do like cloud code better than like the lovable agent and the and the bolt agent.

But yeah, Bolt is recently switched to I think bolt now you can use cloud and codeex agents. Yeah, inside the inside of Bolt. Yeah, that's a pretty cool decision generally to like try to try to go down that path. Yeah. Yeah.

Let's see what what we got here. There we go. Nice. We have our head shot. So theoretically we now have I mean we probably want to delete some stuff in the template, right?

like the AI chat and some other stuff. Um, but we now have our professional headshot editor. We have to like do some basic prompting to put in our own logo and stuff. Um, maybe rearrange the pages a little bit, but uh, yeah, we used one out of five this month. Oh, you got to use my best template, though.

You're not using my best template. What's that? Do you want me to restart that whole thing? No. Yeah.

Can you just up upload a picture again? Sure. Uh, let's give it a try. So, let's let's You got the third one. The one on the right.

Third one. Executive portrait. Okay. All right. All right.

Um, there you go. But yeah, so we also store your past headsh shot in the database and we'll take a look at the database in a second. Um, here's our executive one. There you go. That looks good.

Yeah, that looks good. Yeah. So, yeah, let's take a look at the database and let's just refresh here and we'll see what tables we have. Right. So, we have head shot.

Now, we have a new table and it's storing the user ID and the style. Um, and anything else? Maybe that is it. Wait. Uh, okay.

Got that. That is it. Okay, got it. Yeah, I think that was the only change that I made to the database. Uh, just storing their their past history of like using the tool.

And if we head back over, we can see that down below that that's basically how this is showing up, right? Our past head shot. As I mentioned, I'm not storing the images right now. I just wanted to do that to save a little bit of time. But ideally, we'd be storing the files for the images as well.

But, uh, how did I know to just start storing this stuff? it was part of your uh yeah so part part of the the template includes all this like database access patterns okay that are already in the code and so generally speaking when you put in a prompt it's going to follow the code that's already there okay and so it just it just sets it up following all the existing patterns and everything works so that's why like it's much easier to oneshot something on top of an existing template than it is to oneshot something from scratch um because all this stuff already works and one other thing just for fun and we might be running short on time but um let me pull this up I also have product analytics hooked up to this already. So we can see like our number of you know daily active users and how many times they're visiting and all this good stuff um already inside of the the template as well. So like you can kind of as I said you know add in all these third party integrations and all that kind of good stuff uh to make this more like a real product and less like you know a vi vibe coded thing. So basically let's recap the steps okay to build a real product.

Sure. So, first of all, we got to use your magical temp template, right? I would say it's a good idea to use a template and there's more than mine available on the on the internet. So, you know, find one that you like, but uh yeah, template is a good idea. Okay, we'll put a link to your template or your course below this, but I think there's also like free templates, right?

This is not just pure sell your course. There actually is free SAS templates, right? Yeah, exactly. Yeah, I mean, if you want to use mine, obviously that's an option. It comes included with the course.

Um, but there's free ones you can use as well. And just like search on GitHub or something. Yeah, I mean, Versell has some really good ones. Um but if you generally if you speak look Google like the technology so it's going to be like you know next.js boilerplate template or node react template uh and it'll come with all the stuff. Okay.

Got it. Okay. So number one is to use the template. Number two is to like start building in a template with like you know uh some some some uh cursor or VS code or something. Right.

And and and your preferred combination right now is VS Code plus codeex. Yes. Yeah. Yeah. Yeah.

I know we demoed cloud code here and it works pretty well, but I'm using codeex more for especially for larger code bases. I find it works better. Um, but either either is fine. I think cloud code or codeex. Okay.

And then number three is to uh just to add a bunch of a API keys, right? For for like um is is that it? Well, I mean, I guess it depends on what you're trying to do, but like yeah, so you need your key for like Stripe uh for payment. I assume you want that one. Uh you need your O stuff for like your Google login, right?

Um, you probably want file storage if you're doing anything with files. So like yeah, there's a couple of keys you need to kind of add in for those things. Got it. And then and then how do you put this whole thing under interwebs? Like how do you Ah, yeah.

Good question. Yes. So typically I use a service called render for deployments. Um, so what we would do is we basically sync this code to GitHub. We'd commit it back to GitHub and then render would automatically deploy it whenever we make an update in GitHub.

So that's that's one option. Another option is like if that feels too sophisticated, you can also use this template inside of Replet and that's what a lot of students are doing currently in my cohort. So they're not even doing any local setup. They're just importing the template into Replet. Replet gives them the database.

Replet gives them the server. They click a button to publish. Um so they kind of get the best of both worlds. They first import template into Replet or they import the whole the whole app into Replet. Yeah.

Like the the the whole template that I I we kind of went through and modified, they import that whole thing into Replet. Okay. Okay. Got it. Okay.

Got it. Got it. Okay. Yeah. Awesome, dude.

All right. Looks like I have to take your course again. Yeah. One of the just just to plug it just, you know, it's my job. Uh is the course also comes with like dedicated engineering support.

So, I know it's like a a challenge that a lot of people have and I really tried my best to like get rid of all of the barriers. So, as I mentioned, like the template is pentested for security. Uh you engineering support. You get a template so like you don't have to figure out the Stripe integration yourself. And then obviously there's it's an 8week course.

Um, so you have like plenty of support and other students and all that good stuff. So yeah. Awesome, dude. And let me let me just close on this, man. Like if you're taking Colin's courses, like you should really like the point of taking the course is to actually build something and hopefully like make some money money, you know, from from your software tool.

Right. Right. It's like, you know, don't don't don't just take his courses to get create credentials, you know? Yeah. So just keep that in mind.

Yeah. Maybe this is a bad thing for me to say, but like I'm actually not a huge fan of credentials, especially in product or in tech like as a as a mechanism of advancing your career. I think the experience is what makes you better, right? Like the skill. Uh so that's the main thing is like learn the skill and then like get a material outcome like building yourself a side project that makes some revenue.

That's way cooler than like having a certificate. So that's my opinion anyway. But we went to see my SAS app to generate certificates, dude. Yeah, there you go. No, I'm just kidding.

Yeah. Cool. All right, man. Well, thank thanks for coming again. This is a great great chat.

Yeah. And uh yeah, if you want to find Colin, you can follow him on LinkedIn, right? Yep. Is there anywhere else to follow you? Substack.

Yeah. Actually, I have my own podcast. If you want to see people building SAS apps, I interview them now. Mostly PMs. Okay.

Um so, it's called Built with AI on YouTube right now. And I have to get the Spotify thing up, but you can check that out if you're interested. And uh we also have a community together, right? Oh, yeah. We do for sure.

Yeah, there's that one, too. Uh we have like I think we're almost 700 people strong now, which is pretty cool. Yeah. So, sign up for our newsletters if you want to join our community. Cool.

All right. Um, yeah, I think that's it. Thanks so much, Colin. All right.
