---
title: "The CORRECT Way to Prototype Apps with AI in 38 Min | Xinran Ma"
guest: Xinran Ma
publish_date: 2025-11-30
youtube_url: https://youtube.com/watch?v=QgvQbcPmioE
channel: Behind the Craft
keywords:
- coding
- design
- ai
- ai-tools
- product-management
---

After I've been vi coding for a while, I've noticed some gaps that is particularly around design explorations. There is a feature in magic patterns which is canvas. You get to see all the design explorations that you had. You just throw it on a whiteboard. What happens if I like one component from prototype one and another component from prototype 2?

We can easily just drag and drop here and then delete this. Do you have any prompts to try to make it look less like, you know, purple AI slop? use reverse prompting. I provide CHBT several typical screens and I ask it to generate a custom instruction just for the design system foundation component library paired with a custom instruction can Okay, welcome everyone. My guest today is Shinan uh founder of design with AI newsletter with almost 20,000 subscribers and instructor of a very popular course named AI for product designers.

Now, Shamra is going to show us exactly how to design great apps using AI by walking through practical uh five practical vibe design tips. So, welcome sir. Hello. Hi, Peter. Hi, everyone.

Awesome. So, yeah, you have this awesome course and why don't we get right into it. Uh maybe you can start by talking about some of the drawbacks of using VIP coding tools to design and also what these five tips are. Sure, sounds good. Um I actually I've draw something in advance on a board.

So, maybe I can share my screen. so it's easier for everyone to visualize it. Yeah, go for it. So before I talk about quote unquote VIP designing, I wanted to start with VIP coding first because it's such a popular concept and uh a very popular workflow that both engineers and non-engineers are playing with VIP coding. And no matter which tool that you're using for VIP coding, whether it's loverable vzero or cursor club code, typically it's following something like this, which is a linear path from prompt to iteration and then you ask a follow-up prompt and then you come up with another iteration.

Then you ask another follow-up prompt, then it gets to another iteration. More or less like that, which is great. It's very refreshing and empowering. But as a product designer after I've been vi coding for a while I've noticed some gaps that is particularly around design explorations. So I was wondering if there's a way that we can still honor the strengths of vibe coding workflows but giving some room for design ideation or design exploration and that would be great for designers and for anyone who want to explore the designs with those vibe coding tools and that's why I would like to share some of the vibe designing techniques and I'll start with the five gaps.

that I noticed. By the way, there are more gaps if you want to think from a broader perspective, but for the sake of time today, I'm going only going to tap into the five gaps here, which are more around design exploration, I would say. So, the first gap is some clarity up front that can go a long way. Like Peter, you probably have explored a lot in vibe coding. So you may know that the very first prompt matters.

If you provide a confusing prompt, chances are you have to spend a lot of tokens to cost correct later. Worse yet, you may, you know, never get to the direction that you want just because of you start with a confusing starting point and then it just keep going circles from there. So that's why there's a there is a gap at the very beginning before you even feed into the very first prompt to any of the AI prototyping tools out there. Uh the second gap is the need to better keep track of the iterations. The third gap the need for divergent thinking the need to mix match mix match ideas and the need to revise the design manually.

This is just an overview and I I can go through it one by one. So Peter shall we just dive into them? Uh yeah I mean let's let's start. Number one, I I definitely echo with number one. If you just ask AI to like design like build build a gift giving app, like it's not going to give you what you want.

Like you have to plan first, right? So yeah, why don't we start with addressing gap number one. Sounds good. All right. So for the first gap, I believe that some clarity up front that can go a long way.

It doesn't mean that I wanted to defeat uh to go against the strength of vibe coding because vibe coding is meant to be fun. It meant to go with the flow, right? But I try to find, you know, efficient ways to help us gain some clarity before we providing the very first prompt. Like for example, who am I designing this product for and what are their needs? What are they are what are they trying to achieve and what user flow we would like to focus on that is addressing the most important problem from the users and it also can help us focused because you know if we provide such a broad prompt the AI tool may consume a lot of tokens spending a lot of time but the result is less ideal just because it spreads out too thin so That's those are some typical points that I would like to get clarifi get clarity before um I provide a prompt and I can do that with CHBT with claude I also have come up with multiple custom GPTs forelves so I don't have to start from scratch and in terms of which GPT that I would like to use really depends on my use cases like sometimes I wanted to start with a blue sky idea so that I may use one GBT that I built that is fit for generating a blue sky prototype rapidly and sometimes I have a lot of thoughts and I don't mind spending more time interacting with GPT then I may use another GPT that I've built.

