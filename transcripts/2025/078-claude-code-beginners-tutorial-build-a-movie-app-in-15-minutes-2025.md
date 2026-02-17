---
title: "Claude Code Beginner's Tutorial: Build a Movie App in 15 Minutes (2025)"
guest: Peter Yang
publish_date: 2025-09-03
youtube_url: https://youtube.com/watch?v=GepHGs_CZdk
channel: Behind the Craft
keywords:
- ai
- ai-tools
- user-research
- coding
- product-management
---

Hey everyone. So today I want to share a super beginner friendly tutorial to using clock code. I think claw code is the best AI agent available in the market today. And the best way to see what it's capable of is to try yourself. So here's what we're going to cover today.

First, we're going to cover how to install claw code both in terminal and in cursor. And then we're going to clone this amazing movie discovery app into our project. And then we're going to ask CL code to explain to us how this app actually works. Number four, we are going to install dependencies and uh get clock code to run the app locally. And then we're going to use plan mode to create a detail spec to add a watch list feature to our app.

After that, we are going to create a claw.md file with some best practices for using claw code. And finally, we're going to get claw code to actually build or watch this feature and see if it works. Okay, so let's dive straight in. So, how do you install claw code? Well, if you go to clause documentation, installation as installation is as simple as just pasting this single line right here into your terminal.

Open your terminal app. Just type terminal and copy this line here. And all you got to do is paste a line here and it should install. And then just type claude to load claw code. Okay.

So there you go. Clock code is now live in terminal. But personally, you know, I prefer to use claw code inside an IDE like cursor. So let me show you how to do that too. Here I have a cursor project called movie discovery with no files and everything blank, right?

You know, apologies to the cursor team for this, but these days instead of using the cursor agent, I prefer to just open terminal incursor here and type claude and say, you know, yes, I trust these files. And that's pretty much all it takes. And now you can use claw code in cursor. And the reason I like using clock code in cursor is because you can easily view and edit your project's files in cursor. While if you have a terminal window open, it's a little bit harder to do so.

All right, so let's go back to our checklist. And now we pretty much install clock hole. So let's add a checkbox to that. And let's go to the next step, which is to clone the movie discovery app. So I found this pretty awesome movie app on GitHub.

And you know, you can see it here. You can browse recent movies. You can even view the trailers of movies if you want to right down here. So, let's go ahead and clone this app into your cursor project. And to do so, all you got to do is just type get clone with the link to the app.

So, let's go ahead and clone our app with Claude. Okay, great. So, that was fast. So, now we have our app here cloned called movie app. And now let's before we actually you know make any plans or do anything let's ask claw code to tell us about the codebase that we're working with.

So let's just say tell me how this app actually works. Let's say I'm a PM with 10 plus years of experience but I'm not an engineer just to give it some more context. Okay. So claw will now start exploring the files and give you a detailed overview of how the app actually works. So, we skipped ahead a little bit and now Claude has generated an overview of how the app works.

Let's take a look. So, this is a movie and TV discovery app that provides a Netflix-like browsing experience. And the user experience is you can discover stuff, you can search, there's detailed content pages with links to trailers. And let's look at the technical architecture. So, it's pulling movie and TV show data from the movie database, not IMDb, but TMDB.

And you notice here that it requires an API key configuration. So we'll get to that later. The front end is built with TypeScript and Tailwind CSS. Pretty standard. There's a bunch of stuff here that I don't fully understand.

And that's basically how the app works. Now you can dig further and for example, you can ask it to explain the text stack in layman's terms or ask for more information. And the reason I want to show you this is because number one, claw code is really good at analyzing existing code bases and help you ramp up fast. But number two, as someone who is not an engineer, asking Claude to explain different code bases is one of the best ways to learn how to recode and to become more technical. Okay, so now let's go back to our checklist.

And we've done steps two and three now. And now let's actually get the app to run locally and see how it looks. So I'm going to go ahead and copy this and just paste into cloud code. So now uh basically we're asking claw to install any kind of dependencies and run the app locally on local host. Okay.

