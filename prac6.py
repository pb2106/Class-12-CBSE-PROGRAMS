#prac6
def CreateTextFile( ) :
    file1=open(r"C:\Prabhav\Project\data.txt",'w')
    for i in range(3):
        text=input("Enter Text to write into the file: ")
        file1.write(text+'\n')
    file1.close()
def CopyVowelWord( ) :
    file1=open(r"C:\Prabhav\Project\data.txt",'r')
    file2=open(r"C:\Prabhav\Project\vowel.txt",'w')
    vow=['a','e','i','o','u']
    words=[]
    vowwords=[]
    for i in file1:
        words.append(i.split())
    for i in range(len(words)):
        for j in words[i]:
            for k in vow:
                if k in j:
                    file2.write(j+'\n')   
                    break
    file1.close()
    file2.close()
def contents():
    file1=open(r"C:\Prabhav\Project\data.txt",'r')
    print("contents of data.txt:")
    for i in file1:
        print(i,end='')
    print()
    file1.close()
    file2=open(r"C:\Prabhav\Project\vowel.txt",'r')
    print("contents of vowel.txt:")
    for i in file2:
        print(i,end='')
    file2.close()
def numvow():
    file2=open(r"C:\Prabhav\Project\vowel.txt",'r')
    print("There are",len(file2.readlines()),"words with vowels")
    file2.close()
anss=['y','yes']
ans="yes"
while ans.lower() in anss:
    choice=input("""Menu:
a) To CreateTextFile() - create a text file "data.txt" with several lines of text 
b) To CopyVowelWord() - create another text file "vowel.txt" which will store all the words starting with vowel from "data.txt". 
c) To Read & display the contents of both the files. 
d) To Display the total number of words starting with vowel.\nEnter your choice from the above menu as [a/b/c/d]: """)
    if choice=='a':
        CreateTextFile( ) 
    elif choice=='b':
        CopyVowelWord( )
    elif choice=='c':
        contents()
    elif choice=='d':
        numvow()
    else:
        print("invalid choice!")
    ans=input("Do you want to continue?: ")
