import os
import shutil

from_dir = "C:/Users/vishn/Downloads"
to_dir = "C:/Users/vishn/OneDrive/Desktop/Document_Files"
list_of_files = os.listdir(from_dir)

for fileName in list_of_files:
    name, extension = os.path.splitext(fileName)

    if extension == "":
            continue
    if extension in [".gif", ".png", ".jpg",".jpeg",".jfif"]:
        path1 = from_dir + "/" + fileName
        path2 = to_dir + "/" + "image_file"
        path3 = to_dir + "/" + "image_file"+ "/" + "fileName"

        if os.path.exists(path2):
            print("moving" + fileName +".......")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving" + fileName + "....")
            shutil.move(path1,path3)

    
    



