# -*- coding: utf-8 -*-
# @Author: linlin
# @Date:   2016-04-17 22:29:14
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-23 00:49:50

import re

from pymongo import MongoClient
f = open('1.txt', 'r')
data = []
name = {}
re_str = r"([0-9]{8,10})|([a-z0-9A-Z_]+@[a-z]+\.[a-z]+)"
time_str = r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{2}"
p = re.compile(re_str)
t = re.compile(time_str)
message = None
i = 0
client = MongoClient()
db = client.qq

from chatterbot import ChatBot
chatbot = ChatBot(
    "Ron Obvious",
    io_adapter="chatterbot.adapters.io.JsonAdapter",
    storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter",
    logic_adapters=["chatterbot.adapters.logic.ClosestMatchAdapter",
                    "chatterbot.adapters.logic.ClosestChineseMeaningAdapter"],
    database='qq',
    statements="statements")

recent_message = []
for content in f.readlines():
    if content == '\n':
        continue
    if content.startswith('2016-'):
        message = p.search(content[20:])
        time = t.search(content).group(0)
        if message:
            message = message.group(0)
            previous_name = message
            if message not in name:
                name[message] = []
    else:
        if message in name:
            previous_message = None
            if recent_message:
                previous_message = recent_message[-1]

            name[message].append(content[:-1])
            # data.append([previous_message, content[:-1]])
            if previous_message:
                chatbot.train([previous_message, content[:-1]])
            recent_message.append(content[:-1])
            i += 1

# print(data[0])
print(type(data), len(data))

# print(name.values())
print(i)
# for single, messages in name.items():
#     for item in messages:
#         timeline, message = item
#         # result = db.single.insert_one({timeline: message})
#         result = getattr(db, single).insert_one({timeline: message})
