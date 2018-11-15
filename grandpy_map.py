#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import os
import googlemaps

print(os.environ.get("GOOGLE_KEY"))
class GoogleClient:
    """
    The module sentence_manipulator.py returns a string of key words.
    This class uses those key words to find an address with
    the Google Maps API.
    """

    def __init__(self, address=None):
        self.address = address
        self.gmaps = googlemaps.Client(key=os.environ.get("GOOGLE_KEY"))

    def get_address_from_keywords(self, address=None):
        """
        This function gets the result of the module sentence_manipulator.py
        and send it to the Google maps' API.
        """
        place_to_find = self.gmaps.geocode(address)
        # insérer une réduction des infos pour avoir que adresse et coord gps
        # avoir un dictionnaire plus simple
        return place_to_find


def main():
    """
    Executes the module.
    """
    google = GoogleClient()
    address = google.get_address_from_keywords("")
    print(address)


if __name__ == "__main__":
    main()
