class eventitem:
    # DECLARE eventname : STRING
    # DECLARE type : STRING
    # DECLARE difficulty : INTEGER
    def __init__(self,eventname,type,difficulty):
        self.eventname = eventname
        self.type = type
        self.difficulty = difficulty

    def getname(self):
        return self.eventname
    
    def getdifficulty(self):
        return self.difficulty
    
    def geteventtype(self):
        return self.type
class chaarcter:
    # DECLARE charactername : STRING
    # DECLARE jump : INTEGER
    # DECLARE swim : INTEGER
    # DECLARE run : INTEGER
    # DECLARE drive : INTEGER
    def __init__(self,charactername,jump,swim,run,drive):
        self.charactername  = charactername
        self.jump = jump
        self.swim = swim
        self.run = run
        self.drive = drive

    def getname(self):
        return self.charactername
    
    def calculatescore(self,type,diffculty):
        skill = 0
        if type == "jump":
            skill = self.jump
        elif type == "run":
            skill == self.run
        elif type == "swim":
            skill = self.swim
        elif type == "drive":
            skill = self.drive
        
        if skill >= diffculty:
            return 100
        else:
            difference = diffculty - skill
            if difference == 1:
                return 80
            elif difference == 2:
                return 60
            elif difference == 3:
                return 40
            elif difference == 4:
                return 20
            else:
                return 0


group = [0] * 5
group[0] = eventitem("bridge","jump",3)
group[1] = eventitem("water wade","swim",4)
group[2] = eventitem("100 mile run","run",5)
group[3] = eventitem("gridlock","drive",2)
group[4] = eventitem("wall on wall","jump",4)      

chaarcter1 = chaarcter("Tarz",5,3,5,1)
chaarcter2 = chaarcter("Geni",2,2,3,4)
# first for bridge
C1points = 0
C2points = 0
for i in range (5):
    C1score = chaarcter1.calculatescore(group[i].geteventtype(),group[i].getdifficulty())
    C2score = chaarcter2.calculatescore(group[i].geteventtype(),group[i].getdifficulty())

    if C1score > C2score:
        C1points = C1points + 1
        print(f"event{i+1} was won by Tarz!!!")
    elif C1score < C1score:
        C2points = C2points + 1
        print(f"event{i+1} was won by gary!!!")
    else:
        print(f"event{i+1} was a draw")

if C1points > C2points:
    print("Games won by Tarz!!!")
elif C1points < C2points:
    print("Games won by Gary!!!")
else:
    print("its a draw")
