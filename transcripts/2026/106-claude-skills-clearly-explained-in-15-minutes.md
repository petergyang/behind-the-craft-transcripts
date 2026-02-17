---
title: "Claude Skills, Clearly Explained in 15 Minutes"
guest: Peter Yang
publish_date: 2026-01-14
youtube_url: https://youtube.com/watch?v=loz60mALXxA
channel: Behind the Craft
keywords:
- ai
- ai-tools
- productivity
- product-management
- design
---

Hey everyone. So today I want to show you how to build a claw skill to write better and avoid AI slop writing permanently. You know skills the potential to be the biggest AI productivity unlock since project. Think of a skill as a specific expertise or template that AI can trigger from any conversation. There's a lot of hype out there about skills, but I'm going to give you the real no [ __ ] take.

The reality is the product is still early and AI isn't really good at triggering skills yet, but I have a hack to actually get AI to do it reliably and for you to use skills to save time. All right, let's dive in. So, what exactly is a skill? It's just a folder with bunch of files that have instructions that AI can trigger based on a given conversation. For example, here we have a skill that applies Anthropics brand guidelines to any slide deck or artifact.

Okay, so let's take a look at the skill, right? So here's a breakdown of each file. There is a skill.md file, which is the most important file and is required that tells AI what the skill does. For example, main color should be a certain color. And be sure to write a clear description that AI will use to decide when to trigger the skill.

And then you could have other files like a reference file, for example, a slide deck.md, which is additional instructions for AI to apply anthropics template to slide decks. And you might also have script files such as apply template. py which is basically just code that AI can execute to apply the skill. Okay. So when should you use skills versus projects?

Well, they actually complement each other very well. You should use projects to upload materials for a specific work stream. And you should use skills to train AI to follow your instructions across all relevant conversations. So for example, if you were working on a new product, you might upload a bunch of reference material research to a project and you might use your create PRD scale to actually create a PRD from that material. All right, so this is a simple comparison table of skills versus project.

And to me, the core value of skills, the core promise is that AI is supposed to know when to trigger the skill based on your conversation so far. But in practice, this doesn't quite work reliably yet. So, I'm going to share a hack later on in this video to fix the reliability problem. All right, so enough talk. Let's now build a writing scale that writes concisely based on my writing style and avoids AI slop.

So, let's take a look at this prompt on the right. Note how I start with a clear name and description for the skill. And critically, I included the keywords to trigger the skill as well, such as draft or edit. When AI sees these words, hopefully it will trigger the skill in some way, shape, or form. I then go into my desired format and tone, such as short paragraphs and bullets for easy skimming.

And finally, I wrote down some guidance to avoid AI slop writing, like using too much padding, using words like delve, using templates like question and answer format, and this isn't X is Y. These are like kind of telltale signs that someone generated this crap using AI. Okay, so now let's go ahead and paste this prompt into Claude and see what it comes up with. Okay, so I have the exact same prompt here. Let's hit send and see what it comes up with.

Okay, we're back. So, as you can see, Claude has created a skill.md for us. Let's take a look. It's got our description. It's got the trigger words.

It's got our writing style guide, format, tone, and most importantly, it's got a bunch of stuff to try to avoid AI slop, right? Writing. So, we can continue to iterate with scale, but let's assume that we're happy with it. And now all we have to do is click copy to your skills button on the top right. All right.

So now claude has copied a skill. Let's go into manage and double check. And you can see basically in claw settings under capabilities and under skills now we have a writing skill that's turned on. Right. So now let's go ahead and actually test the skill.

So to test the skill, I'm going to copy this interview transcript from interview that I did with my friends Aman and Tao. And I'm just going to copy it into Claude here. And I'm going to say write a blog post based on this transcript in my style. Okay. So now hopefully Claude will apply our writing style skill and draft a really well done blog post.

Let's see what it comes up with. Okay, we're back. And you can see here that Claude actually checked for a writing style scale to apply my style and then it did a bunch of work to apply my style. So, let's take a look at the blog post. How three real AI PMs actually use AI, not the LinkedIn version.

Okay, that's pretty good. All right, most PM AI workflows are fantasy. Here's the honest truth and here is some takeaways. So I basically demoed uh prototyping with Google AI studio. TA demoed using AI as his thinking partner using obsidian and cursor and clock code.

And the man demoed his personal OS using clock code. So this is a pretty good uh initial blog post, right? And and you can take a look at this. The original transcript was basically just a bunch of timestamps and had way more text. All right.

So that's the promise of skills. Bas basically instead of having to create a project to edit the blog post which I do have I can now apply my writing style to any kind of writing from any chat right it can be you know a blog post it can be an email it can be anything and hopefully uh AI is smart enough to trigger my skill when I use keywords like draft edit and so on and so forth okay so that is the promise of skills but here's the reality you know and I promise to give you guys the No [ __ ] take, right? So just chatting with Claude to create skills works for simple examples like we just showed. But I found that this approach falls apart for more complex skills that have multiple files. So let me show you actually how to rebuild our writing style skill and also have it create great strategy docs based on my template.

And we'll do this manually using cursor instead of talking to Claude. And you can actually use any text editor to do this, but I like to use cursor's UI. So basically uh to create this in cursor, the first thing you need to do is you need to have a folder that has the same name as your scale. So in this case, it's writing dash style, right? And in this folder, you need to have the skill.md file, which is required.

