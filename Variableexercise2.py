# define weights for each category
fltHwWeight = 0.4
fltExamWeight = 0.5
fltDiscussionWeight = 0.1

# ask the user for their grades
hw_grade = float(input("Enter your homework grade: "))
exam_grade = float(input("Enter your exam grade: "))
discussion_grade = float(input("Enter your discussion grade: "))

# calculate the weighted total grade
total_grade = (hw_grade * fltHwWeight) + (exam_grade * fltExamWeight) + (discussion_grade * fltDiscussionWeight)

# print out the total grade
print("Your total grade in the class is:", total_grade)
