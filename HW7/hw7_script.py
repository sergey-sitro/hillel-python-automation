import requests
import os

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url).json()


def get_title_and_bodies(lst):
    content = [(i["title"].capitalize(), [j.capitalize() + ".\n"
                                          for j in i["body"].split("\n")])
               for i in lst]
    return content


with open(f"{os.getcwd()}/file.txt", "w") as file:
    for t, b in get_title_and_bodies(response):
        file.write(t + "\n\n")
        file.write("".join(b) + "\n")
