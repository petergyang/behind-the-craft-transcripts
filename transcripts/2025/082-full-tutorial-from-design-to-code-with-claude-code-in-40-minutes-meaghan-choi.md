---
title: "Full Tutorial: From Design to Code with Claude Code in 40 Minutes | Meaghan Choi"
guest: Meaghan Choi
publish_date: 2025-09-21
youtube_url: https://youtube.com/watch?v=1-x-QzNjFHQ
channel: Behind the Craft
keywords:
- ai
- product-management
- coding
- design
- leadership
---

I myself probably spend an equal amount of time now in quad code as I do in Figma. Instead of handing off a Figma mock to an engineer, I'll hand them like a draft PR that I have with like a description of what I was trying to do. So, right away I say like from my eye, I can tell, oh, this doesn't look exactly how the app I designed did, right? There's all these little details. And so, this is actually where I spend most of my time in cloud code.

Last 10% of polish. At Anthropic, anyone can code and it's such a collaborative environment that I feel like our roles don't matter. you have like another slide uh where you have this like whole flow diagram. Can you walk through this one too? Yeah, definitely.

So, okay, welcome everyone. My guest today is Megan uh as a design lead for clock code. Megan not only designs features but also ships to prod on a regular basis and I'm really excited to talk to her about how AI can help designers work faster and get her to demo her exact workflow to go from design to prototype. So, welcome Megan. Thanks so much.

I'm super excited to be here and yeah, just really excited to talk about how I use cloud code myself. Yeah. All right. So, um, so I guess let's start with this. Um, how does it feel to be finally a designer who ships to prod on a regular basis?

Honestly, it feels a little terrifying and simultaneously very magical. I think, you know, over the years, I've always really just been interested in development, but it felt like at the time, especially when I started my career, you really need to hone your craft in either design or either development. It was just hard to bridge the gap into between both unless you're a really special unicorn. And then just in the past, I'd say like 5 years, it just became so much easier to code. and all those like little details that I always felt I couldn't really ask my engineers cuz it'd be a P2 or it would take me a really long time to set up and fix, I can just ship them and have them.

And so like that really polished product that you always want is just there and ready for you. Uh it's pretty amazing. Yeah, exactly. I always feel bad asking my engineers be like, "Hey, can you tweak like five different copies like make this pixel change or something?" And and yeah, now you can just do it yourself, right? Mhm.

Exactly. And sometimes, you know, I think when you're actually porting designs or something that you have in this idea into prod and then you actually see it, you're like, "Oh, that actually didn't look how I thought I would." And then you feel even worse asking them to change it back or changing again. And this just gives you the power to do it all yourself. That's awesome. That's awesome.

So, maybe uh you can walk through like the entire design process and and where like AI and cloud code can help. Definitely. So I would say for me I actually have a slide for this I can share which is really useful. Let me share my screen. Yeah.

Right now there's a few different ways my workflow has changed. I would say a big one that I have is kind of I would bucket it into three big workflows that I now use cloud code for specifically. Uh this first one is one that I think folks who are maybe less technical reach for the most often. uh and it's one that you can do even in cloud AI today with artifacts uh without needing necessarily the code tool on top of it and this is 0ero to1 exploration so you can kind of explore new ideas but very often this is kind of in a silo and it's not necessarily in your codebase I think the superpower of these 0ero to one explorations if you're doing it in cloud code is that it can actually be in the codebase and understand your code and where it fits and so it's a lot more real than doing just it on a side on a prototype and then the other two workflows that I do most common now are to um I'll go to the third one here actually understand the codebase often when I'm developing a new feature or I'm working on a new project I'll actually spend my first pre-brainstorm era uh asking claude about how it currently works uh how it was implemented today down to like even what the system prompt is and how it's configured how it's architected uh to really understand the use cases sometimes I'll even ask like how would you design this differently Uh, and then there's a phase where I'll go into Figma and then do the designs and then I'll go back into code once it's ready and I'll kind of do the final polish pieces if an engineer has built a lot of the infrastructure that needs to be there or sometimes I'll try it myself at a first stab and see how far I can get with uh cloud code. Got it.

Okay. And you probably do the understanding codebase and building the code more, right? Like working on a you know mature feature, right? Definitely. Definitely.

