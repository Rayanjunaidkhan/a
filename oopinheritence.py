
class vehicle:
    def __init__(self, IDP, MaxspeedP, IncreaseAmountP):
        self.__ID = IDP
        self.__Maxspeed = MaxspeedP
        self.__IncreaseAmount = IncreaseAmountP
        self.__currentspeed = 0
        self.__HorizontalPosition = 0
        
        def getcurrentspeed(self):
            return self.__currentspeed
        
        def getincreasedspeed(self):
            return self.__IncreaseAmount
        
        def gethorizontalposition(self):
            return self.__HorizontalPosition
        
        def getmaxspeed(self):
            return self.__maxspeed
        
        def setcurrentspeed(self, newcurrentspeed):
            self.__currentspeed = newcurrentspeed

        def stehorizontalposition(self, newhorizontalposition):
            self.__horizontalposition = newhorizontalposition

        def increasespeed(self):
            self.__currentspeed = self.__currentspeed + self.__increaseamount
            if self.__currentspeed > self.__Maxspeed:
                self.__currentspeed = self.__Maxspeed

            self.__HorizontalPosition = self.__HorizontalPosition + self.__currentspeed
    class helicopter:
        def __init__(self,IDP,maxspeedP,verticlecP,maxheightP):
            super().__init__
            self.__verticleposition = 0
            self.__verticlechange = verticlecP
            self.__maxheight = maxheightP
            def getverticleposition(self):
                return self.__verticleposition
            def increasespeed(self):
                self.__currentspeed = self.__currentspeed + self.__IncreaseAmount
helicopter = vehicle()
helicopter.__ID = "parrot"
helicopter.__currentspeed = 80
print(helicopter)