Do you want to show us uh maybe like uh the giftgiving one or like another example of talking to GBT? Yeah, sure. Sure. I can I can showcase one of the GBT that I've built to help me clarify the prompt before I go into those AI prototyping tools. So for this GPT, it's best fit for come come up with a blue sky prototype in a very rapid amount of time.

So let's get started. Click here to start, which is pretty straightforward. Um, you know, if we have more time here, we can actually do something more interactive. But just for the sake of time, let let me just, you know, put in some of the preset u answers. But I've done this multiple times with a live audience.

You can always, you know, provide the goal whatever that you have. All right. The second question from that GBT is that who are the intended user of your product? Um, again for the sake of time, I'm just like picking one of the examples as opposed to um, you know, providing something from scratch. The third question, what platform is your product for?

And there are different platforms or you know break points whatever you call it. But the whole idea is to make it more focused at the beginning because once I get a sense of you know this is the prototype that I wanted to go deeper into then I can easily scale it up to different different platforms. But for the very beginning, I always like to, you know, make it as focused as possible just to create a prototype to begin with. Um, so I can just type any of the number here. Um, there is a recap of what I have provided and now it's some of the key user flows that will address the particular user goal that I mentioned earlier.

And I can say something like one and two or maybe one and a bit of three or two and four. It really depends. So, you know, how about just like one and a bit of two or three, right? Doesn't really matter. I like how it comes up with the user like the use cases for for you, right?

Brainstorm some. Yeah. Yeah. Thank you. All right.

So it generated a preliminary spec just for AI prototyping tools like for generating a prototype. It's not a PRD in the you know conventional fashion right it's just like a spec for for the for a prototype you get to see the key components interactions and I always recommend people to double check this you know make revisions if they want um if yes if no so I can always ask for some revisions um let's say yes let's say we're happy with with this preview and I just say yes as you can see every step. Um, I made it very simple. So, I don't have to type a lot of, you know, text. I can just simply type in a number or like a like a couple of words and that's good enough.

And all of those steps are what I put in the custom instruction in the back end. Got it. All right. Okay. So, now it generated a spec.

Yeah. Nice. Mhm. Right. I made it into a code block.

So, you can just easily copy code. That's it. You don't have to write the very first line generating a prototype. It's everything is bundled within the code block and I can go to any of the prototyping tools out there like I can paste it in loable I can paste it in cloud.ai you know any any prototyping tools that I I want to and this GPT is uh like anyone can find this GPT or it's chat GP right? Yeah it's semi private I didn't publish but I can share with you after this.

Okay. Yeah. Yeah. Maybe we can like do like a sim simpler prompt for like maybe a simpler prompt version of this or something. Yeah.

Sure. Sure. Sure. I can share it out. Okay.

Yes. And uh you know I don't want to wait there but as you can tell this is the idea of this. Yeah. This is great because uh I think a lot of I think a lot of beginners uh with this stuff they just like typing like a oneliner like like you know hey build build me a expense tracking app and and then and then they wonder why it doesn't look like what they want. So, I like how this like, you know, has discipline walking you through the actual steps to design the user flows, the target audience, and so on.

Yeah, this is great. Thank you. This episode is brought to you by Reforge Build. You know, I took Reforge's first growth class 5 years ago, so I'm really excited to see Brian and the team expand into AI prototyping. Most prototyping tools make you start from scratch each time and produce the same purple-looking AI slop.

Reforge Build learns from your design guidelines to generate prototypes that actually look like your product. You can even generate multiple variants to compare approaches side by side and collaborate with your team directly in the product. Reforge understands how product teams actually prototype better than most other companies. So check out their new product at reforge.com/peter. Use the code build for 1 month free of premium.

That's reforge.com/peter. Now back to our episode. All right. So so now so now we use this GPT or prompt to have the first version. So now maybe let's let's move on to the second gap which is uh being able to iterate and tracking your iterations.

All right. Yeah. So the second gap is keeping track of iterations. For example, when we are designing or when when we were when we were exploring the designs, chances are it's not following a linear process. For example, let's say we go down a path and at this point we're like hitting a wall.

