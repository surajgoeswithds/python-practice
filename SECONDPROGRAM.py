str1= "Hey this is COSMIC. \nRevising python" # \n= new line , \t = tab space
print(str1)

# CONCAT STRING
str2= "who"
str3= " are you?"
final_str= str2+str3
print(final_str)
print(len(final_str))

str4= "COSMIC HUH?"
ch=str4[3] # to get string character & remember[] bracket
print(ch)

#SLICING 
#-> ENDING IDX NOT INCLUDED
str5="HUH COSMIC?"
print(str5[2:5])
print(str5[3:12])
print(str5[3:len(str5)]) #same output as 19th line (3:12)
#negative index
str6="APPLE"        # A  P  P  L  E
print(str6[-3:-1])  #-5 -4 -3 -2 -1  #here also ending index not included

#STRING FUNCTIONS
str7="COSMIC REVISING PYTHON, HUH?"
print(str7.endswith("uh?"))
# .capitalise = captilises the 1st character
print(str7.replace("O" , "X"))
print(str7.find("M"))
print(str7.count("L"))

#Q> WAP input users first name and print its length
name=input("enter your name=   ")
print(len(name))

#CONDITIONAL STATEMENTS
age=19
if(age>=19): #if age is less than 19 then can drive/vote will not be printed
    print("can drive")
    print("can vote")

light="green"    
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("wait")
#ELIF=else if
#ELIF & IF DIFF THROUGH AN EXAMPLE 
num=5
if(num>2):
    print(">2")
elif(num>3):
    print(">3") #if is 1st prior then elif alway IF used first

light="pink"    
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("wait")
else:
    print('light is broken')    
#Example:
marks=66
if (marks>=90):
    print("A")
elif(marks<90 and marks>=80):
    print("B")
elif(marks<80 and marks>=70)   :
    print("C") 
else:
    print("student should improve")
#Nesting(if ke andar if)
age=95
if(age>=18):
    if(age>=80):
        print("cannnot drive")    
    else:
        print("can drive")
else:
    print("cannot drive")

#QUESTIONS
# Q1> WAP to check if a number entered by user is odd or even 
num1=int(input("number= "))   
if (num1%2==0):
    print("number is even")
else:
    print("number is odd")

#Q2> WAP to find the greatest of 3 numbers entered by the user
num2=int(input("number2=  "))
num3=int(input("number3=  "))
num4=int(input("number4=  "))
if(num2>=num3 and num2>=num4):
    print("first number is largest" , num2)
elif(num3>=num4 and num3>=num2):
    print("second number is largest" , num3)
else:
    print("third number is largest", num4)      
  
#Q> WAP to check if a number is multiple of 7 or not
num7=int(input("enter you number=  "))
if(num7%7==0):
    print("NUMBER IS DIVISIBLE BY 7!")
else:
    print("NUMBER IS NOT DIVISIBLE BY 7")

