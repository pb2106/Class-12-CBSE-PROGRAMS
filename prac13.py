#prac12
import csv
def creation():
    with open(r'C:\Prabhav\Project\emp.csv','w',newline='') as file:
        write=csv.writer(file)
        anss=['y','yes']
        ans="yes"
        a=["EmpID","EmpName","Salary","Department"]
        write.writerow(a)
        while ans.lower() in anss:
            details=[]
            details.append(input("Enter Your EmpID: "))
            details.append(input("Enter Your Name: "))
            details.append(int(input("Enter your salary: ")))
            details.append(input("Enter your department: "))
            write.writerow(details)
            ans=input("Do you want to Enter more entries ??: ")
def search():
    with open(r'C:\Prabhav\Project\emp.csv','r') as file:
        read=csv.reader(file)
        s=input("Enter EmpID to search: ")
        for r in read:
            if s in r:
                print("Record found!:\n",r)
                break
        else:
            print("Record not found!")
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
        search()
    else:
        print("invalid choice!")
    ans=input("Do you want to try the program again?: ")
