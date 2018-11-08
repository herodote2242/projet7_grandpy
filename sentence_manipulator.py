#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import fr_stop_words


class SentenceManipulator:
    """
    This class modifies the written message by removing punctuation,
    accents, capitals and chitchat words in order to keep only
    the key words.
    """

    def __init__(self, question=None):
        self.question = question

    def lower_case(self, question=None):
        """
        Converts the message in lower case.
        """
        if question:
            self.question = question
        self.question = (str(self.question)).lower()
        return self.question

    def suppress_accents(self, question=None):
        """
        This functions removes the french accents.
        """
        if question:
            self.question = question
        for accent in "àâä":
            self.question = self.question.replace(accent, "a")
        for accent in "éèêë":
            self.question = self.question.replace(accent, "e")
        for accent in "îï":
            self.question = self.question.replace(accent, "i")
        for accent in "öô":
            self.question = self.question.replace(accent, "o")
        if accent == "ù":
            self.question = self.question.replace(accent, "u")
        if accent == "ç":
            self.question = self.question.replace(accent, "c")
        return self.question

    def suppress_punctuation(self, question=None):
        """
        This function removes the punctuation marks.
        """
        if question:
            self.question = question
        for punctuation in ",?!\\;\"./:'&~{[(-|`_^@)]=}+*<>²%$£€µ§°¤":
            self.question = self.question.replace(punctuation, " ")
            self.question = self.question.strip()
        return self.question

    def cut_question(self, question=None):
        """
        Separates each word of the message and return them into a list.
        """
        if question:
            self.question = question
        self.question = self.question.split()
        return self.question

    def suppress_stop_words(self, question=None):
        """
        Removes the words if they are part of the stopwords'list.
        """
        if question:
            self.question = question
        words = []
        for word in self.question:
            if word not in set(fr_stop_words.list_of_stop_words):
                words.append(word)
        self.question = words
        return words

    def clean_sentence(self, question=None):
        """
        Launches the different manipulations of a sentence.
        """
        self.question = question
        self.lower_case()
        self.suppress_accents()
        self.suppress_punctuation()
        self.cut_question()
        self.suppress_stop_words()
        return " ".join(self.question)


def main():
    """
    Launches the module.
    """
    main = SentenceManipulator()
    question = main.clean_sentence()
    return question


if __name__ == "__main__":
    main()
