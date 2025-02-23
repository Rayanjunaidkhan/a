# text file and main file bust be in same folder
f = open("students.txt",'r')
# print(f.read())

list = f.readlines()
print(list)
f.close
