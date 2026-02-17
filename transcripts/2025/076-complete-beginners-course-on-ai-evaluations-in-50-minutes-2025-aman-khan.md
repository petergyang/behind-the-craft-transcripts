---
title: "Complete Beginner's Course on AI Evaluations in 50 Minutes (2025) | Aman Khan"
guest: Aman Khan
publish_date: 2025-08-24
youtube_url: https://youtube.com/watch?v=TL527yTpxlk
channel: Behind the Craft
keywords:
- ai
- leadership
- execution
- metrics
- coding
---

The CPOS of these companies are telling you eval are really important. You should probably think what are AI eval exactly. I think there's really just four types of of evalu. And we can define what's good or bad for any of these. So all you're doing here is basically building out a golden data set in the first place.

So, we're going to hit generate and let's see what the agent comes up with here. So, okay. So, it starts giving me a prompt. You want LLM as a judge to align with your human label and the the judgment that you're giving it. Let's get super practical.

Now, there's like a lot of eval videos out there about frameworks and blah blah blah. Like, I just want to like actually walk through a real example. All right, let's look at one. So, okay, welcome everyone. My guest today is Aman, head of product at Arise.

And today, Aman and I are going to show you exactly how experienced PMs like ourselves run AI evaluations using a real example. And we're going to walk through all the steps including uh defining the evaluation rubric, creating our human label golden data set, running Elm as a judge, eval, and more. So, welcome Aman. Yeah, thanks for having me back, man. It's awesome to be back, and it feels like a lot has changed since we last talked about this, so I'm pretty excited to dive in.

All right, so let's do a quick recap and then we'll dive into our example, right? So like um what are AI evals exactly and why are they uh you know the most important skill for PMs to build? So I think first off we know this to be true, right? LLM hallucinate. We've all experienced this in our day-to-day life using LLM based products or trying to build around this for our company.

But you don't have to take my word for it. Don't take Peter's word for it. like the CPOS of these companies are telling you you should probably have eval when you're actually building around AI products. So if the if the people selling you the LLMs in the first place are telling you eval are really important so that when LLMs do hallucinate they don't you know they're not going to like negatively impact your company or your brand. You should probably think okay well how should I use eval in the first place to actually build products that matter.

So I think that that's a really important component which is you know don't just take our word for it. The actual CPOS of these companies product people leaders are telling you eval are the emerging skill because LLM hallucinate and eval measure the quality of your AI system in the first place. Yeah. It's like the the people selling these models are telling you to check the model's answer. So it's probably true.

Yeah. Exactly. Yeah. Yeah. I think there's really just four types of of evalu deployed and you know even all the way from development through to production with AI and those four types of eval are like codebased eval.

binary sort of pass fail, right? This is like checking for a string or presence of a string in a message. So, for example, if you are, you know, an airline like United and a company says, "How do I book a flight with Delta, you know, or a person or a user asks you that question, you you probably don't want to respond with an answer of like, how to go book a flight with Delta if you're United." Yeah. So like just checking simple things like that is like level sort of level one level zero of initial code-based eval. They get a lot more complicated.

But the beauty is because of code generation today it's actually become a lot easier to create code-based eval. Then you have the human eval which is like the PMs or the subject matter experts doing a thumbs up thumbs down on an individual sort of back and forth. And that's really like was the answer good? Did it meet the criteria? And we're going to kind of go into the deeper here, but that's like having a human in the loop.

And then there's the use the LLM as a judge, which is probably the most prolific example of having scaled up evaluations, which is actually having an LLM system sort of act as if a human is labeling the data. And it's like training, it's like similar to training an agent or training an LLM to actually respond like a human by giving a label. And then there's the user eval which is like the closest I think of this as like a business metric. I'm curious what what you think too here but this is like how do you collect data from the real world and this could be an actual user interacting with your application that a downstream customer giving you feedback on how their experience went. So these are this is it.

I mean this is like generally when you think about eval types that come up um pretty much 100% of the time. Yeah, I I totally agree. And I think um like having done some of this, I I think the human in the loop is like really important. Like there's no magic formula for this stuff. You have to, you know, care care about how this stuff is going and like really have um attention to detail on some of the stuff.

Yeah, exactly. And that's that's when I think people are saying, "Oh, well, where does the PM fit in here?" The PM's job is to have judgment on what that end product experience should be. And so being in the details on that when it comes to the human evals is really what determines whether or not your product is successful or fails. Yeah. Like I I never found it useful to just completely outsource the human evals to some contractors or labers.

