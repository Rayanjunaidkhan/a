name = str(input("enter name: "))
marks = int(input("enter marks: "))

percentage = marks*100 / 120

if (percentage >= 90 and percentage <= 100) :
    print("A*")
elif (percentage >= 80 and percentage < 90):
    print("A")
elif (percentage >= 70 and percentage < 80) :
    print("B")
else:
    print("F")
