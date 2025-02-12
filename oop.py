class employee:
    def __init__(self,name,contact,address,status,date_join,salary):
        self.name = name
        self.contact = contact
        self.address = address
        self.status = status
        self.date_join = date_join
        self.salary = salary
    
    def set_name(self,name):
        self.name = name

    def set_contact(self,contact):
        self.contact = contact

    def set_address(self,address):
        self.address = address

    def set_status(self,status):
        self.status = status

    def set_date_join(self,date_join):
        self.date_join = date_join

    def get_details(self):
        print("name: ",self.name)
        print("contact: ",self.contact)
        print("address",self.address)
        print("status: ",self.status)
        print("date of joining: ",self.date_join)
        print("salary: ",self.salary)

    def calculate_salary(self,salary):
        return self.salary * 0.9

emp1 = employee("john doe",1233212,"jt","active","23/11/2000",150000)
emp1.get_details()
print("salary after tax: ",emp1.calculate_salary(150000))