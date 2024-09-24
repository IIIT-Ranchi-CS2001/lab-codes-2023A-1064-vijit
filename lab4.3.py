course_codes = ["CS2001", "CS2005", "CS2007", "CS2009"]
course_names = ["Python", "C++", "Algorithms", "Java"]
combined_list = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]
print(combined_list)
