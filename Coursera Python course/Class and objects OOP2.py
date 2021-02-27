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
    #class variables
    #class variables are variables that are shared among all instances of a class
    
    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)
        return self.pay

    @classmethod  
    def set_raise_amt(cls, amount): #ini lansung manggil classnya
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod #doesnt take instance or class as the first argument
    def is_workday(day): #just pass in the argument we want to work with
        if day.weekday == 5 or day.weekday == 6: # 5 & 6 itu sabtu dan minggu 0 = senin
            return False    
        return True

emp_1 = Employee('Haekal',"Ghifari",50000) 
emp_2 = Employee('Test','User', 10000) 

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1) #pas manggil class ga perlu manggil selfnya lagi
print(new_emp_1.email) #buat ngeliat masing2 self instancesnya yg udh di set dari class
print(new_emp_1.fullname())
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016,7,10)

print(Employee.is_workday(my_date))