#to count the occurrence of character in string

string=input("Enter a word")
char=input("Enter char to search in string")

i=0
count=0

while(i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1

print("The {0} appears {1} times in {2}".format(char,count,string))