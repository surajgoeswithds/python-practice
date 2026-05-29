#LOOPS
count = 1
while count<=3:
    print("hello")
    count+=1

i=1 #iteration used in loops
while i <=7:  #just change number how many time u wanna print
    print("cosmic",i)
    i+=1

#Print numbers from 1 to 5
i=1
while i <= 5:
    print(i)
    i+=1

#Print numbers from 5 to 1
i=5
while i>=1:
    print(i)
    i-=1

#Print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

#Print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

#Q> Print the elements of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
nums=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx=0
while idx<len(nums):
    print(nums[idx]) #nums[0] , nums[1], nums[2]
    idx+=1
#SIMILARILY 
heroes=["batman" , "luffy" , "spiderman"]
i=0
while i < len(heroes):
    print(heroes[i])
    i+=1


# Q>Search for a number x in this tuple using loop:
(1, 4, 9, 16, 25, 36, 49, 64, 81,100, 49)
nums1=(1, 4, 9, 16, 25, 36, 49, 64, 81,100 , 49)
x=49
i=1
while(i<len(nums1)):
    if(nums1[i]==x):
        print("number found" , i)
        break
    else:
        print("finding.....") #optional extra point added hehe
    i+=1
print("end of loop")

# KEYWORDS OF LOOP
i=1
while i <= 5:
    print(i)
    if (i==3):
        break #breaks the loop when used witH IF condition!
    i+=1

print("end of the loop")


i=1
while i<=5:
    if(i==3):
     i+=1
     continue #continue helps in skipping with IF condition
    print(i)
    i+=1
#example of continue 
# if we want to skip even value in b/w 10
i = 1
while i <= 10:
    if(i%2==0): #if != used after 2 then even value will be returned as that sign represent not equal to
     i+=1
     continue #continue helps in skipping with IF condition
    print(i)
    i+=1   


#Q> Print the multiplication table of a number n.

n=int(input("enter ur number:  "))
i=1
while i<=10:
    print(n*i)
    i+=1


# FOR LOOPS -> USED FOR SEQUENTIAL TRAVERSAL
 #for loops
nums = [ 1 , 2, 3 , 4 ,5 ]
for val in nums: #arranges values without index sequencing
    print(val) 

veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]
for val in veggies:
    print(val)

tup = (1, 2, 3, 4, 2, 8, 9)
for num in tup:
    print(num)
    
#Q> using for
#Print the elements of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
numb1=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for val in numb1:
    print(val)

#Q>Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100,49]
numb2=[1, 4, 9, 16, 25, 36, 49, 64, 81,100,49]
x=49

idx=0
for val in numb2:
    if (val==x):
        print("number found at idx" , idx) # if we put break after that then only idx 6 would have shown
    idx+=1


#RANGE()-> RETURNS A SEQUENCE OF NUMBER , STARTING FROM 0 BY DEFAULT & INCREMENTS BY 1 BY DEFAULT & STOPS BEFORE A SPECIFIED NUMBER!
for i in range(10):
    print(i) #can be wrriteen 1st seq=range(10) then for i in seq

for i in range(2,10,2): #(start, stop , step)
    print(i)

#Q> PRINT NO.S FROM 1 TO 100
for i in range(101):
    print(i)
#Q> PRINT NO.S FROM 100 TO 1
for i in range(100, 0 , -1):
    print(i)

#Q> Print the multiplication table of a number n.
n = int(input("enter ur number:   " ))
for i in range(1 , 11):
    print(n * i)

#PASS-> USED AS PLACEHOLDER FOR DIFFERENT WORK 
for i in range(5):
    pass #for now not printed maybe used in future

print("some useful work")

#Q> WAP to find the sum of first n numbers. (using while) 
n=5
sum=0
i=1
while i <= n:
    sum += i
    i += 1
print("total sum:  " , sum)

#OR (USING IF)

n=5
sum=0
for i in range( 1 , n+1 ):
    sum+=i
print("total sum: " , sum )

#Q>WAP to find the factorial of first n numbers. (using for)

n=6 
fact = 1
for i in range( 1 , n+1 ):
    fact *= i
print( "factorial of n :  " , fact)

#OR(USING WHILE)

n=6
fact=1
i=1
while i <= n:
    fact *=i
    i += 1
print("factorial: " , fact)

