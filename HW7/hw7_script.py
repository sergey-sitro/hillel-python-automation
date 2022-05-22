import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url).json()


def get_title_and_bodies(lst):
    content = []
    for i in lst:
        for _ in i["body"].split("\n"):
            content.append((i["title"].capitalize(), [j.capitalize() + ".\n" for j in i["body"].split("\n")]))

    return content


with open("file.txt", "w") as file:
    for t, b in get_title_and_bodies(response):
        file.write(t + "\n\n")
        file.write("".join(b) + "\n")
