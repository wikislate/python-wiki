import os 
print(os.getcwd()) 
# To print absolute path on your system 
#print(os.path.abspath('.'))
  
# To print files and directories in the current directory on your system 
#print(os.listdir('.'))

fd = "temp.py"
os.rename(fd,'mathmodule.py') 
