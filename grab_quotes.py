"""
    Basic web crawler.

    Input:
        Filename for output
        Tag for quote website to filter quotes by

    Uses GoodReads to search for quotes based off of the tag.
    Goes to each quote, grabs text and writes to output file with delim.
"""
import sys
import requests
from bs4 import BeautifulSoup

def base(output, tag):
    """ Base crawl function. Go to base website, recursively get quotes, write to output """

    request = requests.get("http://www.goodreads.com/quotes/tag/" + tag)
    html = request.content
    soup = BeautifulSoup(html, "html.parser")

    quotes = sub_page(soup)

    for quote in quotes:
        output.write(quote + "\nDELIM\n")


def sub_page(soup):
    """ Recursively examine each sup-page and append any quote text to output list """

    quotes = []
    for quote in soup.find_all("div", {"class" : "quoteText"}):
        quotes.append(quote.contents[0])

    if soup.find("a", {"class" : "next_page"}) is None:
        return quotes
    else:
        quotes += sub_page(BeautifulSoup(requests.get("https://www.goodreads.com/" \
            + soup.find("a", {"class" : "next_page"})['href']).content, \
            "html.parser"))

    return quotes

def main():
    """ Main function.  Take in file and tag, open output and send to base function """

    filename = sys.argv[1]
    tag = sys.argv[2]

    output = open(filename, "w")
    base(output, tag)

if __name__ == "__main__":
    main()
