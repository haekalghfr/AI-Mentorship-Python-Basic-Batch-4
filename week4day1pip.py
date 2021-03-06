my_list = [1,1,1,1,1,1] #list datanya bisa sama
#list datanya dapan diurutkan
#datanya bisa diambil gt kalo may ngambil index ke 0
#datanya juga bisa diubah
print(my_list[0])
my_list[2] = 10
print(my_list)

my_dict = {
    'umur' : 21
} #umur = key, value = 21
#ga bisa dipanggil lewat index kyk list
print(my_dict['umur']) #liat value dgn manggil key nya
my_dict['name'] ='joko'
#nambahin key dan value ke dict
my_dict['umur'] ='13'
#ganti value

my_tuple = ('apel', 'pisang', 'gangga') #tuple pake dalam kurung biasa
#ini bisa diindexin juga jadi kayak
print(my_tuple[2]) #sifatanya kayak list bisa dipanggil perindex
#tuple datanya ga bisa diubah 
#datanya bisa duplikat juga

my_set = {'apel','mangga','jambu'}
a = set() #mau menginisiasi kalo ini set kosong
#kalo ga ditulis set depannya jadi dictionary

for buah in my_set:
    print(buah)

#ga bisa di panggil perindex
#datanya bisa ditambah 
#pake method add, kalo list append

my_set.add('melon')
my_set.remove('jambu')

#set datanya ga bisa duplikat dan berurutan kalo dipanggil
my_set2 = {2,3,4,5,5,3,1,2}
print(my_set2)

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}

print(A | B) #gabungin a dan b
print(A & B) #cari irisan data
print(A - B)

print('')
print('scope operation')
print('')

x = 300 #ini variabel global x nya ini
#bisa diakses didalam atau diluar function

def myfunc():
    x = 200 #ini local variable x nya
    y = 100
    print(x) #cuma bisa di akses didalem function tersebut

myfunc() #hasilnya x = 200
print(x) #hasilnya x = 300
#print(y) #ini ga bisa soalnya y itu punya local function
#bukan global variable