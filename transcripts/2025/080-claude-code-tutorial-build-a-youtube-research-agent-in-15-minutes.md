---
title: "Claude Code Tutorial: Build a YouTube Research Agent in 15 Minutes"
guest: Peter Yang
publish_date: 2025-09-10
youtube_url: https://youtube.com/watch?v=iW0lMW-Ff5I
channel: Behind the Craft
keywords:
- ai
- storytelling
- product-management
- ai-tools
- productivity
---

Hey everyone, today I want to show you how to build an AI research agent with clock code. You know, most people use clock code for coding, but it's really an everything agent that can automate any task for you. So, this is the tutorial that we're going to walk through today. I am going to build a YouTube research agent that finds the best videos from your favorite YouTube channels and then analyzes each creator's winning formula. And we're going to do this in six steps.

So first we're going to explore solutions with Claude. Then we are going to update permissions so that it can auto approve changes. Then we are going to ask Claude to write a spec for the slash command that we'll use. Convert the spec into a detailed to-do list. Create the slash command.

And finally add batch processing so that we can analyze multiple YouTube channels at once. Okay. Okay, so I'm going to assume that you have clock code installed already, both in terminal and also set up in cursor. And if you don't know how to do that, then check out this other video that I made with the instructions. It's very simple.

It's just a oneline thing. Okay, whenever I start a new project, I always like to start by exploring solutions with Claude in plan mode. And to enter plan mode, just press shift tab until you see plan mode here. And plan mode basically lets you brainstorm and draft plans of claude without having a code. And doing this can save you hours of going down the wrong path.

So let's go ahead and put a prompt into cloud right here, which is I want to build a tool where if I type /youtube at channel name, it outputs a YouTube- research MD file with that channel's top recent videos plus a key insight about what content is working for that channel. And let's kind of explore three different ways to do that and see what Claude comes up with. Okay, so you see here that Claude has explored three different solutions. First one is using a YouTube data API. It's official and reliable.

However, it requires a Google cloud account and API key. There are quota limits and then it can cost us money. Second option is to explore web scraping. Just pasting a HTML directly for the YouTube page and trying to scrape that. Now obviously that is like not super reliable.

And the third option is to use thirdparty libraries like YT- DLP, which is open- source tool that let you extract YouTube data without requiring an official API. So, this option sounds pretty good to us, not having to get a API key and just be able to get data from uh this third party tool seems to be the best option. And you can see down here that Claude actually wants to start coding right away. And when you see this, when you're in the planning stages of the product, you should definitely say no. I would not like to proceed because there's a lot more planning that we still have to do.

We have to make a spec. We have to make a to-do list and so on and so forth. So, let's say no. Now, let's move on to step two of our list, which is to set permissions to auto approve changes. And I think this is a just a convenience thing to do because you notice how claw is always asking you for permissions to do stuff which can be pretty annoying, right?

If you want to just like let claw work and go grab coffee and then come back 10 minutes later to see it output. So what I like to do in the beginning of different projects is to type slash permissions. And what this does is that Claude is going to create a new file where you can give it different access permissions. So I prepared a list of allow tools here that let's just paste into cloud. Okay.

And these tools are you know the ability to read files to write files and to run these uh commands. mpn to run like you know localhost and other functions yt-dlp which is the third party YouTube tool that we can use to get information just to be able to run all these commands without having to ask me for permission each time. So let's go ahead and enter to submit and see what happens and we want to save this just in the local file. Okay, so now this stuff should be in the local file. So let's take a look and uh there it is.

You can see that we have a bunch of allowed permissions including web search, including be able to read, including mpn and yt.dop. So now we finished our second step and let's come back to our checklist here. Let's just kind of check off a few steps. You know, we want to kind of like build this project the way that Claude likes to do, which is to do checklist and to-do lists. All right, so now we're going to write a spec for the slash command.

Now, what exactly is a slash command? A slash command is just a convenient way to save and reuse your favorite AI prompts and workflows inside claw code. So let's go ahead and ask claw to write a spec first to create our YouTube slash command. All right. So I'm going to put this in here which is create a spec in a spec folder called YouTube-command-spec.md to create a custom slash command.

Right? And what the command should do is it should fetch 20 most recent videos from a YouTube channel. Show the top 10 by views with title, URLs, view count, and duration. And then above the top 10 list, I wanted to include a key insight section with specific performance patterns and a your next video section with title suggestions. And I want to include in the spec what the ideal output format is for the slash command.

All right. So now Claude is going to go ahead and make this spec and I'm going to skip ahead and come back so that we can review the spec together. Okay, we're back and you see here that Claude has created a spec. So let's take a close look at it. All right, so we're going to make a custom slash command that analyzes a YouTube channel, right?

You can paste in a channel URL or handle. So let's just do at uh channel handle to make this simple and then it's going to use YT DLP to fetch the video metadata. This all looks good. I think upload date I don't think we need that information. So let's get rid of that here and let's keep going down.

And I think it's particularly important to view the ideal output format that you want. Right? So it's right here. So first we're going to have key insights. Let's put that here.

Display 305 bullets analyzing performance patterns. Yep, this looks pretty good. Let's get rid of the peak performance time frames. I don't think we need that. Um, and there's another section up here called your next video with title suggestions.

That sounds good. Let's just stick to three suggestions for now. Okay. And then there's another section on top 10 videos from the channel. And let's make sure that this is correct.

Uh the format that we're going to have is like this with the YouTube link and the views. That seems right. All right. This all looks very very good. And you can see that I reviewed the spec pretty carefully before proceeding to the next step.