And you notice here that you know claw sometimes will ask you for permissions do stuff. So usually I like to go with yes and don't ask me again because I'm lazy. But of course you want to read what kind of permissions it's asking for. All right. So, you notice here that it created a EMV file with placeholder values for the TMDB API configuration.

I I think by asking claw to understand how the codebase works probably helped prompt it to actually create this end file and uh have us loading the API key. So again, the more understanding you can give Claude up front, the more likely it is to actually make the right choices for you. All right, so now we have the app running on localhost 5173. Let's go ahead and just see how it works. Create a new tab here and load it here.

And you can see here that we don't have much of an app. There's no movies or TV shows loading, right? Unable to fetch the movies. What's going on? Again, if you read the notes here, it says the app will show limited functionality because you need a valid TMDB API key.

You have to go to these uh steps to actually get the free API key from TMDB. Let's go ahead and do that now. Okay, so let's go ahead and copy this link here and go to TMDB. I've actually loaded it here already. And what you have to do is create a free TMDB account and then navigate to settings/ API.

And then there's a API key down here that you can use. Right now, let's go ahead and copy this API key. And then let's ask Claude add this TMDB API key. So the movies and TV shows will load. And let's go ahead and paste the API key.

Okay. So now claw is going to work to add the API key to thev file. And then hopefully everything will work. All right. So claw has finished his work.

Let's go back to our local host link. Voila. We have movies loading now and uh trending top rated movies. Everything seems to be working. My favorite movie is War of the Worlds.

No, it's a terrible movie. But but um let's go back to our checklist now. And now we've done step four. So so far all we've done is actually just clone the app right into our local project. Now let's go ahead and add our watch list feature.

So we can keep track of movies that we want to watch. Now here's a key point. Instead of just asking Claude to add the watch list feature, we want to get to write the spec. So this is kind of a hidden feature in cloud code but if you press shift tab then you will enter plan mode where claude will do research and planning without changing its codebase. So now let's give Claude a very basic spec here and the spec is basically you know I want to add watch this feature save my favorite movies and TV shows create a spec folder and write a detailed spec that includes requirements design approach and tech stack keeps things simple so I can test along the way now this line is very important these models they tend to over complicate the feature set right so just including this line and having it build features one by one will help you test things and make sure that nothing breaks.

All right, so let's go ahead and copy this whole thing into clock code and get it to write a spec. So while doing this, you know, a lot of people say the PRD is dead, the spec is dead. This PRD is not dead, but instead of writing the PRD yourself, you are basically working with AI to write the PRD or you're giving AI some simple directions to create the spec and then you can edit the spec afterwards to make it better and make it simpler, right? Okay. And this is so much better than obviously drafting everything from scratch yourself.

Okay. So now I'm going to go skip ahead to when Claude actually creates the spec. Okay, we are back and uh claw code has created the spec right over here. And I want to show you this. It actually started to implement the spec without me asking it to do so.

And in moments like this, you want to hit escape to cancel what it's doing, right? Because you know, you want to be a good product manager, a good engineer, and you want to actually review the spec before claw just starts implementing things. Okay, so let's actually do so. So here's the spec. It's going to add the watch list.

It's going to add remove from watch list. Going to add view watch list. data persistence using local storage and then uh there's a bunch of stuff around here and it gets into technical design and everything else right and and this is like just like super important context for clock code to actually implement the watches feature properly okay now this is a very important section down here in the spec there's implementation phases and there's phase one core infrastructure phase two UI integration phase three enhance enhancements and you know there's some features here that I don't really want like I don't really care about toast notifications and uh so let's get rid of that and let's get rid of bulk operations too. So again it's very important to review the spec to see if all the features it wants to build makes sense because it tends to build more than you actually want and to actually try to cut scope and simplify so that uh you can build this stuff out in different steps. All right.

