![](img/flc_design2022040817792.png)

---

## ⚡ What is HummScroller?

Do you feel like you've curated a good Crypto Twitter? Put your money where your likes are! With HummingScroller, you sit and zone-out on Twitter, liking crypto posts you agree with, as you already do. HummScroller watches your Twitter account and buys the tokens (present in `$cashtags`) in the Tweets that you hit "like" on!

After 24 hours, HummScroller then sells that token back into stablecoins, and pulls your new recent likes to build a new portfolio. New portfolios are built every day based on the changing sentiment towards coins that you decide by liking them.

## 📈 How to Use It?

Install it Via Telegram: TBD

Telegram Bot Command: `/hummscroller @my_handle` -- call the bot and enter your Twitter handle.

This registers a paper "mock" trading account in a Hummingbot instance.

Now just keep zoning out on Crypto Twitter! It's scanning tweets that you like, not your own tweets.

# ✨ How it Works

Currently only working on paper trading with a Binance connector through Hummingbot.

Your most recent 100 Tweets will be scanned for any cashtags, which will then build a dataset about what you've liked recently.

# 📟 Backend

Hosting: TBD

---

Set Twitter [API Keys](https://developer.twitter.com/en/portal/projects-and-apps):

`export TWITTER_HANDLE=elonmusk`

`export TWITTER_API_BEARER=AAAAA...`

Twitter Script: `humscroller.py`

![](img/musk_anselm_griffith.png)

---

Hummingbot Script: `humminggram.py`

---

Telegram Bot: TBD

# 📡 Future Plans

Additional Twitter Intelligence:

- Scan not just likes, but retweets also.
- Get audio from `Spaces` you were in and correlate that to tokens.
- AI sentiment classification to break tweets into the bullish and bearish parts.
