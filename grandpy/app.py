#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import random
import grandpy.sentence_manipulator
import grandpy.maps
import grandpy.wikidata
import grandpy.answers


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
        manipulator = grandpy.sentence_manipulator.SentenceManipulator()
        google = grandpy.maps.GoogleClient()
        wiki = grandpy.wikidata.WikiClient()
        self.keywords = manipulator.clean_sentence(self.question)
        self.coordinates = google.get_address_from_keywords(self.keywords)
        self.summary = wiki.get_article_from_geodata(self.coordinates)

    def get_summary(self):
        """
        This function returns a summary of the wikipedia's article
        and its url about the place found by the API.
        """
        return self.summary

    def get_coordinates(self):
        """
        This function retuns the GPS coordinates of the place found by
        the API.
        """
        return self.coordinates

    def get_grandpy_speech(self):
        """
        This function creates the structure of the grandpy's speech. It
        randomly chooses (from pre-existing lists) a catch-phrase, a positive
        answer if a summary is found, or a negative answer if not.
        """
        # Grandpy says a catch-phrase, to simulate the arrival of the user.
        welcome = random.choice(grandpy.answers.WELCOME_PHRASE, 1)
        """
        If the modules find an answer, Grandpy gives a positive answer,
        followed by the summary of the wikipedia's article.
        """
        if self.summary:
            self.speech = welcome, random.choice(
                grandpy.answers.POSITIVE_ANSWER, 1)
        # If there is no available answer, Grandpy gives a negative answer.
        else:
            self.speech = welcome, random.choice(
                grandpy.answers.NEGATIVE_ANSWER, 1)
        return self.speech

    def get_answer(self):
        """
        This function associates the three previous returns into a single
        dictionnary, which will be used by the JavaScript part of the app.
        """
        total_answer = {
            'speech': self.speech,
            'summary': self.summary,
            'coords': self.coordinates}
        return total_answer


def main():
    """
    Executes the module.
    """
    app = GrandpyApplication()
    app.get_summary()
    app.get_coordinates()
    app.get_grandpy_speech()
    app.get_answer()


if __name__ == "__main__":
    main()
