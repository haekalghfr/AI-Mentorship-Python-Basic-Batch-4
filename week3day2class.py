class Myclass:
    x = 5

obj1 = Myclass()
obj2 = Myclass()

class Person:
    def __init__(self,name,age) : #ini namanya method
        self.name = name #ini namanya attribute
        self.age = age

    def greetings(self):
        print('Hello my name is {}'.format(self.name))

p1 = Person('bay', 20)
print(p1) #si p1 ini object dari kelas person
print(p1.name) #ngambil attribute name dari object person
print(p1.age) #ngambil attribute age dari object person
p1.greetings()


