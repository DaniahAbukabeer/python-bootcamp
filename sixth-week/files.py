#read only r


#creating fiels with x
with open('createdFile.txt', 'x') as f:
  f.write('hello from python')

#mod r reads the file, and with print f.read() it prints whatever it read
#retuns a big string with everything
with open('createdFile.txt','r') as f:
  print(f.read())

#wrting in a file mod w !! but this would overwirte whatever was already here
with open('createdFile.txt','w') as f:
  f.write('am using python \n')
  
#to not overwiret we use

with open('createdFile.txt', 'a') as f:
  f.write(' hello from python')
  
#function readline would read the file line by line os you can process it line by line
#it returns a list of each line
with open('createdFile.txt', 'r') as f:
  for line in f.readlines():
    print(line.upper())
    
#to read and write at the smae time we use r+
with open('createdFile.txt', 'a+') as f:
  for line in f.readlines():
    line = line.upper()
    f.write(line)
    
    
import os 
os.getcwd() #prints the name of the directory

os.chdir('path/of/direcotry')# changes the dirctory based on the path sent to 
#and all the work we made will be saved in the new files

#to make a new direcotry 
os.mkdir('newdir')
import os 
os.makedirs('dir1/dir2')#this makes multipile direcotries neastied in each other

#to remove a dir
import os
os.rmdir('dir name') #must be inside the dir
import os 
os.removedirs('dir1/dir2')#this would remove both the parent and the child

import os, shutil
#shutil.rmtree(dir1)

for i,j,k in os.walk():
 print(f'current directory {i}')
 print(f'directiores {i}')
 print(f'file names {k}')