Like the PM has to be in the spreadsheet doing the stuff themselves too, you know? So totally totally I mean I I I mean I can give you an example like even ever since we started you know when I was working on like self-driving cars way back in the day too we would just look at data almost every day or once a week and just go in and label did the car should the car have done that or not and kind of the same thing with these agents like just look at your data and pull your team together to make a determination of what's good or bad. Yep. There there's a lot of uh there's a lot of spreadsheets involved so as as we'll see soon from the demo that that we'll do. Yeah.

Yeah. So, um, so actually, yeah, so let's get super practical now and, uh, you know, there's like a lot of eval videos out there about frameworks and blah blah blah. Like I just want to like actually walk through a real example, right? So like for example, I love to run, uh, even though I run pretty slow slowly and uh, let let's assume that we're building a customer support agent for for on running shoes. Um, so, uh, on is like, I think European brand and gain a lot of popularity recently.

And this product actually exists. If you go to the on website, there actually is a customer support agent. Do you want to actually quick quickly show it? Yeah, let's do it. Yeah.

Let me let me pull it up. All right. They got send. That's great. Yeah.

Yeah. Yeah. I think somewhere on the bottom they have like a customer support thing. Oh, yeah. Here it is.

Yeah. All right. So this is not a real human, right? This is like a custom port. So maybe a ask it about return policy or something.

Yeah. How do I return my on cloud running shoes? So there's a couple things I guess while we're waiting for we're kind of looking at the responses. Like it responds with emojis. It's asking like follow-up questions if it needs more information.

uh and then it sort of suggests what should I what can I go do next? So it actually these are generated suggestions as well of actions that you know that the agent probably has access to to show to a user saying return an order or just asking more about the policy. So it's sort of has some branching logic to to figure out what's the right next step and so now it's giving me more information on the policy. Okay great. So before we uh start doing the evals, we have to um write a prompt, right?

To actually get our customer support agent to start working. So so can you uh show us, you know, how to write this prompt and also what kind of information we need to give the prompt to make it great. Yeah, good question. So let's go ahead and pull this up. So I really like to use uh Anthropic has a really great uh product for this actually.

So if you go to Anthropic, they have this console system and the console actually helps you get started from like 0 to one with writing a prompt in the first place. So it's a really good starting point. So what we're going to do is we're actually going to build this prompt in uh Anthropics console which is if you go to Anthropic, they have this tool called workbench uh which is really cool. It helps you like actually get started with u building an agent in the first place. And a really core part of building an agent is the initial prompt that you want to give the agent with the context to help it perform the task in the first place.

And rather than like going and trying to do this all from scratch, we can actually use a you know this generate function which allows us to kind of create a prompt uh using best practices right off the bat. So what I can do is say uh design a prompt for a customer support bot that handles customer interactions for on running shoes. And it's pretty forgiving like it you don't have to be like super descriptive but it's good to give it a couple of reference points here. So you'll take an input variable. So this is like maybe going to be the user's question.

Mhm. [Music] product information and should respond. Oh, and then uh the policy information as well. [Music] So there's there's kind of three pieces of information here. There's the user question.

So you're going to take input variables which are the user question product information and maybe the policy which is like the return guidelines right like so this is like it knows about on it has a user's question and it has policy information of like return guidelines and things like that and you should respond with a helpful answer. How does this look to you Peter? That looks great. Yeah. Awesome.

So, we're going to hit generate and let's see what the agent comes up with here. So, okay. So, it starts giving me a prompt. It's actually putting in the variables for me here. So, that's what prompt variables look like.

There are and it's actually giving examples, too. And it actually has uh the the curly braces here represent variables and it even calls out over here that there are variables as placeholder values that make your prompt flexible, reusable. So we can hit continue here and let's say we want to use this to iterate on or actually start building out this example of this this customer support agent. So pretty pretty good first pass and it even puts an example in there for a back and forth that the agent should handle. Um cool.

So yeah. So you have to actually add the product info and the policy info, right? Yeah, exactly. So this the product info and policy info are going to come directly from the on website. So let's go ahead and pull that in and maybe we can run an example here.

So I'm going to hit run and it's going to ask me for me to actually provide this information, the product info and policy info. So what I'll do is actually I have the the uh the on website up on the other, you know, on my my end. I'm just gonna go ahead and copy over a ton of the the context here from the on website itself. So, let's go ahead and do that and we'll copy the return policy. Okay, here we go.

So, that's the policy info. So, I just copied that over from the on website. There's product info which also comes from the on catalog. So, let me go ahead and copy that over to and and I think we just got like a chatb claw to look up the own website and extract the like the shoe prices and descriptions and names. I think that's how how we did.

Yeah, exactly. Yeah. So, so that that's a great point. Yeah. So like you can get started with this with like you can just ask you can even ask chat JBT get me policy info for on right or or give it copy paste it in and it'll kind of figure out and maybe give you like a little bit of context here to get started with and then the product info in your case you're you know we kind of go to the on website and you're like you know copy paste that into cloud and you're and you're basically saying give me my product info to get started with.

