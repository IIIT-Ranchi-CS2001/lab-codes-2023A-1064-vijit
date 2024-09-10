n=int(input("Enter the number for the multiplication table: "))
end=int(input("Enter the limit: "))
print(f"Multiplication table for {n} up to {end}:")
for i in range (1,end+1):
    print(f"{n}x{i}={n*i}")