Right? It's very important to edit and modify the spec so that it's to your liking. Especially, you know, for slash commands, the ideal output format that you want. Again, the more work that you put up front into planning, the more likely Claude is able to get to the ideal output that you want in one shot. Okay, so now we're done with the spec stage of our to-do list.

So, we did that and now we're going to convert the spec into a detailed to-do list before Claude actually starts implementing the code. And to do that, we're going to put a prompt, very simple, just a oneline prompt saying create a to-do list to implement the slash2 command based on the spec. So, I'm going to skip quickly ahead and let's see what Claw comes up with again. All right, so Claude has created a to-do list. There's 12 different tasks that it wants to implement.

And let's take a quick look. I think the error handling and the caching and everything else is kind of like a nice to have. So why don't we just do let's just start with doing steps one to seven. Okay. And see what it comes up with.

And now we're finally at the stage where actually asking Claude to start coding. And again I want to recap here that first we explore different solutions with Claude to find the best solution which is to use this YT-dLP tool. Then we ask claw to create a spec and review that spec. And then we ask claude to create a to-do list from that spec before we ask it to start the code. So this is the exact process that you should follow in my opinion each time you want to do a project with cloud code.

All right. So now let's skip ahead and see if cla can make this thing work in one shot. Okay. So we're back and now that we've uh created the slash command, we can test it with a real channel, right? So, we type slash YouTube and let's put the channel name and let's just use my channel.

Peter YangYt is the channel. And let's see if Claude successfully makes the YouTube-resarch.md file and asks the top 10 videos and results for my channel. All right, we're back and I've opened the uh YouTube/research file where Claude has added a bunch of details about my channel. And let's take a look. It says, "Your channel thrives on comprehensive tutorial content with full tutorials and complete guides generate three times more views and shorter videos.

Sweet splot is 45 to 60 minute in-depth tutorials featuring practical demonstrations, right? And it has a bunch of information about title formats that work like using the words full tutorial and complete guide seems to work well. And it also has a bunch of ideas about the next video that I should make. And some of the stuff is like pretty questionable, but you know, it at least kind of tries to give you an idea. And down here is listed uh my top 10 best performing videos out of the uh 20 recent videos that I made.

And it looks like there's some maybe bugs with some of the titles. So, we can give Claw that feedback and uh make sure that it's outputting the full title instead of a truncated version. And let's also test to see if the links actually work. So, let's open this link. And yeah, it seems like the links work totally fine.

All right, so now let's come back to our to-do list. We've done the spec. We've created a slash command. And now we're at the last step, which is to add batch processing. Analyzing channels one by one is pretty tedious, right?

Having to run this command for every single channel. So batch processing is basically adding additional feature where claude is going to read from a file with a list of channels and then it's going to process all of those channels at the same time. So let's go ahead and open cursor again and let's give it this instruction. Update the spec and the YouTube command to check for a YouTube- channels.md file. If no channel is specified in the command, then process all the channels in that file.

Let's go ahead and give this command. And while we're waiting, let's make a new YouTube- channels.m MD file right here. And let's go ahead and add some of my favorite channels to this file. So, these channels include my own channel, Lenny's podcast, Greg's channel, Tina and Jeff. We all make content about AI and, you know, practical tutorial content.

And let's wait until Claude finishes making the changes to the spec and the /youtube command. And then we're going to run the command to see if it can do the analysis for all five of these channels at once. Okay, we're back. So, Clockode has finished it analysis. And let's pull up our YouTube research file.

And yeah, we have my channel analysis here at the top, but let's scroll down. And as you can see, we also have the analysis for the other channels. So for Lenny's podcast, the insight is uh the podcast excels with founder interviews and product leadership content with episodes featuring famous people averaging 2.4 5x more views. Yeah, that's pretty clear. Let's keep going down uh with Greg.

Greg's channel dominates with startup idea validation with videos about specific business ideas averaging four times more views. All right, let's keep going down. Tina's channel excels with productivity and career advice videos uh about AI tools of productivity average 5x more views and you know there's also specific title formats that maybe I can try too and down here we have Jeff which is uh again very productivity professional development focused talking about Excel and stuff but I know that recently Jeff has also moved on to AI tools. So this is like just a super valuable analysis right that would have taken us a long time to do manually. Imagine if we had to manually go to each channel, look up all the videos, and then try to write these kind of inside paragraphs and try to identify title patterns that work.

It would have taken a long time. And because of AI and cloud code, we're able to get this done in just what 15 20 minutes. And you know, you can repeat this process for basically any kind of research task, right? So, for example, you can set up slash commands for daily briefs to get recent AI industry news by looking at four or five different blogs. You can get a newsletter digest to summarize your favorite newsletters.

You can do slashmarket research to analyze industry trends on a topic. The key lesson here in this tutorial is that the pattern you should follow to set up the slash command is always the same. First, start by exploring solutions. Then ask claw to write a spec to create a slash command and review it before you move on to the next step. Then ask it to make a to-do list and again review and edit the list and finally get it to code.

The code step is the very last step and in some ways the easiest step. Now I've been following this process for a long time and I haven't ran into a case where Claude hasn't oneshot the actual code because we've done all the preceding steps. So that's it for this tutorial and um like and subscribe to this channel. I have a lot of great content coming including interviews with Cat, the product lead behind Claw Code and also Megan who is the design lead behind Clock Code. You can't get any more AI native than the Claw Code team.

So be sure to subscribe to get the full interviews in the next few weeks. Thanks so much.