So, that's kind of a good starting point. And then I don't know like what's a good what's what what's a problem you hit recently with uh your on running shoes, Peter? Um let's say uh let's say I bought the Cloud Monster shoe and uh it's been like two months, but now I want to return it. Like I don't like it anymore. But now I want to return it.

Okay. Yeah. So now we'll hit run and this is what the response actually looks like from the LLM on the fly. So we're using clo cloud sonnet. I almost said clude um cloud sonnet.

Uh we're using kind of the latest model here. Um one of the latest models and you can adjust any parameters you want. But then you get basically this initial kind of response. So it says, "I understand you'd like to return your cloud monsters that you purchased two months ago. Unfortunately, I have to let you know that our return policy is 30 days." So you've actually exceeded the return window, right?

But what do you think of this response? Like is this how does this response like feel to you as a as an initial take? Um I mean it it looks like it's like uh you know policy compliant. It is seems to be pretty helpful. Uh I kind of wish it was a little bit more concise but but um yeah over overall it seems good you know.

Yeah. So it's like initial first pass not so bad like from a response but as a PM I think you're going to be like nitpicking slash you know wanting to make sure that this thing is actually good enough for you to like go and actually you know deploy right like you you can't just look at one example and think okay is this thing is deployable is this deployable? Yeah. Can you hit deploy and completely all of your support bot questions go through this one? Uh, you know, instead of humans, it's now going through this bot, right?

So, what do you want to do in this case? So, I think it's great to like copy this example and why don't we just go ahead and build a spreadsheet here of what's good or bad and some of the criteria for good and bad um to get started with. So, so as a PM, you're probably familiar with building things in spreadsheets to get started with. I think I think spreadsheets are the ultimate sort of product to use for evaluating LLMs in the first place. And we've got a couple so you kind of mentioned a couple things, Peter, as we were chatting, which is like the product knowledge.

Does it know about the product in the first place? Is it following the rules? This is a very common one. we see customers, you know, kind of users in the space actually doing, which is is the agent actually following the rules that we've given it and then what's the tone? And we can define what's good or bad for any of these, right?

So, you can actually go in and change what the definitions are for the criteria for what's good, bad, average. And it's just meant to be like something that you can give to your team members and say grade the output based on good, bad, average. Yeah. And and um you know you talk to your team to come up with this but you can also work with AI. Yeah.

To come up with this, right? Um but yeah like I I think the rubric is kind of the next step after coming up the prompt. That's right. Yeah. So once you have the prompt in place and you start getting some data, you can start building a golden data set.

So, it's actually the combination of taking that initial prompt that you wanted to build with the context, taking a look and sort of like, okay, does this feel right? Now, I want to get more granular across my metrics. And the metrics are it should know about the company it's you're building it for. It should follow the rules and it should respond in a way that you want it to just to get started with. And so we've got a couple here.

Um, which is kind of this is sort of a let's go ahead and copy this one back in. So this is actually a pretty similar pretty similar question. Maybe we can go ahead and see what the output is here for this. Um, so I'll go ahead and adjust the variables. And so you can just change the use the user question.

And I'm going to say I bought the cloud monster 3 weeks ago. Generate the output. Interesting. So, it says it's been 3 weeks. Uh, you're still within our return window.

Okay. So, let's copy this and we'll go ahead and copy this back to the spreadsheet and that's going to be the AI answer essentially. Yeah. So, all you're doing here is basically building out a golden data set in the first place. And so, now we can grade this across the same rubrics we had before, which are product knowledge.

I think it seems to know about the cloud monster. Uh I'd say that's like good probably. What do you think? Yeah, from product knowledge perspective is good. But this is mo mostly a policy question.

So yeah. Yeah, it's mostly a policy question. Okay. I have some good news and important information for you since you purchased your cloud monster directly from on and it's been 3 weeks. You're still within our return window, but you lost the box.

Interesting. So, it says, "I'd recommend contacting our customer support team." Yeah. I mean, to me, this seems like the policy should actually cover like what happens if you lose the box or if the shoe is damaged, right? Like, it should kind of cover that. So, to me, I I think um I don't I don't think that information is in the policy, right?

So, yeah. Yeah. Interesting. So would you say that the eval here is unknown, bad, good or I think I think the eval here is maybe good based on the existing policy. Yeah.

But the policy itself I think needs to be improved. So maybe we can put that as a note like this is how you like improve a product, right? Yeah. We need a better policy. Yeah.

