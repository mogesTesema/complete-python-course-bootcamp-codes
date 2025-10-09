import shutil,os
# shutil.move("advanced_import/main_programm.py","advanced_import/main_package")
for dir, sub_dir,files in os.walk(os.getcwd()):
    # print(f"dir path:{dir}, sub_dir: {sub_dir}, files: {files}")
    print(f"there are {len(sub_dir)} directory and {len(files)} files inside {dir}\n")