maybe wanted to go back to the starting point or maybe we wanted to explore a little bit further towards that direction and for let's say if we were to go back to the starting point maybe we wanted to explore another direction or maybe another direction. So there's a lot of like uncertainties around here and at one point we were like okay this option this option and this option are the ones with potential but it's very hard to do this kind of things in tools like loverable or claude.ai AI or even cloud code, right? It doesn't really design that way. How I solve this is that I like to use a tool called magic patterns. There is a feature in magic patterns which is canvas.

It is one of the few AI tools that have this kind of feature and I really like it. So I can give you an example if you're up for it. Yeah. All right. So this is a very particular canvas that I was working in.

uh I can spend more time explaining what I was trying to explore which is based on a very like based on the real world scenario but I I don't want to go too deep into the problem I was trying to solve but just to give you a sense of what it looks like this is the original screen and those are the different design explorations about the right rail uh panel as you can see so there are different design explorations um that I had with a right rail. It doesn't mean that every option is valid, but I can always get a lot of inspiration from some of them. So, I just put them side by side. And you know, on the second row, this is the different design explorations uh for the second step of the user flow as you can see. And by the way, so all the things that you've seen here is actually interactive.

It's not just a static design. Um it's interactive. You can play with it. So basically magic patterns let you generate like five different prototypes at once for different explorations. Is that by default it can generate four with a comment but you can always refresh it so that it will generate four more unique design options.

Got it. And in terms of I will mention that in the next step in a little bit about how I actually you know prompted. Uh but for the canvas feature like yes you get to see all the design explorations that you had. You just throw it on the on the whiteboard. That's great.

probably probably cost them a lot of money to generate the stuff but yeah it's good for the designers right I believe there is there are different ways to to mitigate that uh in the back end but again like each of them you can open the editor so it's like a chat window and you can just like go deep into this direction asking more prompts and make more revisions and once you're happy with the updates you can go back to the canvas it will automatically reflect the new updates within this uh preview window. So they are they are stat they are not static designs they are preview windows of a of a chat interface. Okay. Yeah this this is great. So then you can iterate on all five and I I I think you can also share this with other people right for them to take a look.

Yes. Yes. You can share with other people and other people can play on this canvas. can go deep into one of the option and ask you know followup prompts as well. Okay.

So, so how do you uh like yeah h how do you actually generate um like all five signs like like how do you get this divergent view like is is there like a prompt that you use or just like one two three four five and here's like the five different cases. Yeah, great question. That actually naturally leads to this the next gap that I'm going to talk about. So which is go which is going hand inhand with the previous gap that is the need for divergent thinking because this kind of mindset or exploration mental model is very common in design explorations is that we wanted to brainstorm different design options and show them next to each other and then we keep brainstorming from one design option. And it's also very tricky to do this in, you know, in many of the vibe coding tools quote unquote out there.

And for magic patterns, I like to use magic patterns for this kind of task as well in especially in design brainstorming. And I can give you an example. Mhm. So in another live talk the other day there are were some students and we were having some design brainstorming and one of the project that someone was working on is called a gift sharing app and this is like the you know what it looks like you know it's like a it's like a simple prototype and how I did that is that I exactly used the GPT that I shared earlier and I generated a prompt and then I I fed it into magic patterns and it generate a prototype for me and now and then it's a matter of design exploration right so let's go back to uh let's go back to where it was let's say the the main page so I'm going to refresh the browser to go back to the previous state you can do something as simple as generic as slash inspiration so which is a is a comment in magic patterns and you don't to have to type anything. It will generate four design options by default.

And sometimes this works and sometimes you know some people like this and some people don't like it. Like this in the sense that it's like so simple like you can generate four design options but some people want to have more provide more context which you can also do it here. You can be more specific like you know I can even select a let's say component here right and I can add to chat. So I can narrow down the scope. Let me let me zoom out zoom in a little bit so other people can see it.

So I can specifically narrow down the context and then I can type in the slash inspiration where will generate four design options by default and I can describe the type of changes that I want to make. So for example um can you make uh some options that whatever that is which is whe whether it's more accessible or maybe it's more compact in terms of spacing exactly etc. Yeah this is awesome. I you know I I I just did a tier ranking of top AI coding tools and I wish I play with magic patterns before cuz it it does seem like very designed for prototyping and exploration and a lot of the other tools are not. So yeah, this is great.

