#Os module
import os


#1 getting the current cwd using -
#os.getcwd()

cwd=os.getcwd()
print('Current working directory',cwd)


#2 changing the cwd
#os.chdir()
def current_path():
    print('current working directory')
    print(os.getcwd())
    print()

current_path()
os.chdir('/')
current_path()

#3Creating directory
#A)os.mkdir()
parent_dir="E:/python projects/a"

directory="i am vengence"
path=os.path.join(parent_dir,directory)
os.mkdir(path)
print("Directory'%s'Created"%directory)

directory="i am batman"
mode=0o666
path=os.path.join(parent_dir,directory)
os.mkdir(path,mode)
print("Directory'%s'Created"%directory)


#B)os.makedirs()
parent_dir="E:/python projects/a/hello/ok"

directory="spiderman"
path=os.path.join(parent_dir,directory)
mode=0o666
os.makedirs(path,mode)
print("Directory'%s'Created"%directory)


#4Listing files and directories with python
#os.listdir()
path="E:/python projects"

dir_list=os.listdir(path)
print("files and directory in ",path,":")
print(dir_list)


#5Deleting a file and direcrory
#A)os.remove() only delete a file
file="1.txt"
location="E:/python projects/ep/a"

path=os.path.join(location,file)
os.remove(path)

#B)os.rmdir() delete a empty dir
directory="a"
location="E:/python projects/ep"

path=os.path.join(location,directory)
os.rmdir(path)

#6Renameing the file and directories
sd="E:/python projects/ep/a"
fd="E:/python projects/ep/o"
os.rename(sd,fd)

os.rename(sd,fd)







