---
title: "Gemini 3.1 + New AI Studio Is Here: Full Prototyping Tutorial in 18 Minutes"
guest: Peter Yang
publish_date: 2026-02-19
youtube_url: https://youtube.com/watch?v=2sLO9NYr8Rc
channel: Behind the Craft
keywords:
- ai-tools
- big-tech
- design
- coding
- ai
---

Hey everyone, Google just dropped Gemini 3.1 along with a huge update to Google AI Studio. Together, I think they make the best free AI prototyping and coding tool on the market. You know, there are many other great coding tools that cost $20, $200 a month, but I think Google just delivered the best bang for your buck with today's update. So, on top of all the improvements that come with Gemini 3.1, AI Studio is now full stack.

You can build apps with servers, databases, and even multiplayer directly in the tool. But for this tutorial, I want to focus on what I've actually been using AI Studio for over the past six months. Basically, I use it almost every day to prototype new features at work and it's completely transformed how I build products. Let's get started by first talking about the difference between waterfall and prototype first product development. So waterfall development is when you start with a spec, the designer makes design and then you hand everything off to engineering. By the time you get real customer feedback, you've already invested weeks in a product. And prototype first is

when you start with a prototype that you iterate on with your team and real users. And once you actually validate your product idea with the prototype, then you create the spec and design. The key difference is going prototype first helps you get to the truth of what users want much faster. So I've been a PM for over a decade and prototyping has completely transformed how I build products. And basically it comes down to these five steps. build the base template, prototype the feature, iterate with AI, collaborate with other people, stakeholders, actual real customers, and finally go from prototype to real product. So, I'm going

to walk you through all five of these steps with a real example. But first, let's take a look at what full stack Google AI Studio is capable of. All right, so here are some apps that I built. The first app that I built is a poker app where you can play poker with other AI bots. So, here we have a poker table and uh yeah, these two cards aren't that great, but let's just call it and let's see what the outcome is. All right, it looks like KC1. And the great thing

about the latest AI studio is you can also set up a multiplayer game and play with other real users. But let's go on. Here's the next app that I prototyped, a retro time travel booth. So, I've uploaded my picture here, and I can pick whether I want 80s, 90s, Y2K, or some of these other styles. Let's see which one should we pick. Why don't we pick the 80s? I love 80s music. Pick the

80s. Scroll down here and click initiate time jump. And it uses Nano Banana. And of course, AI Studio is default integrated with Nano Banana, so you don't have to paste in a bunch of API keys. You can just pick. And here I am in the 80s. And I actually do have one

of these jean jackets. I'm not so so sure about the hair though. All right. Another thing that uh I didn't build but someone else built that looks really impressive. If you can see a pattern here, I really like retro stuff is a center Bros. game. So here you can start

a game and it's it's like a Game Boy style platform game that looks like Mario except it's for Santa. I think it's pretty impressive, right? You can shoot, you can uh kill the snowman's. Yeah, there's some bugs here, but I intend to fork this game and improve it. Now, let's go back to what we're going to build today. So, for this tutorial, I want to be a little bit meta and prototype a new feature for Google AI Studio itself.

You know, I love prototyping AI Studio because it's fast, free, and integrates with Google APIs like Nano Bernat directly. However, I think this AI studio interface that you see here is still a little bit too busy. There are too many things calling for your attention, right? And just compare this UI with the codeex app from OpenAI, which is much more straightforward. You can make new projects. You can prompt Codex to start building stuff. There are

some suggestions, but overall, this is like a much more simplified UI. So, let's try to make Google AI Studio simple by following our five steps. Okay, so here's the AI Studio UI right now. There is a home screen where you can start a chat or start building an app. And there's playground which I don't really know what that means. And there's also a bill screen which is more focused on vibe coding apps. So to

start, let's just take some screenshots of this and replicate this UI in a prototype, right? And that exactly what I did here. So I have this uh AI studio project and all I did was I took some screenshots of the AI studio UI and I pasted in here. I say copy this UI and make it interactive. There are two screens home and build and then I basically replicated the UI and then I had to give it some more feedback on styling here. But anyway, here's the screens with the UI. And now we have a

home screen. And I've also prototyped the bill screen right here. Right? So this whole thing probably just took like five minutes. Now, here's the important part about step one. The thing is you want to save it as a template called let's say AI Studio template. And when

we actually want to build our new feature, you want to hit this remix button. And let's call it AI Studio simplified. Let's call it V2. and let's hit apply so that we can make a clone of our template. Now, why do this? Why not just continue prototyping on here? If you

