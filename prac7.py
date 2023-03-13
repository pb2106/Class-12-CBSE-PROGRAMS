#prac6
def CreateTextFile( ) :
    file1=open(r"C:\Prabhav\Project\content.txt",'w')
    for i in range(3):
        text=input("Enter Text to write into the file: ")
        file1.write(text+'\n')
    file1.close()
def CountAll() :
    file1=open(r"C:\Prabhav\Project\content.txt",'r')
    wordcount=0
    allcontent=file1.readlines()
    words=[]
    vowels=['a','e','i','o','u']
    con=dig=space=0
    for i in range(len(allcontent)):
        allcontent[i]=allcontent[i].strip('\n')
        wordcount+=len(allcontent[i].split())
        for j in range(len(allcontent[i])):
            if allcontent[i][j].lower() not in vowels and allcontent[i][j].isalpha():
                con+=1
            elif allcontent[i][j].strip().isdigit():
                dig+=1
            elif allcontent[i][j]==' ':
                space+=1
    print("Total number of lines in content.txt is",len(allcontent))
    print("Total number of words in content.txt is",wordcount)
    print("Total number of consonants in content.txt is",con)
    print("Total number of digits in content.txt is",dig)
    print("Total number of spaces in content.txt is",space)
    file1.close()
def ReplaceSpace():
    file1=open(r"C:\Prabhav\Project\wspace.txt",'w')
    file2=open(r"C:\Prabhav\Project\content.txt",'r')
    for i in file2:
        file1.write(i.replace(" ","#"))
    file1.close()
    file2.close()
def numvow():
    file1=open(r"C:\Prabhav\Project\content.txt",'r')
    print("contents of content.txt:")
    for i in file1:
        print(i,end='')
    print()
    file1.close()
    file2=open(r"C:\Prabhav\Project\wspace.txt",'r')
    print("contents of wspace.txt:")
    for i in file2:
        print(i,end='')
    file2.close()
anss=['n','no']
ans=""
while ans.lower() not in anss:
    print("""Menu:
a) CreateTextFile() - To create a text file "content.txt" with several lines of text 
b) CountAll() - To count number of lines, consonants, digits, spaces & words 
c) ReplaceSpace() - To create another file called "wspace.txt" using the original which will contain the text after replacing all the blank spaces with '#'. 
d) To Read & display the contents of both the files.""")
    choice=input("Enter your choice from the above menu as [a/b/c/d]: ")
    if choice=='a':
        CreateTextFile() 
    elif choice=='b':
        CountAll()
    elif choice=='c':
        ReplaceSpace()
    elif choice=='d':
        numvow()
    else:
        print("invalid choice!")
    ans=input("Do you want to continue?: ")
