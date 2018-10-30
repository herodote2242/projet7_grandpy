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
    
    def lower_case(self):
        """
        Convert the message in lower case.
        """
        self.question = self.question.lower()
        return self.question
        
    def suppress_accents(self, question=None):
        """
        This functions removes the french accents.
        """
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
        for punctuation in ",?!\\;\"./:'&~{[(-|`_^@)]=}+*<>²%$£€µ§°¤":
            self.question = self.question.replace(punctuation, "")
            self.question = self.question.strip()
        return self.question

    def cut_question(self, question=None):
        """
        Separate each word of the message and return them into a list.
        """
        self.question = self.question.split()
        return self.question

    def no_stop_words(self, question=None):
        """
        remove the words if they are stopwords
        """
        for stopword in fr_stop_words.list_of_stop_words:
            try:
                self.question = self.question.remove(stopword)
            except:
                pass
        return self.question