---
title: "AI Evaluations Clearly Explained in 50 Minutes (Real Example) | Hamel Husain"
guest: Hamel Husain
publish_date: 2025-09-28
youtube_url: https://youtube.com/watch?v=uiza7wp1KrE
channel: Behind the Craft
keywords:
- ai
- coding
- metrics
- product-management
- leadership
---

this looking at data accounting. You can get insane value by just doing that. And that's the one part that everyone skips. I'm going to use a spreadsheet to drive home the fact that this process can be dead simple and you can get immense value out of it. When you see an average score of 3.2 versus 3.7, no one really knows what the hell that means.

It's not really actionable, honestly. They're like, "Oh, it's like getting better." Honestly, like nobody really knows whether it's getting better or not. So, as a product manager, if you ever see the word agreement, you need to pause and be like, hm, let me dig into this, please. If people don't trust your evals, they won't even trust you. You're done.

Okay, welcome everyone. My guest today is uh Hamill. Haml has trained over 2,000 PMs and engineers from companies like OpenAI, Anthropic, and Google on how to run AI evaluations. He teaches the most popular course on this topic at Mayheaven. So really excited to dig into these best practices and I feel like I made a lot of mistakes that you know and have a lot of assumptions that Haml can help.

So welcome. Really happy to be here. Excited to talk about evals. All right. So you know there's been a lot of like online debate about like you know are evaluable or not like blah blah blah on Twitter and and um let's just make this really practical.

Um like let us talk about evals for like a real product like like do you have a do you have a product example that you want to talk about throughout? I do. Yes. So there's a company that I've been working with. Let me share my screen.

Sure. So just to set the stage, Nurture Boss is a AI powered property management assistant. And so it's a really interesting use case because it's actually one of the best teaching examples and I love using it because it's messy and there's enough complexity to where it's realistic. And so the question comes like oh okay like how do you do emails? So like lot a lot of times when we talk about emails you know we can show toy examples but sometimes those are oversimplified and it's hard for people to generalize that like how is how am I going to do that for my app?

my app is complex, you know, I have other things going on. Well, that's what we're going to show today is actually we're going to look at Nurture Boss's data together and we're going to do like a minimal set of evals and we're going to do that very quickly. Yeah, that'll be awesome. So, I know on your podcast you had Aman on already. He may have talked about Arise.

There's a lot of different solutions out there. The ones that I come across the most in practice are Arise, Brain Trust, Langmith. Those are like kind of three popular ones. Mhm. One of the observability platforms that nurture boss used in the beginning was brain trust.

They actually like created their own but for but I'm going to show you their data in brain trust cuz that's where we have it anonymized. Traces is basically like the chat conversations right with nerbos. Okay. I'll show you what a trace is. The best way is just to look at it rather than me trying to define it.

So I'm just going to open one. So trace is a log of all of the history of a particular interaction that your user might be having with an AI including all of the internal things that might be going on that the user doesn't see. Okay. So this is example of a trace. And so what we see here is we have the system message.

So you are an AI assistant working work as a leasing team member at the arrow and you have different instructions on how to interact with the res the resident or the prospective resident. You know for example how to deal with maintenance requests or um you know what to do with prospective residents and tour scheduling and all kinds of things like applications. Yep. And you know you can there's a lot of instructions here. We don't need to read all of them.

We can scroll down and we see here where is the building located is one of the questions the user is asking. Mhm. And so there's a tool call made. Get communities information. We can expand it and it's pulling back some information.

It's making a tool call. The tool call returns with some information which we can see here. Um and then the assistant is is giving an answer. you know this the arrow is located at this address and then it's the user is saying I'm interested in a two-bedroom what's available and actually then it stops um it just dead ends and um there there is a failure of some kind it just wasn't surfaced to the user so this is not like necessarily the most interesting error um this is just like you know something that you would see in the real world now this is example of a trace so So when Jacob came to me, I said, "Okay, Jacob, this is what we're going to do. We're going to look at traces." And he's like, he's like, "What do you mean we're going to look at traces?

This seems like we're going in the wrong direction." Like, "This is going to take forever, Hamill. Like, this must be like what what are you like, what are you doing?" He said, "Just trust me. We're going to look at about 100 traces and just we're just going to write notes about what is going wrong. The first one may be painful, but we're going to get really good at it. By the time we get to the 10th one, we're going to be really fast." So, we got to this one.

We're like, "Oh, like something happened here." Um, the conversation got cut off. Um, it failed. We had to do some investigation to figure out like what's happened. But we just wrote a note. And so, in this case, um, we can make an annotation.

So, I would write a note saying like, hey, there was an error that was not surfaced to the user. Okay? Just write a note. um you know, end the conversation deadended. The point is not to do a full root cause analysis.

Just observe what's wrong. Okay? And that's all you got to do is do this. Do it like 100 times. Yeah.

