# String Manipulation 4th QuestionPython (student details)

name = input("Enter the student's name: ")
roll_number = input("Enter the roll number: ")
marks = int(input("Enter the marks secured for Mathematics Examination (out of 100): "))

# Grade point and Remark based on marks
if marks >= 90:
    grade_point = 10
    remark = "OUTSTANDING"
elif 80 <= marks < 90:
    grade_point = 9
    remark = "VERY GOOD"
elif 70 <= marks < 80:
    grade_point = 8
    remark = "GOOD"
elif 60 <= marks < 70:
    grade_point = 7
    remark = "AVERAGE"
elif 50 <= marks < 60:
    grade_point = 6
    remark = "PASS"
else:
    grade_point = 0
    remark = "FAIL"

# Output
print("\nStudent Details:")
print("Name: ",name)
print("Roll Number: ",roll_number)
print("Marks: ",marks)
print("Grade Point: ",grade_point)
print("Remark: ",remark)