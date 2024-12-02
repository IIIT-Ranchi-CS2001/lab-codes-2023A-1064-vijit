a=input("Enter the string: ")
flag=0
for char in a:
    if not char.isalnum():
        print("False")
        flag=0
        break
    else: flag=1
if flag==1:
    print("True")
