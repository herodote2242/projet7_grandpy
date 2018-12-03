#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import grandpy_wiki


class TestWikiClient:

    def test_get_article_from_geodata(self, monkeypatch):
        """
        For this mock, let's choose the Lyon' Basilique de Fourviere
        as the place to be found.
        """
        result = "La basilique Notre-Dame de Fourvière surplombe la ville de\
        Lyon depuis le sommet de la colline de Fourvière depuis la fin du\
        XIXe siècle.\nElle est construite à peu près sur l'emplacement de\
        l'ancien forum de Trajan Forum vetus, hypothèse étymologique la plus\
        probable pour le nom actuel de Fourvière). Sur cet emplacement est\
        institué au milieu du Moyen Âge un culte à saint Thomas de Cantorbéry\
        puis, rapidement, à la Vierge. Ce double culte se concrétise avec la\
        construction d'un lieu de dévotion, la chapelle Saint-Thomas."

        def mock_init(self, lang):
            pass

        def mock_geosearch(self, latitude, longitude, radius):
            return ['basilique Notre-Dame de Fourvière']

        class MockPage:

            def summarize(self, sentences):
                return result

        def mock_page(self, title):
            return MockPage()

        monkeypatch.setattr('grandpy_wiki.MediaWiki.__init__', mock_init)
        monkeypatch.setattr(
            'grandpy_wiki.MediaWiki.geosearch', mock_geosearch)
        monkeypatch.setattr('grandpy_wiki.MediaWiki.page', mock_page)
        client = grandpy_wiki.WikiClient(lang='fr')
        assert client.get_article_from_geodata(('8 Place de Fourvière, 69005\
            Lyon, France', 45.7622928, 4.822626)) == result