Do this 100 times. Now, Jacob's like, "What the hell are we doing? Why are we doing this?" Like, I hired you, Hamill, for evals, and you are like a monkey looking at this data, and like I don't understand what is going on. Like, what is the purpose of this Hamill? this is a very expensive consulting engagement and we are looking at data.

I said no trust me we are going to this is going to lead somewhere. Well I mean you're basically human labeling this data right? You're basically saying I'm basically human labeling this data. So let's look at a couple of more like um I think it will become clear why this is valuable really fast. Okay.

So this is another trace. You are leasing team member at the Meadow Brick Gardens and your name is Taylor. So giving it a name. uh your goals are to answer questions. Okay, so it's really the same thing.

You have, you know, uh you're fielding calls from from residents um actually prospective residents because this looks like it's like a salesfunnel type of mode where you're like encouraging customers to schedule tours. Um so let's go to the first user message. So we got the system message out of the way. The assistant says this call, so this is over voice now. Okay, this call may be recorded blah blah blah.

And the the only thing the user says is preview program. I have no idea what that is. Maybe it's something in the system prompt, but I personally don't recall necessarily what that is. The assistant says, "It looks like you might be interested in learning more about community and possibly scheduling a tour. Would you like to schedule a tour?" User says, "No." The assistant says, "Seems like you might have a specific question or need assistance with something related to the our apartment.

How can I assist you? Can I tell to a representative?" Obviously, they're trying to talk to a person. Uh, sure. I can connect you to representative. Um, would you like me to do that now?

Yes, great. I'll connect you to representative. One moment. Would you like me to connect you? I'm already frustrated.

Like, yeah, it's the person to a human being already like so many questions like, "Are you sure? Are you sure? Blah blah." Uh, so okay, like ADU, he wants to talk about ADU. It sounds like you might be interested. Yes.

Could you clarify your query? I just want to talk. We've all had this experience at one point in other in our lives. Yeah. Every time, man, I call.

Yeah. Yeah. This is not, you know, I want to throw my phone out the window whenever I have this interaction with an AI. Um, so, okay, I understand. I'll connect you.

And finally, a tool call is made. We're transferring the call. Okay. So, we feel the pain of the user. We we do honestly.

Um, and it's pretty clear like, hey, we So, this this is an this is a clear error in this case. I'll write the the note here just like it to the other one. And you're not trying to like write solutions. You're just trying to write like the note of the problem. Yeah.

I'm not trying to debug it. I'm not trying to say like why it happened. I'm not trying to root cause a solution. I'm just journaling why it happens. So you do this.

It took us frankly it took us like an hour to do 100 traces. Didn't take us long at all. Okay. But by the end of it, we knew a lot. Like we learned a lot and we learned way more than you could possibly learn by trying to throw any kind of automated solution at this problem.

So if you tried to come at nurture boss and put a hallucination score, toxicity score, coherence score, whatever you want to call it, it would not have given us anywhere close to this insight that we had right now. You know, we identified very specific failures and things that are painful, right? By looking at the data we immediately could like see that did you uh use some AI to like summarize the trace data that you labeled or Aha very good question. So while you shouldn't use AI to like do the you should definitely look at the data put your hands on the data you can use AI to help you do the analysis of it. So what happens is I exported all of these logs plus the notes into a spreadsheet.

Okay. Okay. Um, and you don't have to use a spreadsheet. I'm going to use a spreadsheet to make it to drive home the fact that this process can be dead simple and you can get immense value out of it. So what I did is I exported like all the notes.

So in this column, column A, you have all the notes that I took. Yeah. Okay. So like you know, one note is user was probably asking about lease terms or maybe deposit not about specials. And the AI was talking about specials or another one was the AI offered virtual tours but there is no virtual tour.

Um, okay. You know, so all these different and there's the disperate messaging one that we just saw. Okay. And so all these different notes that it took. So what you can do is you can take these notes and you can do something really stupid simple is you can dump them into like claude or chat GPT or whatever and I say okay please analyze the following CSV file.

There's a metadata field which is nested field called zenote that contains open codes. So this is like some terminology here. Open codes is just a fancy word for those comments that I made. Okay, just the notes for analysis of LLM logs that we are conducting. Please extract all of the different open codes from the zenote field.

Propose five to six categories that can we can create axial codes from. So the axial code is another piece of terminology that means we just want to group them into C. We want to group these notes. We want to just classify them. Okay, this like open code axial code thing is actually some really old technique from social sciences and it's been also used in machine learning for decades.

And so that's why we're using this terminology as a shortcut to give to the LLM because the LM knows exactly what this means. They're like, "Oh, I know exactly what you're doing. You're trying to do this technique." Got it. Okay. So, it's better than just saying it's better than just saying like categorizes stuff.

It's just some shortcut technique. Yeah. Yeah. It know it has like it it gives it some specificity. it like kind of by saying open code axial code it knows like what my goal is because there's a lot of context when I use that terminology in this technique you could also say categorize though I mean there's no you can start wherever you want so if you want to say categorize start with categorize totally fine it's you know the point is make progress and get value as fast as you can I don't want to be too prescriptive but the point is like you can sort of uh so like okay it kind of iterated a lot on how to open the CSV so We can skip that.

