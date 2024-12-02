customer_names = [input(f"Enter name for customer {i+1}: ") for i in range(3)]
customer_ids = [int(input(f"Enter ID for customer {i+1}: ")) for i in range(3)]
shopping_points = [int(input(f"Enter shopping points for customer {i+1}: ")) for i in range(3)]
tuples_with_zip = list(zip(customer_names, customer_ids, shopping_points))
tuples_without_zip = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(3)]
print("\nList of tuples using zip():", tuples_with_zip)
print("List of tuples without using zip():", tuples_without_zip)
