#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import grandpy_app
import grandpy_answers


class TestGrandpyApp:
    """
    This class tests the final module of the application : grandpy_app.py
    which is the last and the launching module to run the app.
    """
    def test_grandpy_speech():
        """
        This test is in charge of checking if grandpy answers one of the
        sentences when a question is asked.
        """
        summary = "La basilique Notre-Dame de Fourvière surplombe la ville de\
        Lyon depuis le sommet de la colline de Fourvière depuis la fin du\
        XIXe siècle.\nElle est construite à peu près sur l'emplacement de\
        l'ancien forum de Trajan Forum vetus, hypothèse étymologique la plus\
        probable pour le nom actuel de Fourvière). Sur cet emplacement est\
        institué au milieu du Moyen Âge un culte à saint Thomas de Cantorbéry\
        puis, rapidement, à la Vierge. Ce double culte se concrétise avec la\
        construction d'un lieu de dévotion, la chapelle Saint-Thomas."
        catch_result = 'Ha ! Mon petit, je suis content de te voir !'
        positive_result = 'Ho, je vois très bien de quoi tu parles.\
        Sais tu que....'
        negative_result = 'Décidément, je ne vois pas de quoi tu parles...'

        def mock_init(self, question):
            pass

        class MockApp:

            def mock_summary(self, question):
                return summary

        def mock_random_choice(answer):
            return catch_result, positive_result

        def mock_app(self):
            return MockApp()

        monkeypatch.setattr('grandpy_app.__init__', mock_init)
        