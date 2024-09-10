s=input("Enter a string: ")
char=input("Enter the character to be searched: ")
count=0
for c in s:
    if c==char:
        count+=1
print("No of occurences: ",count) 
