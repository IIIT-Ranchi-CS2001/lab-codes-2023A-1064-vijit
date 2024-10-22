print("With sorted function")
customers = [("Alice", 102, 150), ("Bob", 101, 200), ("Charlie", 103, 100)]
sorted_customers_by_id = sorted(customers, key=lambda x: x[1]) 
print("Sorted by customer ID (using sorted()):", sorted_customers_by_id)
sorted_customers_by_points = sorted(customers, key=lambda x: x[2])
print("Sorted by shopping points (using sorted()):", sorted_customers_by_points)



print("Without sorted function manually")
customers = [("Alice", 102, 150), ("Bob", 101, 200), ("Charlie", 103, 100)]
def bubble_sort(lst, key):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j][key] > lst[j+1][key]:
                lst[j], lst[j+1] = lst[j+1], lst[j] 
    return lst
sorted_customers_by_id_manual = bubble_sort(customers.copy(), 1)
print("Sorted by customer ID (without sorted()):", sorted_customers_by_id_manual)
sorted_customers_by_points_manual = bubble_sort(customers.copy(), 2)
print("Sorted by shopping points (without sorted()):", sorted_customers_by_points_manual)