Now, before we get Claude to actually start coding the watch this feature, there's one more important step. And that step is to write init to initialize a new claw.md file with codebase documentation. So what is a claw.md file? So claw.md file is a file that gets loaded into the prompt for every cloud code session that you have. So think of it as kind of persistent memory for your project.

And it's always best practice to type slash in it to ask cloud to make this file because it's very important context for cloud to understand how your codebase works and you can also add some important best practices. So again, I'm going to go skip ahead and let's see what this cloud MD file actually looks like. All right, so that took a little bit longer than I wanted to. It probably took like a few minutes, but let's take a look at the claw md file. All right, so it's a file that provides guidance for claw code.

There is a bunch of stuff about setting up the right environment, you know, how the app works, right? Component pattern, styling approach and um project structure. And yeah, this is just like really important context. And we can always add more context to the claw.md file. For example, let's go ahead and ask it to do this.

Let's ask it to update the file with some best practices for development like writing tests for each step, writing descriptive commits, following existing patterns, and so on. And you know, I learned this prompt basically from Lee Robinson, the video interview that I did with him about cursor. So, let's go ahead and add this to the claw.md file real quick. And while it's working, let's go back to our checklist. And now we've done this part and this part.

And now the only thing left is basically to actually add the feature. And notice that you know we actually did a lot of work instead of just asking claw code to add the feature directly, right? And this upfront work and planning and context is absolutely critical to using clock code effectively. All right. Let's go ahead and ask claw code to implement the watch this feature.

And even in this step, what I like to do is I like to first ask it to give me a to-do list, right? Because you know we have the spec, but I just want to review the to-do list real quick before it actually starts implementation. Okay, so claw has come up with a to-do list. Let's take a look. Create a redux store.

Add local storage. create watch this button. This all makes sense, right? And and to be honest with you, I don't really understand what a redux store is. So, I can ask Claude what it is, but uh since we're lazy, well, let's go ahead and just type go.

All right. So, now Claude is finally going to get to actually programming and coding this feature. And because we've asked it to write tests in cloud MD, it should also write tests to check his own work along the way. And typically right now what I do is like to go grab a coffee and come back in a few minutes when Claude is done its work. So again, let's go ahead and skip ahead and see if Claude uh successfully implements our watch list feature in one shot.

Okay, so we're back temporarily and I want to show you that at any time you can type slashtodos to see Claude's current status on working through his to-do list. So in this case, it's finished number one to four. is currently working on adding watch this button to the detail page and a bunch of other things at once, too. Okay, so we'll check back in when Claude has finished its full to-do list. All right, we're back.

Cloud has finished implementing the watch this feature, and let's see if it works in our local host. Let's go ahead and restart this and let's scroll down. And you notice here that now there is this heart button here. So definitely enjoyed watching Superman. Let's add it to your watch list.

Let's make it fun and pretend that I enjoy watching War of the Worlds. All these top rated movies I definitely loved a lot. Spirit Away. Definitely a class classic. All right, so we've added four movies to our watch list.

Let's see if it actually works. And here they are, all four movies. And if I remove one, it gets removed. Let's see if TV series works. I can add alien earth to our watch list and it should be back on here.

And uh let's finally let's check if I can add to watch list from the detail page as well. And it looks like I can add mission impossible from the detail page. So it looks like claude was able to build our full feature in just one shot. But it really wasn't one shot, right? We went through all these steps to actually make the plan, check the plan, create the cloud.md file, ask claw to create his to-do list, and make sure to check that too.

And only after all that was Claude able to build the watch list feature in one shot. So, if there's only one thing you learn from this tutorial is that the more planning you do up front, the more likely Claude will be able to build your features without any issues. And again, planning includes asking claw to write a feature spec, create a claw.md file with best practices, and make a detailed to-do list that you should check before any kind of implementation. All right, so that is our beginner's tutorial that you can follow hopefully in just 15 minutes to clone this movie app and add a watch list feature to it. And I have a lot of really great Clock code content coming, including an interview with Cat Woo, who is the PM behind Clockode.

So, be sure to like and subscribe to get more content like this. Thanks so much.
