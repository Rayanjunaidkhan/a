class character:
    # DECLARE name : STRING
    # DECLARE Xcoordinate : INTEGER
    # DECLARE Ycoordinate : INTEGER
    def __init__(self,name,Xcoordinate,Ycoordinate):
        self.name = name
        self.Xcoordinate = Xcoordinate
        self.Ycoordinate = Ycoordinate

    def getname(self):
        return self.name
    
    def getX(self):
        return self.Xcoordinate
    
    def getY(self):
        return self.Ycoordinate
    
    def changeposition(self,Xchange,Ychange):
        self.Xcoordinate = self.Xcoordinate + Xchange
        self.Ycoordinate = self.Ycoordinate + Ychange

    
        
    