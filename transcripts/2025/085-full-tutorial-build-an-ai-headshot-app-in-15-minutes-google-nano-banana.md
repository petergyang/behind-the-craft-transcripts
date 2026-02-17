---
title: "Full Tutorial: Build an AI Headshot App in 15 Minutes (Google Nano Banana)"
guest: Peter Yang
publish_date: 2025-10-01
youtube_url: https://youtube.com/watch?v=-SenpOqT6Nk
channel: Behind the Craft
keywords:
- ai-tools
- leadership
- coding
- ai
- innovation
---

Hey everyone. So today I want to show you how to use Google's nano banana image model to build an app that converts any photo into a professional headsh shot in three different styles. And I think this is one of the best apps to build if you're new to AI coding. And it's just really fun to make head shot of your friends. Okay, so we're going to build this app in five steps.

First, we're going to work with AI to draft the spec. Then we are going to build the UI and the scaffolding. We're going to create three prompts for different headshot styles and then poke up Google's nano banana API. And finally, we're going to try to fix any bugs or issues. Now, all the prompts that I'm going to use in this video are available in the document that's linked in the description.

So, let's get started. So, here I have a empty cursor project and I've loaded clot code in a terminal, but you can also just use cursors agent if you want to build this app. Now, step one is to get AI to write the spec, right? So, let me go ahead and copy and paste this prompt here. And the prompt is to get AI to write a spec to create a professional headshot app.

Here's kind of how it works. And please include the requirements text stack and two milestones. And for the first milestone, I always like to set the UI first so that I can see the app update live for any subsequent milestones. Another best practice is I always like to include a link to the documentation that I'm using. In this case, Google's nano banana image API so that AI has the right context.

All right, let's go ahead and get AI to write the spec now and we'll come back once the spec is done. Okay, we're back and AI has created a spec. So, it's very important to review the spec, to audit it, to simplify it before you get AI to build anything. All right, so let's take a look. So, everything here looks pretty good.

Preview uploaded image before processing. I don't think that's necessary. Let's get rid of that. Three defined professional styles. Yep.

Integrate with Google's Gemini Nano Banana API. And uh let's just go ahead and paste in the past in the documentation again. Right. Let's go down side by side toggle. Yep.

Zoom functionality. We don't really need zoom functionality. So, let's get rid of that. Swipe slider comparison view. Again, I don't think we need that.

So, let's get rid of it. So, a lot of what I'm doing here is just like making the requirements simpler, right? Let's see. Mera preservation. Okay, this all looks pretty good.

Text stack front end. Okay, so this is actually pretty important because AI is actually really bad at installing these different libraries and especially for Tailwind, you want to use version three instead of version 4 because uh version 4 came out recently this year and AI hasn't really had enough context to actually know what's going on. So definitely try to uh satisfy you want to use version three. Everything else seems right. Let's go down here.

Let's keep going down and and then let's take a look at the milestone one, right? So milestone one is what we want to build. So it's going to build all this stuff. Install Tailwind. Let's say, you know, install Tailwind CSS version 3.

And let's make sure that it is not doing anything else that we don't want it to do. Okay. Yeah, I think Muscle One looks pretty pretty good. So now let's actually just get AI to build milestone one. Make sure you use Tailwind CSS version 3 and react with fight.

Now this stuff comes from experience cuz like you know I've experienced just a ton of bugs with this stuff. So I'm trying to avoid it by specifying this up front. And uh let's also say run localhost so I can test the app. Okay. Uh it's going to build milestone one now according to our spec and uh it's going to install a bunch of libraries and we'll come back once milestone one is done.

Okay. I actually forgot to do one more thing just to make sure that it actually builds according to the requirements we want. Let's go ahead and copy this image into here and just say you know build milestone one according to this image so that it has a frame of reference. And again, this image is also going to be available to you in the document that I have linked in the description. So, we'll come back and see if it does the right job.

