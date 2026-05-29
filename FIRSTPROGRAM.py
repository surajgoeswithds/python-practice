name="cosmic"
age=18
price=26.99

print("age")
print(age)

print("my name is: " , name )
print("my age is: ", age)

age2 = age
print(age2)

print(type(name))
print(type(age2))
print(type(price))

age=23
old=False
a=None
print(type(age))
print(type(old))
print(type(a))

#arithmetic operators
w=100
e=300
diff = e-w #maybe sum + , multi* , divide /
print(diff)

r=5
t=2
print(r % t) # % = remainder
print(r ** t) #power

#RELATIONAL OPERATORS
a=10
b=20
print ( a == b ) #normal =
print(a!=b) # not equal to !=
print(a>=b)
print(a<=b)

# ASSIGNMENT OPERATORS
num = 20 
num = num + 10 # if 2nd step
num += 10 # works same as 2nd step ( we can use - , * , / , **[power func^n])
print(num)
print("num : " , num)

#LOGICAL OPERATORS
print(not True)
print(not False)
#example mentioned:
x=15
y=12
print(not (x>y)) # basically NOT gives the opposite answers of a question
val1=True
val2=False
print("AND operator : ", val1 and val2) #EVEN IF ONE VALUE GETS FALSE 'AND' OPERATOR WILL ALWAYS RETURN "FALSE" OUTPUT

print("OR operator : ", val1 or val2) #EVEN IF ONE VALUE GETS TRUE 'OR' OPERATOR WILL ALWAYS RETURN "TRUE" OUTPUT
#for example 
print( "OR operator: ", x==y or x>y)

name=input("my name is: ") # after "my name is" there will be ____ in terminal to fill
val=input("enter some value: ")
print(type(val) , val) #EVERY VALUE GETS CONVERTED TO STRING AUTOMATICALLY SO WE HAVE TO TYPECAST AND EDIT IT LIKE EXAMPLE GIVEN BELOW
#for example
val1=float(input("enter some value: ")) # SIMILARILY IN PLACE OF FLOAT WE CAN PUT INT, BOOL ETC.......
print(type(val1) , (val1))
#EXAMPLE
name=input("enter name: ")
age=input("enter age: ")
marks=input("enter marks: ")

print("hi" , name)
print("age = ",age)
print(marks)

# Q> WAP input 2 numbers and print sum
num1=int(input("num1: "))
num2=int(input("num2: "))
print("sum= " , num1+num2)

#Q> WAP input side of a square
side=float(input("enter value of side = "))
print("side=" , side**2)

#Q> WAP input 2 no.s print true if a>=b. if not then false
number1=int(input("number1:"))
number2=int(input("number2: "))
print(number1>=number2)