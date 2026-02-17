---
title: "What Alexa Can Now Do With AI Explained in 30 Minutes | Daniel Rausch"
guest: Daniel Rausch
publish_date: 2025-12-07
youtube_url: https://youtube.com/watch?v=bLiSlzWoYYk
channel: Behind the Craft
keywords:
- ai
- leadership
- product-management
- execution
- culture
---

Why do you think it has taken so long to add generative AI to Alexa? There actually over 70 models in the Alexa architecture. Thousands of APIs that you can call. I actually really love the PRF process too. I wish more companies did it because I really like writing from the customer point of view like writing to the customer.

Customer doesn't care. Customer definitely does not care about your revenue. That's not their problem. We have leadership principles that really are how we run the company. We have one called invent and simplify.

We put simplify next to invent like very intentionally. If you're really trying to invent something great for customers, you have to simplify it as you go. How do you try to actually keep this thing simple? I often recommend starting with the Okay, welcome everyone. My guest today is Daniel, a VP of Alexa and Echo and Amazon.

Uh Alexa is in over 70 million US households. So really excited to get Daniel to talk about uh and demo Alexa's latest AI capabilities. and we'll also chat about you know Amazon's working backward process and if that change with building AI products. So welcome Daniel. Hey Peter thanks a lot for having me and nice to meet you.

Yeah so I've bought many Alexa devices uh over the past couple years and uh let's just start with the elephant in the room man like you know um why do you think it has taken so long to add generative AI to Alexa? First thanks for uh being an Alexa customer. That's very cool. I'll have some questions for you. No doubt.

I think look first of all let me just start with you know the what I think of as sort of the audacity of the vision for Alexa and it's it's the thing that keeps me running into work every day uh which is that you know we want Alexa to be the world's best personal assistant. when you pull back and you think about uh what it already meant for Alexa to be striving to be the world's best personal assistant uh when generative AI kind of was introduced to the world uh you have hundreds of millions of customers worldwide uh which means all different kinds of households right different kinds of devices 10 years of our own devices in those homes uh customers have connected hundreds of millions of smart home devices to Alexa. So you have this very heterogeneous landscape that you're building for. Then just think about what Alexa uh does. When we when we launched Alexa, it could do 13 things.

And I know that because that's what we put on the web page. We put we put all 13 on there. Uh we stopped counting when Alexa was into the millions of things. So those are kind of the three buckets of scope. I think answering your question of just the size of the task.

It's not just taking an an LLM and you know we'll just jam it on to what Alexa does. It's actually it's actually really tricky and hard. Got it. Okay. So, basically B because Alexa is so successful.

There's so many different devices and different functionality. Okay. So, why don't we get into it, man? Let's um do you want to demo some of Alexa's new capabilities? Yeah, I do.

I definitely want to. Uh I want to make sure that I'm in view of the camera. So, tell me, can you still see you can see this device, Peter? Yes. Okay, cool.

[Music] Alexa, uh, I'm here with my new friend, Peter, and I wanted, uh, to have you just say a quick hi. Hey there, Peter. Welcome to Daniel's little corner of the Smartome universe. I hope you're ready for some quality time with a Red Sox fan who probably has strong opinions about everything from baseball stats to the perfect coffee brew. Let me just She's into my Red Sox thing.

We were just talking about uh trades in the off season uh earlier this morning. So, just a couple things about it. The new Alexa Plus is much more conversational. She which means that she understands everything I'm saying. She responds in a much more elegant way.

You may have also heard that part of that natural more conversational nature is that she's got a new default voice. Um it's more approachable. Uh it has higher expressivity. it has a bigger range of uh of what the voice can capture and she understands actually my input uh sort of tone and tenor of how I'm talking. So the first thing I notic is that conversationality.

By the way, Peter, I took it for granted that you're around San Francisco, but do I have it right? Yeah. I thought about some things I could show you and your uh listeners and viewers uh based on that. Sure. Alexa, how are the Golden State Warriors doing?

