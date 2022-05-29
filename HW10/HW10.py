import requests
from bs4 import BeautifulSoup

start_url = "https://quotes.toscrape.com"


def get_content(url):
    return requests.get(url).text


def find_next(url):
    next_ref = BeautifulSoup(get_content(url), "html.parser").nav.a.get("href")
    return next_ref


def main():
    pages_counter = 1
    next_url = find_next(url=start_url)

    while True:

        if next_url:
            next_url = find_next(url=start_url + next_url)
            pages_counter += 1

        else:
            print(pages_counter)
            break

    return pages_counter


if __name__ == "__main__":
    pages_count = main()  # you can user any code runner you want
    print(pages_count)