But it gave me it gave me like um you know some categories and I didn't really like I didn't necessarily like all of them and I could have been you know I kind of went back and forth a little bit to refine the categories that made sense to me. Um and I just like took I wrote down some categories actually. Um and here are some categories here. So I said like okay tour scheduling rescheduling issue, human handoff or transfer issue, formatting error with the output. They had some formatting errors um like putting markdown inside text messages for example.

Um conversational flow issues. So that's like the text thing where just abrupt you know the flow. um making up promises not kept like rescheduling and things like that or not rescheduling but other kinds of promises um and then there's another I usually have another field called none of the above but I didn't do that here just out of simplicity okay and so what you can do is then you can kind of go back and forth and what I did is like in the spreadsheet you know you can use AI so there's AI in this Google spreadsheet the Google Google sheets have AI um you can have the AI formula that's very handy to to show you something. So I say, "Okay, categorize the following note into one of the categories." So you're just like c using LM to like categorize it. And you can see I'm just categorizing these notes that I took like the problems that I found.

I'm just putting it into categories. Well, I did know that Google Sheets has this AI feature already. Okay. They're usually very slow. It's cool.

It's cool. It's can be slightly janky, but it's okay. It's lightweight and you don't have to use any tools and everyone can understand how to do this. is like demystifies the whole process of what I'm doing cuz if I like open some code you might think oh like you need to be like software engineer to do this or something and like no you don't uh we can use English all the way. So now you have categorized all of these things and now we can use one of my favorite tools pivot tables.

So pivot tables um you know if you haven't seen them before really handy in spreadsheets so you can just count how many times each of these categories occurred. Okay. And and we can see the just at a high level um hey oh okay we're having like this conversational flow issue is happening quite a bit. Um you know we also have this like human handoff uh transfer issue and you can kind of get a sense like right away uh what the problem is. Now it is likely that before you even get to this count you already know you've looked at 100 traces.

you know in your gut you're like okay you know what I'm going to I need to fix this like human transfer thing like right now you're like I don't even need to like do a data analysis but it's like quick this takes like like less than a few minutes honestly and it just gives you some grounding and it's like lets you see you go from this like mess of like I don't know what's going on to okay like I have some idea about the problems that I have and you have some starting point. Does that make sense? Yeah. Yeah. This is brilliant, dude.

But but let me ask you this question. Yeah. So, um in this case, the agent was already live in production before you started doing all all this stuff, right? Like like um but that's not the ideal approach, right? Like I ideally you want to do some of this before or maybe dog food with your team first or like get some users try it.

Absolutely. How do you Yeah. So the best case scenario is you dog food it with like you know some friendly customers, you dog food it yourself. That's going to be really good. You can also synthetically generate inputs into your system.

So basically what you can do is like think about plausible user questions they may have and you know and try to come up with some hypothesis of where your system will break. Yeah. But there's a certain way to do that. You don't want to just ask an LLM, hey, come up with plausible questions for a prospective tenant that might be looking to rent an apartment. The right way to do it is to come up with some categories.

So, is to come up with some dimensions. And what I mean by that is let's say um let's let's think about what good dimensions might be for nurture boss. So for nurture boss uh you might have like resident uh you can have okay like type of customer maybe apartment class maybe so like luxury standard something else I don't know what that is I'm not that creative to like think about on the fly but what was the thing you suggested just type of customer right you can you can get the tenant manager versus the actual resident right depending on who you're talking to yeah uh resident uh manager. Yeah. And you can think of put your product hat on.

So like by the way this whole process is is very product oriented like so you know when you read the trace it's not so much about engineering it's putting your product kind of hat on and saying is this the experience that you want your user to have? Does this actually make sense? when it comes to like these dimensions I'm talking about, you're kind of putting your product hat on and saying, "Okay, what are the different personas? What are different categories, different dimensions that you may want to consider?" And then what you want to do is like you know you would take um the kind of combination of these um you know so like luxury resident luxury luxury for resident luxury for manager standard for president standard for manager and you would feed those we call it dimensions into an LLM say okay these are the different dimensions for this for every one of these dimensions generate plausible user queries got it that's like way better than just asking an LLM. Yeah, just because um if if you just ask an LLM, it'll be more a lot more homogeneous and you don't want to be homo you don't want to have homogeneous inputs.

You want to explore the space of inputs and so these brainstorming dimensions helps you to kind of make sure you're you're exploring the space being thoughtful about exploring the space. Does that make sense? Got it. Yeah. You want to find all the edge cases and like you know Yeah.

Got it. And that's just scratching the surface of this. There's a lot more to generating synthetic data that we could probably get into here, but there there's like more advanced ways to generate synthetic data or things to think about in terms of being more adversarial, how to, you know, come up with hypotheses to help you break your system, so on and so forth. But the short answer is use our system and you can use LMS to help you help basically pretend as synthetic users. That makes sense.

