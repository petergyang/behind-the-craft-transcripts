---
title: "Full Tutorial: 20 Tips to Master Claude Code in 35 Minutes (Build a Real App)"
guest: Peter Yang
publish_date: 2025-09-24
youtube_url: https://youtube.com/watch?v=jWlAvdR8HG0
channel: Behind the Craft
keywords:
- ai
- coding
- ai-tools
---

Hey everyone, I'm back with a new tutorial. Okay, so today I want to share 20 tips to master clock code while building a real app. And you know, as a parent, I'm always looking for fun familyfriendly activities nearby. So in this tutorial, I'm going to show you how to build a family activity finder like this that shows upcoming local events personalized to your location, schedule, and interests. And while building this, we're going to try to cover all 20 of these tips so that you'll know every essential Cloud Code feature to plan, code, and debug apps.

I only decided to make this tutorial after spending a full month with clock code. So, I hope you enjoy it. Okay, so let's start with a brand new project. We call it family activity demo. And I have it open up an empty folder in cursor here.

And just as a reminder, you can install claw code by simply pasting this line here. Now, since I have it installed already, all I have to do is type cloud to open cloud code. All right. So, proceed. And there we go.

We have cloud code open. Okay. So, the very first tip is to use plan mode before coding. You know, if you just remember one tip, make it this one. The more time you spend planning, the more likely Claude will succeed.

And I always press shift tab to cycle to plan mode. And if Claude for some reason has to start coding, I always hit escape uh to cancel. So think of Claw like an overeager engineer, then you really have to ring all the time, right? So now you see here, let's press shift tab. And now we're in plan mode.

Okay. So let's move on to the next tip, which is to ask Claw to explore solutions with you. So the first thing I like to do in plan mode is to ask Claude to explain the code base and then I'll tell it you know I want to build this feature. Can you explore solutions starting with the simplest one? The whole idea is to collaborate with Claude to come up with a plan first before coding.

So, I have a prompt here where I'm going to tell Claude I want to build a family-friendly activity finder. And parents can enter their city, kids age, when they're free, how far they'll drive, and any other preferences. And then the app will search for weekend activities nearby and return five recommendations with bold titles. And let's also add an emoji and two to four sentences description each. All right, so let's paste this into cloud code and see what it comes up with.

And remember, we're still in plan mode here. Okay, so uh Claude has come up with three different solutions. And you notice here that it's asking to start coding again. And again, you got to hit uh no, I want to keep planning. Like it's just way too overeager to start coding.

Let's actually read through what I come came up with. Uh let's scroll up. Okay, so solution one is using a static database with client side filtering. Okay, so it's going to hardcode activities. Solution two is using a thirdparty API like Google Places, Eventbrite, and Meetup.

The problem with this solution is that, you know, local activities are very fragmented. It can come from like multiple places. Eventbrite, patch, and other websites. So, we're going to have to hook up a lot of different APIs, which is a lot of work, right? And solution three is claw messages API with smart recommendations.

You know, because we're trying to do a demo for claw code, I think this makes a lot of sense. is the most AI powered solution, but really it's just, you know, calling the cloud API and using the web search tool to look up recent activities. Okay, so now we have three different solutions. And now let's go back to our tips. Very important when you want to work with cloud code, you want to follow the spec, to-do, and code process.

So after exploring and selecting a solution with claude, I like to ask it to create a spec with the requirements, tech stack, design guidelines, and up to three milestones to execute. And then I go even further by reviewing the spec, making sure it's correct and simplified, and then asking Claude to create a to-do list for the first milestone. So I'm always auditing and reviewing Claw's plans in each step. Right. So now let's go ahead and ask cloud to make a spec.

So again I have a prompt here. Create a spec.md with requirements text stack design guidelines up to three milestones. Keep it as simple as possible. For milestone one, let's just set up the UI with dummy data. And for milestone two, let's connect to cloud API with a web search tool.

And I've linked the documentation here. Let's load it up. So Claude has this web search tool that can search the internet. And I've did some research ahead of time for this, but you can also just ask Claude, you know, how to implement this stuff and it'll probably point to uh one of these documentation sources. So, let's go ahead and paste this prompt into Claude to create the spec.

