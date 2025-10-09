import os
current_dir = os.getcwd()
print(f"current working dicrectory: {current_dir}")
current_dirs = os.listdir()
print("list of current working dir file and folders:\n")
print(current_dirs)
print(dir(os))