Okay, let's go back to the categories you have on the left. So uh so now you have these I mean they're not they're basically pro problems right problems with the product and uh now what are we going to do with with this stuff is this is how we come up with our criteria or should we just start fixing the issues or very good question next very good question so um when we first did this what the top issue was date handling it's like and it was very clear uh you know the the user wanted to schedule an appointment Yeah. And it was always getting the date wrong. And it was very clear like, "Oh, this is so dumb." Like the LM doesn't know what today's date is. We just Okay.

We just like forgot. They like, "Yeah, they like forgot to put that in the prompt." It's like, "Do you really need an eval for that?" Maybe not. Like, you know, you don't want to eval. You don't like necessarily want to do eval cuz like it feels good. the whole purpose of anything is to make your product better and to and to iterate and you know move fast.

Um and so for that one we're like well let's see like let's just give it what today's date is and that problem basically went away unsurprisingly. So we didn't really need an eval from that. Um other things that more subjective or you know so there's a it's a costbenefit tradeoff. So there's two kinds of evals. One is LM as a judge which we are going to build together.

Another one is codebased eval where you don't really need an LM as a judge. It's some kind of assertion that you can make and that's very cheap compared to LM as a judge. And so uh for the date one we actually did we did the like a codebased eval which is like we had some test cases and we're able to test like does the date that's coming out equal to the expected date. And that was like very cheap. We didn't have to do LM as a judge.

Got it. You know, but that was like really easy to fix. Now something like, hey, you should be handing off to a human like, okay, that one like we don't know exactly like we did have rules for that already, but the LM is struggling and like we don't really know how we're going to do it. That seems like a really good use case for an LM judge. And also the the eval is going to provide tons of value even though it's expensive more expensive because we're gonna iterate against it a lot to make progress and so we said okay like let's you know okay we need an LLM judge for the human handoff let's go ahead and do it it's an important problem also.

Yeah. Yeah. The main problem that people encounter when doing LLM as a judge is they just prompt another LLM to kind of judge what your LM did and they say is it good? Now that should that should be suspicious, right? Like why is that okay?

Like why you just going to tell another LM to tell me if it's okay? Like I don't know. And you would be right to be very suspicious of that. And there is an answer to that. And the answer is you can measure the judge.

So it's like an it's a meta evaluation problem is like you need to measure if the judge is good. It's very important. You don't want to skip that step because if you have a bunch of judges LM judges floating around and your stakeholders are like you're reporting them on the dashboard your stakeholders looking at them and everyone's like oh the judge you know this no one's going to understand what you're using LM judge anyways. They're just going to look at your metric and and when there becomes a significant there's enough gap between reality and your metrics, no one's going to trust you anymore. You want to avoid that.

You want Y cuz like if people don't trust your evals, they won't even trust you. You're done. Yeah. Exactly. Yeah.

You can't you can't make it have like perfect scores for something, but it's actually totally wrong, right? The way you manage it. Yeah. Yeah. And so Okay.

So, how do you go about this? Well, thankfully when you're doing this axial coding stuff, right, you actually I've identified really good test cases or some reasonable text uh test cases that you can use that are labeled. You you already labeled them as a human. So, you have some ground truth. And these are things that you can use to calibrate an LLM judge to see if you can create a judge that's good enough.

Okay, green enough is just like green up is like how closely does it match to human labels, right? That's kind of what how close does the match to human label? Yeah. So that's what we're going to do next is we are going to think about first we're going to write the prompt and this is like the dumbest prompt. I'm not saying like this is a good prompt.

This is just a prompt. And the point is not to like have a prompt recipe or some like magic thing is just to iterate. Okay. And you want to just specify kind of the requirements of like in this case what is a good handoff or when should you be doing a handoff and when should it happen and so you know you are scoring a leasing assistant uh to determine if there was a handoff failure there should be handoff if any of the these things occur um you know or sorry there there is a handoff failure if any of these things occur like if a human requested to be handed off, but you just ignored them or looped through it too many times. That's a failure.

Got it? Yeah. And there's a list of these seven failures. You don't have to read all of them, but you get the idea. And we also say when there's not a failure, just out of completeness.

And we say we want to return exactly true or false, binary. So, it's worth lingering on this for a moment. So, it's very important for an LLM judge that you output a binary score. 99% of the time you don't want to import uh export like a like art scale or a you know a score of one to five um or some kind of score because that introduces tremendous complexity. Yeah.

You know LM's are not good at continuous scores number one. Number two is the output is not going to be clear. When you see an average score of 3.2 two versus 3.7. No one really knows what the hell that means. 3.7.

Yeah. Yeah. No one. And it's not really actionable, honestly. They're like, "Oh, it's like getting better." Honestly, like nobody really knows whether it's getting better or not.

I found that when you try to hide behind a score, you're not really making a decision. And like what you're trying to the frame here is is this feature good enough to ship? Yes or no? Make a decision. You know what?