And let's actually go a step further and copy this image into Claude as well. So, it has a reference point, right? So, just press Ctrl +V to paste the image into Claude. Okay, so now Claude is going to go ahead and write a spec.md file and let's see what it comes up with. All right, it looks like Claude has created a spec.

Let's take a look. Here we are. Family activity finder. The whole point of this thing is to actually review the requirements in detail and edit it to simplify it because cloud likes to build more than you ask for and just make sure that it's accurate and what you actually want, right? So, for example, here it's saying the app returns five personalized active recommendations with engaging descriptions and we should add and a relevant emoji icon, right?

And then here we are inputs. Okay, all these are required. And let's just make this simple. Let's let's just make all these text inputs. Text input for day and time preference.

Uh we can keep this maximum distance as a slider. And then here we have a text input again. All right. And here's the output format. Yep, this looks uh right.

The distance from user city might be hard to do, but let's see what it comes up with. And here is our front end, our back end, and our development tools. Okay, this looks right. design guidelines look right, things look pretty good. Okay, now let's here's the important part, the milestones where it actually starts building stuff.

So like we asked for it to do, the first step is just to create the UI with dummy data, which seems mostly accurate. Uh, and then we're going to hook up to cloud API integration, right? And let's just uh go ahead back here and just copy this documentation again. So it has a frame of R reference use for implementing messages API and web search. Okay.

And there's some more details down here for milestone 3. And yeah, it's written a pretty good spec. It's probably written a much more detailed spec than I would have written by hand. But there's one thing that's missing here. What do you guys think it is?

I think because we're using cloud messages API, we need to have a prompt to actually call the API with the inputs that we have and get the recommendations back. So, let's actually ask Claude, let's go back to our tutorial and ask Claude to create a prompt MD file with the prompt that we're going to use for milestone 2 will call the API. Okay, so let's go ahead and ask Cloud to do that. Now, it's going to create a prompt and let's see what it comes up with. All right, we're back and Cloud has created a prompt file and here we are.

System prompt your family activity recommendations experts. Here we go. Return exactly five in the following format. Yep, this seems right. Let's make sure that it's current and let's say it's timely because we don't want to return like generic attractions information, right?

We want to return timely events. Okay, so now let's go back to our thing. And now we're going to ask it to create a to-do list with tasks from milestone one. Remember, we're trying to follow the spec, to-do, and code process here. These are the two critical steps before you actually start getting into code.

All right, so let's go ahead and paste this here. Let's also make sure that the spec includes details to use the prompt for milestone 2. Okay, we're very much still in planning mode, just writing like documents. We haven't written any code yet. But again, the more you plan, the more likely Claude is to actually build the code without any errors.

Especially for people who are like not super technical like myself, it's very important to the planning step first. So, let's come back once Claude actually finishes the to-do list. Okay, so Claude has created a to-do list. Let's take a look. Um, and uh again, the goal here is to audit the list to make sure it actually makes sense.

So milestone one, we're going to make the UI with dummy data. Everything here looks right. So I installed a bunch of dependencies. Yep, this looks all good. Yep.

Add clear button functionality. Add results. And uh I mean this is quite a long list, but things look pretty good to me. Now before we get clawed code, let's actually do a few more tips. Okay, so my next tip number four is to use output styles to learn while building.

So you can type /output style explanatory to get claw to add inside boxes that explain why it made each choice so that you can learn to recode and understand the tech architecture better while it's building. You can also type output style learning and claw will actually make you write pieces of code so that you can even learn and get hands-on practice. Now, because we're lazy, we're just going to type output style explanatory because I don't actually want to code by myself. So, let's go ahead and turn it on. And now we've set the output style to explanatory.

This is a really good option that the cloud code team built for folks who want just want to learn while building. And uh now cloud will add inside boxes as we ask it to do stuff. Okay, but let's go further, right? Let's go cover tips number five and six as well. Tip number five is you can use this claw.md file to bootstrap your project understanding.

So you can type slashinit in claw code to have claude scan the codebase and create a detailed claw.md file with project context patterns and key files. And this file becomes claw memory for every future conversation. Okay. So let's go ahead and uh just ask claw to create a claw emptyd file. But actually I'm going to ask it to create an empty cloud empty file because uh we don't actually have any code in here right now.