I would say this first bucket I actually I like rarely do at work. It's something that I do maybe myself in my personal time and personal projects but when it comes to working as a designer like with my engineering team with a product team I'd say 90% of my time is spent on the latter two use cases here. Awesome. And I think you have like you have like another slide uh where you have this like whole flow flow diagram like explore. Yeah.

Can you walk through? Yeah definitely. So I think like this is where you get a little bit more granular into what these actually feel. I kind of broke this out into what the typical kind of design process looks like. You know, the double diamond of like explore and discover, then design, then prototype, then you kind of polish and you finish.

And so I think the way I look at it is claude code a lot of people will assume it's really only for development. And so maybe in like step four and five here, but I think step 1, 2, and three are actually where cloud code shines for non-technical folks just because it lets you do a lot of I would say like technical adjacent tasks or like engineering adjacent tasks because you have access to the codebase. I actually think one, two, and three here is something that even our very technical uh customers do in cloud code that they don't even realize they're doing because it's just so easy to get started. And that's really, you know, exploring different solutions that you could uh understand, exploring the history of why something was implemented the way it was and then planning and like sequencing how you can break out uh building different features. Uh the reason I like to do this more in cloud code actually than in cloud AI although I'll often go back and forth in between the two is that um as a designer our job is really to kind of take all the information all the feedback from all different parties including our users including engineers including our product managers and translate that to a working product experience.

But that working product experience is in code. So the faster you can understand how it's going to get implemented in code, the more realistic it's going to be of representing what the actual product experience is. Yeah. Like I I think the code is the source of truth, right? And like I know I I spent like 10 years building products and uh I always noticed that you know I I write like a spec and a PD and then whenever the Figma is actually you know ready to go like people don't look at my spec anymore because Figma is a lot more higher than the spec and then eventually they move into the actual code and and like with this process you can you can basically go into the code direct directly right you can start making prototypes exploring the code direct directly.

Exactly. Exactly. In fact, sometimes in the past, I've instead of handing off a Figma mock to an engineer, I'll hand them like a draft PR that I have with like a description of what I was trying to do and where I didn't necessarily I wasn't able to get to completion myself cuz you know, at the end of the day, a lot of stuff is still quite difficult if you're not uh very coding knowledgeable. And so, it just is really a great starting point to developing features a little bit further down the process than you typically would. And uh you know, now you're like a trusted member of the team, right?

like when you joined the team, how did you get engineers or like get people to give you like GitHub access and like start doing this stuff? What kind of conversations do you have? Uh, you know, I think at Anthropic anyone can code and it's such a collaborative environment that I feel like our roles don't matter. So here it was actually very easy. In fact, I'd say the team was super excited when they saw that I wanted to do this.

A lot of the designers code even themselves. So even, you know, before we had cloud code directly integrated, you would see a lot of designers make PRs and kind of do it themselves. Okay. Um, at companies where was a little bit harder, maybe a little bit toned down, um, part of my process is actually to sit down with an engineer and have them pair program with me for a day because honestly different repositories are set up so differently. I'm sure you know this.

I was a little bit less familiar with this when I first started. Even like how to get a preview app running and get all the like dependencies installed and my local dev environment set up was really hard for me in a new company. And so uh I think it helps you build good partnership with your edge partners. And then it also helps you understand like the unspoken semantics of how like code gets pushed at your company and like expectations of deployment times and like preview builds and things like that. And another quick question like how do you do you guys do you guys have like design reviews or like you know you have to go present to Mike or like do you just present the code or how do you guys do that?

Yeah. Uh you know it's interesting. We do have product reviews and we do have design crit and sometimes we'll have design deep dives or design reviews. It's a mix. Sometimes you'll see Figma prototypes presented.

Sometimes you'll see fully working apps presented. Sometimes you'll see a local preview presented. It kind of depends on kind of what the feature is at the time. And I do say this a lot to kind of other designers I work with now that uh this skill set of code is available to a lot of nontechnical folks. um you should just consider this as a new way you can present your work or new way you can work and similarly to the early questions for design or product like should this be low fidelity should this be high fidelity I think you should consider code the highest possible fidelity so and the effort it takes and kind of what feedback you get will change depending on which one you show got it okay got it I mean ultimately it's about like kind of getting a feel for what the user will actually see and feel in the product right so like you just make prototypes for everything you make prototypes for the core user experience.

