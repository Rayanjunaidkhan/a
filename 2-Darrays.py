# a school has 5 classrooms and 10 students in each class
# a 2-D arrays takes input of marks of each student from each class
# rows are classes and columns are students

Class = 5
students = 10

marks = [[0] * students for _ in range(Class)]

for j in range(Class):
    print("class: ",j+1)
    for i in range (students):
        print("student: ",i+1)
        marks[j][i] = int(input("enter marks: "))

print(marks)
