days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
readings = [[0] * 24 for _ in range(7) ]
avgtemp = [0] * 7
avgtempfaren = [0] * 7
wee = 24
for i in range(7):
    for j in range(wee):
        readings[i][j] = int(input(f"Give {days[i]} reading {j+1}:  "))
        
        while readings[i][j] > 50 or readings[i][j] < -20:
            readings[i][j] = int(input(f"Invalid input. give day: {days[i]} reading: {j+1} again "))
        
        

for c in range (7):
    for d in range(wee):
        value = readings[c][d]
        sum  = value + readings[c][d-1]
        avgtemp[c] = sum / wee

for z in range(7):
    avgtempfaren[z] = avgtemp[z] * ((9/5) + 32)


total = 0
for n in range(7):
    total = avgtemp[n] + total
    avgtempweek = total / 7


summation = 0
for m in range (7):
    summation = avgtempfaren[m] + summation
    avgtempweekfaren = summation / 7

for q in range(7):
    print(f"for day {days[q]} the average temprature in celsius is {avgtemp[q]}C and avrage temprature in farenheit is {avgtempfaren[q]}F ")
    print("______________________________________________________________________")

print(f"the average temprature for the whole week in celcius is {avgtempweek} and in farenheight is {avgtempweekfaren}")
