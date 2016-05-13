# -*- coding: utf-8 -*-
# @Author: linlin
# @Date:   2016-04-21 17:07:08
# @Last Modified by:   linlin
# @Last Modified time: 2016-04-21 18:05:59

from math import sqrt
import jieba
import jieba.analyse

stopwords = [u'的', u'地', u'得', u'呀']

class TextSimilarity(object):
    def __init__(self, string1, string2):
        self.stopwords = [u'的', u'地', u'得', u'呀']
        self.string1 = string1
        self.string2 = string2
        self._words = {}

    def run(self):
        self._analyse()
        return self._handle()

    def _handle(self):
        total = total_string1 = total_string2 = 0
        for word in self._words:
            total += self._words[word][0] * self._words[word][1]
            total_string1 += pow(self._words[word][0], 2)
            total_string2 += pow(self._words[word][1], 2)
        rate = total / (sqrt(total_string1* total_string2))
        return rate

    def _analyse(self):
        for word in self.string1:
            if word not in self.stopwords:
                if word not in self._words:
                    self._words[word] = [1, 0]
                else:
                    self._words[word][0] += 1

        for word in self.string2:
            if word not in self.stopwords:
                if word not in self._words:
                    self._words[word] = [0, 1]
                else:
                    self._words[word][1] += 1


def analyze(string1, string2, stopwords):
    words = {}
    for word in string1:
        if word not in stopwords:
            if word not in words:
                words[word] = [1, 0]
            else:
                words[word][0] += 1

    for word in string2:
        if word not in stopwords:
            if word not in words:
                words[word] = [0, 1]
            else:
                words[word][1] += 1
    return words

def run(words):
    total = total_string1 = total_string2 = 0
    for word in words:
        total += words[word][0] * words[word][1]
        total_string1 += pow(words[word][0], 2)
        total_string2 += pow(words[word][1], 2)
    rate = total / (sqrt(total_string1* total_string2))
    return rate


def similarity(result):
    return result



string1 = u'我 爱 你'
string2 = u'你 爱 我'

# string1 = u'你 爱 sasd我'
# string2 = u'你 爱sadasdsfdsfsdfsadsadasdsafdsfdsgvfsdfdsf 我'
a = TextSimilarity(string1, string2)
# a = TextSimilarity(u'我 爱 你', u'你 爱 我')
r = a.run()
print(r)
r = similarity(run(analyze(string1, string2, stopwords)))
print(r)