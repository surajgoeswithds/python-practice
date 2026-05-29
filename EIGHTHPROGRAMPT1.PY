# OOPS PYHTON #real world scenarios
#Class & Object in Python
#Class is a blueprint for creating objects.

#creating class
class Car23:
    brand= "Aston Martin"
    colour= "blue"


#creating object (instance)
car1=Car23()
print(car1.colour)
print(car1.brand)

#another example

class Student:
    name = "karan kumar"
    def __init__(self): #*The self parameter is a OBJECT REFERENCE to the current instance of the class, and is used to access variables that belongs to the class.
        print("adding new student in database....")
s1 = Student()
print( s1.name )
print(s1)

# __init__ FUNCTION
#Basic Constructor
#All classes have a function called __init__(), which is always executed when the objec is being initiated.

class Student:
    college_name = "XYZ College"
    name = "anonymous" # anonymous wont be printed as obj attribute > class attribute
    def __init__(self,fullname,marks):
        self.name=fullname #obj attribute
        self.marks=marks
        print("adding new student in database....")

    def welcome(self):
        print("welcome student , " , self.name )

    def get_marks(self):
        return self.marks

s1 = Student ("COSMIC" ,89 )
print(s1.name , s1.marks)
s1.welcome()
print (s1.get_marks())

s2 = Student ("LUFFY" ,91 )
print(s2.name , s2.marks)

print(Student.college_name) #in place of student we can also write s1 , s2 then also same output


#Q> Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.

class student1:
    def __init__(self , name , marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("hi" , self.name , "ur avg is:  " , sum/3)


s1= student1("ZORO" , [79 , 97, 50])
s1.get_avg()

s1.name="ROBIN" 
s1.get_avg()

#Static Methods
#Methods that don't use the self parameter (work at class level)
class Student:
    @staticmethod      #decorator       Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
    def college():
        print( "ABC College" ) 

#example:
class UserAccount:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def is_strong_password(password):
        """
        Check if a password is strong.
        Needs NO info about the user — purely checks the password string itself.
        """
        if len(password) < 8:
            return False, "Too short! Must be at least 8 characters."
        if not any(char.isdigit() for char in password):
            return False, "Must contain at least one number."
        if not any(char.isupper() for char in password):
            return False, "Must contain at least one uppercase letter."
        return True, "Strong password! ✅"


# ─── Check password BEFORE creating any account ───────────
valid, message = UserAccount.is_strong_password("hello")
print(message)    # Output: Too short! Must be at least 8 characters.

valid, message = UserAccount.is_strong_password("Hello123")
print(message)    # Output: Strong password! ✅

# ─── Now create the account only if password is strong ─────
if valid:
    acc = UserAccount("alice", "Hello123")
    print(f"Account created for: {acc.username}")

#Why @staticmethod here?
#The password checker doesn't care about:
#Who the user is
#What the username is
#Any class-level data
#It just looks at the password string and makes a decision. Pure, isolated, clean. ✅

# 4 MAJOT PILARS OF OOPs:

#1. ABSTRACTION: Hiding the implementation details of a class and only showing the essential features to the user.
#EXAMPLE:
class car:

    def __init__(self):
        self.accl=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.accl=True
        self.clutch=True
        print("car started......")

car2=car()
car2.start()

#2. Encapsulation: Wrapping data and functions into a single unit (object).

#Q>Create Account class with 2 attributes - balance & account no. . Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self , bal , acc):
        self.balance=bal
        self.account_no=acc

    def debit(self , amount):
        self.balance -= amount
        print("rs." , amount , "was debited from ur account")
        print("total balance=  " , self.get_balance())

    def creidt(self , amount):
        self.balance += amount
        print("rs." , amount , "was credited to ur account")
        print("total balance=  " , self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1= Account( 10000 , 12345 )
print(acc1.balance)
print(acc1.account_no)
acc1.debit(5420)
acc1.creidt(1420)

    

        

    



        
