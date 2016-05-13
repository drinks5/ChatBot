# -*- coding: utf-8 -*-
# @Author: drinksober
# @Date:   2016-04-20 11:16:19
# @Last Modified by:   linlin
# @Last Modified time: 2016-04-23 11:55:46

# class Text_Similarity(object):
#     def __init__(self, text_1, text_2):
#         self._stop_word = (u'的', u'了', u'和', u'呢', u'啊', u'哦', u'恩', u'嗯',
#                            u'吧')
#         self.text_1 = self.participle(text_1)
#         self.text_2 = self.participle(text_2)

from chatterbot import ChatBot
from chatterbot.utils.module_loading import import_module
# from smart_qq_plugins.closest_chinese_meaning.py import ClosestChineseMeaningAdapter
# chatbot = ChatBot(
#     "qq",
#     io_adapter="chatterbot.adapters.io.JsonAdapter",
#     storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter",
#     logic_adapter="chatterbot.adapters.logic.ClosestChineseMeaningAdapter",
#     database='qq',
#     statements="statements")
# print('rr')
# r = chatbot.get_response("下午打")
# print('r', r['text'])
# import_module("corpus.OrderedSet")
