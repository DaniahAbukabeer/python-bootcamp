print('hello world!') 
x=5
print(x)
print(type(x)) #this prints the data type of the varialbe x
#in python u dont have to give the variable a datatype, just give it initial value and 
#the compiler would know what datatype to use!
myVar = input()
#use input() to take values form the user! and it doesnt matter what the user enteres it will be string!
Varx = input('please enter your name: ')
print(type(Varx))
#this will print that line and then take value form the user and store it in Varx
print("your name is ",Varx," and thats how we concatentat")
print("3+3=",3+3)
myNum= 6*7
#to cast the user input from string to other data types to use numeric operations on them
inputN1 = input("please enter the first number")
inputN2 = input("please enter the second number")

inputN1 = int(inputN1)
inputN2 = int(inputN2)

print(inputN1 + inputN2)