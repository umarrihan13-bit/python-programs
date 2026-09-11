classmates = ["Alice", "Bob", "Charlie", "David", "Eva"]
print("Classmates List:", classmates)

print("total number of classmates:", len(classmates))
print("First classmate:", classmates[0])
print("Last classmate:", classmates[-1])
print("first three classmates:", classmates[:3])

classmates.append("Frank")
print("\nafter adding Frank:", classmates)
classmates.remove("Eva")
print("after removing Eva:", classmates)
classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)

teachers = {"name": "Mr. Smith", "subject": "Python", "experience": 5}
print("\nTeacher Information:", teachers)

print("subject:", teachers["subject"])
print("experience:", teachers.get("experience","not Found"))
teachers["email"] = " Smith@school.com"
teachers.pop("experience")
print("updated Teacher profile:", teachers)

roll_numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie", "David", "Eva"]
student_info = list(zip(roll_numbers, names))
student_directory = dict(student_info)
print("\nStudent directory:", student_directory)
print("Student at Roll number 3:", student_directory[3])