#!/usr/bin/env python3.6
"""
Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """
    Fetch a list of words from a URL.
    :params url:
        The URL of a UTF-8 text document
    :returns:
        A list of strings containing the words
        from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_items(story_words):
    """
    Print items one per line.
    :params story_words:
        An iterable series of printable items
    :returns:
        N/A
    """
    for word in story_words:
        print(word)


def main(url):
    """
    Print each word from a text document from a URL.

    :param url:
        The URL of a UTF-8 text document.
    :return:
        N/A
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    main(sys.argv[1])
