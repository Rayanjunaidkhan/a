class character: 
    def __init__(self,character_name,Dateofbirth,intelligence,speed):
        self.charactername = character_name
        self.dateofbirth = Dateofbirth
        self.intelligence = intelligence
        self.speed = speed


    def setintelligence(self,intelligence):
        self.intelligence = intelligence

    def getintelligence(self):
        return self.intelligence
    
    def getname(self):
        return self.charactername
    
    def returnage(self):
         date = self.dateofbirth.split()
         year = int(date[2])
         age = 2023 - year
         return age
    
    def learn(self):
        self.intelligence = (1.10) * self.intelligence
        return self.intelligence
    

firstcharcter = character("royal","1 january 2019",70,30)
firstcharcter.learn()
print(f"name: {firstcharcter.getname()},age: {firstcharcter.returnage()} intelligence: {firstcharcter.getintelligence()}")


class magicharacter(character):
    def __init__(self, character_name, Dateofbirth, intelligence, speed,element):
        super().__init__(character_name, Dateofbirth, intelligence, speed)
        self.element = element

    def learn(self):
        if self.element == "fire":
            self.intelligence = 1.20 * self.intelligence
        elif self.element == "earth":
            self.intelligence = 1.30 * self.intelligence
        else:
            self.intelligence = 1.10 * self.intelligence

firstmagic = magicharacter("light","3 march 2018",75,22,"fire")
firstmagic.learn()
print(f"name: {firstmagic.getname()},age: {firstmagic.returnage()} intelligence: {firstmagic.getintelligence()}")
