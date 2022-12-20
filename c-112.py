import os
import shutil

source="C:/Users"
destination="C:/Users/tejas/Desktop/1"




list=os.listdir(source)
for i in list:
    name,extension=os.path.splitext(i)
    print("name",name)
    print("extenshion",extension)
    if extension == "":
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Image_Files"
        path3 = destination + '/' + "Image_Files" + '/' + i

        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("moving")
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving")
