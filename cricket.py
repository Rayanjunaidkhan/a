
club_no = 12
win = 12
draw = 5
loss = 0


clubs = [" "] * 12
statistics = [[0] * club_no for _ in range(3)]
points = [0] * club_no
matches_played = [0] * club_no


for a in range(12):
     print(f"club id is {a+1}")
     clubs[a] = str(input("what is you clubs name: "))
for z in range(club_no):
    print("club no.",z+1)
    matches_played[z] = int(input("How many matches did the club play: "))
    while(int(matches_played[z]) > 22 or int(matches_played[z]) < 0):
        matches_played[z] = int(input("invalid input enter again: "))

for j in range(3):
    for i in range(club_no):
        if (j == 0) :
            print(f"how many matches did club no.{i+1} win?")
        elif(j == 1):
            print(f"how many matches did club no.{i+1} draw")
        elif( j == 2 ):
            print(f"how many matches did club no.{i +1} lose?")
        if((statistics[0][i] + statistics[1][i] + statistics[2][i]) > matches_played[i]):
            print(f"inputs for club no.{i+1} are invalid. please enter again: ")

        statistics[j][i] = int(input())

for q in range(club_no):
    points[q] = (statistics[0][q] * win)+(statistics[1][q]*draw)+(statistics[2][q]*loss)

x = max(points)
idx = points.index(x)

print("the winning club is ",clubs[idx])
print(f"thay have won {statistics[0][idx]} games")
print(f"they have obtained {points[idx]} points")