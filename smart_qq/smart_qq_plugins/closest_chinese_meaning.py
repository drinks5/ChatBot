# -*- coding: utf-8 -*-
# @Author: drinksober
# @Date:   2016-04-21 16:59:27
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-23 09:11:54

from math import sqrt
from chatterbot.adapters.exceptions import EmptyDatasetException
from .base_match import BaseMatchAdapter


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
    rate = total = total_string1 = total_string2 = 0
    for word in words:
        total += words[word][0] * words[word][1]
        total_string1 += pow(words[word][0], 2)
        total_string2 += pow(words[word][1], 2)
    if total_string1 and total_string2:
        rate = total / (sqrt(total_string1 * total_string2))
    
    return rate


class ClosestChineseMeaningAdapter(BaseMatchAdapter):
    def __init__(self, **kwargs):
        super(ClosestChineseMeaningAdapter, self).__init__(**kwargs)
        self.stopwords = [u'的', u'地', u'得', u'呀']

    def get_similarity(self, string1, string2):
        result = run(analyze(string1, string2, self.stopwords))
        return result

    def get(self, input_statement, statement_list=None):
        """
        Takes a statement string and a list of statement strings.
        Returns the closest matching statement from the list.
        """

        statement_list = self.get_available_statements(statement_list)

        if not statement_list:
            if self.has_storage_context:
                # Use a randomly picked statement
                return 0, self.context.storage.get_random()
            else:
                raise EmptyDatasetException

        # Get the text of each statement
        text_of_all_statements = []

        for statement in statement_list:
            text_of_all_statements.append(statement.text)

        # Check if an exact match exists
        if input_statement.text in text_of_all_statements:
            return 1, input_statement

        closest_statement = None
        closest_similarity = -1
        total_similarity = 0

        # For each option in the list of options
        for statement in text_of_all_statements:
            similarity = self.get_similarity(input_statement.text, statement)

            total_similarity += similarity

            if similarity > closest_similarity:
                closest_similarity = similarity
                closest_statement = statement

        try:
            confidence = closest_similarity / total_similarity
        except:
            confidence = 0
        return confidence, next(
            (s for s in statement_list if s.text == closest_statement), None)
