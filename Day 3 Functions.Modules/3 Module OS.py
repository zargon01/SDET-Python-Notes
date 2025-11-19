import os
print(os.getcwd())                                  #cwd - current working directory
os.mkdir("folder/myfolder")                         #mkdir - make directory
os.makedirs("folder1/folder2/folder3")              #make many folders
os.remove("folder1/folder2")                        #delete a file
os.rmdir("folder1/folder2")                         #delete a folder
print(os.path.exists("folder1"))                    #check if a folder exists
path = os.path.join("C://user","Document","file")   #concat all the paths