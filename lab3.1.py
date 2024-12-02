def display_squares(n):
    print("Number\tSquare")
    num = 1
    while num <= n:
        square = num ** 2
        print(f"{num}\t{square}")
        num += 1
if __name__ == "__main__":
        n = int(input("Enter the value of n: "))
        if n < 1:
            print("Please enter a positive integer.")
        else:
            display_squares(n)
    
