# Twitch Classification
In this project, we attempt to create a classifier for multimedia streams on the live video streaming platform [Twitch](https://www.twitch.tv/). 
To do so, the classifier is based on the Twitch Chat, the chat lobby accompanying each live stream. 
The genres of streams that we classify into, are based on our own categorisation and [Twitch Communities](https://www.twitch.tv/directory/communities):
- Competitive/eSports
- Variety
- Speedrunning
- Chill and Relax
- Educational (Game)
- Educational (Programming, Drawing)
- Game Making
- Cooking
- Music
- Real Talk/Podcast

# Chat Log Collection
To be able to gather all the chat logs of different live streams, we used an existing [Twitch chat logger](https://github.com/bernardopires/twitch-chat-logger) written in Python. 
We have tried to diversify the genres of streams that we log as much as possible, but for some genres the presence of streams was scarse.
In the table below, we keep track of the streams that we have logged with corresponding information.

| Date | Time | Duration | Channel | #Messages | Genre | Comments | ... |
|------|------|----------|---------|-----------|-------|----------|-----|
|17/6|21:45-2:00|4.5hr|nalcs1|TBD|Competitive||| 
||||nalcs2|TBD|Competitive||| 
||||kolento|TBD|Educational (Game)||| 
||||kev1ntv|TBD|Educational (Game)||| 
||||disguisedtoasths|TBD|Variety|||
|17/6|21:45-22:45|1hr|lifecoach1981|TBD|Educational||| 
|17/6|14:00-15:00|1hr|thijshs |TBD|Educational (Game)|Might have stopped earlier due to machine falling asleep||
||||lck1|TBD|Competitive|''||
||||garenatw |TBD|Competitive|''||
||||jonsandman |TBD|Variety?|''||
||||iwilldominate |TBD|Variety?|''||
||||colalin |TBD|Variety|''||
||||redbull |TBD|Music|''||
||||dreamhackhs |TBD|Competitive|''||
||||imaqtpie|TBD|Variety?|''||
|17/6|11:00-12:00|1hr|thijshs|TBD|Educational (Game)|Might have stopped earlier due to machine falling asleep||
||||lck1|TBD|Competitive|''||
||||garenatw|TBD|Competitive|''||
||||jonsandman|TBD|Variety?|''||
||||iwilldominate|TBD|Variety?|''||
||||colalin|TBD|Variety|''||
||||redbull|TBD|Music|''||
||||dreamhackhs|TBD|Competitive|''||
