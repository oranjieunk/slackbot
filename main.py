from rtmbot import RtmBot
from rtmbot.core import Plugin

import secret


def answer(text):
    if "지은" in text:
        message = "히힛>_<"
    elif "주사위" == text:
        message = str(random.randint(1, 6))
    else:
        message = None
    return message

class HelloPlugin(Plugin):
    def process_message(self, data):
        reply = answer(data["text"])
        if reply is not None:
            self.outputs.append([data["channel"], message])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
