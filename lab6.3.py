def my_max(input_data):
    if isinstance(input_data, set):
        input_data = list(input_data)
    if not input_data:
        raise ValueError("Cannot find maximum of an empty list/set/tuple")
    max_value = input_data[0]
    for item in input_data:
        if item > max_value:
            max_value = item 
    return max_value
input_list = [3, 1, 4, 1, 5, 9]
input_set = {10, 20, 30, 5, 15}
input_tuple = (7, 2, 8, 1, 6)
print("Max value in list:", my_max(input_list))
print("Max value in set:", my_max(input_set))
print("Max value in tuple:", my_max(input_tuple))
