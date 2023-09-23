#!/usr/bin/env python

from lxml import html
import requests, sys

def return_html(verb):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.36"
    }

    url = (
        "https://conjugator.reverso.net/conjugation-spanish-verb-"
            f"{verb}.html"
    )

    # gets page and lets us know if access is forbidden, or if it just 
    # didn't work
    page = requests.get(url, headers=headers)
    if page.status_code == 403:
        print("Error: status forbidden")
        sys.exit(1)
    elif page.status_code != 200:
        print("Error: could not connect")
        sys.exit(1)

    tree = html.fromstring(page.content)

    return tree

def scrape_html(tree):
    # inelegant method of locating text on page
    presente = [ 
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[1]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[2]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[3]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[4]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[5]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[6]/i[2]"),
    ]

    futuro = [
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[1]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[2]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[3]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[4]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[5]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[6]/i[2]"),
    ]

    preterito = [
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[1]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[2]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[3]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[4]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[5]/i[2]"),
        tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[6]/i[2]"),
    ]

    presente_text = []
    futuro_text = []
    preterito_text = []

    # all list items are converted to strings within the appropriate group,
    # which is then returned as a single list
    for verbs in presente:
        stringify_elements(verbs, presente_text)

    for verbs in futuro:
        stringify_elements(verbs, futuro_text)

    for verbs in preterito:
        stringify_elements(verbs, preterito_text)

    full_text = [ 
                 presente_text, futuro_text, preterito_text 
    ]

    return full_text

# takes individual list elements and appends the strings within to
# the provided list
def stringify_elements(element, lista) -> None:
    for resultado in element:
        text = resultado.text
        if text is not None:
            lista.append(text)

# prints all the text in labelled columns
def print_text(full_text) -> None:
    print(f"PRESENTE".ljust(15) + f"FUTURO".ljust(15) + f"PRETÉRITO (imp)")

    i: int = 0
    while i < 6:
        print(f"{full_text[0][i]}".ljust(15) + f"{full_text[1][i]}".ljust(15)
              + f"{full_text[2][i]}")
        i += 1

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: conj <verb>\n\tReturns list of common conjugations.")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Error: one verb at a time")
        sys.exit(1)

    verb: str = sys.argv[1]

    tree = return_html(verb)

    full_text = scrape_html(tree)

    print_text(full_text)