I guess mhm I think there are still some instances where I personally find it easier to be in Figma rather than in prototyping. This could be a limitation definitely of my own technical ability. But for bigger changes that are harder to do architecturally in code and sometimes I'll ask cloud like hey like how hard is this going to be to change? Uh if it takes me like a minute to do it in Figma and it might take 30 minutes to do it in code it does make sense more to do it in Figma. So, there's still that trade-off I think we have today of where it makes most sense given what you're trying to accomplish.

Yeah, Figma is surprisingly I mean my designers make fun of me, but like like just trying to get auto layout to work is is hard. Like I can't figure it out. Mhm. Definitely. Figma is not that easy either.

Yeah. Yeah. Yeah. It's definitely a power user tool, I would say. This episode is brought to you by Linear.

Let's be honest, most project management tools suck. That's why I love working with Linear because they share my obsession for craft and quality. Linear is incredibly fast, beautifully designed, and comes with built-in support for AI agents like cursor. As a PM, I love using linear to capture customer feedback, draft PRDs, and manage development and communicate across the organization. Product teams at OpenAI, Versel, BRS, and Cash App all use Linear to build complex products at lightning speed.

See for yourself by visiting linear.app/behindthecraft. That's linear.app/behindthecraft. Okay, now back to our episode. All right, so let's kind of like maybe walk through some of this process with like a real demo, right? Like like a do you have like a little demo app you can show us?

Yeah, definitely. So, let me walk through. Unfortunately, I can't share anything that I do internally, but I can show a little demo app we have called Claude Cafe. And you can kind of see the mocks right here of what it looks like. And um I already have it open and running on cloud code right now.

So I'm in the repository Claude Cafe. I have kind of Claude open and running. So the first thing I tend to do is ask Cloud to help me preview this app. And so it's pretty straightforward to just talk to Claude like I would my engineer and I say help me uh run this locally. I do think this is easier for some engineers like they might say, "Oh, I'll just do this in bash commands." But for me, I don't always know the packages that you need to install or the commands you need to run the app.

And so I find this a lot easier. Um, one feature I really like that we uh recently released that makes this very possible uh that I've been using for months and has now only been available I think for the past month externally is background bashes. And so you can kind of see here it says controlB to run in background. Um running a dev server uh as you probably know but maybe not all the nontechnical folks don't know it's just an ongoing process. And so if you hit controlB you can kind of see it runs in the background now and it'll update you as it's going but you can kind of keep chatting with Claude even as it's still running.

Oh, nice. So, is that like basically having two agents going? Uh, kind of a little bit, I would say. I mean, like right here, you can see that it's been successful. We do have the ability to run parallel agents.

Uh, this just lets you run background bash commands. So, anything that's like an ongoing command. Got it. Okay. You want to should we open a local host and see how Definitely.

So, we can see what it looks like now. Oh, sorry. It opened in another browser, but I can pull it in. This is what the app looks like. So you can see it's running on preview and the app.

It looks great. Yeah. So right away I say like from my eye I can tell, oh this doesn't look exactly how the app I designed did, right? Like the images, if you can see it, aren't necessarily properly aligned. The header is supposed to be left aligned.

Like there's all these little details that uh I can see how it was implemented that way. And there's just like things that I would want to change to get it to that I'd say like last 10% of polish. Mhm. And so this is actually where I spend uh most of my time in cloud code. And so we will have the app running and I'll there's a few different ways you can do this.

So in a previous video I referenced using the Figma MCP server. I would say sometimes I do that if it's very polished, but Claude actually has vision capabilities. So I'll typically start instead of using the MCP server by um exporting this as a PNG to my desktop. Uh, so let me send it to my desktop for now. It's there.

And then I will drag and drop that into claude and I'll say, can you update the header and image alignment so it looks more like this block? Okay. Um, it's like a little bit lower fidelity, but I think the Figma MCP server for me, sometimes I actually don't have it all always logged in or set up properly. And, uh, switching between dev mode for me is, um, just my personal preference of doing it through images. Uh, the other way I tend to do this, which is a little bit more advancedish, I would say, depending on where you fall on the spectrum of technical ability, is I'll actually go in weapon spec mode.

I'll see kind of where the alignment or class is and then I'll direct Claude specifically to look at this page feature uh and then make the updates that way. So there's a lot of different ways you can kind of get into this workflow. So like you actually paste the code here to take a look look. Um I will sometimes I like to actually look at the classes or the way that it's rendered and I'll tell Cloud to search for that code line and update it to the one that I think it needs to be. Okay.

