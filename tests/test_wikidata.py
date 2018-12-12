#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import grandpy.wikidata


class TestWikiClient:

    def test_get_article_from_geodata(self, monkeypatch):
        """
        For this mock, let's choose the Lyon' Basilique de Fourviere
        as the place to be found.
        """
        summary = "La basilique Notre-Dame de Fourvière surplombe la ville"
        url = "https://wikipedia.org"

        def mock_init(self, lang):
            pass

        def mock_geosearch(self, latitude, longitude, radius):
            return ['basilique Notre-Dame de Fourvière']

        class MockPage:

            def __init__(self):
                self.url = url

            def summarize(self, sentences):
                return summary

        def mock_page(self, title):
            return MockPage()

        monkeypatch.setattr('grandpy.wikidata.MediaWiki.__init__', mock_init)
        monkeypatch.setattr(
            'grandpy.wikidata.MediaWiki.geosearch', mock_geosearch)
        monkeypatch.setattr('grandpy.wikidata.MediaWiki.page', mock_page)
        client = grandpy.wikidata.WikiClient(lang='fr')
        assert client.get_article_from_geodata(('8 Place de Fourvière, 69005\
            Lyon, France', 45.7622928, 4.822626)) == (summary, url)