What is the line? there is a line somewhere and so like there has to be right and so we don't want to score um wherever possible you want to simplify it the score just makes it too complex yeah it's like uh fake science you know it's like you know false precision right like who knows yeah it can be yeah it can be there's some like there's some evals where you want a score when you get when you go very narrowly into certain aspects of things like you know when you try try to have evals for retrieval search and like different components then the scores make sense but for this like as a judge case in the overall sense like no and and why why no explanations though like why why don't you want to explain why I marked so explanations actually usually good um so you do you you know what we teach is you want explanations and then a score but this is like a spreadsheet and so we just want it to be tractable if I try to give an explanation then it would like and you know the model here in the spreadsheet isn't the most powerful one they give you. So, uh it was going all over the place. So, I was just trying to simplify it here. But yeah, explanation can be good.

It can help you debug the AI model. And you want to give a structured output. You want like a field. You want to usually output two fields like you want it to output like an explanation and a binary score. And then you can use the explanation to kind of help you debug what went wrong with the LM's thinking.

Oh, so you're actually going to do this LM adjusting using the Google sheet model AI model. Yes, I'm gonna stay in the Google sheet because our goal is to demystify everything and to make it very clear like what is actually happening. Okay. By using a spreadsheet all the way down. So, uh, okay.

So, we have this element judge prompt and now we can go back to those traces. So, we have like this is the original trace column A. This is just in a JSON format. Um and then we have sort of this LM as a judge. So this is like for one error.

So you want them to be scoped usually. So we have this LM as judge just for the handoff error. And we have the formula assess this LM trace according to these rules. Okay. And then it's the LM judge prompt that I just showed you.

That's all it is. And then it's giving us true true or false. Okay. So we have true or false here. And then this is this this column H is the LLM judge handoff uh the like what it said by the binary score true or false is there an error and then this is the human label column G there's an error okay so we have these two labels and we already did column G before that was kind of happened for free because of the axial coding in the in the open coding the process oh so you you have like another AI no the human label is like the notes right so So you have yeah those are like the results of the notes.

Um you know like basically I said hey if the axial code is human handoff or transfer issue I just said it's true otherwise it's false. Got it. Got it. Okay. And so you can then see how aligned the LM is to the human.

That's the main thing that you want to test. Now one thing you want to stay away from. So a lot of people go to just calculate agreement. intuitively it is makes sense right like let me calculate the agreement between the LM and the human it seems like a it seems like a plausible metric it seems like oh that sounds reasonable okay like agreement sure yeah the problem with agreement is most errors hopefully if your system is not jank most errors are not you know happening kind of at the tail like so this human handoff error is is not happening every single time it's maybe happening 15% of the time or 10% of the time, right? Got it.

And so if something is happening 10% of the time, how can you agree with it? So it's like if something if a system is saying something is failing 10% of the time, you can agree with it 90% of the time by just saying it never fails. You'll be in 90% agreement. And 90% agreement seems really good on paper. you go into like a stakeholder meeting like yeah I have a judge you know 90 90% agreement like okay that sounds good no that sounds really bad actually uh potentially you need to like really dig into that so as a product manager if you ever see the word agreement you need to pause and be like hm really let's uh let me dig into this please like and so you need to measure two quantities one is and there's different way there's different uh terms but true positive rate and true negative rate so those are just and there's different words for it sensitivity specificity precision recall there's different words but I'm true positive rate true negative rate and so true positive rate is what is your ability to successfully identify the failures like when the failures actually happen and what's your ability to successfully identify when failures don't happen And that's a better those two quantities are kind of better than agreement because they will show you when something is off like you know and so to make this more concrete because it can be a lot in your head like oh what am I saying right now like why isn't that right and so let's go here to this confusion it's called a confusion matrix it's funny that it's called a confusion matrix sometimes it causes confusion but hopefully today it won't cause confusion what you have here is like okay in this column you have the human label.

Okay. True or false? False and true. And then in this going across here, you have the LM judge label where the green diagonal is where they both agree. Yeah.

Okay. Cuz this is like 100 traces. We have 70. So when the human says it's false, the LM judge agrees with it. Okay.

Like out of you know the 73 times, but then when the human says it's false, the LM judge thinks it's a there is an error 18 times. Interesting. There is a different there's different kinds of errors and this is what I'm talking about here. You don't want to just go in agreement. You want to know what the true positive rate true negative rate is.

Now, how do you know what a good true positive true negative rate is? There is no magic bullet there. That's a business decision. Like what what level of judge are you is is like okay for you in in the in the most base case. You just need to do a sanity check.

Like does it make sense? Okay. Like you know does it seem okay? Calculate the true positive rate, calculate the true negative rate. Is one of them like really bad?

Okay, then maybe you don't want to use that. Um is it really low? Um or you know just look at the confusion matrix do whatever you know and you can use a spreadsheet and say hm is this okay? Like am I okay with this kind of error? Um you know give yourself an intuition.

