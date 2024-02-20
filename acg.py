import re
import requests
from plugins import register, Plugin, Event, logger, Reply, ReplyType


@register
class Acg(Plugin):
    name = "acg"

    def did_receive_message(self, event: Event):
        pass

    def will_generate_reply(self, event: Event):
        query = event.context.query
        if query == self.config.get("command"):
            event.reply = self.reply()
            event.bypass()

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "Use the command #acg(or whatever you like set with command field in the config) to obtain an anime-style image"

    def reply(self) -> Reply:
        reply = Reply(ReplyType.TEXT, "Failed to get acg image")
        try:
            response = requests.get("https://api.oick.cn/api/random/", timeout=30, verify=False)
            if response.status_code == 200:
                reply = Reply(ReplyType.IMAGE, "https://api.oick.cn/api/random/")
            else:
                logger.error(f"Abnormal site status, request: {response.status_code}")
        except Exception as e:
            logger.error(f"Video api call error: {e}")
        return reply