because it's like cloud has access to all this. Yeah. Yes. Yes. Yeah.

Makes sense. Yeah. Um I'd also say in this case, you saw that this kind of went directly to coding. This is actually not my typical workflow. Normally, what I'll do is I actually go into planning mode first cuz I think this is the best way to do it.

be like actually can you provide an overview of the plan and your approach also uh break down this task into easy to understand steps and changes. Um I sometimes add that last one especially if I'm trying to make bigger changes because Claude is kind of designed to be able to speak to you like you're a software engineer. I'm not a software engineer, so I often prompt for additional explanations. Yeah, this is what I do, too. I always get it to make a plan or make a two to-do list and let me review the plan.

It's too overeager some sometimes, you guys. Definitely. Definitely. Especially if you're in auto accept mode, it'll definitely start going on its own way. This also helps you, I think, if you're learning to code, get a better understanding of the architecture of how a software engineer would think about making these changes, which is really helpful for me.

So, we'll see the changes coming in. Um, cloud of course is very complimentary. You'll have a sleek new header. It's really nice. And then if this I'll read through the plan here so you can kind of see it'll list the file where it's making the changes.

It's updating the pad heading. It's moving so it's left aligned. That's what I wanted it to be. I really like when it actually shows the CSS for me actually because it helps me know how to do it in the future. Y and you know this generally looks good to me.

Let's say and then so I'll go yes uh and auto accept edits modes. This is also your best friend if you're not necessarily understanding every line of code that's changing. Uh, auto accept edit modes just lets CL claude make the changes and then you can come back and see the final product. Uh, one really fun thing that I like to do is watch the changes live. I know it's like sometimes breaks in between and they'll rerender, but I like to see things move around.

Yeah. Yeah. Yeah. It's great. Yeah.

Yeah. This that's why it's very important to get local host set up first so you can see what what it's doing. Absolutely. Absolutely. I think design is such a visual job that it's like much more helpful to get it all together.

Is this thing real by the way? Do you guys actually have a claw cafe? No. No. I mean, I wish we do have cafes at the office and you can order drinks.

Uh I wish they were themed this way, but uh unfortunately this is just an app that one of the designers on our team made for a demo. Got it. Got it. I've been trying to do like a lot of like prototyping too. And oftent times AI tends to make this like very same look like like this shaden tailwind CSS look with the purple backgrounds and stuff.

Like how how do you avoid this stuff? It's like super super annoying. Yeah. Is it just using images and like giving more precise instructions? Yeah, I think so.

I I tend to avoid using claude or any AI models in general for like net new designs without any basis to start off with because I think you do get that exact same styling. You could ask honestly any model and it'll give you a very similar styling. Um, the tips that I would recommend are one, I'll often reference parts of the site that exist already or inspiration that I have that I like the way it looks and I'll drop it in as an image and say, "Hey, make it look like this." So, an example was is like a few weeks ago, I was adding a new setting to our cloudi page. And instead of just asking it to generate a setting, I was like, "Hey, look at the existing setting page, specifically this setting, and reimplement it this way. That's the way I like it to look." Or if I'm doing it sometimes in cloudi chat, I'll actually drop screenshots of sites that I really like or like almost like a Pinterest board style in thing.

I'll say like make it look something similar to this. Okay. Kind of like a moo moo board so it kind of understands what it's doing. Yeah. Yeah.

Got it. Okay. Um and uh let's talk about I I noticed that you have a bunch of stuff in the output around like lowrisk, high risk and maybe you can pull up your cloud file. I think you have a really great file. Absolutely.

Let me find it right now. This is what my cloud MV lick file looks like. Yeah, this is a great file like like so I've been using cloud MB just typing init and then it just like analyze the codebase. But I think this is way way better. This is like this is like Megan's cloud MD if you can walk through why why you added all this stuff.

Yeah, definitely. So cloud.md is actually extraordinarily powerful as an ecosystem. I didn't fully understand it when I first started using it, but we made a lot of updates so that you could have multiple hierarchical cloud MDs. And so there's a sh and cloud.mmd is kind of like shared knowledge that claude can have access to about your repository for our entire codebase. We actually have lots of cloudmd files shared across the team and these are checked into the repository.

