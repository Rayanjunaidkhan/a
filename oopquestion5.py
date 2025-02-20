class picture:
    # DECLARE description : STRING
    # DECLARE width : INTEGER
    # DECLARE height : INTEGER
    # DECLARE framecolor : STRING
    def __init__(self,description,width,height,framecolor):
        self.description = description
        self.width = width
        self.height = height
        self.framecolor = framecolor

    def getdescription(self):
        return self.description
    
    def getheight(self):
        return self.height
    
    def getwidth(self):
        return self.width
    
    def getcolor(self):
        return self.framecolor
    
    def setdescription(self,description):
        self.description = description
