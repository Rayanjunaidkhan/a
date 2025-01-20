# highly important to initialize the sum variable
sum = 0
average = 0
min = 9993281749374293847
max = 0
for i in range (10):
    num = int(input("enter number : "))
    sum = sum + num
    if (max < num):
        max = num
    if (min > num):
        min = num
    
print("maximum : ",max)
print("minimum : ",min)
average = sum/10
print("average : ",average)