The Warriors lost to the Heat 110 to 96 on Wednesday with Brandon Potski scoring 20 points. They're currently 9 to8 and in eighth place in the Western Conference. Well, it sounds like they're off to a decent start. When's their next home game? The Warriors are playing the Portland Trailblazers tonight at 700 p.m.

at Chase Center in San Francisco. Oh, cool. Are there um are there any seats for that game available, say under 200 bucks? Great news. There are tickets available for the Warriors versus Trailblazers game tonight.

How many tickets would you like? Well, maybe me and Peter will go, so two tickets. Perfect. I found some great options for you and Peter. The cheapest tickets are in section 215, row 4, seats 10 to 11 for $121.

Actually, you know what? I'm just getting to know Peter. Are there any seats under 100? Or maybe just let me know if there are any seats that come up that are under 100 bucks. I couldn't find any tickets under $100 for tonight's game, but the cheapest ones are still around $121.

Would you like me to watch for tickets under $100 in case any become available? Perfect. That'd be great. Alexa, I'm going to go back and talk to Peter for a bit. Sounds good.

Have fun catching up with Peter. Awesome. So, so it's doing a bunch of I guess it's doing a bunch of web searches and tool calling behind the scenes. Tool calling, searches, retrieval, augmented generation. um you know basically the whole host of what you would expect an LMLM to be doing on the front with tons of services and APIs on the back end.

You saw you saw our own uh you know information APIs being called, sports APIs being called, partner integrations like ticket master and open table being called. So that's the kind of uh experience continuity that we're building with Alexa across this whole host of things where Alexa just gets it done. We we obviously have a lot to build when we're building something like that. But for a customer, it's just dead simple. The user has to link their ticket master and stuff accounts like in Alexa app or something for all all this stuff to work.

Yeah. If you So this clearly is already set up. You know, some services operate in guest mode by default and it's just about u interacting with them. Sometimes, like if I didn't have an account set up here that could complete something, it would bring up a QR code and I do a one-time mutual authentication step. Like Uber's a good example of something super easy to set up.

You just it brings up the QR code once and then you're off and running and uh Alexa can grab you a car. That's pretty cool. That's pretty cool. And I can see in the future you can set up these like you know you know how there's like uh these platforms set up AI workflows like Zapier and OpenAI stuff. Maybe just do it through voice too like you know send me a reminder every Friday to look up look up the five most you know interesting family activity events nearby and send me a list every Friday or something.

That could be cool. So Oh yeah. One actually one of the most popular new features that we built for uh Alexa plus is the ability to set up routines like that that you just said by voice and routines usage has just gone through the roof because you don't it's not the kind of thing you want to program in an interface and actually you brought up a couple of integrations that I find really interesting because computer scientists can go put middleware in to get to access services and maybe people like you and me that are you know in the tech segment but your average customer is not going go figure out what middleware is necessary between my calendar and some LLM that I chat with. It's just not it's just not accessible enough for customers. So, one of our design goals with Alexa is really to just it's our job to take that complexity away.

We need to make it simple. This episode is brought to you by boat. Bolt recently launched a major upgrade to become the fastest tool for product teams to prototype new features. Now you can use both browser interface with the best AI agents like claw code to build working prototypes with real infrastructure like databases, authentication and hosting all managed for you automatically. Now both projects can also sync with GitHub for version control.

And the whole product team can collaborate in a shared workspace without having to switch to other tools. Check out Boltv2 at bolt.fy/per-yang to get started. Now back to the episode. Is it like uh different LMS powering this in the background or uh like one particular one or That's a good question. I mean we in terms of the technical infrastructure uh from a product perspective I think we made some you know very high consequence decisions like supporting everything that Alexa could do and uh you know not fragmenting that experience and bringing along 97% of our installed base of devices.

From a technical perspective, I think we realized pretty quickly that we were manifesting so many capabilities that we would need just a huge range of models. There actually over 70 models in the Alexa architecture. Wow. Okay. It's amazing to have Bedrock and AWS uh as internal partners because we we I mean if if it's up on the Bedrock page, it's probably a model that's in the Alexa architecture uh and that we're taking advantage of.

