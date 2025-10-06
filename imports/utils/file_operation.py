def save_to_file(content,filename):
    with open(filename,"w") as file:
        file.write(content)

def read_file(filename):
    with open(filename) as file:
        return file.read()
print("imported module")