So let's create a empty cloud emptyd file. Okay. And the reason I want to create an empty file is because of the next step which is I want to add my personal preferences to clot. So you can also add your personal preferences on how you want cloud to respond to your cloud file. Here's the thing I'm going to copy and paste into cloud.

I'm a PM with limited coding experience. When you're coding or doing your work, please share tips that explain the tech architecture and any changes that you're making and why. Okay, let's paste it right here. And there we go. I think that should work.

All right. So, we've done all the prep work and now we can finally move on to actually getting cloud code. And here's tip number seven. Use voice to give claude context faster. Right?

So, I've interviewed a lot of great engineers like Kieran and other folks. And a lot of times they don't really type anymore. Instead, they use voice tools like Whisper Flow and Monologue to dictate to Claw directly. and speaking naturally often results in more detail instructions for Claude uh that helps it produce better output. Okay, so definitely use your voice.

And speaking of that, let's cover tip number 82, which is to get your app running as soon as possible. I specifically asked it to just build a UI first with dummy data as the first milestone because I want to see the app live as soon as possible, right? So that you know when I make subsequent changes like hooking up to cloud API I can actually see the app update in real time. So here I have a prompt build monster one based on to-do file and run local host. Loc host is basically just running the app locally on your machine right so you can see it live.

So instead of copying this in I'm just going to voice dictate to cloud and I have whisper flow installed. So all I have to do is press control to dictate stuff into cloud. So let's say build milestone one based on the todo.md file and then run local host and also use this image as your reference. All right, here we go. Uh here's the voice and it's not quite perfect.

So let's edit it. Build milestone one using to-do and file and roll close. Also use an image as the reference and let's go back and just pasting our image here. Uh let's copy image and paste it here. Okay, use this image as reference.

Okay, great. All right, so now Claw is finally going to code milestone one, which is to set up the UI and just use dummy data on our uh local recommendations. And let's see if Claw can uh come up with this in one shot. Okay, so Claude is in installing a bunch of dependencies. And while it's coding, I want to quickly cover tip number nine, which is press escape if Claude is going off the rails to stop and redirect Claude.

So at any time while Claude is coding here, it's asking to install a bunch of stuff. You can just hit escape and it will stop whatever Claude is doing and it's not going to lose the context. This is very useful if you see Claude going down the wrong path or doing more than you want it to do. Uh, so don't be afraid to hit escape, right, if it's doing the wrong thing. All right, so now let's come back uh whenever Claude finishes actually building milestone one.

Okay, I came back real quick. Claude is still working through his to-do list, but you see now that it's sharing these insights because we changed the output style to explanatory, so we can learn as we build apps, right? And there's some other insights up here. So, you know, if you're new to coding, if you're trying to learn to become more technical, I definitely recommend using the explanatory output style and also updating your claw. MD to ask it to overexlain stuff.

All right, we'll come back once it's finished coding. Okay, claude claims that it's finished coding and now there's a local host link. But you know what? When I load the local host link, absolutely nothing shows up. So, I want to show you kind of these bugs because it's not perfect, right?

So, what's going on here? It's not loading anything. And let's actually go ahead and go back to our tips and let's skip ahead to the section on debugging. So there's kind of two tips on debugging. One is to ask Claude to think ultra hard or why do you think this happened to help you debug bugs, right?

So think ultra hard basically gets claw to think longer before coding. And why do you think this happened causes it try to root cause the issue more, right? And of course, a really good best practice is to just give very specific feedback to attach images and to look at browser console logs to help cloud debug issues. You know, the more context cloud has, the more likely it is to figure out what went wrong. So, here we don't have an image.

It's just a blank screen, right? But let's go ahead and inspect here and let's see if there's any kind of console bugs. And lo and behold, there is. See, there's uncaught error and there's something going on here. So, let's go ahead and copy and paste this bug into Claude.

And let's say uh I only see a blank screen. Think ultra hard on why this happened. And here's a bug I see in the console. Let's go ahead and paste this bug. All right.

So, we g a lot of context. We've asked it to use a lot of tokens and think ultra hard. And hopefully now it can fix the bug. And then we'll come back later to see if it fixed it or not. All right, we're back.

Uh let's take a look at our app now. And here we go. It looks like uh the UI is working. Zoom a little bit. I can enter a city, kit, ages, availability, distance, and preferences.

