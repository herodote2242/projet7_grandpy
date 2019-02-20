#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import grandpy.app


class TestGrandpyApp:
    """
    This class tests the final module of the application : grandpy_app.py
    which is the last and the launching module to run the app.
    """

    def test_get_answer(self, monkeypatch):
        """
        This test is in charge of checking if grandpy answers one of the
        sentences when a question is asked.
        """
        summary = "La basilique Notre-Dame de Fourvière surplombe la ville de\
        Lyon depuis le sommet de la colline de Fourvière depuis la fin du\
        XIXe siècle."
        coordinates = ('8 Place de Fourvière, 69005 Lyon, France',
                       45.7622928, 4.822626)
        positive_result = "Ho, je vois très bien de quoi tu parles..."
        url = "https://wikipedia.fr"
        total_answer = {
            'speech': positive_result,
            'summary': summary,
            'coords': coordinates,
            'url': url}

        def mock_init(self, question=None):
            self.speech = positive_result
            self.coordinates = coordinates
            self.summary = summary
            self.url = url

        def mock_get_grandpy_speech(self):
            return positive_result

        monkeypatch.setattr("grandpy.app.GrandpyApplication.__init__",
                            mock_init)
        monkeypatch.setattr(
            "grandpy.app.GrandpyApplication.get_grandpy_speech",
            mock_get_grandpy_speech)
        appli = grandpy.app.GrandpyApplication()
        assert appli.get_answer() == total_answer
