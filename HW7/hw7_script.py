import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

response_json = response.json()

titles = [t["title"].capitalize() for t in response_json]
bodies = [b["body"].replace("\n", ". ") for b in response_json]
print(bodies)

list_bodies = [s.split(". ") for s in bodies]
print(list_bodies)

real_bodies = [i for i in [j for j in list_bodies]]

# for i in list_bodies:
#     for j in i:
#         real_bodies.append(j.capitalize())

print(real_bodies)


# title_and_body = list(zip(titles, bodies))
# print(title_and_body)
#
# fp = "/Users/sergeymatkobozhyk/Desktop/Hillel/Hillel Project/Homework/hillel-python-automation/HW7/file.txt"
#
# with open(fp, "w") as file:
#     for t, b in title_and_body:
#         file.write(t)
#         file.write(b)

