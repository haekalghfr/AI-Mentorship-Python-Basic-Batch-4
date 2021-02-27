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

class Developer(Employee):
    raise_amount = 1.15

    def __init__(self, first, last, pay, prog_lang): #ngasih developer class its own programming by giving init method
        super().__init__(first, last, pay) 
        #buat masukkin variable ke developer tapi yang employee gaada variable prog_lang
        #bisa juga super() di ganti sama nama classnya yaitu Employee. jadi ditulis sbg berikut
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None): #employees = none berarti kita udh set defaultnya jadi none
        super().__init__(first, last, pay)                #ini namanya default argument
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp): #ini function/method buat nge add employee nanti buat dijadiin argumen
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp): #ini function/method buat nge remove employee nanti buat dijadiin argumen
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self): #buat ngasih list employee yang dipegang managernya
        for emp in self.employees:
            print('-->', emp.fullname())
    


dev_1 = Developer('Corey', 'Schafer', 50000, 'Java')
dev_2 = Developer('Test', 'Employee', 60000, 'Python')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(dev_1.email)
print(dev_2.email)
print(dev_1.prog_lang)
print(dev_2.prog_lang)


Developer.apply_raise(dev_1) #gaji naik sesuai raise amount di class developer
print(dev_1.pay) #argumen diatas masukkin class developer ke apply_raise employee
Developer.apply_raise(dev_2)
print(dev_2.pay)
#diatas depannya dikasih argumen developer.apply_raise dulu soalnya di class developer
#ada function apply_raise yang value nya beda sama employee 
#jadi diketik developer.apply_raise buat apply raise yg udh di define
#di class developer

print(mgr_1.email)


mgr_1.add_emp(dev_2) #ini ngetiknya depannya ga pake Manager
#Soalnya ini Function baru jadi ga usah
#jadi langsung aja untuk ngeadd dan remove langsung nama variable.method(nama variable yg dimasukkin)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(Manager.apply_raise(mgr_1))

print(isinstance(mgr_1, Manager)) #buat nyari tau kalo mgr_1 itu instance dari Manager
#jawabannya true and false
print(issubclass(Developer, Employee)) #buat nyari tau kalo developer itu subclassnya Employee
#jawabannya juda true and false