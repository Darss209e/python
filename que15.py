marks = {"A": 85, "B": 92, "C": 78}

# max_marks = -1
# top_student = ""
# for student in marks:
#     if marks[student]> max_marks:
#         max_marks = marks[student]
#         top_student = student

# print(top_student)

print(max(marks , key=marks.get))