often times you I would say for most people who haven't are not used to true positive rate true negative rate it takes some time for it to click even I have to think about it sometimes honestly even I've been doing this for years just to like ground myself I mean I think the confusion matrix is actually way more clear than the percentages I mean yeah 18 where it's marked as true when it's false yeah right yeah so there's a problem when it's false you like you know where it's false is where there's um you know out of these 91 times you have like 18 of these 91 times it has this specific error is that okay you know so basically so basically 18 times it actually did successfully hand off to the to the human to the human uh sub support but like the LM thinks it did not or like there's too many turns or something yeah yeah the like 18 times it LM thinks there is an error when there's not right is that okay and so like you know different sit situations you might be uh like the the false positives are not as expensive as the false negatives, you know? So like you you might be okay with catching things like catching more errors that don't actually exist. You just want to make sure you do catch all of them. So then what do you do with this 18 like you look back at the traces, see what happened and then you try to modify the prompt. Yeah.

Yeah. So what you do is you can look at these like 18 um and you can you know you can say okay like what happened here and you can iterate and you keep iterating a bit on the prompt. Yeah. Um and often times it's quite straightforward. Um sometimes not as much but one thing I did leave out here is a lot of times in the LMS judge you want examples.

I didn't put examples here because I just wanted to keep it simple. Once you start putting examples in the prompt, you do have to um split the data set a bit. Like you can't just you can start overfitting to your data. So like if I put all of these traces in my prompt, it would get 100%. Because it would know the answer exactly, right?

So like you don't want to do that and and so um you want to hold aside some data to make sure you're not cheating yourself and you know so that that's so we don't have to get into all that from a product manager perspective the best thing you can do is like just know just have a trigger in your mind about agreement and just don't just ask some clarifying questions like okay agreement is 90%. What's what is the baseline error rate if they say 10%. Yeah, you know that agreement 90% you're like this this is really bad like something something went wrong here and this is like pretty common right for for teams running evals they they just have a they just have like a agreement store they don't they don't have the TPR thing uh very extremely common is like yeah this is this is a reason I'm making a big deal out of it is uh because we just see it so much that uh it's worth uh calling out. Okay, got it. All right.

So now we have some jud judges uh live and um like what what what's the next step? You want to put his judges into production to run all time. So now you have this really uh so let's say you have the judge like this human handoff score judge. That's right. And you like it enough.

So now you have this like powerful tool that you can use like number one uh you can you know you can set aside some data. you can uh put it in CI. You can have a test anytime you make a change to code or whatever. You can test what the you know how good you're doing on this human handoff problem. But also you can run your judge in production.

You can run it on a sample or a large portion of your production traces and you can see like where this handoff failure is happening and you can debug it even more. You can say I want to find all of the places where handoff failure is happening. I want to find a lot more situations where it's happening. Um and you can put you can do production monitoring of it um of problems. You can see you can use these judges to kind of run on a sample of traffic.

You can know like hey are handoff problems happening you know so on and so forth. And you can build this suite of evals over time. Okay. Most of the time people ask me how many evals I have. Usually have under a dozen.

I don't really have that many because I'm pretty parsimonious about the emails that I need. It depends like sometimes I have more than that if uh it depends how expensive they are. Um it takes some work to maintain this stuff as well. Um you know for the LM judge the codebased ones not so much. Uh because you don't have to do all this like you know because I don't have to do too many human this like human label stuff because like in the codebased stuff there's a there is a right and answer.

Yeah. Yeah. And that's like that's called a reference based eval. And this is a reference free eval. So depending on what kind of eval it is um it'll you know there's a there's like a total budget sort of roughly in my mind of like okay how many you should have.

So let's say you have like uh you know five or six judgy valves in production and and you just like so basically in production just means that like like this um human handoff jud judge like it it just randomly samples like out of 100 conversations it looks like five or something and then it kind of gives a pass fail. Yeah, it depends how many you have. Like it depends how many how what kind of scale you're at. you know, if you're serving like billions of users a day or something, then you probably don't want to run an LM judge across like everything. Um, you know, it really depends like you can get a lot of data from just sampling.

But if you have like very low amount of data, like you're only serving like thousands of users a day, then just run the whole I don't know, just like score the whole Yeah. I mean, it's probably not that expensive. So, it really depends. And then you have a dashboard that has basically like TPR and TNR for each judge or or something. Yeah.

And so what you can do is actually like you can bake this into a score. There are ways to like combine these TPR TNR. There's like F1 score and stuff like that that weight them equally or whatever. You can get into this. Usually do a report one score.

That's probably beyond the scope of I have to go into a lot of like data science to like talk about how to do that. Yeah. Um but usually there's one score um that report and actually there's like all these evaluators and I try to have like one aggregate score um y that is like aggregated across all of them just to give me a sense and then I can drill in and see okay what's going on and and when do you do like human labels uh like you know because you you did it in the beginning with looking at 100 traces but like when when do you do human labels again? Oh, so always do them all the time. I do it like revisit it.

