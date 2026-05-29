marks=[94.4 , 95, 83 , 87.5 , 92]
print(marks)
print(type(marks))
print(marks[0]) #indexing of list
print(len(marks)) #length of the list
#STRINGS ARE IMMUTABLE AND LISTS ARE MUTABLE IN PYTHON, FOR EXAMPLE:
student=["KARAN" , 96 , 19 , 'MUMBAI']
print(student[0])
student[0]="ARJUN"
print(student) #POSSIBLE
#but in string: #NOT POSSIBLE

print(marks[1:4]) #slicing in list

#LIST METHODS:
list= [ 122 , 233.4 , 423.54 , 322 , 980.76 ]
list.append(932) #ADDS 1 ELEMENT AT THE END
print(list)

list.sort #sorts in asc order
print(list)

list.sort(reverse=True) #sorts in desc order
print(list)

list.reverse
print(list)

list.insert(1 , 699.9) #(idx , element)
print(list)

list.pop(1)
print(list) # removes element acc to idx mention in () better than .remove imo

list.remove
print(list) #removes first occurence of element

#TUPLE
#tuple is () of list only diff is tupple is immutable
tup=( 98 , 76 , 67 , 94 , 23)
#tup(any func^n,)==tuple if after function no "," is the it may be considered accordingly like float , int ,string etc....
print(tup)
print(type(tup)) 
#slicing same as list and all
#tuple meths

print(tup.index(94)) #gives the index of the element
print(tup.count(67)) #return the count number of occurences of elements

#Q> WAP to ask the user to enter names of their 3 favourite movies and store them in a list
movies=[]
mov1=input("fav movie1=  ")
mov2=input("fav movie2:  ")
mov3=input("fav movie3:  ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#Q> WAP to check if a list contains a palindrome of elements. (Hint: use copy() method) {palindrome means both side same spelling of a word}
list1=[ "m", "a", "a", "m", ]
copy_list1= list1.copy() #.copy -> return a shallow copy of the list
copy_list1.reverse()
if(copy_list1==list1):
    print("PALINDROME!!")
else:
    print("NOT PALINDROME!")    

# ex:
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)

