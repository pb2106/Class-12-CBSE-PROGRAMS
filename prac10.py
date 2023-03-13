#prac10
import pickle
def createbin():
    detail={}
    anss=['y','yes']
    ans=" "
    file=open(r'C:\Prabhav\Project\EmployeeDetails.dat','wb')
    while ans.lower() in anss:
        detail["CompanyID"]=input("Enter your CompanyID: ")
        detail["Company Name"]=input("Enter your company name: ")
        detail["Turnover"]=int(input("Enter your Turnover: "))
        pickle.dump(detail,file)
        ans=input("do you want to continue adding data?: ")
    file.close()
def contents():
    file=open(r'C:\Prabhav\Project\EmployeeDetails.dat','rb')
    print("Contents of EmployeeDetails.dat are: ")
    try:
        while True:
            a=pickle.load(file)
            print(a)
    except EOFError:
        file.close()
def turnover():
    file=open(r'C:\Prabhav\Project\EmployeeDetails.dat','rb')
    turn=int(input("Enter turnover value: "))
    print("Companies with turnover more than",turn,"are:")
    try:
        while True:
            a=pickle.load(file)
            if a["Turnover"]>turn:
                print(a["Company Name"])
    except EOFError:
        file.close()
def searchID():
    file=open(r'C:\Prabhav\Project\EmployeeDetails.dat','rb')
    ID=input("Enter Company ID: ")
    val=True
    try:
        while True:
            a=pickle.load(file)
            if a["CompanyID"]==ID:
                print("Company name of the entered ID is",a["Company Name"])
                break
#if company name not found            
    except EOFError:
        file.close()
anss=['y','yes']
ans="yes"
while ans.lower() in anss:
    choice=input("""Menu:
    a)	To Create a binary file with following structure
        •   CompanyID
        •   Company name 
        •   Turnover 
    b)	To Display the contents of the binary file. 
    c)	To Display the Company whose turnover is above user given value. 
    d)	To Search a Company by Company ID given by user..\nEnter your Choice from the menu as [a/b/c/d]: """)
    if choice=='a':
        createbin()
    elif choice=='b':
         contents()
    elif choice=='c':
        turnover()
    elif choice=='d':
        searchID()
    else:
        print("invalid choice!")
    ans=input("Do you want to try the program again?: ")
