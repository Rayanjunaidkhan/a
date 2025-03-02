class queue:
    def __init__(self,QueueArray,Headpointer,Tailpointer):
        self.Tailpointer = Tailpointer
        self.Headpointer = Headpointer
        self.QueueArray = QueueArray
        QueueArray = [QueueArray] * 100

Thequeue = queue(-1,-1,-1)
print(Thequeue)