Yeah. Policy to handle the box being thrown away. So, I mean, for what it's worth, I you know, this is like uh this is, by the way, like if if we were working together on this, I'm I'm a PM on your team. I would probably I would probably argue and push back a little bit and say, well, is it in the policy or not? Have we are we actually taking a close look at the policy or is it because it's not in the policy you know now that the agent is saying I recommend c contacting our customer support team like should we instead just have said you know what sorry uh that's not covered in our policy and just been more direct because what you're actually doing is you're you're pushing the blame over to another team to go handle this and it's just going to create more work but it's a borderline one right so like that's that's a good one where it's like it's probably a good one to debate on your team and it and it's like a healthy debate to have which is like how should this agent have responded in the first place.

Yeah. May yeah I think that's a good point because maybe it should just default say like it's not in a policy because there could be all kinds of crazy edge cases right with the shoes and the boxes. So yeah and then if it's not in the policy like yeah how should how should the agent respond in that case? Um and maybe that's a rule that should be in the agent as opposed to even in the policy which is like recommend a next action. So that's like a good product product debate to have.

And I also noticed that uh it doesn't actually tell me how to contact a support agent. Yeah. You know, exactly. And I think if you look at the uh the policy from on I think it does have a support information that you can that you should be able to access. So Oh, really?

Okay. Then then the policy compliance is not good then. Yeah. Yeah. So it's probably bad.

And on top of that, the the tone is like it's fine. I think, you know, if we want this to be like a customer support bot, it's a little bit formal. Uh if you look at, you know, how we were interacting with the onbot before, it's a little bit more like upbeat, cheerful. Yep. This this kind of feels formal.

I'd probably say this is like average to bad, you know. Um but it's it's a healthy debate because then if you have multiple people labeling the data, you get better better sort of labels overall. So this is like step you we're already doing eval right like we're we're looking at the data we're evaluating it we're debating back and forth what the label should be and and it's it's kind of based on that that you're going to start building your LLM as a judge and and and like I I want to bring on the point that like this stuff is not super sexy you're like in a Google sheet but this is probably like the one of the most important things that you should get right right with your team because if going to the SI sucks then the rest of your emails will be terrible you know totally there's no point in I mean It's like it's it's the most important step before you start trying to build anything complicated on top like LLM as a judge or codebased eval like just look at the data and debate are these the right metrics for us to look at do we have the eval criteria in place do we know how to evaluate this or not um and you just start we just start with five rows of data right um just to get started as well and um I I think you actually filled out the rest of it Right. All right. Yeah.

So, yeah. So, you know, yeah, we'll go off. We'll kind of like fill this out really quick. And okay, so here we have all the responses all of the responses basically laid out from the initial questions. So, this this is, you know, basically just generating data to get started with to to kind of start grading.

And I went ahead and just started grading some of the the data as well. So, we've got, you know, in this case, it's good uh good product knowledge, policy, and tone. Tone is kind of bad. But what's interesting is as I was going through, I was actually seeing there's a couple of examples here that are kind of interesting, which is, you know, let's take a look at this one really quick. I just placed an order 45 minutes ago, but need to change the delivery address.

Is that possible? And it says, unfortunately, I have some news for you. Because it's been 45 minutes, you've passed the 60-minute window. we provide for order cancellations. So, the LLM, fun fact, LM are really bad at math.

Uh, it it seems to not realize that like 45 minutes is not past the 60-minute window. And this is this is like actual real real world data. Um, and uh and so I gave that one a bad, right? Like that means the LM is like taking the policy and just making stuff up. Yeah, that's not good.

Getting an answer. Yeah. Yeah. Um, so, so that one's like one I want to go take a look at with my team and go deeper on. Yeah.

And, and what I like to do is I like to write like little notes next to the bad ones and then and then like, you know, like in reality, we're going to be doing more than five, right? Like probably, you know, um, and like what I do at the end is like um, use the LM to summarize all my notes and be like, "Hey, here's like the top three things we need to fix with the pro product like the prompt or the the product." Yeah, exactly. I think that that's like a good example of something where the notes help you figure out I need to go take a look here a little bit more. Yeah. So, maybe like the the prompt update here is like, you know, you had like a very important please check your math or something.

Yeah. Yeah. Maybe. Yeah. I mean, what's what's kind of cool um you know, as we get deeper into this is LLMs are really good at suggesting prompt improvements, too.

So, Peter, the fact that you're like giving notes and labels Yeah. on top of your data means you can take that data and then use it back in your anthropic console or wherever you're doing development and actually prompt it again to improve on the data that you gave it. And that's like self-improving agents in a way or creating a self-improving agent. Cool. So uh so now we have our human labeled data set uh and and let's talk a little bit about this actually because this is kind of important.

So when you're just starting to build this product like how many examples should you have, you know? like do you have any rough guidelines? So, usually it depends a lot on the type of use case that you're building for. Uh so if it's like something that's very in a highly regulated environment, you need a lot of data to feel confident. It's really it's a statistics question which is like how much data do you need to feel confident in your eval in the first place?

