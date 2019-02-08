from wxpy import *

bot = Bot(cache_path=True)
bot.self.send("加油")

friends=bot.friends().search()
for f in friends:
    print(f)
# 发送消息给自己