make a template this way, you can easily start over again with what's live in your product today if you don't like the direction that your prototype is going. And the great thing is anyone can come visit this template and remix it and start prototyping off the same base. Okay, so step one is to just build the base template. Now let's move on to step two which is to prototype our new feature and simplify Google AI through this UX. So first we need to decide what to simplify. One lesson from this tutorial is that everything that you do you can do with AI's help. Right? So

what I did is I went to Gemini and I created a Gemini gem called Google AI Studio. And a Gemini gem is basically just an AI project like Chad and Claude except Google calls it a gem. And what I've done here is there's nothing in this gem except for a prompt. So the prompt is you are a senior product designer with over 15 years of experience and I want you to help me be my design partner. I will share screenshots and description of the UI and you will critique them and suggest specific improvements. Okay. Um how did

I come with this prompt? The trick is I basically just ask AI to come up with a prompt to be a senior product designer so we can work on simplifying UX together. and it came up with this very long prompt. So again, I did not manually write any of the stuff. This is just a prompt that AI came up with. All right, so now that we have this prompt, we can actually start talking to this gem that we made. Okay, so I've loaded

the gem and let's go back to our AI Studio template and let's go here and just copy these images over. Copy image, paste here. And then let's copy the bill screen too. All right. And uh let's say I want to simplify this Google AI studio UI so that we can focus on making it a prototyping and vibe coding tool. Give me your top three suggestions to simplify this. All right.

And let's see what uh Gemini comes up with. So you can see here it's loading our custom prompt and here's his critique. So it says collapse the feature gallery into unifi command bar pivot from home to active project workspace. And it has a bunch of suggestions here. Okay. And of course in this step you also do some research about what users actually want. So, uh, for example,

right here, I found this thread about people giving feedback about Google AI Studio and the number one feedback point is they want to have folders where they can set up their project to add files and so on so forth. Okay, so these are some pretty good suggestions, but let's apply our human taste and opinions to this, right? So let's go back to the AI studio screen again and let's actually try to apply my human taste to try to make this more simpler. So I've actually pre-written a prompt here and let's walk through the prompt. Right? So basically I want to redesign interface to be much simpler. Number one, I don't understand

why there is a home screen and a bill screen that's separate. If the primary goal of this tool is to help people to prototype and to vibe apps, I think the bill screen should just be the default screen. Number two, there's like a lot of stuff on the sidebar. Playground, dashboard, documentation, so on so forth. I think we can simplify all this by just having a list of projects that I worked on and a new project button. And here are some examples of projects. And

uh on the main screen, I was trying to do a lot of different things at once. For example, this jump back in thing, I don't think it's really necessary if all my projects are already listed here, right? Um and I think this quick start thing is interesting. But I think it can be put into like documentation or the API key and somewhere else. So what I think is that the main screen should just have a single chat box that says what do you want to build today? And on this chat box there should be a way to pick the model toggle between plan mode and build mode which a lot of other AI coding tools have. I have a button to

add photos and of course one of the main draws of AI studio is that you can integrate natively with Google APIs like Nano Banana. So there should be a button in the chat box to actually add different APIs to your app. Okay, so that is the prompt that we made. And again, you can work with the gem to come up with this or go back and forth with AI to figure this out. But let's go ahead and copy and paste this prompt into our remixed AI Studio template. Let's paste it here. And I'm just going

to submit this prompt and see if it can simplify this UI in one shot. Okay, we're back. So that took about 141 seconds and now we have this much simpler UI uh where we just have one screen. There's a project list right here. You can make a new project and you can pick the model and you can pick between plan and build mode. You can add and check different Google APIs to include in your app. Uh and there's some

other buttons here. Now the next step is to iterate with AI to make your feature better, right? because AI usually doesn't get it right in one shot. So, for example, one thing I don't really like with this is the model picker is up top and so is plan build mode instead of part of the chat box. So, let's say uh move the model picker and plan versus build options to be part of the chat box like the Google API selector. All right, let's put that in first. And uh let's see what it comes up

with. Okay, so it looks like it's moved the things to the chat box like asue. So now we have a model pick here and uh plan and build is right here. And um yeah, I think this looks a lot better than before. Now let's add a new feature actually. So, one thing that I like about some of the other AI coding tools like Lovable is it's a focus chat box, but if you scroll down, there's actually a bunch of templates and stuff that you can discover to give you inspiration, but this stuff doesn't crowd the UI. That's

