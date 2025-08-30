try:
    student={'Alice':90}
    x=input("Enter the student\'s name: ")
    print(student[x])
except KeyError as e:
    print("Student not found.")