Yeah, I I do like it. And not to mention there is also another feature called export to Figma. So you can actually convert the designs and you know put it into to Figma. And by the way for those design options as you can see it's very easy to toggle from one to the other. Um like for example this is one type of idea for the and uh this is another type of idea which is accordion right obviously and this idea is a questionnaire.

So every idea has pros and cons right some ideas is more you know space saving but it involves more steps. So it really depends on, you know, which which idea I'm I'm into. Yeah. I think the difference between this tool and some of the other tools is like I feel like, you know, the other tools like Lovable and some of these other tools are just built for actually building a simple app, but I feel like this tool is more for like designers and PMs to explore different prototypes and then maybe you continue to build one of it or like you just go build it some somewhere else, right? like like that that whole like exploration stage is kind of like missing from some of the more popular tools, right?

Yeah. And I you can theoretically do that in those tools, but I tried different ways. They are just not designed for this like Yeah. You have to go back to checkpoint and stuff. It's like very annoying, right?

Yeah. Right. You can fork. You can make multiple forks. Okay.

You know, you can have a sort like a overlay components that allows you to switch from option to option, but it's not designed beauty like this. Yeah. Okay. This is awesome. But but but let me ask this.

What happens if I like uh like one component from prototype one and another component from prototype two? That's a that's a great question. It's also I think that actually leads to the next gap I don't need to talk about. So great question. So if I go to go back to the whiteboard that I did, there's another gap which is mix matching ideas, right?

Sometimes we want we like design option one, but I wish it had a little bit of two and some parts of three. I can do that in u I can do that in magic patterns actually. So just to say can you can we use option three like it has a option name right with a bit of this I can do that but there's another tool called subframe which also provides an interesting experience that I can show you. So subframe if there is a spectrum I would say magic patterns the mental model of magic patterns is closer to lovable like it's very easy for you to understand like it's closer to lovable whereas for subframe is closer to Figma if I were to have a spectrum of all those tools in terms of mental model so like for example let's say if this is the designer that I have I can you know import from Figma or I can design it from scratch in subframe and I can make a changes of that. Uh for the sake of time I'm just like just doing something very generic.

But again we can always provide more specific instructions once we have more time after this talk. But let me try to generate something uh to as a quick demo. Well why is generating like what what is the difference between subframe and magic patterns? It's just like um yeah what what's the key difference? I think the key difference is that if you are a product manager then I would say like magic patents is very easy for you to get on board because the mental model is similar with lovable like it's a AI prototyping tools and you ask different kinds of text based questions and for subframe it's just a different it's just a different mental model it feels like Figma with some of the integrations like you can switch to code very easily and you can switch to a ask AI mode I would say but again I don't know Peter if you've used the tool called wizard which was acquired by mural this April um I heard about it I haven't used it yeah it feel like it feels like wizard in many ways okay interesting okay so it's generating all four mocks and then maybe afterwards like so so I guess the difference is like you can maybe like drag and drop stuff or like make more manual edits Yeah, true, true.

If you go to um I will cover that in a little bit as well because in the design mode which is like the typical manual adding mode menu editing mode, you can drag and drop components on the board and you can change spacings just like just like Figma. I think my prompt is too generic that's why you know it's like generating different things. But again uh let's say if we are interested in this one so we can apply design so that this becomes the base of things and let's say if we go to another design option. Let's see if there's something interesting there. I'm trying to find some of the interesting patterns.

So let's say if we like this components right from this design we can easily just drag and drop here. Oh that's awesome. And then and then delete this. And let's say I'm there's anything fun. I like this photo better.

I can just drag and drop here and delete it. And then I can go always go back to the design mode which I will talk about right now. Yeah. So basically when you're doing this you're actually drag and dropping code or I I don't really know how it works behind the scenes. Yeah.

I'm drag drag and dropping the components which is based on code. Got it. Got it. Okay. All right.

Yeah. This is awesome. So So okay. So how about now I want to go to design mode and like make some manual tweak tweaks or or something right this is also a common need which is the gap that I wanted to talk about here is that sometimes we want to revise the design manually let's say I just wanted to move this around and then I wanted to go back to the AI mode quote unquote right for magic patterns it has a way for you to uh which is also quite rare in those AI prototype typing tools for you to export a design to Figma. And by the way, when we export to Figma, of course, we're going to lose some of the interactivity, which is expected because of the different different mental model between those AI prototyping tools which are code- based compared to Fakemon.

