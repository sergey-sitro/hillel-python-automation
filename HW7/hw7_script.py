import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url).json()


titles = [t["title"].capitalize() for t in response]
bodies = [b["body"] for b in response]

list_bodies = [s.split("\n") for s in bodies]

groupped_bodies = [
    [string.capitalize() + ".\n" for string in string_list]
    for string_list in list_bodies
]

final_bodies = ["".join(b) for b in groupped_bodies]

title_and_body = list(zip(titles, final_bodies))

fp = "/Users/sergeymatkobozhyk/Desktop/Hillel/Hillel Project/Homework/hillel-python-automation/HW7/file.txt"

with open(fp, "w") as file:
    for t, b in title_and_body:
        file.write(t + "\n")
        file.write(b + "\n")