And we're also going to add a resources folder that has our stratey memo template. Okay, so let's take a look at both files. Now, let's take a look at our skill.md. So, our skill.md is pretty typical. It's kind of what we just covered, but there is one key difference.

So, at the bottom of the skill.md, I've included a resources section that mentions a strategy-me. And I've also included trigger words for using the strategy memo and instructions to apply this template when you're drafting or editing strategy documents or one pages. So this is key to get AI to know when to apply the strategy template because AI will initially only read the skill.md. All right. So now let's take a look at the strategy-memb.

So here I also have my skill name which is strategy-me and description which also includes a bunch of trigger words like strategy, memo, one pager, proposal, product, plan, brief, right? Uh so basically you know if I mention hopefully any of these words in chat from any chat then AI will hopefully apply or at least reference this skill. Now let's take a look at my actual template. My template is basically a one-pager memo that includes a user problem, product vision, principles, goals, solution, and what you're not doing all in one page. I've been a product manager and product leader for over 10 years and these days I believe that any kind of memo or strategy document that you write should be no longer than one page because if you write too long people are just going to use AI to summarize it anyway right so there's a lot of detail here about principles goals solution and what we're not building which is also very important and actually I'm pretty proud of this template and if you want to get it check out the link in the description to my blog post that will have a link to the template But now that we have these two files and remember to organize it like this, what we should do is we should zip up this folder into a zip file.

All right. And now let's come back to Claude and let's actually remove the writing style scale that we created with Claude before because now we have a better version that has a strategy doc template. And let's hit add over here. Okay. And here I'm going to upload my zip file.

So, let's go ahead and go to our writing-style zip file. We'll upload it right here. And you can see here that Claude has uploaded our writing style zip file that has both the skill.md and our strategy memo template. Now, this process, frankly, is terrible, right? Having to zip up stuff and upload it in some settings to claude is it's just not a good user experience.

So I'm sure that Anthropic will improve it soon when skills comes out of preview. But there's actually one final step to make sure that our scale gets invoked reliably. And I haven't seen this in any other tutorial and it took me a while to figure this out. So the final step is we want to go to general settings in claude and we want to add this line to our custom instructions. So basically this whole thing gets pasted to cloud every time we submit any kind of prompt right and the line here is always check this folder for applicable skills before responding.

So this is a critical line because in practice if you don't include this line claude is not very reliable at using your skill at all. Even if you start using some of the keywords like you know strategy docs and edit this file and so on and so forth it's just not very reliable at least not right now. So this is my noble should take. You got to add this line to make scales work consistently. All right.

So now we have all this stuff added and let's take a look and test the skill and hopefully it works. So let's actually test the skill by saying research do some research and uh why don't we pick anthropist competitor OpenAI and write a onepager strategy doc for open AI to win in 2026. Okay. So if we set up everything up properly, hopefully uh AI will automatically apply not only our writing style scale but also our strategy memo.md template. So you can see here that's checking for applicable user skills.

It's checking my writing scale for my preferences and it's smart enough finally to check the strategy memo resource. So to be fair, this does make a little bit longer for AI to respond to your prompts because it's actually checking for value scales and templates. But now it's going to do some searches about how OpenI did in 2025. This is not part of the skill, by the way. This is just like because I asked it to do some research.

And let's see what kind of strategy document it comes up with. Okay, here we go. It's starting to generate the strategy document. And you can see here that it follows my format of problem vision principles and so on so forth. It does use m dash a little bit too much.

Maybe I should put that in my writing style guide not to use m dashes so much. But let's actually take a read through this. Right. So openai faces excess challenge. Chat GP mobile growth has flatlined because uh Gemini is surging and there is a big enterprise gap.

enterprises prefer to use cloud or Gemini instead of OpenAI solutions. So I think so far so good, right? Oh, and there's also a margin trap, right? Open eye losses money still. And here's three different options for the vision and some product principles that we can use some goals, you know, to get to 40 billion AR.

I'm not sure how accurate this is. We might want to check the numbers. And here is a bunch of solutions. So win the browser war, go after enterprise, so on and so forth. And you know this might not be the right solutions, right?

You got to use your brains, you got to use your critical thinking, maybe you ask more research, maybe you voice dictate your own opinions. But the point is it's starting to write as output in a format that I like instead of in some random format and I have to apply my format afterwards. So the fact that it can just do this from any chat window as long as I mention the right keywords, you know, write a strategy doc or edit this document is a huge timesaver, right? If you set up properly. Now, let's wrap up.

We just built a writing style scale that also includes a strategy memo template and it can apply my writing style. It can avoid AI slop writing. It can structure strategy docs and output it in the format that I like. And unlike projects, it can work from any chat that I start with Claude. So start with just one skill and consider adding additional templates to write PRDS to write weekly stack updates or emails and more.

As I promised, I gave you my no [ __ ] no hype take on skills. I think it's a great product. There's a lot of promise to be able to invoke any expertise and template from any chat window that I have, but the product is still early. Like, you know, I shouldn't have to use zip files to make this thing work. All right, so that's it.

Please consider liking and subscribing to this channel if you enjoy this tutorial. And I have a lot more practical AI tutorials and interviews for busy people coming up
