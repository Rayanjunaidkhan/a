class employee:
    def __init__(self,name,ID,salary):
        self.name = name
        self.ID = ID
        self.salary = salary

    def setsalary(self, salary):
        self.salary = salary

    def getsalary(self):
        return self.salary
    
    def getdetails(self):
        return self.name,self.ID,self.salary
    
class teacher(employee):
    def __init__(self,name,ID,salary,subject):
        super().__init__(name,ID,salary)
        self.subject = subject

    def getdetails(self):
        return self.name,self.ID,self.salary,self.subject
        
class custodian(employee):
    def __init__(self,name,ID,salary,job):
        super().__init__(name,ID,salary)
        self.job = job

    def getdetails(self):
        return self.name,self.ID,self.salary,self.job
       
# example usage
taech1 = teacher("ali Khan",1001,144000,"math")
staff1 = custodian("zahid",2001,44000,"kitchen")
print(taech1.getdetails())
print(staff1.getdetails())