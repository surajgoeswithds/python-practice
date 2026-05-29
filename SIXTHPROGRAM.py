# FUNCTIONS IN PYTHON 
# def= FUNCTION DEFINITION
def calc_sum ( a , b): # a & b are PARAMETERS 
    sum = a + b 
    print (sum)
    return sum

calc_sum( 5 , 10)
calc_sum( 2 ,5 )
calc_sum( 9 , 72 ) # we can call like this without repeating same code like sum ( x + y )
# Once we use DEF for something our repeating repeating same code will decrease

def calcn_sum( m , n): #m & n are parameter
    return m + n

sum1= calcn_sum( 4, 47 ) # function call;  4 & 47 are arguments which get stored in m & n
print(sum1)

# ANOTHEr EXAMPLE 
def print_hello():
    print( "hello" )
print_hello()
print_hello()
print_hello() #function call , now as many time we call print_hello() func^n that many times it will be automatically printed

# CREATE A FUNCTION WHICH CALC. AVG OF 3 NUMBERS!
def avg_num ( x , y , z):
    avg = (x+y+z)/3
    print(avg)
    return avg

avg_num(2 , 4 , 6)

#Functions in Python-> 
# ==>BUILT IN -> PRINT(), LEN() , TYPE() , RANGE()
# ==>USER DEFINED -> NOT BUILTIN

def calc_prod( a=3 , s=4 ): # if here a = something , s = something then the something would be called as default parameter , & if 1 element as default parameter then it will written neear last bracket like if a had only value then then ( s , a = 7)
    print ( a * s)
    return ( a * s)

calc_prod()

# Q> WAF to print the length of a list. (list is the parameter)
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


#Q>WAF to find the factorial of n. (n is the parameter)
def fact(n):
    fact=1
    for i in range(1 , n+1):
        fact = fact * i  #fact*= i same as that
    print(fact)

fact(5)

#Q> WAF to convert USD to INR.
def conv(x):
    conv = x * 90
    print(conv)
    return conv
conv(7)  #my attempt

def converter(usd_val):
    inr_val = usd_val * 83
    print( usd_val , "USD =", inr_val , "INR")
converter (73) #AC attempt


#Q> WAF which return ODD/EVEN value when we input a value usinf def
def oddeven(int_input):
    if (int_input%2==0):
        print("EVEN")
    else:
        print("ODD")
oddeven(46)

#Q> WAF to print the elements of a list in a single line. ( list is the parameter)
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]

def print_list(list):
    for item in list:
        print(item , end=" " ) #if we put end="/n" then each element would have been in a new line

print_list(cities)

#RECURSIONS 
# WHEN FUNCTION CALLS ITSELF REPEATEDLY
#Every recursive call says just one simple thing:
#"I don't know the full answer — but I know my answer is the result from below + my own value."


# reverses the no.
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(6)    

#returns n!
def fact(n):
    if ( n == 1 or n == 0):
        return 1
    else:
        return n * fact(n - 1) # as we know n!=(n-1)! * n like 5! = 4! x 5
    
print(fact(4))


#Q>Write a recursive function to calculate the sum of first n natural numbers.
def calc_summ(n):
    if (n == 0):
        return 0
    else:
        return calc_summ(n-1) + n
    
sum = calc_summ(7)
print(sum)
    
#OR

def calc_sumn(n):
    if n == 0:
        return 0
    return calc_sumn(n-1) + n  # ask below, then add MY own n

print(calc_sumn(4))

#Q> Write a recursive function to print all elements in a list.
#Hint : use list & index as parameters.

def print_list( list , index=0):
    if index == len(list):
        return
    print(list[index])
    print_list( list , index+1)

fruits = ["mango", "litchi", "apple", "banana"]
print_list(fruits)