It depends on the dynamics of the system. So depends like anytime there's like big changes, I'll definitely do it again and I'll also do it on a regular cadence. Let's say like once a week, once a month. It depends like how fast the systems are changing and how what the scale of the system is. But I'll do it like on both a cadence and also um and then you get better every time.

But also you can build tools that help you do this. So, one of the things that we talk about in our course is okay, we use like brain trust. We did this here. We did this a spreadsheet or whatever. Um, for nurture boss, what they ended up doing and I took some screenshots and I put it in my blog.

So, let me just share that with you. Um, so they actually built their own annotation tool because it's so valuable of a process. Probably the most valuable process of eval is this like is annotation is the annotation and counting. Even if that's all you do, you don't build any judge, you don't do any eval what like you don't do whatever, you can get insane value by just doing that. And that's the one part that everyone skips.

They try to like go directly to like whatever. Yeah. Um and so uh you know this is a screenshot of what they like the tool they built for themselves and they built this in less than four hours. Um because this is type of thing that AI is really good at. Yeah.

helping you build. So it's like okay, you know, you can see this is a trace viewer. You have these selectors for different channels. You have um this is their interface. The system prompt is hidden by default.

They could just create add notes here and then they had they baked it in into their tool where they just did the axial coding for them. You see like it just tried to do it for them and it gave them a count. Got it. They loved it. There's a video in this blog post here.

This is Jacob and he's like super happy. Uh yeah, he looks happy now. Yeah, he talks about how like he did this and how like the the impact that it had on on his uh on nurture boss. So, okay. Um yeah, like you can get really fast.

So, like you know with these like your own tools it gets ridiculously fast and it's not painful at all. Um, yeah. But basically, yeah, I mean, but basically, you should still like basically manually like before I make a major update to a prompt or something like I should still manually look at the, you know, like the traces and like just make sure like uh everything makes sense, right, before I ship ship anything. Yeah. I mean, you don't have to do it on every single prompt update.

You don't have to look at man, you don't have to manually look at traces. You can just you can run your evals that you have um and do that way. Just make sure you're looking at your traces every so often. Yeah. because it's like it might be mysterious like oh like how often and how many traces.

So we tell people look at 100 traces minimum. And the reason we say that that is not a magic number. We always find that if we don't give a number, people don't start. And then when we give a number, when people get in to like let's say 20 or 30 traces, they they they keep going uh until they So we tell people like the term is called theoretical saturation and that just means you keep doing the activity until you it's like a dimension returns. Yeah.

When Yeah. until you aren't learning anything new. Got it. So we find that people once they start this they kind of get addicted to it and they find it so valuable that they just do it. So just keep in mind like 100 traces as a goal.

Okay this is actually a great convers maybe I have to take down the video of Aman because but this is actually a great conversation because um so first of all so TRDR is that the the trace looking at the actual conversations of whatever AI product you have is the most valuable thing and kind of like counting on labling that right. Yes. and like okay so let let let's just wrap up by dispelling some myths okay so so I'm gonna put some I'm gonna put a statement out there and maybe you can tell me why it's is right or wrong okay so uh one thing that I that I thought was right was like you know you know you want to do a eval for a new product and then you get your team together and you be like oh you know like like should we do helpfulness or should we do toxicity or should we do like what should we do like and what what is the right criteria like what what is good toxicity and bad toxicity but that doesn't seem to Right. Based on what we just talked about. Yeah, that's right.

So, a lot of people go straight to helpfulness toxicity score. Yeah, it's a very appealing idea. A lot of vendors, they sell that. They're like, "Hey, don't worry about evals. You just plug and play this tool.

We got you. You don't have to worry about it. Just like push this button and then we'll give you a dashboard. Don't worry." The fundamental problem is generic prompts in those generic things usually don't match to the most important problems that are actually occurring in your application. They're just like super generic and they lead you astray and they actually waste your time because you spend a lot of mental energy looking at those metrics and looking at the dashboards and talking about the dashboards and having meaning about the dashboard and all of that could have been directed towards real problems that are actually happening.

Now there is a right way to use generic metrics. There's like an advanced Jedi trick that you can do once you have learned error analysis. It will make sense. And what you can do is you can take your hallucination score. You can score this generic hallucination score on all your traces and you can sort the traces by the hallucination score.

Okay? And you can see you can do error analysis and see does the top hallucination score like okay you can start doing like smart sampling with these different generic scores. You can use the generic these like all these generic scores as like sampling mechanism to see like is there anything interesting there. And what you'll find is sometimes there is interesting stuff. Sometimes it's not quite like hallucination but something else.

And you can kind of see if any of these scores are helpful, but you shouldn't just report the scores. Should never report the scores as is. Probably shouldn't use the scores, but you can use them as meta tools. Got it. Okay.

But but like it's way more important to identify as problems wrong with your product. Yes. Okay. Then another thing is like uh and maybe this is more a question like how much of the stuff that we just walked through should we do before we even launch the product? you know, like like should we try to have like a bunch of judges set up and like, you know, do a bunch of synthetic stuff like how how much because what once you launch you actually get real signal, right?

