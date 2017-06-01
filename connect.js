const TwitchBot = require('node-twitchbot')

const Bot = new TwitchBot({
  username : 'chattyviewbot',
  oauth    : 'oauth:uov2nai4d184fyjsdny3eucv1cvdc2',
  channel  : 'keraito'
});

/* Connect bot to Twitch IRC */
Bot.connect()
.then(() => {

  /* Listen for all messages in channel */
  Bot.listen((err, chatter) => {
    if(err) {
      console.log(err)
    } else {
      console.log(chatter.msg) // 'Hello World!'
    }
  })

  /* Listen for an exact messages match */
  Bot.listenFor('KKona', (err, chatter) => {
    console.log(chatter.msg)
  })
  /* Send a message in the channel */
  Bot.msg('BibleThump this is the message text PogChamp')

  /* Listen for raw IRC events */
  Bot.raw((err, event) => {
    console.log(event)
  })
})
  .catch(err => {
    console.log('Connection error!')
    console.log(err)
  })