They're kind of shared with things like the structure. That's typically what you get when you get slashinit that you mentioned. It like understands your codebase. Uh over time um we also added a personal cloud.mmd file. So this is to my cloud running instance.

It doesn't have to do with the codebase. It actually runs for my global experience of cloud uh code running in any repository and it's attached to me as a user. This is where uh initially I had actually asked the nam. I was like hey could we make a version of cloud code that is directed specifically to product designers because it'd be really amazing as a tool to use. and they said, "Oh, like have you tried adding it to your cloud MD?

Like Claude is pretty good at following instructions. We think that you might be able to get pretty far that way." And uh so I worked with Claude to actually draft this cloud MD. I iterated on it a bit and this is where I've landed up as a way to direct Claude to be a cloud for designers. Okay. So it's like, you know, you know, I'm a designer.

You got to explain more stuff to me. And then I I I like the emojis like, you know, there's a high-risisk modification. Yes. Yes. Yes.

Yes. I've definitely recently I was guilty of causing an incident. My very first one u from pushing code to prod. Fortunately, it was caught very quickly and resolved and everyone's really great here. It happens.

Someone told me it happens to everyone. If you're pushing code to prod, you'll like cause an incident at one point, but I did add that in after. But uh but all the stuff you push to prod is like in PRs, right? Like some does some engineer have to re review it or Yeah, everyone's still reviewing it. But I think things get through a little bit sometimes things slip through the crack.

It happens to everyone. Got it. Yeah, this is great. Uh and and basically, so okay, so this is in your project's root directory or is this in your global? This is my global root directory.

Yeah. Okay. And basically, okay, let's kind of explain how cloudd works. So basically, it puts this into context each time you have started a new conversation or Exactly. Exactly.

And so it will always have awareness and it'll adhere to these quite like we prompted cloud so it'll adhere to your cloudmd files. So my outputs frequently look very different than what the engine would look like. They're a lot more ver verbose and a lot more detailed than anyone else. And I have a feeling that you played a pretty big role in shipping the new output styles feature. Did you play a big role in that or uh I did not actually.

I would say that was a combination of a bunch of folks across the team who were more on our go to market side and marketing side and comm side thinking about uh extending it even more into like a non-technical audience. So, I was really excited when it came out because you can still use it. I think alongside your cloud MD, I felt the cloud. MD was enough for me and I think that's one of the beauty beautiful parts about cloud code. It's so permutable.

It's like very customizable. You can make it your yours. Yeah, exactly. Exactly. Um but but can you like uh can you actually go back to that slide with the flow flowchart because I kind of want to talk about like a real example of a feature that you guys shipped like maybe you can share example of like ideation stage all the way to launch and like how you work with CAD and like the the engineers.

Yeah, let's think what's a good example of that. Why don't we take agents? I think that's a really good one. Uh so cloud code recent release sub aents or agents and what these are are programmable agents that let you oop sorry run cloud codes in parallel. So um this was actually I think a really great feature because it shows how like AI tooling in general allows for a lot of fluidities of roles.

So agents was originally conceived as an idea by an engineer on our team Sid and he was really rapidly prototyping the idea and um I think Cat might have mentioned this in her session but here at Enthropic everyone uses cloud code very often so we're like our best dog foodters like we use the product all the time we give feedback and so he built the feature he posted internally a demo of it working and then he launched it to our internal working version of quad code from there I reached out to him I like, hey, this is a really cool feature. I started using it. I was like, I have a bunch of design um kind of updates I would recommend. I think like we should highlight this even more. I think there's a way we could show parallel agents.

Uh and so we did some rapid iteration cycles with myself, another designer on the team, and Sid to kind of iterate on the feature and get it to a level of polish that we felt happy with. And then once it felt good, we prototype it a little bit more with the team. A few other folks gave feedback who were using it and then it was kind of ready to go. So I feel like a lot of the feedback cycle is actually using it ourselves. Wow.

Okay. So basically like uh Sid um maybe spent a week or a couple days just like prototyping himself and he just shipped it to internal users first, right? Exactly. Exactly. There's no spec or anything or like design or anything.

You just shipped it. Not for smaller features like that. No, I think it can happen pretty organically. Okay. And then you guys went back and forth and then uh you made it better.

