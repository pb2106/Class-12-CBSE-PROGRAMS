#prac5
with open(r"C:\Prabhav\Project\project try.txt",'r') as file:
    def lines():
        for i in file:
            print(i.replace(" ","😊").strip('\n'))
    def rm():
        for i in file:
            if 'a' in list(i):
                newfile=open(r"C:\Prabhav\Project\newfile.txt",'a')
                newfile.write(i)
    anss=['y','yes']
    ans="yes"
    while ans.lower() in anss:
        print("""Menu:
        a)To read and display the text file content line by line with each word separated by “😊”.
        b)To remove all the lines that contain the character ‘a’ in a file and write it to another file.""")
        choice=input("Enter your choice from the above menu as [a/b]: ")
        if choice=='a':
            lines()
        elif choice=='b':
            rm()
        else:
            print("invalid choice!")
        ans=input("Do you want to continue?: ")
