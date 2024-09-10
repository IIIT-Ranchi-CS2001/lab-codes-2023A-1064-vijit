n=int(input("Enter the number of terms for Fibonacci sequence: "))
a,b=0,1
if(n<=1):
    print("0")
else:
    print("0 1", end=" ")
    i=0
    while(i<n-2):
        sum=a+b
        a=b
        b=sum
        print(sum,end=" ")
        i+=1