And then when when how do you know when it's ready to go? like like the internal people were like, "Hey, let's let's get this out." I think like when we initially launch new features, we'll often get a lot of feedback from the team. You know, our teammates are our best sources of feedback and our most honest. And so, you'll kind of see initially when we launch a new prototype, we'll get a lot of feedback on it as people discover it. And then over time, it'll slowly taper off because we've addressed all the bugs and features and it just becomes a natural freaking part of the product.

We do also look at analytics and adoption of features to see if they're being wellreceived with uh ants as we call them or folks at Anthropic. And if we see that steadily growing and we see the negative feedback steadily going down, there's just a moment where we feel like, yeah, this is good to go. I also think we are on the side, which is always a little bit nerve-wracking for me, but it's been really beautiful to see on releasing early and letting our community also get feedback because we can continually update and improve things as they go. Oh, because you have like an early preview program or something like uh not even an early preview. We'll just release it early once it feels like it's reach a point of readiness where we'll get better feedback from our community because we've gotten all the feedback we can from internal folks and then when you get ready to release it the go to the market just like you know uh maybe getting coms and per marketing involved and putting like a post out there and they just exactly exactly um often it'll be the engineer who built the feature themselves uh making a little screen recording of them of their feature or they'll work with our devril team or coms team but it's all very very That's great.

You know, like because that's not how uh typical company ships this stuff, right? Like you know, typical company is like, you know, you know, this waterfall thing, right? Where like you write a spec, you go debate it about it internally and then you go make a design and then you like you hand it over to engineers like here here's a perfect design spec and go go build it. Maybe you guys still do that for like really big features like you know enterprise or some or something. But like yeah, I mean it's way more fun the way that you guys do it.

I think so. I think so. One thing that I often reflect upon is like how fluid the roles have become on the team and like how quickly you are to able to just like make the product better and make the product that you want it. Uh like the slashexplanatory slash like learn mode that you mentioned that was released a few weeks ago that was actually a custom command because we have custom slashcomands uh that you can kind of work on and customize yourself that someone on the team built and they're like hey I actually think this will be useful for a lot of other folks. And so they started to work on that in that direction and that evolved into our product feature.

I think one thing to note that uh I always really like that we still do is there's still experts on the team and what they do. So if a new feature is going out the engineers will often reach out to myself or the other designer on our team Nate and say like hey can you give a quick pass on this like it feels good but we just want to make sure that aligns with our system and we'll stamp it. Often we'll just try it and use it. And similarly, if the designers are building a feature, we have code review for that to make sure that it's all kind of good and working. Does Cat have like a spreadsheet that tracks all the features in progress or Oh, yes.

Oh, yes. She has a master spreadsheet of everything that's going on. uh she's uh we're always constantly trying to keep it up to date and there are a lot of kind of bigger features that do follow a little bit more of a traditional product development process but I would say while it follows that traditional process the role of like who drafts that and like who's contributing to it is extremely fluid across our team. I mean that's the best right where people don't have like people still have their expertise but like people can just like cross across functions and just do what's best for a product. Absolutely.

Absolutely. May maybe you guys should just use like a slash camera or something like cat can run it every morning, check the codebase and see what kind of new features there. I mean I think that sounds like it'd be incredible for her. Uh I'm not sure how well that would work because we often have like random ideas spinning out everywhere. Got it.

Okay. And I think you have one more slide on like some pro tips of using claw hot code. Yes, definitely. Let me share that as well. So pro tips, these are my pro tips for cloud code.

I recommend these for folks who are getting started. One thing I will say is that these pro tips hinge initially on the idea that you're comfortable in terminal uh or CLI. So if you're not, my biggest recommendation there is actually to just chat with an engineer on your team. Like no engineer is ever not going to be happy to explain to you how to use terminal or what terminal commands are. Even people who've used like CLIs their entire life might not know every single command out there.

Uh, another way to learn how to use CLIs is to just ask cloud AI in chat. Like I'm frequently asking cloudi how to do a thing before I open cloud code in terminal just to make sure I'm in the right place or have the right git branch, things like that. Sometimes ask cloud code in cloud code to help me. It's kind of a little inception, but once you get there, these are the cla code specific key bindings and or like best practices I would recommend. Um, the reason I call it being comfortable with terminal is that a lot of these are designed for developers.