And uh I can search and a bunch of activities load. Now, these activities are again dummy data. They're not using a real API because we're still on milestone one. It looks great. There's a bunch of emojis.

And yeah, overall it seems to work well. So, let's go back to our cloud code. And let's actually ask Claude to check things off in to-do.md that are done for milestone one. and also add to-dos for milestone 2, which if you recall is hooking up the cloud API and the web search tool. So, you know, we want to make sure our to-do list is up to date as we build more and more milestones.

And while it's doing that, let me talk about something else. So, let's go back to our tips. Let's go back here and let's talk about tip number 10. So far, we've just been kind of like asking cloud to code, right? But I think it's really important to add version control with GitHub integration.

I like to save changes to GitHub after each milestone. GitHub basically provides version control so that you can revert to a previous version of your codebase if things get messed up, which they will inevitably happen with AI, right? And let's go to our GitHub. And here I am going to create a new repository. Let's give it the same name, family activity demo.

So if GitHub is new to you, it's not too complicated. Just create a new account uh right here. And then there's a button to create a new repository and then just hit create. So after you create the repo, you there's a link to the repo here. So um you can just go into claw code and link this project to this repo that I've created and you know it's clearing some insights about how git works and it's like asking for permissions to link to repo and it wants to make an initial commit.

So it wants to commit the code to the repository. There's also another way to do it which is to type install-github-app and walk through a few steps. But since we created a repo already, we're just going to use the manual way that we did above. So now it's saying that it's pushed the code to GitHub. And let's take a look at our project.

Refresh. And there we go. We have a bunch of code here, including our specs and to-do. And there's a bunch of code in this folder. So now our code is in GitHub.

And we can uh ask Claude to, you know, revert to previous version or, you know, add new commits as we move along. All right. So now, what are we gonna do next? Let's go back to our thing here and let's talk about tip number 11. You see that Claude keeps asking for permissions to do stuff and I have to set permissions and you know this can get pretty annoying, right?

So what you can do is you can set up permissions to let Claude work more autonomously. The way it does it is it'll create a claude settings file and uh where we can grant it auto permissions to read, write, and run specific save commands without having to ask us for permission each time. We can also skip all permissions by just typing dangerously skip permissions, although you know, again, I don't recommend this unless you really know what you're doing. So let's go ahead and copy this prompt into cloud which is to get to create a uh file to auto grant permissions. Now very important you probably don't want to auto grant cloud permissions to remove or delete files because that's more dangerous.

So I've kind of called that out here but let's go ahead and paste in. Okay, Claude has finished creating the settings file. Let's take a look. It's allowing all these different permissions. Read, write, so on and so forth.

bunch of get commands and it wants to deny any kind of remove commands like we asked it to. So there you go. Now we have our permissions file. Now let's go back to our tips list. And before we build milestone 2, let's actually talk about this tip, which is to clear context strategically with clear and compact.

Because we spend all this time going back and forth through Claude in a chat window, Claude's contest window is probably pretty full by this time. And AI just gets progressively worse as your conversation history gets longer. So let's actually type in compact here to clear the conversation history but keep a summary in the context. Right? Let's go ahead and do that.

And we can also use clear to just clear the conversation history in total. But I like to use compact more because then it creates a summary. Okay. So while it's compacted the conversation, let's look at this tip here. I think again if you remember one thing from this tutorial is to follow the spec to-do and code process with each milestone.

So before we build milestone 2 by hooking up the cloud API, let's make sure our to-do list is updated to check off any completed milestone one items and add any milestone 2 items. And I remember we did this before we asked Claw to do this. Let's just take a look at the to-do list. And you see that it's checked off a bunch of milestone one items that are done. And it's added milestone 2 items.

And let's just quickly take a look. Yep, this all looks right. Set up request body. Very important to ask it to use the web search tool. Set up proper model parameters.

For some reason, it wants to use claude 3.5 sonnet, which is a old model. I don't know why. uh it should it should be using really let's say clot 4 sonnet instead. So again it's important to review these details that actually catches these mistakes right and uh prompt engineering. So again we already have a prompt template here in prompt MD.

