nama = input ("Enter your name : ")
umur = input ("Enter your age : ")
kalimat = 'Your name is {} and You are {} years old'.format(nama,umur)
print("kalimat") #kalo argumen ga bisa di define dengan print
print("Your name is not " +  nama + ", I am steven" )
#index operation buat string
print(" ")
print("string operation")
print(" ")
a = "Hello, World !"
print(a[1]) #ngeprint index pertama yaitu e mulainya dari 0 
print(a[-1]) #pake minus ngeprint dari belakang jadi tanda seru yg keluar
print(a[2:5]) #ngeprint index ke 2 sampai sebelum 5 yaitu sampai 4 jadi llo 
print(len(a)) #nyari tau panjang string
print(a[3:]) #ngambil dari baris tiga sampe semuanya
print(a[:3]) #dari 0 sampai baris sebelum 3 yaitu 2
print(a[:-1]) #ambil semua sampai baris sebelum terakhir pertama jadi ga pake tanda seru

b = "Artinya Halo, Dunia! "
c = a + " = " + b + "2"
print(c)

print(" ")
print("Boolean operation")
print(" ")

print(10>9) #buat cari tau True of False
print(10==9)
print(10<9) 
print(True and True) #hasilnya jadi true
print(True and False) #hasilnya jadi false
print(True or False) #hasilnya jadi true

print(" ")
print("Conditions operation")
print(" ")

l = int(input("Type any number for l : ") )
m = float(input("Type any number for m : ") )

if l>m: 
    print("{} lebih besar dari pada {}".format(l,m))
elif l==m: #kalo mau tambah kondisi lagi tambah elif
    print("{} sama dengan {}".format(l,m))
else: #else kondisi terakhir
    print ("{} lebih kecil dari pada {}".format(l,m))

num = int(input("Type any number : ")) #pake int atau float biar tau kalimat yg diinput itu angka

if num % 2 == 0: 
    print(" {} adalah bilangan genap".format(num))
else: #else kondisi terakhir
    print ("{} adalah bilangan ganjil".format(num))

print(" ")
print("list operation")
print(" ")

mylist = [] #pake sqr brackets buat ngasih tau itu array
print(type(mylist))

mylist.append(1) #tambah .append buat nge add angka ke kolum array
mylist.append(2)
mylist.append(3)
mylist.append(4)
print(mylist)

x = [9,8,7,6,5,3]
print(x[0:2])

for i in x: #variable i mengakses setiap angka diarray, looping buat ngeluarin satu satu angka atau data di arraynya
    print(i)