So, a developer is very comfortable and very familiar with these key bindings. So, as you use terminal more, you'll be more familiar with them. Um, but it might be a little bit new if you're not. So, the first one here, shift tab to go between auto accept mode and plan mode. This is like my most used mode.

I think I always start in planning mode whenever I'm doing something just so I can make a plan with cloud and understand the changes that it's making. And then uh auto accept mode lets cloud kind of autonomously accept the code changes and I'll wait till the final uh code changes are done before review. Um MCP lets you connect to MCP servers. These give access to more tools that Claude can have. So the Figma MCP is one that a lot of designer use.

Um a lot of folks also use a PlayWrite MCP to preview their app. That can also be really helpful. You can talk to your engineering team about which MCPS they have set up. Um I think it's a thing that's actually very valuable to share. Um, controlV to paste images.

I think I showed how I use that today. It's really just to show cloud what I'm working on. Um, escape to cancel is a big one. Just uh if Claude is doing something and it makes you nervous or you're not sure where it's going, you just stop Cloud's progress right away by hitting escape and it'll stop it. Double escape lets you go back in history, which I also really like.

So, if you've sent a prompt and you didn't like where it went, you can hit double escape twice and like go back to that prompt and then see uh and then update the instructions or you can see past instructions that you've sent to cloud. Got it. D-res lets you uh reaccess an old session. So, if you like opened a cloud code session, closed it, and then you want to get back into that task, you can use resume. And then slashmemory to update your cloud.

Mmd file. When do you use the last one slashmemory? Like we have a new tip that you want to share or like Yes. Yes, I use it a lot when I end up in a space where uh I wish uh I do a thing repetitively with Claude and I want Claude to just do it automatically. And so for a little bit I did add preview my app before I start or preview my app for every change but that became a little bit too hectic.

So I did remove that and I'm constantly playing around with it to optimize Claude for my workflows. Uh so uh in my most recent memory update, I actually asked Claude to look at the existing component library before it finalizes any implementation decisions to make sure that we're following design systems best practices. Okay, got it. Okay. Yeah.

Like actually a lot of uh some some of these other tools are like trying to add design system support. So, so does clock code just like support that natively just like access the files and understand the files or I think this is where like you kind like design systems is the role that really beautifully covers design and engineering. Um, and if the design system team actually starts to design a system and a component library in mind with a coding tool or an AI collaborator reading through it, it actually is a lot easier than for cloud code to be able to read through our documentation and implement features. That makes sense. Makes sense.

Okay. Okay, let me ask you some other random questions that I forgot to ask Cat. Um, so, so like obviously a lot of the stuff depends on the quality of the model and like what the model team is doing, right? So, how do you guys work with that team like the AI researchers? So, I would say there are a few kind of dedicated work streams around cloud code for like bigger features that we know we want to work on or like bigger improvements that we see feedback from the community and those have kind of dedicated pods within the research product team and there's partnerships to continue iterating on them.

That's one way. It's like the very standard way of just like we got feedback from the community or we noticed a thing and we want to kind of train the model to get better at this. Um the second way is something uh that we are kind of looking into around how we can help cloud code help researchers better. So that's the second way that we partner really closely like the software development flow is so wide and widespread. But one thing we think we can do is train cloud to be really good not just at like production code but also at researching.

So that's another pod that we have. And then a third one is um we're very bottoms up at anthropic as a process perspective. So sometimes from the product team, sometimes with the research team, someone will have idea an idea of a thing that they want cloud to do. It'll spin up and they'll just start a mini pod of working together on a brand new thing. That's great.

Yeah, that's fun. Um got it. Okay. And and you probably have access to all like their early models and stuff so like yes. Yes, we uh definitely uh try out all the models ourselves internally at first and uh we get a lot of very strong feedback immediately if the model's not performing as well uh because people will switch.

Got it. Okay. Got it. Um all right, M. Well, this is super awesome.

Yeah. Um so, how do you think the design and maybe like the PM role will evolve like you know or is already evolving? I mean I I I guess everyone is just kind of like a builder with their own specialty or Yeah, I think that's a great question. I feel like across tech, espec specifically if you're in a coding adjacent role, we're actually becoming more and more fluid in our responsibilities if that makes sense. you know uh historically I used to talk a lot about the design PM fluidity like depending on if your product manager is a lot more design oriented or your designer is a lot more product oriented uh as you get more and more senior or even in like smaller teams you'll see the responsibility like really kind of become fluid you'll see that with EM as well like it'll become a little bit fluid around who does product strategy or things like that uh and I think that's because the skill set of being more product minded grew over time but the product manager was still the expert and the expertise and the decisionmaker in that uh when it comes to these coding tools, I kind of see it very similarly where now we all have kind of a skill set and ability to code.

