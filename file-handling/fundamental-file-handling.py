example = open("file-handling/example.txt","a")
print(example)
example.write("you are amazing guy!")
example.close()
example = open("file-handling/example.txt","r")
text = example.read()
text = text.split(" ")
# print("you" in text,text)
example.close()
# context manager
with open("file-handling/example.txt","w") as example:
    example.write("this is cool feature of context manager.")
    # print(example)
with open("file-handling/example.txt","r") as example:
    print(example.read())

with open("file-handling/example.txt","a") as example:
    example.write("\nwe are ganna use context manager,the best built in feature that manage file handling in python using with keyword")
with open("file-handling/example.txt","r") as example:
    print("this is the final version of example.txt file",example.read())

# CSV file handling
with open("file-handling/isris.csv","r") as isris:
    data = isris.read()
    data = data.split("\n")
    # print(data)
with open("file-handling/isris.csv","r") as isris:
    isris_data = isris.readlines()
isrises = []
for row in isris_data[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")
    isris_dict = {
    "sepal_length":int(float(sepal_length)),
    "sepal_width":float(sepal_width),
    "petal_length":float(petal_length),
    "petal_width":float(petal_width),
    "species":species
    }
    isrises.append(isris_dict)
print(isrises[0])

# another way to handle file
with open("file-handling/isris.csv","r") as file:
    isris_file = file.readlines()
header = isris_file[0].strip().split(",")
isris_data_v2 = []
for row in isris_file[1:]:
    isris = row.strip().split(",")
    isris_data_v2.append(dict(zip(header,isris)))
print(isris_data_v2[0])