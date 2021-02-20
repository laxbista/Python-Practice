# Exercise Question 7: Assign a different name to function and call it through the new name
def displayStudent(name, age):
    print(name, age)


showStudent = displayStudent
displayStudent("Emma", 26)
showStudent("Jemma", 27)
