def grade_finder(marks):
    perc = (marks / 100) * 100
    if (perc >= 90 and perc <= 100):
        print('A')
    elif(perc >= 80 and perc < 90):
        print('B')
    elif( perc >= 70 and perc < 80):
        print('C')
    else:
        print('F')


mathsmarks = int(input("enter maths marks: "))
physmarks = int(input("enter physics marks: "))
csmarks = int(input("enter cs marks: "))

grade_finder(mathsmarks)
grade_finder(physmarks)
grade_finder(csmarks)