We've got for um for our biggest sets of inference, we have our amazing Nova team internally. Uh our NOVA models take the vast majority of traffic in terms of the biggest inferencing we do. Uh we've got an amazing partner in Anthropic uh and and we've had a great partner with ship with them building uh capabilities for Alexa as well. But it's really just a what we've built is a model agnostic system. And I think that this is sort of another uh interesting kind of fork in the road that we came upon as we were building Alexa.

Is the model the product? Is it about communicating to customers that it's some new model or is it a product where you're just trying to use the best technologies to deliver whatever customers are trying to get done. And I think this was a you know most of the pattern in the segment for LLM based products is to is to communicate that that customers are using a model and I think that that's actually that's actually got a ton of limitations in it for customers. Customers actually in general don't care like they're just trying to get something done. You know I happen to know the operating system version running on my smartphone.

Most customers don't care about that. They don't care about what LLM using. They just want to get a job done simply, easily. They want a great experience. They want that experience to be predictable and reliable, all those kinds of things.

So, I think that helped us understand we would always just use the best tool for the job. And that's what allows us to do things like it might not be 70 models, maybe it's 300 models, maybe it's 10, but we'll we'll stay flexible enough to be able to bring the right technology into the stack. Yeah, that makes sense. Yeah, I think sometimes I'm too involved in the Twitter sphere. Everyone's talking about models, but yeah, every customer doesn't care.

We care. We care. And that's great. It's great, but we don't have to pass that through to customers. Yeah, that makes sense.

Okay, so let's talk a little about uh behind the scenes of making like all this stuff work and like Amazon's call culture, product culture. Um I I used to work at Twitch, so I'm pretty familiar with Amazon's Oh, cool. You know, working backwards, PR FAQ, like this whole pro process. Um may maybe give a quick recap of like this process and and like does this change when you're building AI products? is more iterative or Oh yeah, that's very interesting.

Uh so right so what the PRFAQ uh sounds like a complex acronym I'm sure to your listeners but it stands for press release and frequently asked questions and the point of this document coming at the beginning of the process is to really communicate the vision for a product that we're building in customerf facing terms. So, it's really it's the press release. You write the press release. You date it sometime in the future, a year, two years in the future, or six months, three months in the future, depending on the scope of what you're delivering. And you write it down as though you're going to put this press release on the wire.

These are the most important things we want to say about it to to communicate with our customers, and this is what's it's going to accomplish for them. This is the simplicity of communication that we want around it. for example, and these are the most important things to get done. And then the FAQ part, sometimes we have an internal facing and external facing FAQ so that we bear out the idea for ourselves, but also we build an FAQ that's sort of like the FAQ you'd find on a website that says, "Hey, here are the frequently asked questions about this given product." Um, I really value the process. Some people, it's interesting because when when folks first come to Amazon, I don't know what your experience was, Peter.

I'm interested to hear. But um it seems burdensome to get a product going sometimes when people first get here uh because you're like, "Wow, you're writing this six-page document and is that really what it takes to start start moving in earnest on a product?" And in fact, it helps you go so much faster to know where you're actually headed. So much time is wasted in technical uh product building on this kind of dead reckoning that ends up being wrong. You think you know the point of the compass that you're sailing towards, but you hit rocks or you go the wrong way or you realize you most unfortunately you realize you've been building the wrong thing and you start to figure out what customers want or your organization is such that you build something and then you throw it over the wall to marketing and you say good luck. I hope it works for customers.

the PR FAQ process really helps you like see the end of the process and work backwards from that and I think it's incredibly valuable and I think Peter just to keep going your your question was something like hey PRPQ process and does it work for AI products was that right I mean when you when you have big consequential inventions I think it's even more important to use a process like the pure process what you have to do is adjust as you go though you have to be willing to incorporate the latest technologies adapt your vision overall but that doesn't mean abandoning the process that just means tuning it as you go yeah I I uh I actually really love the PRF process too I I wish more companies did hit it because I really like uh writing from the customer point of view like writing to the customer as opposed to writing to some ex executive because like then you like you know we want to grow this revenue we want to grow that and the customer doesn't care like who cares definitely does not care about uh you know your revenue. You're exactly right. And it does it does help us really focus on of course we we need to build big sustainable businesses because that's what lets us continue to deliver products for customers, but that's not their problem. Um and I think I do think it also just helps you get down to the few things that matter. You know, one of the one of the other things that comes up a lot in building these highly technical pro products is just they're complex.