So if it's something like you know if you're just getting started with the PC I think that there's like a couple ways to phase out your product development. So if you're going to do internal product development first and just launch this to a small subset of users or test it yourself. You can get started with I would recommend somewhere between you know five at least usually it's around 10 or more examples for the type of testing that we're doing which is we want to see if this thing is even confident for us to even worth investing further in our with our team and with the data that we have or do we need to invest in better data invest in better tooling upstream. So start with 10. Y if you're building for production and you want to get to more confidence, that's when you might need maybe a 100 examples or more depending on the industry.

So that's like a general rule of thumb which is internal test start with like 10 rows. Just take a look at the data to get started and then if you want to scale up get closer to about a 100 rows of data. Yeah, I I think that's a good benchmark because like in the beginning you're still making a lot of updates to the prompt and the product, right? Like you don't want to have to do 100 manual emails each time. I'm like that'll take forever.

Right. Right. You know, yeah, you're really there's a few dimensions as PMs. We think about things in this way, but you're you're actually trying to optimize for speed of iteration and confidence in result. And these are kind of two sort of orthogonal dimensions.

And the more data you have, the more confidence you have, you are. But the longer it takes for you to iterate, the fewer data, less data you have, the faster you can iterate, but you're not going to feel as confident. So, you need to kind of define what that looks like for your team. get started. Okay.

Um so why don't we actually uh simulate kind of update the prompt real quick? Yeah. If you go back to the anthropic Yeah. So um so let let's just say let's just say um like the like the answers are just too long, man. Like it's too much text to to read.

Like how do we make it more friendly like the tone? Yeah. So, Enthroic has a really cool uh feature here which allows Claude to optimize the prompt and you can actually just say, you know what, make it sound more friendly and less formal. So, this will impact your your tone, right? So, um so this is actually going to take a look at your data based on the example that you have.

One interesting kind of thing here is it's doing a ton of work like it's building it's building like a mermaid graph to define what friendly should even be. So it's like doing code because I think it's a really strong coding agent and then that's what's used in the reasoning to then go back and iterate on the prompt. It's like a multi-step prompt iteration flow. Yeah. In my opinion, it's it's kind of it can be a little bit of like overkill a little bit, especially since the main addition it made is just to say your role is to provide helpful and accurate information and then here's the steps to follow.

Format your response with always do this, always do this. It's like super again like super formal like rules that it's put in place. Do you need all of these rules? Is this just adding more to your your prompt? It's not clear, you know?

It's not I'm not really sure how much this will improve my prompt at scale. We can run one example just to see and maybe take a look at it. Mhm. It still doesn't sound super friendly. In fact, it it almost like got longer and uh and it's and that that's sort of the interesting thing about these LMS like you need real world data and a little bit of like taste and nuance to iterate on the prompts as well to know what data to feed in.

So um so this is an example where having human labels and eval might actually give you a better uh sort of optimization once you start looking at those results. Yeah. And I guess uh you can like you know you can also include like a some few shot examples right like of what a good responses. Exactly. Yeah.

There's other things you can do as well. Uh like this in this tool you get started you know with the prompt creation. It it writes in the user prompt. you might want to start with a system prompt. So, there's a lot of nuance here.

Um, but uh but to get started with, you know, you actually need real world data. And I think that this is one where, you know, if I'm iterating on this, it's like not clear to me that this was better. Um, honestly, I think it might might be might even be worse. Yeah. But this is like a this is actually core to like a AIPM's job, right?

Like you literally just like iterate on the prompt and run the evals and iterate prompt like 100 times and hope better. Exactly. And ideally ideally you have like some way to to do this at scale with more data and iterate with you know more confidence as well. So like that's the but I totally agree like get getting started this is the reality you are just to recap you start with initial prompts you feed in data you put the data in a spreadsheet and once you have the data in a spreadsheet you label it you figure out okay do I want to which dimension do I want to improve on you go back and you iterate on the prompt you get a new result and then that's where that's how that's what the journey looks like Yeah. And maybe like you also add like another criteria or something.

You add another criteria. I think another way to to look at this as well is um you know once you've kind of started to get a good feel of this type of data, you might want to look at a tool to help you kind of run these eval scale and feel more confident in the eval results as well. And uh so that's actually what what we're building. Um this is kind of what I work on. Uh so it's a platform.

It's called Arise that helps you actually iterate on your prompts using data and it's a good it's another kind of good starting point. It's another tool that you can kind of think about in your your toolkit where you can actually upload an example CSV. So I actually went ahead and just downloaded the the data that we have from the the Google sheet in the first place here and I can upload it and use that as a way to to kind of get started. So let me go ahead and uh upload that here. And we'll just call it Peter's on or let's call it on golden data set.

