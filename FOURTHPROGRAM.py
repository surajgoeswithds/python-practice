#DICTIONARY
info= {
    "key" : "value" ,
    "name": "COSMIC" ,
    "learning" : ["coding" , "set" , "dict"],
    "age": 35,
    "is_adult":True
}
print(info)
print(type(info))
print(info["key"]) # wanna print any specific
info["name"]="COSMIC HUH"
info['surname']="revising?" 
print(info)

# NESTED DICTIONARY
#ex>
student={"name": "cosmic",
    "marks": {
        "PHY":92,    
        "CHEM":78,
        "MATH":90}
}
print(student["marks"]["CHEM"])
print(student.keys())
print(tuple(student.keys())) #just to remove disct_keys in terminal we r using list/tuple
print(list(student.values())) #O/P = IDX VALUES
print(list(student.items())) #O/P= (IDX, VALUES {BOTH})
print(student.get("name"))
print(student["name"]) #same as .get(name) but if we put name2 which is not there then it will give ERROR but .get(name) will give O/P-> NONE
student.update({"city" : "DELHI?"}) #inserts new value
print(student)

# SETS   
collection={1 , 2,2 ,4 , 5, 6, 6 , 6, "hello" , "cosmic"} #duplicate value gets ignored in SETS
print(collection)
print(type(collection))
print(len(collection)) #here also dupes ignored
#SETS --> MUTABLE
#SETS-->elements-->IMMUTABLE
collection.add(99) #adds element inside set 
print(collection)
collection.remove(2) #removes element from set
print(collection) 
collection.pop() #removes random value
print(collection)
collection.clear() #empties the set
print(collection)
#UNION & INTERSECTION OF SETS
set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(set1.union(set2))
print(set1.intersection(set2))

#Q> Store following word meanings in a python dictionary :
#table : "a piece of furniture", "list of facts & figures"
#cat : "a small animal"
word_dict={"table": ["a piece of furniture" , 
           "lists of facts and figures"],
           "cat" : "a small animal"
}
print(word_dict)

#Q>You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
"python", "java", "C++", "python", "javascript",
"java", "python", "java", "C++", "C"

subject={"python", "java", "C++", "python", "javascript",
"java", "python", "java", "C++", "C"}
print(len(subject)) #->no of classrooms needed

#Q>WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={}
key1=int(input("marks1: "))
marks.update({"phy": key1})
key2=int(input("marks2: "))
marks.update({"math" : key2})
key3=int(input("marks3: "))
marks.update({"chem":key3})
print(marks)

#Q> Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types)
values={9, "9.0"}
print(values)