they're they're inherently complex and and none of that complexity can go to customers, right? You want to keep it as simple as you can for them. So that's the other part that I love most about it. That part was probably mostly captured in the FAQ and stuff like that, right? To sorting through all the questions that people have.

It is. It is definitely captured in the FAQ, but it's also sort of like what are the one, two, or three things that you can actually communicate to a customer. Got it. About writing that press release. sort of like you don't have, you know, it needs to be a page for anyone to read to the bottom of it.

Yeah. And you probably can, you might be able to communicate three things, but definitely not four and ideally one or two uh when you're explaining what it what it is. Uh and it really helps you focus on I think on that end of things as well. Yeah. And and like just to give people a bit better idea like you know the PR FQ there's like a you got to express the customer problem very clearly what the value is you're delivering.

And I think there's like some quotes you can have from the customers, you know, and kind of just bring the whole thing to to life, right? I actually uh when I get an opportunity to talk to new Amazon leaders about the process, and I I do that sometimes through some of our internal trainings. Yeah. I I often recommend starting with the customer quotes. Yeah.

What What do you want a customer to say about your product? What are they going to go to their neighbor at the barbecue and say? I used to, man. I used to manage that family calendar. It was on the wall.

What a mess with the Sharpie and different color for each kid. Said, you know, Jane, longtime Amazon customer. Now I just use Alexa plus 21 in, you know, Echo Show. And on the wall is the whole family's calendar. I've linked my calendar from work, my husband's calendar, and we've got the Roush family at, you know, Gmail calendar all together right up on the wall.

Anytime we need to add a new event, we just say, "So, and I sent each of the kids school calendars at the beginning of the school year." Alexa automatically uploaded every event and we're off and running or something. It'll be like a quote like that where you just say, "Oh, actually, I get it." And I do want customers to say that at the barbecue next door and explain the product that they bought. Yeah. Yeah, that that quote is like captures everything and and maybe you can even like, you know, show your PR FQ to some customers and like get a real real quote, you know. Totally.

But yeah, but but but but dude, let me let me kind of push back a little bit now. So, you know, again, I love Amazon's writing process. I love the six pager process. It really forces you to think through the problem in detail. But I also see a lot of these AI startups like, you know, like Curser and these other companies.

And um I think now you know being like a decade plus as a PM sometimes I also feel like uh you know being fast be right like being being able to iterate fast like even if you ship the wrong thing and then you can uh learn from customers and then adjust that that to me is potentially better than like trying to come with a perfect strategy and and then like not shipping anything for like six six months. May maybe it's a little bit different for Alexa because it's like a very complicated ecosystem that you have to ma manage but like you know how do you balance these two things because one thing from Amazon is like you can really spend like you know two or three months or you know even longer working on that six pages trying to get get it right right so how do you how do you balance these two things I think that's a really good question I mean I think there's speed and agility and then there's rushing and sort of testing on customers right if you want to take both extremes I do believe in, you know, AB experiments and getting things out quickly, responsibly, quickly. But if the customer experience just isn't ready, there's no reason to give it to a customer. You're not learning anything. If you have something to learn and you've built something that you think is whole enough to give to a customer, that's great.

And you might not give it to every customer in some cases. you might AB it or you might find other ways to introduce it or call it experimental or identify for customers that you know it's something that you're looking for feedback on. Uh and those those ways of getting things to customers are incredibly valuable. Spaghetti at the wall or rushing or testing on customers, it's just never acceptable. No one wants to be, you know, being an experiment subject signing up for that and giving feedback on something and through your usage or through your direct feedback.

I think that's great being a test subject where it's like you weren't asked to be a test subject and you're using something that's not ready. And believe me, there's plenty of those things out in the AI world. Use, for example, use some of the best versions of things where people are trying to actuate APIs or capabilities, agent modes or things like that. Yeah. You know, success rates below half success rates below 20%.