Okay. Our very rigorous five example golden data set. But you know what? Fi five is better than nothing. You know, like that's the best part.

Like it's it's so much better to start with some data that you can then kind of iterate on top of. And so that's that's really what the whole point is is just start somewhere. Now we've we've moved our CSV over to uh Arise where we're going to upload it as a data set. And then what's really cool is we can it's the same data that you saw in the CSV already. But the beauty is that we can take this data set and actually iterate on it with our eval kind of set up in a in a kind of userfriendly environment.

And so this is the same prompt that I had from my my spreadsheet. These are the variables, the same variables. And then if I look at this, this is every single row I already put into the spreadsheet. And this is actually loaded in. So I can replay multiple examples.

You know what we were doing before, Peter? We were looking at like one example at a time. Yeah. And trying to figure out, okay, is this good or bad? Here, I can put in hundreds, thousands of examples even, and replay in my prompt what the new output is.

On top of that, we can even add evaluators that sort of match what we were looking at in the first place in the spreadsheet, which is our our sort of criteria. I actually just copied this in as the prompt. I said, take a look at the output from the playground, which we're going to run. And the job of this is building an LLM as a judge type of system. So, this is actually the eval prompt.

So, this is actually taking the the sort of the criteria that we had from the spreadsheet and we're making that a prompt for an LLM to give us a label. And I'm saying here's the output, here's the question, here's the product information and the policies. Give me a score or label of good, bad, or average based on that criteria. Yep. And we've got three eval here.

So, the same three dimensions we were looking at before. We have product knowledge, policy compliance, and tone. And it's really it's just kind of encoding the same information we had from from before. Yeah, there's a table that we had, right? The the criteria table.

Same table. So, let's go ahead and turn those on here. X out of this. And now I can replay it. And I can do things like try out a different model and see if that gets me a better result.

Let's maybe let me You want to try like uh you want to try GPT5? We got GP. Yeah. GB. Yeah.

All right. So, let's see. Um, so we've got, you know, instead of comparing cloud, now we're comparing it to GPT and we're going to try and regenerate the same results and see if this this is better or worse than what we we had initially. Is it the same five questions or is it generating same five questions? Same five questions that we just that we just ran through.

So, this is I can even uh show the question. GBD5 might be a little bit slower because I think a lot of people are probably hitting it today, but let's see. Um, we can while it's running, we can take a look at one of the questions here. The question is, I'm training for my first marathon. I need something with maximum cushioning.

What shoe would you recommend? And then this is the answer. Says, hi there. Big congrats for maximum cushioning. I recommend the cloud monster, a couple of great alternatives, and it also gives me more shoes here with the product information.

It's pretty good. Um, yeah, it's pretty good. And it it what's what's interesting is, you know, it has it's actually like pulling that product information and doing a pretty good job. What else is cool is I was running those eval the text in the first place. So I actually have the compliance, product knowledge, you know, tone, all of that information sort of as eval rows.

And so what's interesting is I can actually go and take a look at that uh you know in a more granular way and say like what are my eval what I just generated and that's actually just new columns here. Okay. And and now the AI is doing the eval GP AI is doing the eval. What else is what else is really powerful here is when you're doing AI eval using LLM as a judge, I highly recommend, especially when you're getting started, have the LLM create an explanation as well. And why that's useful is that's a lot like having a human give you notes on why the LLM is giving you a label.

So you can see here this is the eval for policy compliance explanation and it says the response aderes perfectly to the company's policy. So these this is this is new right like this is information that you can use to make a judgment whether the LLM as a judge is giving you a good eval or not. Do you agree with the explanation it's giving you? Yeah. Does that make sense?

Can you find uh has it actually rated anything bad or No, it gave everything good. What about some of the other criteria? Yeah. So, that's that's sort of the thing where like if we take a closer look here, let's take let's take a closer look at some of this. So, personally, I think that you know this might be a definition between how we've created the eval in the first place or what our human sort of judgment looks like.

But if I look at the response here, it says, you know, oh, I'm really sorry how your cloud boom strikes wore out. It's really frustrating. Uh, here's some recommendations. It's super long, right? Like it's like a really verbose sort of answer that it's giving to the user.

So, what we can do is actually put human labels on some of this and actually compare the human labeled. So you know from this I can I can in the same platform I can create human labels or just upload them as a CSV the same way that we did before and then we can use those human labels to compare to the LLM as a judge labels in the first place. So that kind of gives us a good sense of is this result good or bad based on the human label and does it match the LLM as a judge and then that can tell us how good the LLM as a judge is because it's just giving everything good. So do we even trust this result or not? Well, we kind of need human labels to verify and align with the LLM as a judge.