We're back and despite our best efforts, it looks like there is an issue with Tailwind. All right. So, let's go ahead and copy and paste this whole thing into AI to get it to fix it and say, uh, remember to use Tailwind 3 and see if it can fix the problem. Now, this is a really annoying part of AI development. It's just not very good at understanding these libraries.

Hopefully, it fixes it this time. We'll come back uh once it's done. Okay, so now we have a somewhat working app. I don't know why it's not taking up this space, but let's try dragging an image in here. We'll drag a headshot here.

And there we go. We can pick between three different styles. Let's generate professional headsh shot. And of course, it doesn't work because we haven't hooked up Google's nano banana API. So first of all, let's try to fix this spacing issue, right?

So let's say the app is not taking up the full width. Can you fix? And here we go. And uh while it's doing this, let's look at milestone 2. So milestone 2, we want to hook up Google's API.

So there's a couple things we need to do. So first of all, we need to create three different AI prompts for these three different styles. And how do you create an AI prompt? What I like to do is just go to cloud or chatpt dragging a portrait style of image that you like. So in this case, this is a image that looks I think pretty great.

We just ask AI to write the prompt. So can you help me write an AI prompt to convert my photo into this headshot style? Right? And just say aim for 500 characters. Okay.

And uh AI is going to write the prompt for you. So let's take a look. All right. So this looks pretty good, but there's some details here that we don't really want. For example, we don't really want everyone to wear a dark suit.

This detail is too specific. I'm looking more for just the photos style than what the person should wear. Okay. So, it's going to edit the prompt and make it better. And um there we go.

And now let's go ahead and ask it to create a prompt file with AI prompts for the three different headshot styles that we want. Okay. And while we're doing this, let's also check to see if the app is now properly formatted. Let's restart. Doesn't look like it.

It looks like there's still a spacing error. So, we can continue to try to get to fix it like this. There's still a spacing error with the UI. So, you know, AI can do multiple tasks for you at the same time. You just keep giving a task and then it'll just add it to this to-do list.

And it looks like it's actually created the prompt. MD file. So, we have our prompts here. Looks great. But I actually have three different prompts prepped already that I want to use.

So, let's go ahead and just paste that in. Corporate classic. I actually have a prompt here called transform this photo into professional business headshot with clean even lighting, subject center, and so on and so forth. Create a professional. I have another prompt that I made.

And again, all these prompts are going to be available in that document that I'm going to link in the description. Okay, so let's uh let's get rid of this stuff. This is too much detail. Let's get rid of this stuff. And then primary prompt, let's put it here for creative professional.

And then similar for executive portrait, I have a prompt that I made as well. All right. So, let's put it into here. And there's a bunch of additional details here. I don't think we need all this stuff.

Let's get get rid of it. Okay. So, we now we have this prompt empty file with just our prompts. And again, I made these prompts just by taking images from the internet and asking AI to describe them. And I've also added uh make the subject look great and accurate to their original appearance at the bottom of all these prompts.

Very uh scientific, right? Okay. So, now we have all this stuff. Uh let's make sure everything is working properly. Okay.

So, let's double check our app. Yeah, I don't already know what's going with the spacing. We'll fix it at some point, but let's actually go ahead and get it to build milestone 2 now with the prompts in the prompt MD. And we're going to use Google's API, right? So, let me show you this.

So, you have to go to Google AI Studio. You go to the API key section, and you just create a new API key right here. And you got to pick a project. Let's say my first project. And just say create a new API key.

And it's going to create API key that you want to copy into cursor. Okay. So let's go ahead and copy this API key. And just say use this API key for Google API. Right?

And not only that, but just to give it even more context, let's go ahead and go search for Google image generation API. So this is the docs for Google image generation API. And uh you know earlier we pasted in the URL for docs, but let's be even more specific, right? Let's actually find the code for image to image generation. And here's like some sample code.

So, let's actually just go ahead and copy and paste this code. Here's some sample code for image to image generation from Google's API docs. All right, so we've given it a bunch of context here, right? We've given it the API key. We've given it the sample code from the documentation.

