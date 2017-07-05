# twitch-classification

In this project, we attempt to create a classifier to categorize multimedia streams on the live video streaming platform [Twitch](https://www.twitch.tv/) into multiple genres.
To do so, we extract the messages from Twitch chat, the chat lobby accompanying every Twitch stream, and classify it by means of different features of the chat log.
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

| Date | Time | Duration | Channel | #Messages | Genre | Comments | #Viewers | ... |
|------|------|----------|---------|-----------|-------|----------|----------|-----|
|17/6|21:45-2:00|4.5hr|nalcs1|51892|Competitive||||
||||nalcs2|22077|Competitive||| |
||||kolento|7245|Educational (Game)||| |
||||kev1ntv|1264|Educational (Game)||| |
||||disguisedtoasths|20389|Variety||||
|17/6|21:45-22:45|1hr|lifecoach1981|223|Educational||| |
|17/6|14:00-15:00|1hr|thijshs |TBD|Educational (Game)|Might have stopped earlier due to machine falling asleep|||
||||lck1|TBD|Competitive|''|||
||||garenatw |TBD|Competitive|''|||
||||jonsandman |TBD|Variety|''|||
||||iwilldominate |TBD|Variety?|''|||
||||colalin |TBD|Real Talk|''|||
||||redbull |TBD|Music|''|||
||||dreamhackhs |TBD|Competitive|''|||
||||imaqtpie|2143|Variety?|''|||
|17/6|11:00-12:00|1hr|thijshs|TBD|Educational (Game)|Might have stopped earlier due to machine falling asleep|||
||||lck1|TBD|Competitive|''|||
||||garenatw|TBD|Competitive|''|||
||||jonsandman|TBD|Variety|''|||
||||iwilldominate|TBD|Variety?|''|||
||||colalin|TBD|Real Talk|''|||
||||redbull|TBD|Music|''|||
||||dreamhackhs|TBD|Competitive|''|||


- For most categories, there is no hard boundary. A lot of the user defined categories are similar.
- Most prominent categories on steam are speedrunning and pro. But pro streamers may switch from competitive to something like chill. Same for speedrunners. Depends if people watch for streamer or for game.
- Hard to determine the actual category of a stream. We selected streams based on the categories entered by the streamer. Hard to figure out which steams are nice to track.


# Future
Research viewer movement and see if this provide useful info on categories.


# Problems with twitch
Streams are sorted on amount of viewers, this limits the exploration of viewers. Most people will probably find something they like in the streams that already have a lot of views.