So we should ask it to use prompt MD right and then uh go down here data flow testing performance everything else looks pretty good. Okay. So now we've compacted everything. So we have a new conversation here. And let's go ahead and ask it to build milestone 2.

So I'm going to use my voice. Okay. Now build milestone 2 by following our todo.md file very closely. And one more thing before we start. So for milestone 2, we're going to need to have a cloud API key because it's going to call the cloud API, right?

Uh let's go to claude console here. And here I have set up a couple of API keys here. And I actually have an API key saved here that I can paste in. So use this cloud API key. Okay.

So now let's ask it to build. But real quick on API keys, you know, I I just briefly flashed my API key on the screen. And you should never do this. You should never share your API key with anyone. So, I'm probably going to delete this API key afterwards in case you guys want to charge my cloud account, but you know, you can just go to cloud console, anthropic console, and create a new key and just name it something.

Let's say test key and add, and then it will create a new key here, right? Um, and just copy that into cloud and it will do the work for you. But the important point here is to never share your API key with anyone and not even your spouse. keep it secret because otherwise people will start charging your account. And uh of course to actually use this API key, you're going to have to put maybe $5 or something on your Claude account.

$5 is worth it if you want to learn how to code with AI. All right, so now Claude is working through the to-do list and it's going to create the backend server and hook up the API. It's going to take a while, so let's skip ahead and see what it comes up with. Okay, let's come back for a little bit. I've been reading what it's doing and it's trying still is trying to use claw 3.5 sonnet which is deprecated.

So let's actually tell it to use claw 4 as the model instead. Okay. And again, you know, it's tempting to go off and get a coffee while it's doing all this work, but there is a benefit to sitting around watching a code because you get to learn. It's still sharing these insights with with me, right? And you also can see when it's actually going off track like using an older model.

So now it's going to update the model to cloud 4 and hopefully uh it will work better. All right, we'll come back when it's done. Okay, it said uh it's finished all this work. It's checked off all the milestone 2 items and I've tested it here and it is loading results. But the problem is the results are very generic, right?

Talking about going to Exploratorium, California Academy of Science. These are just like very generic results. So, let's give it some feedback. You're showing generic results like Exploratorium. What I want is more timely and relevant familyfriendly local events like um let's say Explorer torium after dark or maybe you know Lindy in the park which is a dance thing.

How would you fix this? Let's not accept edits. Let's actually go to plan mode and just ask it how it plans to fix this. Chances are it's probably going to update the prompt, but let's see what it comes up with. Okay, so uh it's saying propose solutions enable clause web search tool recommended.

So it didn't actually enable the web search tool even though it was on our to-do list, I'm pretty sure. And it uh checked it off. So again, you got to be careful here. is like a overeager junior engineer that claims it did something but it actually didn't. It wants to search the web for how to use the web search tool.

But you know, we've already given it a documentation on how to use the web search tool, right? So, let's actually just paste this documentation in. Add the web search tool functionality. You know, follow this documentation very closely. There we go.

Because otherwise, it's going to do a bunch of Google searches and like maybe you'll find a relevant article and maybe not, but we did a research for it. So now hopefully it actually does add the web search functionality and then we can get more real-time current events and let's see if it does the job or not. Okay. So uh coming back briefly it started to add a bunch of like location and time zone region detection helpers. But you know in our app here the user is already providing this information right.

Uh again I interrupted his work and I say hold on why don't you just use the users's inputs on data and location include that part in your prompt and of course they said you're absolutely right and the inside is sometimes the simplest solution is the best. So again you have to sometimes monitor what cloud is doing and correct it to simplify as much as possible because otherwise you'll build a bunch of stuff here that makes it overly complicated. All right so we'll come back again uh to see if it actually does something good this time. Okay, everyone. We're back.

And uh I'll be honest with all of you. It took me 10 minutes of going back and forth to get this app to work because there was a bunch of rate limit issues with the cloud API. And you can see here my excitement when we finally got it to work. But basically, I went through the same process of the tips that we covered. you know, I gave a bunch of context on what was going wrong and uh I uploaded browser console logs and other things and I made it up to the prompt to be more brief and eventually we're able to get it working.

