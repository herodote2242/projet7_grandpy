#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from mediawiki import MediaWiki


class WikiClient:
    """
    The module sentence_manipulator.py returns a string of key words.
    The module grandpy_map uses those key words to find an address with
    the Google Maps API.
    This class uses the previous address to find some background on wikipedia
    to be told by the good old gramps'.
    """

    def __init__(self):
        self.geodata = None
        self.wikipedia = MediaWiki()

    def get_article_from_geodata(self, geodata):
        """
        This function gets the result of the module grandpy_map.py
        and send it to the Wikipedia's API.
        """
        self.geodata = geodata
        # récupérer uniquement lat et long pour les passer à geosearch pour retourner une liste de titres
        titles = self.wikipedia.geosearch(self.geodata)
        # choisir un titre avec randomchoice et le passer à wikipedia.page, récuperer le résumé et le lien vers la page wiki
        return titles


def main():
    """
    Executes the module.
    """
    wiki = WikiClient()
    background = main.return_background_from_address()
    return background
    print(background)


if __name__ == "__main__":
    main()
