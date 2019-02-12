#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import os
import html

import googlemaps


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
        # -tc- si l'utilisateur tape n'importe quoi, place_to_find est une liste
        # -tc- vide
        place_to_find = self.gmaps.geocode(address)
        # To find the exact address of the location :
        # -tc- tester si place_to_find contient un élément. Si place_to_find est vide, donner des 
        # -tc- indiquant vide à exact_address, latitude et longitude ou retourner une indication d'erreur.
        exact_address = place_to_find[0]['formatted_address']
        # To find the gps coordinates :
        latitude = place_to_find[0]['geometry']['location']['lat']
        longitude = place_to_find[0]['geometry']['location']['lng']
        # To avoid XSS attacks, using html.escape() function :
        return html.escape(exact_address), latitude, longitude


def main():
    """
    Executes the module.
    """
    google = GoogleClient()
    address = google.get_address_from_keywords("")
    print(address)


if __name__ == "__main__":
    main()