Anyway, but but again, this is quite helpful and I've been using this a lot in my day-to-day. But regarding subframe, it also has a nice feature that can let you toggle between ask AI and design very easily. So like in the in the manual editing mode, let's say here, you know, I can move things around. I can change the spacing, I can change the padding, and I can be more specific with the padding. And then I can go back to ask AI mode to ask questions to, you know, based leveraging AI.

And then I go back to design mode is, you know, I can just like switch back and forth. Wow, that's that's pretty awesome. Yeah, because design mode does look a lot like Figma. Yeah, it's pretty awesome indeed. It has like, you know, this is a prototype layer, but I don't think it's relevant to today's topic.

But again, you know, switching to code design and AI mode, they are integrated as opposed to isolated experience. Yeah. Yeah, because uh with magic patterns, even if you can export to Figma, you export to Figma and then you make some changes in Figma and then you got to import that stuff back in, right? Like it's kind of like a pain to to do all stuff. I would say it depends like it's there's pros and cons.

Like for subframe, you have to stay within like subframe. Like if you're not comfortable with the the environment with subframe then this could be tricky because it lets you stay within one platform such as wizard like you basically stay in one platform as opposed to magic patterns again like when I'm using magic patterns often time I really enjoyed it in the design exploration phase so I don't mind you know exporting to Figma for the final touch if I need to. Got it. Got it. Yeah.

Got it. This is awesome. Yeah. It's like having it's having like a a junior designer like do a bunch of explorations for you. Yeah.

Right. And I always again the things I I've shown is very generic because I just wanted to keep it short but you can always try very specific prompt which I tried before as well in the sense that you know I just wanted I just wish it it was more compact or I want it to be more interactive. You can ask more specific prompts here to get you a better like more relevant design inspirations. Do you have any prompts to like I always ask this to designers that I interview. Do you have any prompts to try to make it look less like you know purple AI slop like even this one has like it just looks looks like all the AI stuff looks very similar you know like do you have any tips to make it look a little bit more unique?

Oh unique that's a that's a great question. There are there are different ways for me to approach it. So uh first of all if I were in magic patterns there are different presets libraries that will connect to different component libraries. So which can be it already has a like a unique styling based on Oh wow. Okay.

Like for example let's say Uber um so here is a preset right like by default it's it's based on base. If I were to go to wireframe, then it will generate a mid-fraid or low fidelity styling for me. If I were to put it on a Y, let's say if we were to go to Uber, right? So, I'm going to show you behind the scene what's what's what it looks like. So, the name of Uber and this default prompt, it's like the custom instruction for include code.

So, this is like, you know, it shows you the color, the hierarchy, the spacing, and grid all those. So if you go if you were to go to a design system this is like the foundation the part of the foundation right all those structure and and this is something that you came up with or is this like came with magic patterns Uber one this one I did it by myself okay yeah so what I did is I often like to use reverse prompting it's basically I provide I provide CHBT several typical screens of Uber and I ask it to generate a custom instruction ction just for the design system foundation such as with color, typography and spacing for example. So that's one part of the equation. Another part of the equation is the components but it's hard to describe components here. That's why I ask it to connect to a library.

So if I were to go to library Uber, those are the typical uh components that I fed into magic patterns. Uh this is code that you fit into magic patterns like component. It's like I how to say I recreate a proxy of the component libraries that I I want to have. Is that something that chatb can generate too or you have to make it yourself? You got to make it right.

It's very straightforward. Like what I did here is like for example if you have a let's say story book of a design system I would just take snapshots of different states of the button and I'll just paste it here and it will automatically generate open up a code editor like this um and everything is reusable. So in other words in the future let's say if I'm designing I can just say use um sorry use button uh red button and like input field for example do I have input probably not okay got it so I can say something like this but since I've already you know included as part of the the library connected to the library I don't have to manually call them out. It will just automatically reuse those components by default. Okay, summarize.

So, number one, you can uh get the the preset by just like pasting some screenshots of Uber and then telling AI to come up with like the the fonts and like the, you know, like the colors and stuff, right? Like you can get AI to help you generate that stuff. And then it sounds like you can also build individual components like buttons and stuff through this app, right? So for the components part, magic patterns can assist you to build a component library. Got it.

