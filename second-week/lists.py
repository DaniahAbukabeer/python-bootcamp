l= [1,2,"hello",9.2]
#lists in python works like array and can have any data type all together and the 
#index is like c++ starting form 0, dont have to specify the size either
l[2] #to access a specifc elemtn by index
l[1:2] #we access the element in this range, the range be read like
#[1,2) so index 1 is with us but 2 is not bc its not enclusive
l[0:]#this would access all the elements in the list
#l[start:stop(not included)]
l[:4] #starts form the begining and stops at 4 (4 not included)
l[:] #this would print the whole list as well
#l[start:stop:steps]
l[0:3:2] 
#so if the list had [0,1,2,3]
#this would print [0,2]
#if we need to access the list backward 
l[3::-1]#this would print the whole thing backwards
#if we say l[4:0:-1] this would skip the elemetn l[0] bc the end [4:0] is not included 
#also in python we can access the same element by either their index or the negative index
#l[1,2,  3, 4]
#  0,1,  2, 3
# -4,-3,-2,-1
#-----------------------------------------------------------------------
l= [1,2,3,4,"hello"] #if we want to change the word hello we just access it 
l[4]= 5
l[1:3]=[1,2] # if the list was [1,2,3,4,5]
#the result would be [1,1,2,4,5]
l=[1,2,3,4,5]
l[1:3]=[90,90,90]
#this would take a block from index 1 to index 2 and replace it with three 90s
#so the output would be 
#1,90,90,90,4,5

l=[1,2,3,4,5]
l[1:3] = []
#the out put would be [1,4,5]

l=[1,2,34,5,6,]
l[0]=[1,2,3,4]
#l=[[1,2,3,4],2,3,4,5,6]
#this how we get a list inside a list 


def newlist(l):
  return l[0::2]


listheheh=[1,2,3,4]
returned = newlist(listheheh)
print(returned)
#------------------------------------------
l=[1,2,3,4,5]
#l[2]=90
#or simply use mehtod
#l.insert(index,value)
print(l.insert(2,90))#insert doesnot overiied it it just addes it to the list 

#so the list would be [1,90,2,3,4,5]

l.append(1000)
#this adds to the end of the list
#dir => directory if we say dir(l) it would show us all hte methods that we can use for the thing we added 
#in this case a list named l
l.append([1,2,3,4])
#[1,2,3,4,5,[1,2,3,4]]

l.extend([1,2,3,4])
#[1,2,3,4,5,1,2,3,4]
#this method takes the values as numbers and add them not as list in append
l=[1,2,3,3,3,4,5]
l.remove(3)
#this would remove the first 3 !!not index 3
#[1,2,3,3,4,5]
#to remove with index we use pop
l.pop(0)#and it returns the poped value
#if we didnt give it any value it removes the last element in the list
x=l.pop()

l.count(3)
#counts how many time theres a 3 in the lsit

#if we want to know at what index 3 is 
l.index(3)#and it returns the index of the first 3 it finds in case of multiple 3s!


#to sort a method we use sort
l.sort()
#merge sort
#if we want to sort reversse
l.sort(reverse=True)
#this would sort it decsindeing 

original = [1,2,3,4]
copied = original

original[2]=0
#this would also affect the copy bc its by refrence 
#bc both original and copied just points at the same place in the memorey

original = [1,2,3,4]
copied = original.copy()
original[2]=0
#this wouldnot make it a copy by refrence so this wouldnt affect the copy

max([1,2,3,4])
min([1,2,3,4,5])
#max and min takes intergers not just lists and it takes strings and chars and comparse them with ascii code
len([1,2,3,4,5,6])
#returns the length of the list
sum([1,2,3,4,5])

l=[1,2,3]
l2=[4,5,6]
l+l2 # this would be [1,2,3,4,5,6]

l=[1,3,4]*3 #thsi would repeat the list three times
#[1,3,4,1,3,4,1,3,4]

3 in [1,2,3,4]
#returns bool if 3 is in the llist or not
if 3 in l:
  print(l)
elif 2 in l:
  print(2)

l=[1,2,3]
l2=[1,2,3]
if l==l2:
  print("yes")
else:
  print("no")

#in python for loop works like a foreach so it just works with listsn

l=[1,2,3,4]
for i in l:
  print(i)
  print(i,end=" ")
  #this would change the default for pirint that the end is a new line to the end being a space so all elemnts
  #will be printed on the same line
#thers no i++ only i+=1

for i in l:
  print(l.index(i))#this will print all the index of all the elements

#in python we cant use i as a counter to do stuff, we need a counter

l= [1,2,3,4]
counter = 0
for i in l:# i is the value inside the list, to move accoding to the index we need to create a counter 
  l[counter]= i
  counter+=1
  print(i,end=" ")

list(range(5))
#this creates a list from 0 to 4 , 5 indexes

for i in range(5):
  print(i)
#print 0 1 2 3 4

i = 0
while i < 10:
  print(i)
  i+=1


