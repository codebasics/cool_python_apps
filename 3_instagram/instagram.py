from instabot import Bot
bot = Bot()
bot.login(username="faraaz_temp", password="faraaz")

######  upload a picture #######
bot.upload_photo("yoda.jpg", caption="biscuit eating baby")

######  follow someone #######
bot.follow("faraaz_bhai78")

######  send a message #######
bot.send_message("Hello from Dhaval", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("dhavalsays")
for follower in my_followers:
    print(follower)
