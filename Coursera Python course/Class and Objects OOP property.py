class Employee: 

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property #biar kita bisa akses method kayak atribut
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter #biar bisa ganti full name lgsg 
    def fullname(self, name): #kyk emp_1.fullname = 'baba baies'
        first, last = name.split(' ') #first sama last attribute nya jg lgsg keganti
        self.first = first
        self.last = last

    @fullname.deleter #deleter berguna buat nge delete isi attribute 
    def fullname(self): #ini bisa digunain dgn bilang del variable
        print('Delete Name!') #ini buat nge clean up data
        self.first = None
        self.last = None
        
    

emp_1 = Employee('Haekal', 'Ghifari')
emp_1.fullname = 'baba baies'

print(emp_1.fullname)
print(emp_1.email)
print(emp_1.first)

del emp_1.fullname #buat ngedelete full name dan semua data

# class Employee: 

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com"

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#emp_1 = Employee('Haekal', 'Ghifari')
#emp_1.first = 'Jim'

#print(emp_1.email)
#print(emp_1.first) --> ini buat akses attribute
#print(emp_1.fullname()) --> ini buat akses method
#nanti keluarnya emailnya tetep haekal.ghifari@email.com
#buat gantinya liat keatas

