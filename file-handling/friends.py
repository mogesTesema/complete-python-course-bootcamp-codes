# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# for each near by friend, we 'll save their name to nearby_friends.txt
friends = input("Enter three friend names, saparated by commas(no spaces, please): ").split(",")
with open("file-handling/people.txt","r") as people:
    people_nearby = [line.strip() for line in people.readlines()]
friends_set = set(friends)
people_nearby_set = set(people_nearby)
friends_nearby_set = friends_set.intersection(people_nearby_set)

with open("file-handling/nearby_friends_file","a") as nearby_friends_file:
    for friend in friends_nearby_set:
        print(f"{friend} is nearby! Meet up with them.")
        nearby_friends_file.write(f"{friend}\n")

  