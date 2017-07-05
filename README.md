# Twitch categories

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

# Issues
- For most categories, there is no hard boundary. A lot of the user defined categories are similar.
- Most prominent categories on steam are speedrunning and pro. But pro streamers may switch from competitive to something like chill. Same for speedrunners. Depends if people watch for streamer or for game.
- Hard to determine the actual category of a stream. We selected streams based on the categories entered by the streamer. Hard to figure out which steams are nice to track.

# Future
- Research viewer movement and see if this provide useful info on categories.

# Problems with twitch
- Streams are sorted on amount of viewers, this limits the exploration of viewers. Most people will probably find something they like in the streams that already have a lot of views.
