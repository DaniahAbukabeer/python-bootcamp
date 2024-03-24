#{'key1':'value','key2':'value'} thats its syntax

dic = {'name':'Aftaf','Age':20}
print(dic)

print(dic['name'])#to access an elements it awayts the key and returns the value for this key

dic[0] = 'python'
dic['HAHAH'] = 'laughter'
dic['Age'] = 30
dic['Age'] = "35" #also works, so if hte old value for the key age was int we can still assign it new value of aother datatypes


dic = {'name':'daniah','age': 22}
l = list(dic.items())
print(l)
l[0]
#if we dont use list() then the returned datatype would be dict_items thingy but we cant access it like a list so cast it to list
#saves them as a pair of key and value
key = dic.keys() #this returns the keys in the dictionary but as dict_keys
key = list(dic.keys())# this solves the issue and make it into a list
print(key)

values = dic.values() # this one returns everything both keys and its values but all toghter and not as pairs
print(values)
lv = list(values)
print(lv)

dic = dic.clear() #this method deletes everything from the dictionary
print(dic)

dic = {'name':12,'age':233}
dic2 = dic.copy() # this would make a copy of dic but not with refrence, it would be by value
#so if anything change in one copy it wont affect hte other, but 
dic3 = dic # if anything changes in one of them, it changes the other 

#----------------how to use loop with dic------------------
dic = {'key1':1,'key2':2,'key3':3}
for i in dic:
  print(i)#this prints the keys
  
for i in dic.values():
  print(i)#this prints the values 
  
for i,j in dic.items():
  print(f'{i} : {j}')
  