#FILE I/O IN PYTHON
#Python can be used to perform operations on a file. (read & write data)
#Types of all files
#1. Text Files : .txt, .docx, .log etc.
#2. Binary Files : .mp4, .mov, .png, .jpeg etc.

#Open, read & close File
#We have to open a file before reading or writing.

# f = open("file_name" ,  "mode")
#            |              |  
#            V              V
#       sample.txt      r : read mode
#       demo.docx       w : write mode   

# data = f.read()
# f.close()

f = open("demo.txt" , "w")
#data = f.read()
#print(data)
#print(type(data))

#line1 = f.readline()  # we put # above cuz once file read means reach we can get any other output for learing purspose
#print(line1)


#line2 = f.readline()  
#print(line2)


f.write("what to do huh?")
f.close()

#Character Meaning
#'r' ----> open for reading (default)
#'w' ----> open for writing, truncating the file first
#'x' ----> create a new file and open it for writing
#'a' ----> open for writing, appending to the end of the file if it exists
#'b' ----> binary mode
#'t' ----> text mode (default)
#'+' ----> open a disk file for updating (reading and writing)
# r+ ---> does overwrite on something like id 'this' and we overwrite abc then it will be 'abcs' "thi" gets overwritten [read + overwrite and pointer is on starting position and no truncate]
# w+ -----> read + overwrite and truncates file
# a+ -----> read + append ( pointer at end ) no truncate


# WITH syntax
#with open( "demo.txt", "a") as f:
#data = f.read( )

with open ("random.txt" , "r" ) as f:
    data1=f.read()
    print(data1)

with open("random.txt" , "w") as f:
    data2=f.write("new data?")

#Deleting a File
#using the os module
#Module (like a code library) is a file written by another programmer that generally has a functions we can use.
#import os
#os.remove(filename)

#Q>Create a new file "practice.txt" using python. Add the following data in it:
#Hi everyone
#we are learning File I/O
#using Java.
#I like programming in Java.

with open("practice.txt" , "w")as f:
    f.write("Hi everyone\n we are learning File I/O\n using Java.\n I like programming in Java.")

#Q>WAF that replaces all occurrences of "Java” with “python” in above file.
with open("practice.txt" , "r")as f:
    data3=f.read()

new_data=data3.replace('Java' , "Python")
print(new_data)

#Q> WAF to find in which line of the file does the word "learning"occur first. Print -1 if word not found.
def check_for_line():
    word = "learning"
    line_no = 1

    with open("practice.txt", "r") as f:
        for line in f:           # ✅ Loop through ALL lines
            if word in line:     # ✅ Check each line
                print(line_no)
                return           # ✅ Stop once found
            line_no += 1         # ✅ Properly increment counter

    print(-1)                    # ✅ Print -1 if word never found

check_for_line()


#Q>Search if the word "learning" exists in the file or not.
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(word in data):
        print("Found")
    else:
        print("not found")

#Q>From a file containing numbers separated by comma, print the count of even numbers.
count=0
with open("num.txt" , "r") as f:
    data4=f.read()
    print(data4)

    nums= data4.split(",")
    for val in nums:
        if(int(val)%2==0):
            count += 1

print(count)
        




    











