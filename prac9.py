#prac9
import pickle
def createbin():
    file=open(r"C:\Prabhav\Project\STUDENT.dat","wb")
    studetail={}
    anss=['y','yes']
    ans="yes"
    while ans.lower() in anss:
        studetail["Admission_number"]=int(input("Enter Admission_number: "))
        studetail["Student Name"]=input("Enter Student Name: ")
        studetail["Percentage"]=input("Enter Percentage: ")
        pickle.dump(studetail,file)
        ans=input("Do you want to continue adding data?")
    file.close()
def countrec():
    file=open(r"C:\Prabhav\Project\STUDENT.dat","rb")
    a=" "
    count=0
    try:
        print("Students who scored above 75 percent are: ")
        while True:
            a=pickle.load(file)
            if a["Percentage"]>"75":
                count+=1
                print(a)
    except EOFError:
        file.close()
    print(count," students got above 75")
anss=['y','yes']
ans="yes"
while ans.lower() in anss:
    choice=input("""Menu:
    a)	Create a binary file “STUDENT.DAT” with following structure:
        •   Admission_number
        •   Student Name 
        •   Percentage
    b)	Write a function countrec( ) in Python that would read contents of the file “STUDENT.DAT” and display the details of those students whose percentage is above 75. Also display number of students scoring above 75%..\nEnter your Choice from the menu as [a/b]: """)
    if choice=='a':
        createbin()
    elif choice=='b':
         countrec()   
    else:
        print("invalid choice!")
    ans=input("Do you want to try the program again?: ")
