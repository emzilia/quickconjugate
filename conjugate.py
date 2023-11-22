#!/usr/bin/env python

try:
    from lxml import html
    import requests, sys
except ImportError:
    print("Error: Script requires pip packages that are missing: html, requests")
    sys.exit(1)

def scrape_html(verb):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.5938.92 Safari/537.36"
    }

    # the website to be scraped from, changing this would require changing
    # the hard-coded xpaths below
    url = (
        "https://conjugator.reverso.net/conjugation-spanish-verb-"
            f"{verb}.html"
    )

    # gets page and lets us know if access is forbidden, or if it just 
    # didn't work
    page = requests.get(url, headers=headers)
    match page.status_code:
        case 200:
            pass
        case 403:
            print("Error: Status forbidden")
            sys.exit(1)
        case 404:
            print("Error: Page not found")
            sys.exit(1)
        case _:
            print("Error: Unable to connect")
            sys.exit(1)

    html_tree = html.fromstring(page.content)

    return html_tree

def parse_html(html_tree):
    # inelegant method of locating text on page
    presente = [ 
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[1]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[2]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[3]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[4]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[5]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[2]/div/ul/li[6]/i[2]"),
    ]

    futuro = [
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[1]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[2]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[3]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[4]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[5]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[3]/div/ul/li[6]/i[2]"),
    ]

    preteritoimperf = [
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[1]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[2]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[3]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[4]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[5]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div"
                    "/div[1]/div[4]/div/div/div[1]/div[4]/div/ul/li[6]/i[2]"),
    ]

    preteritoperf = [
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[4]/div[1]/div/ul/li[1]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[4]/div[1]/div/ul/li[2]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[4]/div[1]/div/ul/li[3]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[4]/div[1]/div/ul/li[4]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[4]/div[1]/div/ul/li[5]/i[2]"),
        html_tree.xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div[3]/div/"
                    "div[1]/div[4]/div/div/div[4]/div[1]/div/ul/li[6]/i[2]"),

    ]

    presente_text = []
    futuro_text = []
    preteritoimperf_text = []
    preteritoperf_text = []

    # all list items are converted to strings within the appropriate group,
    # which is then returned as a single list
    for verbs in presente:
        stringify_elements(verbs, presente_text)

    for verbs in futuro:
        stringify_elements(verbs, futuro_text)

    for verbs in preteritoimperf:
        stringify_elements(verbs, preteritoimperf_text)

    for verbs in preteritoperf:
        stringify_elements(verbs, preteritoperf_text)

    full_text = [ 
        presente_text, futuro_text,
        preteritoimperf_text, preteritoperf_text 
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
    print(f"PRESENTE".ljust(16) + f"FUTURO".ljust(16) +
            f"PRETÉRITO (imp)".ljust(16) + f"PRETÉRITO (per)")

    i: int = 0
    while i < 6:
        print(f"{full_text[0][i]}".ljust(16) + f"{full_text[1][i]}".ljust(16)
              + f"{full_text[2][i]}".ljust(16) + f"{full_text[3][i]}")
        i += 1

# only accepts one argument
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: conj <verb>\n\tReturns list of common conjugations.")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Error: only one input is allowed at a time")
        sys.exit(1)

    verb: str = sys.argv[1]

    html_tree = scrape_html(verb)

    full_text = parse_html(html_tree)

    print_text(full_text)
