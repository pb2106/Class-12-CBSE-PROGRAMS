#prac12
import csv
import math
def creation():
    with open(r'C:\Prabhav\Project\student.csv','w',newline='') as file:
        write=csv.writer(file)
        anss=['y','yes']
        ans="yes"
        write.writerow(["Roll no","Name of student","Mark in Sub1","Mark in sub2","Mark in sub3","Mark in sub4","Mark in sub5"])
        while ans.lower() in anss:
            details=[]
            details.append(input("Enter Your Roll number: "))
            details.append(input("Enter Your Name: "))
            for i in range(5):
                print("Enter marks of subject",i+1,"out of 100",end=": ")
                details.append(int(input()))
            write.writerow(details)
            ans=input("Do you want to Enter more entries ??: ")
def percent():
    with open(r'C:\Prabhav\Project\student.csv','r') as file:
        read=csv.reader(file)
        j=0
        for r in read:
            per=0
            if j>0:
                for i in r:
                    if r.index(i)>0 and i.isdigit():
                        per=per+int(i)
                print("For",r[1],"Total is",per," and Percentage is",round((per/500)*100),"%")
            j+=1
def above80():
    with open(r'C:\Prabhav\Project\student.csv','r') as file:
        read=csv.reader(file)
        j=0
        for r in read:
            if j>0:
                for i in r:
                    if r.index(i)>0 and i.isdigit() and int(i)>80:
                        print(r[1],"got above 80")
                        break
            j+=1
anss=['y','yes']
ans="yes"
while ans.lower() in anss:
    choice=input("""Menu:
    a)	To Define a function to write the following data into a CSV file  
        •   Roll no 
        •   Name of student 
        •   Mark in Sub1 
        •   Mark in sub2 
        •   Mark in sub3 
        •   Mark in sub4 
        •   Mark in sub5 

    b)	To Define a function to read the CSV file and calculate total and percentage for each student. 
    c)	To Define a function to display the name of student if in any subject marks are greater than 80% (Assume marks are out of 100).\nEnter your Choice from the menu as [a/b/c]: """)
    if choice=='a':
        creation()
    elif choice=='b':
         percent()
    elif choice=='c':
        above80()
    else:
        print("invalid choice!")
    ans=input("Do you want to try the program again?: ")
