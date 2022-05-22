import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url).json()


def get_title_and_bodies(lst):
    content = [(i["title"].capitalize(), [j.capitalize() + ".\n" for j in i["body"].split("\n")]) for i in lst]
    return content


fp = "/Users/sergeymatkobozhyk/Desktop/Hillel/Hillel Project/Homework/hillel-python-automation/HW7/file.txt"

with open(fp, "w") as file:
    for t, b in get_title_and_bodies(response):
        file.write(t + "\n\n")
        file.write("".join(b) + "\n")