I mean, yeah. How much of the stuff should we do? Yeah, I wouldn't get carried away with eval especially in the beginning. I would I would definitely look at lots of data. Um, and looking at data includes using it yourself.

Okay. I mean if that like it says like if if you're building a tool for yourself like you are n equals one user. So you don't need to like just use it yourself and you know the air you're doing error analysis like just by being alive and using your tool like if you're actually using it that's fine. You don't need to do all this stuff. It's like when it kind of gets beyond the scale of your comprehension when it starts to you know there's like lots of users or lots of things going on different use cases.

Yeah. Then you might think about okay that then you can see like where that data might be helpful or maybe you know you can roll out to like 5% of users and you know like maybe they get a [ __ ] shitty experience but then you can start getting real data to improve. Yeah then nothing beats real data. Got it. And like the the liker stuff is just is it just completely you sis or or like do you are you dogmatic about it the one to five stuff should you stay away from it?

I would say I haven't seen you have to be extremely disciplined to use it correctly. Okay. Um you have to have very clear rubrics. You have to make sure everyone is calibrated on that rubric. Um and it usually doesn't go well and for most companies it adds tons of complexity.

I would say it's exponential complexity on like relative to binary scores. And so I just haven't seen it done in most cases correctly. There's there's some rare exceptions where it does is okay, but it's usually like, you know, and I press teams to say, hey, like can we just make this a binary score? Like is there a point where this is like good enough versus not good enough? We're able to do it.

But dude, then where does this stuff come from? Like why do teams keep doing this stuff? Yeah, because it it's a kind of an appealing idea, right? to like we've all been graded on like we have a grading system from school A through F like you know it's not nothing is black or white like we want to like have this like high fidelity sort of assessment but the problem is like what what would what do you even do with this highfidelity assessment like yeah it just makes you feel like false precision right it's like you know I got a three versus a four like what does that even mean like yeah like humans can't even tell a difference between a three and a four yeah yeah yeah most most people can't and it gets just gets lost in the sauce and already, you know, it's just like it's already complicated enough. You need to really reduce complexity in this whole thing and be pragmatic about it.

All right, dude. This is this is super awesome conversation. So, so I guess let's go back to the Twitter debate. Do evals matter? It does matter if you do the problem properly, if you're actually solving real problems.

Yeah, that's a really good question. Do evals matter? Yeah, I would say so eval don't exist in a silo. If you just try to do if you try to eval and get carried away with evals, it will probably hurt you. What you want to do is definitely ground yourself in the data analysis, in the looking at the data part.

And like, you know, everyone says look at your data, but I I think um it's hard to know what that means. What we went through today actually shows you what it means and hopefully demystify what what it is to look at data. But it should be it's like a very tightly coupled with evals and I I say that it is eval like this data this looking at data counting I just say you you because you can't do evals without it. Yeah. It's not like the super sexy part of it but yeah it's the most important part of it.

Yes. Yeah. Got it. Makes sense. All right dude.

All right man. I I I think you convinced me to take your core course now. So uh can you talk about your course and um when you teach it and if you have a discount for folks? We are teaching a course on evals where we walk you through the end-to-end detailed process on how to do evals correctly. We go into subjects like okay how do you evaluate your rag systems?

How do you evaluate retrieval? How do you evaluate agents? Um how do you deal with all kinds of edge cases that you might encounter? How do you do this effectively? Like how do you actually read a trace in you know save yourself from kind of all the complexities that might happen?

and how do you get through this effort? And we've been we've taught over 2,000 students including lots of people from Google, open AAI, things like that. Um, you know, the big labs are really interested in this because, you know, they focused on foundation model benchmarks, but we're talking about application specific evals like if you're building an application, what is that? And that eval is very different. Yeah.

Yeah. And so, uh, I teach the course of Shrea Shankar. Sha Shankar has been writing about eval as well for years now and been doing a lot of research in the space. So we both have a machine learning and data science background as well as software engineering background. You know in the course is four weeks long.

We give students lots of resources. So we have over nine hours of office hours. Yeah. Uh we give students a uh AI evals assistant. So it's like everything that we've ever said about evals publicly in the course, blog posts, talks, papers, you name it.

Uh we've put that in an AI and we give that to you as a like an assistant as well. So you know it's a it's a modern course and you got to have evals on top of that too, you know. Yeah. And we're doing emails. Yeah, we are doing evals on top of that.

This is the first time this is the first cohort we're doing it for. Uh so this next one coming up in October. And so we also give people a 160 page book on evals that you can take with them. So there's a lot of resources there is a it's a good community and we're offering Peter's community 35% off. Awesome dude.

So please see the link in the in the description. Awesome. Yeah, dude. I I personally learn a lot from this. I need to reevaluate how I do evals.

So So yeah, I I hope to see uh folks there. Definitely want to take the course in October. Thanks so much Hal and sharing your knowledge and um keep dropping non knowledge box man like on social media. Yeah, thank you so much. Thanks for having me.
