"""
Message sending channel abstract class
"""


class Channel(object):
    def startup(self):
        """
        init channel
        """
        raise NotImplementedError

    def handle(self, msg):
        """
        process received msg
        :param msg: message object
        """
        raise NotImplementedError

    def send(self, msg, receiver):
        """
        send message to user
        :param msg: message content
        :param receiver: receiver channel account
        :return: 
        """
        raise NotImplementedError

    def build_reply_content(self, query, context=None):
        from model.openai.chatgpt_model import ChatGPTModel
        return ChatGPTModel().reply(query, context)
