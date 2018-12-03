#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import random
import sentence_manipulator
import grandpy_map
import grandpy_wiki
import grandpy_answers


class GrandpyApplication:
    """
    This class uses the three previous modules to analyse the user's question
    by parsing the words with sentence_manipulator, then using the keywords
    to search for a gps coordinates with granpy_map, and finally using the
    gps coordinates to find a page on wikipedia and extract its summary with
    grandpy_wiki.
    """

    def __init__(self, question=None):
        self.question = question
        manipulator = sentence_manipulator.SentenceManipulator()
        google = grandpy_map.GoogleClient()
        wiki = grandpy_wiki.WikiClient()
        self.keywords = manipulator.clean_sentence(self.question)
        self.coordinates = google.get_address_from_keywords(self.keywords)
        self.summary = wiki.get_article_from_geodata(self.coordinates)

    def get_summary(self):
        """
        This function receives the user's question, manipulates it and
        returns an summary of the wikipedia's article.
        """
        return self.summary

    def get_coordinates(self):
        return self.coordinates

    def get_grandpy_speech(self):
        """
        This function creates the structure of the grandpy's speech. It
        randomly chooses (from pre-existing lists) a catch-phrase, a positive
        answer if a summary is found, or a negative answer if not.
        """
        # Grandpy says a catch-phrase, to simulate the arrival of the user
        welcome = random.choice(grandpy_answers.WELCOME_PHRASE, 1)
        """
        If the modules find a answer, Grandpy gives a positive answer,
        followed by the summary of the wikipedia's article.
        """
        if self.summary:
            return welcome, random.choice(grandpy_answers.POSITIVE_ANSWER, 1)
        # If there is no available answer, Grandpy gives a negative answer.
        else:
            return welcome, random.choice(grandpy_answers.NEGATIVE_ANSWER, 1)

    def get_answer pour aovi run dictionnaire de toutes les réponses


def main():
    """
    Executes the module.
    """
    question_test = 'Salut ..'
    app = GrandpyApplication(question_test)
    print(app.get_summary())
    print(app.get_coordinates())
    print(app.get_grandpy_speech())
#mettre dans un dictionnaire avec question initiale 


if __name__ == "__main__":
    main()