And component library is just like building blocks like Legos, but it does not have a principle to guide them how to place things. And that's that's where the uh the custom instruction part come in handy because you know it's like component library paired with a custom instruction can give me the best result. Th this is awesome. Yeah, this is awesome. Uh may I can bribe you to share a little prompt uh in the description about how to come up with like the the custom instructions.

Yeah, but you know we can share that afterwards. Sure. Sure. Sure. And uh I do that even for cloud code as well because cloud code you know like I know you use cloud code it's just like the custom instruction in cloud code that you come up with right you probably use cgbt for help to generate something like that.

Got it. Okay. So cloud code you have like a some sort of like a temp template CS like template empty or some some sort of file that has like all the instructions right for for the style. Yeah. Right.

I have a I have a lot of them. Yes. I have a lot. Okay. Like different markdown files.

Okay. This is awesome. Okay. Cool. Why don't we quickly recap the five gaps and then Yeah, sure.

I can start. Uh the first gap is we need some clarity up front that can help us go a long way in terms of prompting because if the very first prompt is confusing or it's too generic, then it's hard for you or it's tricky for you to explore from there. That's why uh I used CH GBT and some personal GBTs for me to generate a effective prompt and uh help me you know gain more clarity around what I really want around things like users or project goals, users, project goals, use cases. Yeah, like that kind of stuff. Yeah, got it.

Use cases like user flows like what I would like to focus on from the beginning. Okay. Yeah. The second gap is keeping track of the iterations and I was leveraging the canvas feature in magic patterns and there are only very few tools that have this feature as part of the AI prototyping experience uh that I appreciate. The gap three is divergent thinking, right?

We often want to explore different options based on what I want at the same time. And I was leveraging the inspiration command in magic patterns to do something like this. And again, I can always refresh it like rerun it to generate four four more unique design options for me if I'm not happy with the the first four. Gap four is the need to mix match ideas which I did a demo in subframe that you get to grab a component from one option and plug into another option. Gap five is the need to revise design manually and often times we wanted to switch back to the to the AI mode.

is basically switching from the AI mode to design mode. And I did a quick demo in subframe. And if I want to move from magic patterns to subframe like uh like let's say I build a little prototype in magic patterns and I want to like move to subframe to mix and match stuff like uh how how to just export the code and then import it in subframe. That's a great question. You can try it.

Sometimes works but sometimes not. So okay like theoretically uh I don't think it's going to be good experience if you wanted to do that just because like theoretically you can download your code from magic patterns and throw it into substax AI mode or you can because in subframe there's a feature that you can import Figma but what it essentially is doing you know as you can tell it's essentially taking a snapshot of Figma and rebuild it in subframe. So in this case theoretically you can take a snapshot of magic patterns and paste it here but I've never tried that. I try not to convolute those kind of workflows but but you can try it out if you're interested. Okay.

So your tip is to uh you know either like I I guess try both magic patterns and subframe and just pick the one that you want. That's a great question. It really depends on my use cases. Okay. Uh again I use magic patterns a lot more often than subframe.

Uh particularly because you know I'm a product designer and often time I put an emphasis on design explorations and that's something that I I need the most. Uh again for I still use a lot Figma. So that's why like magic patterns it feels like a very simple extension of Figma that I can always you know go back to Figma you know take some inspiration and go back to Figma so that it doesn't really convert with my workflows in Figma but I can imagine maybe there are some smaller teams that I wanted to do everything in subframe but that's a different story. Got it. Okay that makes sense.

All right man this is this is super this is super useful. I also liked how we went on a tangent about, you know, getting the right components and presets in place. I think that's great. Um Um So, so Shinra, if people want to learn more from you, like where can people find you? They can always connect with me on LinkedIn, which I'm quite active on, and they can also go to uh designwithai.co.

It's also named designwithi stack. they can. So I write practical newsletters every week in terms of AI's application in design that people can check out. Yeah, this is awesome. Uh why why the horse?

Do you do you know? You probably even know. You don't know. Anyway, I've never shared with others. Uh but it's pretty obvious.

It's my last name, of course. Oh. Oh, because your your your Chinese name. Yeah. Ma, right?

Yeah. Yeah. Okay. Got it. Okay.

Got it. Okay. That that makes sense. Yeah. Okay, cool, man.

All right. Well, I'll I'll put the link to all all the resources that we talked about in the in the video description and and yeah, this is awesome. I I definitely learn a lot. Sounds good. All right.

Thanks so much for your time. All right. Thank you.