just a focus chat box. So, let's actually add these templates into our AI Studio prototype, too. Let me go back here and let me paste a screenshot of the lovable templates. And here's the prompt that I'm going to give it. So, the prompt is add inspirational shelf similar to Lovable that fades into view as I scroll down with some showcase prompts for beautiful websites, games, and more. It should look amazing and even more beautiful than an attached image, right? Separate

a bit from the main chat box to keep it the above the full section mostly clear. And then maybe you can even organize it by Google API because again, that's one of the main differentiators of AI Studio. you can find some relevant examples for Nano Banana, Google Maps and so on. All right, let's submit this and see what it comes up with. Okay, so let's take a look now at what AI studio has made. So we still have our chat box at top, but now you can see down here there's explore ideas thing, right? And

if you scroll down, yeah, there's a bunch of app ideas for Nano Banana, for maps API, for voice API, and more. And for beginner users, this gives them some inspiration and templates that they can start remixing, right? You know, we can keep iterating like this. We can keep making our product better. But when it comes to prototyping, don't worry about making it perfect. Just get it to a point where you feel comfortable showing your prototype to other stakeholders and real users. And that brings me to step

four, which is to collaborate with others. And this is where the magic really happens. The great thing about prototyping is that anyone can improve your prototype. Now that we have a decent prototype, we can share it with stakeholders. So let's go ahead and come back here. And here you can see a share button. And just like a Google doc or

you know Google Drive file, you can share it with specific stakeholders in your team. So for example, you can send this link to a designer and let them clone it and iterate on it directly or with you. Right? Another thing is you can test it with real users. So, I went ahead and actually tweeted this out. I think the Google AI Studio UX is too busy, so I made it simpler. And here's a

prototype that I made. And you can see here there's a bunch of feedback down here. Putting Logan on the spot. Sorry, Logan. And yeah, people love it. Some people think it's much better, but you know, if you scroll down, some people are also haters and think uh it's overly simplified. [gasps and laughter] So,

yeah, the point is you can get user feedback. And of course, you can just go ahead and ask AI to summarize all this feedback and give you more suggestions to improve your prototype. Finally, there's so many PMs out there who are presenting these slide decks and long Google docs to leadership during product reviews. And I just think this stuff is not as efficient as just showing them a prototype. So during a product review, just pull up this prototype, send them a link via Slack to your VPs and let them play with it. In fact, you don't have to wait for the review at all. Like one of

my pet peeves is just waiting weeks and months for some executive to review my product. So just send this prototype to them through a Slack message. And VPs are extremely busy. But I found that they always make time to play with prototypes because it's just way more fun than reading documents. And overall, I find prototypes generate much better product feedback than any slide deck or document because they make things concrete. So the last step is to uh turn this prototype into a real product. Iterating

on the prototype with both internal stakeholders and users will tell you if this product idea is great or is actually a bad idea, right? And it will tell you this before you actually build anything. So you can again get to the truth much faster. And let's assume that people love this UI like I got some signal here from my tweet. So now the next step is to move forward and write a onepage spec that outlines the user problem, the goals and the solution. Link the prototype as your solution. In

the spec, maybe create a design to iron out the edge cases to make it a little bit more polished that this UI here. And finally to build a production app and again with Google AI Studios full stack update you can now start building directly in this tool with server database and other API integrations. The key difference here is that you've already validated your product through this prototype with real users before investing heavily in specs designs and engineering time and you know that makes all the difference in terms of speed of iteration. Okay, so to recap, here are five steps to practice prototype first product development. Number one, build a base template, replicate your existing product and save the template for your team. Number two, prototyped the new feature. You can create a AI project or

a Gemini gem and just talk to it to come up with a great prompt to add your new feature and put that prompt into AI Studio. Of course, it's not going to get it perfect in one shot. So you have to iterate with AI. Go back and forth with it. Give it feedback. Get it to a point where you feel comfortable sharing it with other people. And that's step four,

which is collaborating with others including stakeholders and most importantly with real users. Maybe have calls with users, show them the prototype, let them play with it. And you can even iterate on the prototype in between your customer calls. And last but not least, turn your prototype into a real product after you've already validated the idea. To summarize, prototype first product development in my opinion is a must have skill in the AI era. I now spend more time building prototypes and getting excited with my team instead of tweaking words in Google Docs. And just remember, code is now

free. Code is now easier to create than any kind of slide deck, doc, or intermediate artifact. So definitely start by prototyping first. All right. This is probably the most practical tutorial I think in terms of actually changing your tech job, whether you're a PM or engineer. Prototype first and I promise you won't regret it. And uh like

and subscribe to this video if you enjoyed it. And I'll see you next time. Thank you.