So that responsibility is a little bit more fluid. We can kind of lean into each other's rules and help each other out and collaborate a lot more, but the ultimate decision maker should still be the engineer and the reviewer should still be the engineer. So yeah, it's more like fluidity and then an expansion of our skill set. Now we just have another tool in our toolkit that we can reach for which is code. Yeah.

And I also think there's also a very good trend uh around more senior designers like yourself choosing to stay in kind of like a builder role because previously you kind of have to become like a manager or something like you got to work on like some management stuff, right? But like you know I feel like more and more now people who care about the product and the craft are more valued. I don't know maybe I'm biased but have you seen that? I don't know. I can't say if I've seen that personally.

I would definitely I would definitely believe it though. Like I myself probably spend an equal amount of time now in cloud code as I do in Figma. And um you know I talk about this sometimes with folks at Anthropic. It's just so fun to build here because you can build so quickly that it's hard to imagine not wanting to be a builder. A lot of our managers at Anthropic are building themselves too though.

Like I think the manager role also has more access as well because you can get into these tools so much quicker. Okay. So like let's say like I'm a designer and like you know I want to become like a AI native designer like Megan and like or like maybe get a job at anthropic like how how do I get ready? Yeah. Uh okay.

So I would say if you're like totally new to coding and it's something that you want to get into my recommendation is honestly to just start like just start using it because it's hard to know the unknown known. So you can uh first start with like claw.ai and artifacts that will actually give you a good understanding of like what it looks like to have a model that produces code. um you can start and then from there I would recommend you go into cloud code directly. Uh it's a really great partnership if you have an edge partner to actually collaborate with us on because your engineering partners will be excited that you're you're wanting to code because it'll help them get faster. You'll learn a lot more.

I think it's like a nice moment to build that partnership and that bridge. Um a few things that I did is I did take an intro to React and an intro to Tailwind class. Most of the changes I make are front end and it helped me get a little bit deeper in the understanding of you know how these libraries work and how they're rendered uh directly. Not a requirement but I do think it helps to understand the code that's being implemented. Um and then to get into like the actual vibe coding and the actual kind of AI side of things.

I would say the community is very open and collaborative right now. Like we're in that nice spot of new tech where people are just excited and sharing what they do. So, uh, X is a really good place. I would say GitHub is a really good place to learn. Uh, we have a few courses actually that we offer at anthropic that teach you how to vive code.

Those are really great because there is a little bit of a skill to learning how to vive code. That's even different from just coding like a separate thing. Yeah. Like you know just just like you know probably number one tip I have for people is just to like get to plan first like absolutely. And also like another tip I have and I don't do this a lot.

It's just like after it makes something, you just kind of ask it to explain how you did it, you know, cuz then you can actually learn like how what what the code is actually doing. Absolutely. Absolutely. I think it's really really helpful to actually get into the code itself. Uh it also lets you do more complicated things in the future and you can detect when cloud is wrong because sometimes cloud will go in like a direction that you need to course correct it a little bit.

Yeah. Yeah. When it starts saying you're absolutely right that that's something that's going wrong. Yeah. Exactly.

Cool. All right. Well, make it out. Where can people find you or, you know, learn more from you? Uh, yeah.

So, you can follow me on uh X I, uh, my handle's a little bit complicated because my name is spelled complicated, but it's me E A G HAN H_C. Uh, I will often share tips and tricks there on how I use Cloud Code for nontechnical folks. And I'll also share some of the launches that are upcoming and how I use them in a way that's maybe not necessarily geared uh directly towards technical developers. I I also have gotten feedback that it's helpful for devs to learn there because then they can see how their nontechnical peers are using cloud code as well. Yeah, I I love your post like they're very practical and like yeah I I I think you know I I posted that this thing like cloud code is kind of like it's really just a really good agent.

So it can like right now it's most used for coding but it can be used for design for product stuff. Absolutely. Absolutely. Absolutely. Yeah.

All right. Well, keep working on it. Keep working on it. I'm I'm a power user. Yeah.

All right, Megan.
