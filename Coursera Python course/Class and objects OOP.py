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

# kalo print(Employee.num_of_emp) ini diletakin diatas emp_1 saam emp_2 bakal = 0

emp_1 = Employee('Haekal',"Ghifari",50000) #self di function diatas itu = emp_1
emp_2 = Employee('Test','User', 10000)

print(emp_1.email) #ini attribute, attribute yang ada di function nya
print(emp_1.fullname()) #butuh tanda kurung soalnya ini methon bukan attribute
print(Employee.fullname(emp_1)) #kasih emp_1 musti dikasih tau self yang mana

print(Employee.raise_amount) #ini tiga hasilnya sama soalnya udah kedefine di class variable
#kalo misalnya diatas dibilang emp_1.raise_amount = 1.05 jadi buat emp_1 1.05 tapi yg lain sama
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emp)
emp_1.apply_raise() #ada tiga cara bisa kyk gini
print(emp_1.pay)
print(emp_1.apply_raise()) #kyk gini
print(Employee.apply_raise(emp_1)) #sama bisa kyk gini


    

