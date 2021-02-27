class Employee:

    num_of_emp = 0
    raise_amount = 1.04 #ini class variable ini variable bakal masuk kesetiap function

    def __init__(self, first, last, pay):
        self.first = first #ini semua instance variables
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emp += 1 #setiap ada emp_x baru num_of_emp nya nambah 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)
        return self.pay

    def __repr__(self): #repr is meant to be an unambiguous representation of an object
        #should be used for debugging and logging, meant to be displayed to developers 
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self): #readable represantion of an an object an is meant to be displayed to the end users
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self,other): #untuk penjumlahan tp ditaro function 
        return self.pay + other.pay #niatnya ini mau gabungin salary employees

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Haekal',"Ghifari",50000) #self di function diatas itu = emp_1
emp_2 = Employee('Test','User', 10000)

print(emp_1) #resulted in vague result kalo gaada str or repr
print(repr(emp_1))
print(str(emp_1))

#bisa juga kyk gini
print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_1 + emp_2) #kalo gaada dunder add ga bisa
print(len(emp_1)) #kalo gaada dunder len ga bisa diitung 

# __xx__ --> double underscore itu namanya dunder
#ada banyak function yang pake dunder, dunder itu special function