Yeah. It's just that's not that's not something for all customers to get. It might be something to give to some customers or ask adopters. Yeah. Like that's cool.

Um but I don't that's not really speed and agility to put things like that out in the world. That's more um releasing you know alpha software. That's not speed. Yeah. I I I I think uh I I really believe in like kind of releasing to concentric circles like you know when you have like something kind of shady maybe you release to 100 customers who are really early adopters who want to try something new and they get a bunch of feedback and they make it better and then you release to more and more people along the way.

Exactly. And we have, you know, we have we have our we have internal beta populations. Sometimes we have external beta populations depending and those are customers that we communicate with in particular ways. You know, sometimes we have features that we will label experimental or make sure customers understand the status of of something and that we're really flagging that we're looking for feedback on it. All of that helps you move with speed and agility.

Um but again it's just things have to be ready enough for each of your concentric circles I think and you have to you have to make sure you're communicating clearly. Yeah. Okay. Let's talk about something else. Uh let's talk about um I I I think you have this principle of radical simplicity and uh it's it's like one like trying to keep your product simple is like one of the hardest things.

It's like super super difficult. So maybe you can give some advice for the PMs or folks out there. you have all these like you know dependencies and stakeholders to manage like how do you try to actually keep this thing simp simple for customers yeah I that's really it's astute I think because it is one of the hardest things and we work in tech so things are inherently complex sometimes right you mentioned dependencies and even building a feature that gets out as simple right is quite hard for us all in our work in any given day I do think it's about figuring out a product's usually one thing what's the way you could say a product's one thing or a features one thing. Again, you might have a second or third that are kind of also rans or important secondary things you would explain to a customer. But once you know the one or two or maximum three things that your product is supposed to do uh for a customer, you can use that to triage and scrape away everything else.

The challenge is when you don't know a product's one thing. Uh that's when we have the hardest time simplifying. One of the things I love about our leadership principles at Amazon, you've been asking about Amazon culture. So, um if your listeners don't know it, we have leadership principles that really are how we run the company. And I think they're they're just kind of hallmarks of our Amazon culture.

We have one called invent and simplify. And I talk about it a lot when I talk about the leadership principles because we put simplify next to invent like very intentionally. It's not a separate leadership principle. It's basically they go together. If you're really trying to invent something great for customers, you have to simplify it as you go as a principle.

And it's captured I think also in this process we were talking about PR FAQ where you know when you force yourself to write how you're going to communicate with customers about a product, it forces you to simplify. I think Alexa plus is, you know, a really interesting, challenging example because it's so big. Alexa can do so much, but when you communicate with customers about it, you just have to make it dead simple. It's going to help you keep your house organized. It's going to connect to all of your devices.

It's going to do things like your calendar. It's going to communicate with your family. Like, you have to come up with ways of simplifying it down to a handful of things. Yeah. And like, you know, like it just has to work, right?

Like part of the value prop is I think with Lexa Plus is just like it can actually take actions for you and get stuff done for you and uh it it just has to work across like a variety of different popular apps. I guess tens tens of thousands of devices and services, right? But it presents the kind of question you're talking about. That's an incredible amount of complexity that we've built to but we express it to customers simply. Yeah.

Organize your life, organize your home, manage all your entertainment in one place. You know, these kinds of simple propositions help customers understand this massive range of what Alexa Plus can do. Yeah. You know, you know, you got to add a feature, man. I'm I'm begging you to add this feature where if someone says, "Alexa, play K-pop demon hunters and uh you and it's already been played 100 times." Alexa should tell the person no.

I like it. I see that a parenting feature maybe. Is that Yeah, it should be it should be a parental control cuz like uh my kid knows just like keeps talking like, "Hey, K-pop demon, play Alexa, play Golden. Alexa, play Golden." It's like the same song over and over again. Believe me, I know the stage you're in.

My uh my kids are all teenagers now. So, okay. You know, I'm not cool enough to listen to their music anymore. But, uh but clearly, you've got some some people that you live with that are at that point where they'll watch something a million times or listen to something a million times. I will take your feedback to the team.

