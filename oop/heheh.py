#to define a class

class className: 
  pass #we use the pass just to check if the class is created well 

className #this is how we call the class ?

class Person:
  age = 20
  def ageAfter10(self): #self is kinda like how "this" works
   #self is not syntax tho
   return self.age+10

Person.age

#to change the age
Person.age = 30


obj = Person()
obj.ageAfter10() # we do this to access the function insde the class
#but we dont need to create an obj to change an attriute inside the calss
#but to call a method from the class then 

obj.age = 90 #this changes the age for this object alone
Person.age = 90 #this would change the defalut value for any new object that will be created
#does not change the values of the older variables 

class Person1:
  "this class for personal information"
  age = 20
  def ageAfter10(self): #self is kinda like how "this" works
   #self is not syntax tho
   return self.age+10
 
print(Person1.__doc__) #this would print the line added "this class for personl information"
#used as a discription for the class


#protected public and private

#to create a construcotr in the class

class Person:
  def __init__(self,age): #can add default value for age by simplay saying age=10
    self.age = age #if thers no default value and we didnt send one it will give an error
  def ageAfter10(self):
    return self.age+10

obj = Person(30)
print(obj.age)

#ACCESS MODIFIERS
#by default the attributes are public 
#public attribute: 
class Person:
  def __init__(self,age):
    self.age =age
  def ageAfter10(self):
    return self.age+10
  #Accessing adn changing its value
  obj = Person(10)
  print(obj.age)
  obj.age= 20
  print(obj.age)
  
  
#private attribute
class Person:
  def __init__(self,age):
    self.__age = 10
  def getAge(self):
    return self.__age
  def setAge(self,value):
    if value > 1:
      self.__age += value
    
#accessing and changin tis value
obj = Person(10)
obj.setAge(3)
print(obj.getAge())

#private cannot be accessed out side the class unless with a getter


#INHERIT FROM OTHER CLASSES
class Person:
  def __init__(self, age = 10):
    self.age = age
  def ageAfter10(self):
    return self.age+10
  
class students(Person):
  def __init__(self, age, name):
    super().__init__(age) #super makes it inhert everything instead of just
    self.name = name
  def studentsInfo(self):
    print(self.name)
    print(self.age)

obj = students(19, 'sara')
obj.studentsInfo()
#eihter all the attributes for the class have default values or non do
#bc other wise it will 