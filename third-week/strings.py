s = 'hello python'
#how to declare a string
# h >> 0 e >> 1 basiclly treates it like an array/lists chars
#it counts the spaces too
#whats diffrnet from a list and a string is we cant change any of its element by accessing it
#s[0] = 'p' would give an error
help(s.capitalize())
#putting anything in a help method would give u info about it
s.capitalize() # only changes the first letter of the string to be capital
s.upper() # this makes the whole string capital
s.lower() # this changes the whole string to lower case
#it wouldnt crash if the words were already lower or upper 
# it doesnt change the original string only if we assign it to that

sr= '          HELLO PYTHON          '
sr.strip() # only removes the white spaces from the start and end of the string,

sr = 'hello python'
sr.replace('python' , 'world') #finds the first word in the string and replace it with the second
#is case sensetive, if the first word is not found then it doesnt do anything, if multiple word is there, then it would replace all of them 

s = "hello python python"
s.find('python')# returns the index of the first letter of the word python in the string if found
#if the word looking for was not found then it returns -1
s.rfind('python')# starts form the end and looks for python until it find the first p of the word python then returns its index

s = 'Apple Banana Orange'
l = s.split() # this takes the string and puts every word seprated by spcase in a list of strings
s.split(',') # this would change the default of split form space to ,
' '.join(l) # this would join the list elements l by a space
'.'.join(l) # this would join them with a .

s = 'hello python python'
l = s.split()
l[1] = 'world'
s= " ".join(1)
# this is how to change one elemnt in the string with another 

#-------------------------------------------------------------------

name = 'daniah'
age = '22' #if age was int of float this wouldnt work, either keep it a string or cast it as a string using str(age)
print('my name is '+ name + ' and my age is '+ age)
#or use formating
print('my name is {} and my age is {}'.format(name, age)) # fromat is better for the runtime compiler
print('my name is {} and my age is {}'.format(name, age+5)) #can even treat it like a number 

#F-string
print(f'my name is{name} and my age is {age}')
print(f'my name is{name} and my age is {age+5}') #can also change it like an int

email = 'daniah@gmail.com'
l = email.split('@')
s = l[1]
l2 = s.split('.')
print(f'Domail {l2[0]}')


def findDomail(email):
  l = email.split('@')
  s = l[1]
  l2= s.split('.')
  return l2[0]


email = 'daniah1234@gamil.com'
findDomail(email) 
#for methods one method can return multiple datatypes, one time a string, another an integer issokayyy

email = 'ehehheh@gmail.com'
start = email.find('@')
end = email.find('.')
email[start+1,end]
#this is a diffrent way to split the string

