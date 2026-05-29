class Student:
    def __init__(self , name):
        self.name=name

s1= Student("cosmic")
print(s1.name)
# del s1.name deletes s1 and gives error


# OOPS CONT.D

#3.INHERITANCE: When one class(child/derived) derives the properties & methods of another class(parent/base).

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)  #access methods of parent class
        self.name = name
        Car.start()        # ✅ Call static method via class name, not super()

car1 = ToyotaCar("prius", "electric")
print(car1.type)


#Multiple Inheritance example:
class A:
    varA="welcome to class a"

class B:
    varB="welcome to class b"

class C(A , B):
    varC="welcome to class c"

c1=C()
print(c1.varA)
print(c1.varB)

#CLASS METHOD
#A class method is bound to the class & receives the class as an implicit first argument.
#Note - static method can't access or modify class state & generally for utility.
#example:
class person:
    name = "unknown"

    # def changeName(self , name):
          #self.__class__.name = "rahul"     or person.name = name 

    @classmethod
    def changeName(cls , name):
        cls.name = name

p1 = person()
p1.changeName("rahul huh?")
print(p1.name)
print(person.name)

#Property
#We use @property decorator on any method in the class to use the method as a property.
#example

class disciple:
    def __init__(self , phy , chem , math):
        self.phy = phy
        self. chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

disc1 = disciple(84 , 92 , 95)
print(disc1.percentage)
# this @property helped me changing the %age value automatically when marks got changed
disc1.math = 91
print(disc1.percentage) 


# P O L Y M O R P H I S M (operato overlaoding)
#When the same operator is allowed to have different meaning according to the context.
#Operators & Dunder functions ( dunder = double underscore)
# a + b #addition   a .__ add __ (b)
# a - b #subtraction  a .__ sub __ (b)
# a * b #multiplication  a .__ mul ____ (b)
# a / b #division a .__ truediv __ (b)
# a % b #addition a .__ mod __ (b)

class complex:
    def __init__(self , real , img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real , "i+" , self.img , "j")

    def __add__(self, num2): #self = obj1 or num1
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex( newReal, newImg )
    
num3 = complex(3 , 7)
num3.showNumber()

num4 = complex(5 , 9)
num4.showNumber()

num5 = (num3 + num4)
num5.showNumber()


#Q Qs. Define a Circle class to create a circle with radius r using the constructor.
#Define an Area() method of the class which calculates the area of the circle.
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):                                    #def area(self):
        return (22/7) * self.radius **2                         # print((22/7) * self.radius ** 2)  # prints directly, no return needed                      
    
    def perimeter(self):
        return (22/7) * self.radius * 2
    
c1 = circle(20)
print(c1.area())
print(c1.perimeter())


#Q Qs. Define a Employee class with attributes role, department & salary. This class also a showDetails() method.
#Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

class Employee:
    def __init__(self, role , department , salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print( "role: " , self.role )
        print( "department: " , self.department )
        print( "salary: " , self.salary )

class Engineer(Employee):
      def __init__(self, role, department, salary, name, age):
        super().__init__(role, department, salary)  # ✅ pass to Employee
        self.name = name
        self.age = age

# Example
e1 = Engineer("Software Engineer", "IT", 90000, "Rahul", 25)
e1.showdetails()
print(e1.name)
print(e1.age)

#Qs. Create a class called Order which stores item & its price.
#Use Dunder function_gt__() to convey that:
#order1 > order2 if price of order1 > price of order2

class order:
    def __init__(self , item , price):
        self.item = item
        self.price = price

    def __gt__(self , ordr2):
        print(self.price > ordr2.price)

ordr1 = order("chips" , 20)
ordr2 = order("tea" , 15)

ordr1 > ordr2
 #Approach	Why?
#print inside __gt__	Works but value is not reusable
#return inside __gt__	✅ Value can be reused, stored, or checked in if statements {thats whu use mostly this)}
        

        








        
        