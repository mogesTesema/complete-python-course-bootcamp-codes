import json

with open("file-handling/json-files-handling/friends-json.txt") as friends_json:
    file_contents = json.load(friends_json)
print(file_contents)

cars = [
    {"make":"Ford", "model":"Fista"},
    {"make":"Ford","model":"Focus"}
]

with open("cars.txt",'w') as cars_file:
    json.dump(cars, cars_file)

with open("cars.txt","r") as cars_file: 
    print(cars_file)