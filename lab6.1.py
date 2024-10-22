def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("All input lists must be of the same length when 'strct' is True.")
    else:
        min_length = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_length)]
customer_names = ["Alice", "Bob", "Charlie"]
customer_ids = [102, 101, 103]
shopping_points = [150, 200, 100]
try:
    result_strict = my_zip(customer_names, customer_ids, shopping_points, strct=True)
    print("Strict zipping result:", result_strict)
except ValueError as e:
    print(e)
result_non_strict = my_zip(customer_names, customer_ids, shopping_points, strct=False)
print("Non-strict zipping result:", result_non_strict)