So, yeah, my takeaway is like from this is you want LLM as a judge to align with your human label and the the judgment that you're giving it. Um, so, so like this is like a toy example, right? But in a real example, you probably have uh for LMS judge at least like 100 plus or even more examples, right? So, like as a human like I I don't want to review all 100 examples one by one. Should I look for uh examples where they're bad or like how how do I look at this stuff?

Yeah, I think it's helpful to start with at least a few like five or 10 to get started with like uh like kind of before you remember how we were talking about designing a prompt for the agent and labeling that data in a spreadsheet. Mhm. That's the human eval on your system prompt or your agent prompt. you need to take a similar approach with providing labels against the eval labels for your LLM as a judge. And so when you start with like five or 10 examples, you can start figuring out, do I trust the LLM as a judge or not?

And then you can go run it on a 100 examples and see, okay, what's the score on 100? Let me go look at the bad ones. Because right now, I don't even trust the result on these five, right? Like it's just saying everything is good. So I need to actually label these with a human label and run the LLM as a judge on this again to to see the match rate.

And that's actually that's actually a a type of eval which is called match rate which matches the human judgment with the LLM as a judge and you can see how much those line up. You can we can run those really quick and see. Yeah. And you can but do you have the human labels there or Yeah. So I have the I have the original human labels that I'm going to compare.

Yeah. Um but we can we can go ahead and uh actually yeah we can just go ahead and label this in the platform too. Um if you want to do that. Yeah. Let's let's look at let's look at one example.

All right let's look at one. So yeah so what we can do is um let me go ahead and go back here. You can actually create a labeling criteria here. Uh-huh. And so I could say like uh let's call it like Peter's Peter's eval.

I'm just going to assign myself can assign you to Peter. You're in you're in the account. Um and we'll say okay look at look at all of the outputs and give me your judgment. And we're going to put the same annotations that we had before. So we'll put uh we'll put these actually do categorical.

So you have to do a little bit of setup here. Um but we'll do product knowledge. We'll just do good, average, and bad. Okay. Yeah.

So we can test this one just to start with and basically say like does it have good product knowledge or bad product knowledge. Actually I kind of like the tone one too. Maybe we can just do that really quick. Yeah, let's do it quick. Yeah.

So we'll do tone and we could say like good average bad. So I know this is also like not the most uh oh let me call it tone for on. And that's going to create the labeling queue. And we're going to send these examples to a labeling queue there. Okay.

So now it's going to compare the human labels with the LM labels. Ex. Uh yeah. So this is comparing the uh the this is actually just doing the human label on the output. So we we're going to label the data again here.

So we're going to say like is this tone good? I think we're saying like the tone is kind of bad because it's kind of long, right? Yeah. long response and we could say, okay, product knowledge. So, we could take a look at a few of these um and say, okay, like is this good or bad?

I think in this case, you know, it's it's kind of hard to say from the from here. You're reaching out about the cloud monsters. You're within our three 30-day window. So, I mean, that's good. So, we'll just kind of go in and do that really quick as well.

Yeah. I mean, they're really they're pretty they're pretty long. Okay. So, we got a few of these now. Okay.

Good. So, now we can do the that that step that we were just uh where we have human labels and we're going to compare the human label on top of the EVA label. And we're just going to go ahead and do the tone match really quick. So, I'm going to go ahead and say take a look at this column. We're going to call it just we just named it from our eval, right?

So it's like tone annotation tone on label and we're going to compare that to the eval for tone. And what it's going to do is going to give us a match or no match score on that output in the f in the first place. And we'll do the same thing here for product knowledge. Okay, we didn't end up doing the policy, but we'll we'll just go ahead and run those two. Give that a second.

Okay, refresh the page. All right, so we have our score here. So, this is our match score of the experiment that we just ran, which is does the tone match? It looks like 100% of the time the product knowledge matches, but the tone only matches once in from our human labels. So this is an example of where we probably have some room for improvement for our eval based on the human labels that we had.

Makes sense. Yeah. Yeah. Then uh so so now you basically have both the prompt for your actual product and a bunch of prompts for evals. So so given this thing you should go off and improve the tone eval prompt, right?

Exactly. Yeah. you should go improve the tone eval prompt to basically be stricter on how long the answer to the response is. Maybe you want to put like criteria there which is like don't respond when it's super long. You know, don't don't say it's a good response if it's really long.

And then you can take this information and even go improve on your system prompt back in the anthropic console and say or in with an arise as well. You can just take that same system prompt and if we create another experiment here, we can pull in that prompt here, the same prompt and we can say don't respond super long and we can test it against that eval as well once we've done that. Yeah. All right, man. This is this is super this is great.