So, hopefully it can actually get to what we want in one shot. And we'll come back and see if it actually works. All right, we're back. Uh, that took about five minutes to generate. And now we have a beautiful looking app.

And let's just see if this actually works. So, I'm going to use my photo over here. Drag and drop it inside. And I'm going to say executive portrait and generate professional headsh shot. All right.

It is clearly not working. It's changing my photo into a white person. That is clearly not working, right? So, let's go ahead and just give it some feedback. The app is not using the actual API.

Let's paste a screenshot of what it looks looks like. And also the design is not quite right for the output. So let's actually get it to fix the output. So I'm going to copy this image again. Also I want to see both images side by side like this.

Okay. So, let's actually get it to see if it can fix this. And uh if it doesn't fix it, we'll try to troubleshoot further. All right, we're back and I want to show you guys the real hardship, right? The real troubleshooting.

So, it's still not generating the image that I want. And if you look at what it's done here, it says the API is configured to use Gemini 2.0 flash model. But if you look at the documentation here, the model is actually Gemini 2.5 flash image preview. So I don't know where it got Gemini 2.0 flash from. So let's say I use Gemini 2.5 flash image preview instead.

And by the way, the the image generation still isn't using my uploaded image. All right. So we're just giving it more feedback to get it to do it properly. And hopefully the third time here is a charm. Okay, we're back and uh here's the moment of truth.

So, I'm going to upload this image into our headshot app. Pick executive portrait and see what it comes up with. All right. So, there you go. So, it looks like it is actually converting my face.

It's making me look a bit different from what I actually look, but at least it's somewhat close to my original photo and it converted into an executive portrait. Uh, let's try again with something else. Let's try applying this and make it into a creative professional. So, I think this looks better. It's uh added a bunch of lighting in the background.

It's made me more in focus. Yeah, I think this looks great. So, we can hit download headshot here to download the headshot. Save it. And then I can upload it to my LinkedIn or share with my friends.

And just for fun, let's actually just do someone else. So, my friend Steve here is a pretty popular YouTube. And I'm just going to upload this thing here. And let's let's do executive portrait again cuz I really like the black and white style. All right.

So, here we go. So, it's it's done a lot better job with Steve, I have to say, than with me for executive portrait. For some reason, he's got his finger on his lip. I don't I don't know why, but uh yeah, I think now I can send this to Steve and have some fun. And let's just do one more.

Let's let's I have another friend name is Satchin. You probably know him. This is a pretty low resolution picture. So, let's put it here and let's make corporate classic instead and see what it comes up with. All right, looks great.

So, it's giving sachin a suit uh and a very clean shot, right? And it's much more higher resolution. So, now we build our app in these five steps. We asked AI to write the spec, right? Then we asked it to build the UI and actually also the backend server.

And then we created three prompts for hedgehog styles. So we created by just using images and then asking AI to write the prompt. Then we hooked up Google's nano banana API. And you know when you hook up a API it's very important to pay attention to what AI is doing. It was using the wrong model for example.

And we also gave it a bunch of context and sample code from the actual API documentation. Right? And then finally we fix any bugs. And surprisingly and you'll realize this a lot of the bugs with some of these apps actually just incentive the libraries and the stuff up front. So if you run into issues there like don't give up, right?

That is like the lame part, the boring part. And once you have those tailwind and blah blah blah all set up, then you can get into the fun part of actually building your app. So now that we have this, we can commit this app to GitHub and we can share it with our friends. And just keep in mind that each time you generate an image, it costs you probably like a few fractions of a cent, right? Because it does call the API and maybe there's some like free usage involved, but just keep that in mind.

So I wouldn't share this link publicly with everyone, but you know, you can use it to just like generate fun images for your friends. Okay, so that's it for today. And uh if you enjoy these tutorials, I have a lot more on cursor and clock code on my channel. So, please like and subscribe and I'll make more tutorials like this. Thank you so much for watching.
