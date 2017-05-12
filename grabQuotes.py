import requests
from bs4 import BeautifulSoup
import sys

def base(output, tag):
    
    
    r = requests.get("http://www.goodreads.com/quotes/tag/" + tag)
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    
    quotes = sub_page(soup)
    
    for quote in quotes:
        output.write(quote + "\nDELIM\n")


def sub_page(soup):
    
    quotes = []
    for quote in soup.find_all("div", {"class" : "quoteText"}):        
        quotes.append(quote.contents[0])

    if soup.find("a", {"class" : "next_page"}) == None:
        return quotes
    else:
        quotes += sub_page(BeautifulSoup(requests.get("https://www.goodreads.com/" + soup.find("a", {"class" : "next_page"})['href']).content, "html.parser"))

    return quotes


def main():
    
    filename = sys.argv[1]
    tag = sys.argv[2]

    output = open(filename, "w")
    base(output, tag)


if __name__ == "__main__":
    main()