This is super practical. So, um let's just kind of recap the whole process for our view viewers, right? So I think uh just recap we're trying to build a on customer support agent for for shoes and the first step is to write the prompt right and and try to gather the relevant information the policy and the shoe information in the prompt. Um and I think the second step was to uh uh create the human the create the eval criteria like like the three different buck buckets. Yeah.

And the third step was to do manual evals with like, you know, a bunch of example questions and and try to score the Yeah. score the answers in your spreadsheet and then, you know, you and I can debate it. Yeah. Exactly. Start start with a basic prompt.

Yeah. Yeah. And then you've got Exactly. I mean, this is this is basically all of the steps live in the process. Yeah.

Okay. Yeah. Yeah. So, let's walk through this. start based upon categorize uh and define failures.

Uh yeah, so that's basically the eval criteria and then uh you do the manual labels. Yeah. And and like the manual label like that step is like pretty involved, right? Like you probably take like a good amount of time on that step just iterating on the prompt, iterating on the criteria. You know, there's probably like a lot of work there.

Totally. I think this is like manually label and debate and then I think that there's a ton when it goes into like actual iterating. This is this is probably like a step in between which is like iterate on the actual data. Yeah. Yeah.

That that is like a that is like a you know that like a loop that goes back and forth maybe like I used 20 20 times. Yeah. Yeah. Exactly. Exactly.

It just goes back and forth like a bunch basically to start at least initially and then you can start thinking about LLM as a judge. Yeah. Eval 100 rows for like start with 10 rows align with the human and the goal is really align with your human labels. Yeah. But like before you go to prod or something or even run like a a test you probably have at least 100, right?

100 examples. Yeah, exactly. Yeah. And that's what that's what this would look like. It's like align with human labels and then get, you know, once you feel good about like the 10 examples, then do the same process on 100.

Yeah. Yeah. Okay. 100. Um then then you know we haven't already covered it but um like you should probably launch this thing as like a AB test first like maybe like a 10% of traffic or something.

Mhm. And then uh see if the actual users complain or not right. Yeah. AB test maybe you know like 1% traffic or something depending on the the type of company you have right. Uh start internal usually internal.

Yeah. Plus maybe 1%. You really I think like people dog fooding their own product helps a ton here too. So you can kind of get a feel for like if it's good or bad. Yep.

And then you actually get real world data and that's what gives you uh back here. That's what gives you like a good sense of the overall basically like how good is the system overall. Yeah. You know, I I I thought about maybe like making the actual users be the labelers like like if if they thumb thumbs down or say something is bad like or if if they want to get feedback on a product like I thought about maybe actually like um letting them score the policy compliance saves the team a bunch of work. But I I haven't really seen that being pulled off.

Have you seen it being pulled off? You know what's interesting about that is Yeah. Having your customers actually label your data will give you it will be a useful signal for you for sure. This is where the the customer sort of like labels come in. But and and you should take a look at that data for sure.

The problem is that let's say you have an example where you're you know you're frustrated with your onsport bot Peter that you that you now have to interact with and you say you know you give it a thumbs down when it says you're not eligible for a refund. What does that actually mean, right? Does that mean that your support agent did something poorly? Is it just that you're mad at the support agent, so you gave it a thumbs down? Like, how do you interpret that signal?

So, there's a few questions that I recommend folks ask their teams and debate with the teams, which is what happens when the eval is good, but the business metric goes down. How do you break that tie in the first place? like if the thumbs down comes from a user, but the system looks like it's good in the first place. Like that's a really really important question to ask because in this world this this is non-deterministic and your LLM is going to produce different answers for different inputs and you you know you don't always know whether you should trust your user's label either. So that's a really good example of you have to go back and look at the data again there.

Got it. Yeah, that makes sense. Yeah. All right, man. Well, this is this has been super super great.

I'm I'm glad we're able to do this live. uh as as people can see it's kind of messy like you kind of have to go back and forth a lot. Yeah. And figure stuff out. But uh yeah, this is what eval looks like in practice.

Yeah. Thanks so much for having me on. This was a ton of fun. And yeah, it is super messy uh to get started with. You know, it's kind of funny like people are always looking for a silver bullet, but I do think that PM's sort of understanding how this process works is going to be really important for us to live in a world where AI products actually work and don't suck in in the real world.

So, thanks for having me on so we can talk about this and build real world AI products. Yeah, man. And and where can people find more of your stuff? You can find me on uh on LinkedIn and X, but you can also just go to amman.ai AI and uh you'll find all the different links to subscribe and uh yeah would love to to chat with folks that are building real world eval or real world AI systems too. Awesome man.

It's always a pleasure chatting with you my friend. Yeah likewise. Thanks again. Good to see you. All right.

I bitter.
