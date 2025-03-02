Highscores = [[""]*3 for _ in range(7)]
def readdata():
    try:
        file = open("HighScoreTable.txt","r")
        for i in range(7):
            Highscores[i][0] = file.readline()
            Highscores[i][1] = file.readline()
            Highscores[i][2] = file.readline()
            
            # Highscores.append([t,u,x])
        print(Highscores)
        file.close()
    except:
        print("no file found")

def Oupputhighscore(array):
    for i in range(7):
        print(array[i][0],"reached level,",array[i][1],"with a score of,",array[i][2])
def SortScores(array):
    n = len(array)
    for i in range (n-1):
        for j in range(n-i-1):
            if array[j + 1] > array[j]:
                array[j],array[j + 1] = array[j + 1],array[j]

readdata()
Oupputhighscore(Highscores)
print(SortScores(Highscores))