All right, so without further ado, let's load up our app right here. And you can see here now that I've entered Los Angeles in here uh and some information and it's actually pulling up relevant recent events for Los Angeles. So let's just try it again with San Francisco one more time just to see uh if it works. And you know it does take a while to call the cloud API and have it do web searches. So we have to wait a few seconds.

Okay. So you see here that it's loaded the events and these are relevant events. There's Golden Gate Parks. There's a whales tail event happening. MUN Heritage Weekend happening and you know these are much more recent and relevant events than just listing the attractions, right?

So now we have our family activity finder basically complete and we can always make improvements to it. But I think we should give ourselves a pat on the back because we built this in about 30 minutes while covering most of the tips. So now that we have a fully working app, there's of course just best practice. We should go ahead and commit these changes to GitHub. Commit to GitHub.

So that the version on GitHub also has our latest backend and API changes. And while it's doing this, let's take our time and cover a few more tips in our list. Right? So we're not going to do a live demo of these tips, but I just want to quickly cover them. All right.

Number 16 is to create a custom slash command for repeated workflows. It's one of my favorite tips and you can check my dedicated tutorial on it up there. All right, the next one is tip number 17. So you can ask Claude to build specialized sub aents with name, description, and their own prompt. And each sub agent has its own context window.

So it's not going to pollute your main conversation. So for example, anthropic engineers use sub agents for stuff like documentation updates, security audits, and incident responses. the main agent decides when to call them. Okay, let's keep going. Tip number 18 is to set up hooks to trigger specific behavior.

So hooks let you run scripts that run after Claude completes specific actions. For example, you can ask claw to trigger a Slack notification using a hook when it has finished his work. Once again, with, you know, sub aents and hooks, all you have to do is just ask claw to create them, right? you know, I want to create a hook for uh setting up a Slack notification. And maybe this can be a future tutorial, too.

All right, two final tips. You can install MCP servers for specialized capabilities. So, useful servers include Serena for co- search, Playright, which lets Claude screenshot and tests its own UI, and Figma, which is designed to prototype. So, to run an MCP, just uh run claude space MCP space add whatever the server is. And uh you can check out Anthropic's official documentation here to look at MCPS.

One thing to watch out for MCPS is that it tends to load a lot of context into your prompts. So typically you don't want to have too many NCP servers running at the same time. All right, last but not least, you can also run multiple clause sessions in parallel for faster development. So you know how in our milestone we first built the front end and the UI and then we built the back end. But you know if you already know what you're doing if you're an engineer you can actually use git workree to build both of these simultaneously with different clouded conversations.

Now I'm not advanced enough to do this but you can check out my interview with Kieran for a live demo. All right, so now let's go back here and it looks like Claude has committed our changes to GitHub, right? So we should be all done here. And let's just quickly end this tutorial by recapping our list of tips. Okay, so here's a list.

So number one, for planning and project setup, you want to use plan mode. You want to follow the spec, to-do, and code process, right? Uh, and then you want to use output styles and cloud MD to help you learn while you're building apps. And then once you actually get to your core coding workflows, you want to use your voice to give Claude context fast. You want to get your app running as soon as possible so you can see the changes live.

And if Claude starts doing something you don't want it to do, which happened quite a few times during this tutorial, just hit escape and give Claude better directions. Okay? and use GitHub to add version control, set the permissions to work faster. And always follow the spec to-do and code process when you're building new features so that uh you know cloud will make less mistakes. And for debugging, ask cloud to think ultra hard and reflect on why things happened and just give it a lot of context including uh specific feedback, images, and browser console logs to help Claude debug issues.

And last but not least, you can use advanced features like slash commands, sub aents, and hooks. And they might be intimidating to a beginner, but really just kind of like ask cloud about them in the conversations here, and it can help you figure it out together. All right. Uh maybe eventually I'll do an advanced tutorial on setting up MCPs and running multiple clouds in parallel. But hopefully this tutorial gives you a complete view of all 20 tips that you can use to really master cloud code to build apps.

And as someone who is kind of a beginner and not super technical myself, you know, clock hole can be really intimidating, but I really do think it's worth spending time to figure it out because at the end of the day, it's really just about you having a conversation with an AI agent. All right, so I hope you enjoyed this tutorial and uh you can check out all the prompts and everything that I used in the description and the linked article and please like and subscribe and I'll make more content like this. Okay, I'll see you around.
