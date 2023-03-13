#prac8
with open(r"C:\Prabhav\Project\STORY.txt","r") as file:
    def DISPLAYWORD():
        content=file.readlines()
        print("Words with less than 4 characters are:")
        for i in content:
            for j in range(len(i.split())):
                if len(i.split()[j])<4:
                    print(i.split()[j])
    def SEARCHWORD():
        search=input("Enter word to search in the text file: ")
        count=0
        string=file.read()
        print(search,"has occured",string.count(search),"times.")
    anss=['y','yes']
    ans="yes"
    while ans.lower() in anss:
        choice=input("""Menu:
        a) DISPLAYWORDS( ) to read lines from text file STORY.TXT , and display those words , which are less than 4 characters.
        b)SEARCHWORD() to search a word and its frequency in a text file.\nEnter your Choice from the menu as [a/b]: """)
        if choice=='a':
            DISPLAYWORD()
        elif choice=='b':
            SEARCHWORD()
        else:
            print("invalid choice!")
        ans=input("Do you want to continue?: ")
