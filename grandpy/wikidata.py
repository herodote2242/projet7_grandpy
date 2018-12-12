#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from mediawiki import MediaWiki
import random


class WikiClient:
    """
    The module sentence_manipulator.py returns a string of key words.
    The module grandpy_map uses those key words to find an address with
    the Google Maps API.
    This class uses the previous address to find some background on wikipedia
    to be told by the good old gramps'.
    """

    def __init__(self, lang='fr'):
        self.geodata = None
        self.wikipedia = MediaWiki(lang=lang)

    def get_article_from_geodata(self, geodata):
        """
        This function gets the result of the module grandpy_map.py
        and send it to the Wikipedia's API.
        """
        formatted_address, latitude, longitude = geodata
        """
        geosearch(latitude='x.x', longitude='x.x') returns a list of
        different places/monuments within the radius (in meters).
        """
        titles = self.wikipedia.geosearch(
            latitude=latitude, longitude=longitude, radius=5000)
        # Select just one of the different results of the geosearch function :
        if titles != []:
            title = random.sample(titles, 1)
            title = title.pop()
            construction_to_describe = self.wikipedia.page(title)
            # In order to return the address of the wikipedia's article.
            url_address = construction_to_describe.url
            # The summarize function returns x first sentences of the summary.
            summary = construction_to_describe.summarize(sentences=4)
            return summary, url_address


def main():
    """
    Executes the module.
    """
    wiki = WikiClient()
    article = wiki.get_article_from_geodata()
    return article


if __name__ == "__main__":
    main()