I love I love the idea of that. Or at least give him a little flack like don't you think dad's heard that enough? Yeah. Don't don't maybe should listen to some Rolling Stones or like something a little bit better. Alexa can easily do that.

And by the way, one idea for you. I walked my kids through kind of the cannon of music that I love by setting alarms in their rooms. Uh music alarms in their rooms. So, you can say, "Hey, Alexa, wake up, you know, wake up, you know, Timothy to the Beatles, uh, every weekday at 7 a.m." And then next thing you know, kids know the Beatles. Next up, Rolling Stones.

I I did Beatles and then Rolling Stones. So, that's why your your call for the Rolling Stones helped me remember that. Oh, that's a pretty good idea because I I always have to yell at them to wake up. So, yeah, maybe I'll use music instead. There you go.

I love it. Yeah. Okay, cool. One more question. like um you know you've written all these PR FAQs I'm sure for Alexa.

So um you know let's say like a year from now like I I I think in AI you can only look out a year from now like what do you think uh Alexa should be able to do? Is it still like this device at home that you can just talk to or like you know what what are some really cool stuff that you guys are building towards? Well I think um you know I see you wearing earbuds there right? I do think there'll be uh there'll be stories. We already see customers loving taking Alexa Plus with them outside the home.

Um and so I think you'll see that that is a that's a big part of what we imagine for Alexa Plus. You know, you you you can do so much for customers when you have this deep engagement with them at the in at the home and you're helping them organize their life and get things done. But of course, we live a we live our lives outside the home equally as well. And so I think, you know, you we see our buds, you see our our Echo Frames, uh, and we see customers already loving Alexa Plus on those devices. You heard me mention the app and the browser, Alexa.com and the Alexa mobile app before.

So those are other great places I think you'll see us continue to lean into uh, as ways really we want Alexa plus available wherever a customer is. So that's kind of what I'm indicating there. Uh, I think you'll for sure see we have so many partners lined up that we just haven't had a chance to uh announce yet and that haven't released their software yet. The tip of the iceberg has been things like Ticketmaster, Open Table, uh Uber, uh, but the the range of things that Alexa Plus can do through these integrations is so big. And then of course, you know, you'll see us continue to invent uh devices for the home that are purpose-built for Alexa Plus.

We we launched four new devices this fall. Echo Show 8 and 11, our brand new Echo Studio and our Echo.max product. All they're each doing great. Customers around the world are loving them. But in particular, you know, they've really been designed working backwards from this new conversational, smarter, more personalized, and more capable Alexa Plus.

So, building devices that are really purpose-built for Alexa Plus is a huge part of what we're looking forward to as well. Awesome. Yeah. I mean, if the vision is to build a personal assistant, like maybe um maybe you can like you be proactive and be like, "Hey, you know, hey, Peter, like uh I I have like 10 spam emails that I've you can just say yes to unsubscribe to or like, hey, I I clean up your calendar for tomorrow, you know?" It's like I love how you think, Peter. We've got some openings here in the product management time.

Yeah, maybe I'll come back. Yeah, I love I love the idea of an even more proactive Alexa. We do have ideas already like the the ambient screen on an Echo show does follow up on conversations that you've had. You saw me set a ticket watch before. So, she'll reach out to me.

She finds us tickets for under a hundred bucks. We're going to the game. So, I think you will. You're right to say that uh Alexa will continue to get more proactive as well. Yeah.

I mean, buying tickets is like, you know, there's like a lot of uh scams going on. So, anything that can help with that is is great. Totally. Yeah. And I think watching for tickets at a given price is it really is a killer feature.

Okay. So, uh I don't know if you're active online, but where can people find out more about you, Daniel, or Alexa? LinkedIn's the best, I think, for professional contact. So, look forward to hearing from you on LinkedIn. All right, Daniel.

Well, uh yeah, really excited. Don't forget about my K-pop demon hunter feature. So, yeah. I got it. I got it.

It's It's a feature with your name on it already. All right, cool.
