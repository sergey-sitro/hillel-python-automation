import requests
from bs4 import BeautifulSoup

start_url = "https://quotes.toscrape.com"


def get_content(url):
    return requests.get(url).text


def find_next(url):
    try:
        next_ref = BeautifulSoup(get_content(url), "html.parser").find("li", {"class": "next"}).a.get("href")

        return next_ref
    except AttributeError:
        print("End of pages!")
        return None


def main():
    pages_counter = 1
    next_url = find_next(start_url)
    while True:

        if next_url:
            next_url = find_next(start_url + next_url)
            pages_counter += 1

        else:
            break

    return pages_counter


if __name__ == "__main__":
    pages_count = main()  # you can user any code runner you want
    print(pages_count)
