def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("All input lists must be of the same length when 'strct' is True.")
    else:
        min_length = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_length)]
def my_sort(tuples_list, key=0):
    n = len(tuples_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tuples_list[j][key] > tuples_list[j + 1][key]:
                tuples_list[j], tuples_list[j + 1] = tuples_list[j + 1], tuples_list[j]
    return tuples_list
customer_names = ["Alice", "Bob", "Charlie"]
customer_ids = [102, 101, 103]
shopping_points = [150, 200, 100]
zipped_list = my_zip(customer_names, customer_ids, shopping_points)
sorted_by_name = my_sort(zipped_list.copy(), key=0)
print("Sorted by customer name:", sorted_by_name)
sorted_by_id = my_sort(zipped_list.copy(), key=1)
print("Sorted by customer ID:", sorted_by_id)
sorted_by_points = my_sort(zipped_list.copy(), key=2)
print("Sorted by shopping points:", sorted_by_points)
