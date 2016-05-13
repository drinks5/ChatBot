# -*- coding: utf-8 -*-
# @Author: linlin
# @Date:   2016-04-16 23:41:08
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-23 01:28:48
from smart_qq_bot.signals import (on_all_message,
                                  on_group_message,
                                  on_private_message, )
from chatterbot import ChatBot
chatbot = ChatBot(
    "QQ",
    storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter",
    io_adapter="chatterbot.adapters.io.JsonAdapter",
    logic_adapter="chatterbot.adapters.logic.ClosestChineseMeaningAdapter",
    database="qq", statements="statements")


@on_all_message(name='chatbot')
def callout(msg, bot):
    reply = bot.reply_msg(msg, return_function=True)

    # if msg.poll_type == 'group_message':
        # if '@drinksober丶' in msg.content:
        #     reply_content = chatbot.get_response(msg.content.lstrip(
        #         '@drinksober丶'))
        # elif '@我弟弟好帅！' in msg.content:
        #     reply_content = chatbot.get_response(msg.content.lstrip('@我弟弟好帅！'))
    # else:
    reply_content = chatbot.get_response(msg.content)
        # reply = bot.reply_msg(msg, return_function=True)
    reply(reply_content['text'])