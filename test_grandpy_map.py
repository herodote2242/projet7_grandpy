#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import grandpy_map


class TestGoogleClient:

    def test_get_address_from_keywords(self, monkeypatch):
        """
        For this mock, let's choose the Lyon' Basilique de Fourviere
        as the place to be found.
        """
        geocode_result = [{
            'formatted_address': '8 Place de Fourvière, 69005 Lyon, France',
            'geometry': {
                'location': {
                    'lat': 45.7622928, 'lng': 4.822626
                }
            }
        }]
        result = ('8 Place de Fourvière, 69005 Lyon, France',
            45.7622928, 4.822626)

        def mock_init(self, key):
            pass

        def mock_geocode(self, address):
            return geocode_result

        monkeypatch.setattr(
            "grandpy_map.googlemaps.Client.__init__", mock_init)
        monkeypatch.setattr(
            "grandpy_map.googlemaps.Client.geocode", mock_geocode)
        client = grandpy_map.GoogleClient()
        assert client.get_address_from_keywords(
            'Lyon Basilique de Fourvière') == result
