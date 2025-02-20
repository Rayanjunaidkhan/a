class Treasurechest:
    # DECLARE question : STRING
    # DECLARE answer : INTEGER
    # DECLARE points : INTEGER
    def __init__(self,question,answer,points):
        self.question = question
        self.answer = answer
        self.points = points

    def getquestion(self):
        return self.question
    
    def checkanswer(self,answer):
        if self.answer == "Hello World":
            return True
        else:
            return False
        
    def getpoints(self,attempts):
        self.points = self.points - attempts
        return self.points 
