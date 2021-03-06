nama = input ("Enter your name : ")
umur = input ("Enter your age : ")
kalimat = 'Your name is {} and You are {} years old'.format(nama,umur)
print(kalimat) #kalo argumen ga bisa di define dengan print
print("My name is not " +  nama + ", I am sans" )
#index operation buat string
print(" ")
print("string operation")
print(" ")
a = "Hello, World !"
print(a[1]) #ngeprint index pertama yaitu e mulainya dari 0 
print(a[-4]) #pake minus ngeprint dari belakang jadi tanda seru yg keluar
print(a[2:5]) #ngeprint index ke 2 sampai sebelum 5 yaitu sampai 4 jadi llo 
print(a[::2]) #ngeprint semua kalimat tapi setiap index yang genap atau kyk 2 terus 4 6 gitu
print(a[0:5:3]) #ngeprint index 0 sampe  5 tapi yang bilangan element 3
print(len(a)) #nyari tau panjang string
print(a[3:]) #ngambil dari baris tiga sampe semuanya
print(a[:3]) #dari 0 sampai baris sebelum 3 yaitu 2
print(a[:-1]) #ambil semua sampai baris sebelum terakhir pertama jadi ga pake tanda seru
print("cara ngeprint backslash \\ harus dua kali") #print blackslash \\ harus dua kali
print(r"cara ngeprint backslash \ harus dua kali") #print blackslash atau ga depan kasih r (raw string)


b = "Artinya Halo, Dunia! "
c = a + " = " + b + ", begitu"
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

print(" ")
print("String operation 2 ")
print(" ")

gg = "Mary had a little lamb Little dumb"
gg.find("lamb") #buat cari lamb diindex ke berapa outputnya angka pertama indexnya yaitu l diindex keberapa
print(gg.find("lamb"))

ff = "You are wrong"
ff.upper() #buat jadiin ke uppercase
print(ff.upper())

gg.replace("Mary","Barry") #buat ganti kalimat
print(gg.replace("Mary","Barry"))

print("Michael \n Jackson") #\n buat ngasih tau new line
print("Michael \t Jackson") #\t buat ngasih tau spasi banyak atau tab

print(" ")
print("Tuple operation")
print(" ")
#tuple bisa gabungin int, float, str data type ke satu kelompok. list juga bisa
#tuple can be nested with list, so does likewise
#bedanya kalo tuple immutable kalo list mutable
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2))) #tuple ga bisa diubah tuple pake () kalo list pake []
#ini diatas adalah nested tuple, didalemnya tuple ada tuple lagi gitu
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

print("Element 2, 0 of Tuple: ",   NestedT[2][0]) #buat manggil 2 element sekaligus
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])

print(NestedT[2][1][0]) #nge print tuple ke dua yaitu pop rock, data ke 1 yaitu rock dan idex ke 0 
#yaitu r

C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple) #ngurutin data dari gede ke kecil
print(C_list)

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock","R&B", "progressive rock", "disco") 
genres_tuple
print(genres_tuple.index("disco")) #buat nyari disco ada diindex keberapa yaitu 7 

print(" ")
print("List operation")
print(" ")

List = ["Michael Jackson", 10.1, 1982] #pake sqr brackets nandain itu array of data
print('the same element using negative and positive indexing:\n Postive:',List[0],
'\n Negative:' , List[-3]  )
print('the same element using negative and positive indexing:\n Postive:',List[1],
'\n Negative:' , List[-2]  )
print('the same element using negative and positive indexing:\n Postive:',List[2],
'\n Negative:' , List[-1]  )
List2 = ["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)] #list can be nested with tuple and list

List.extend(['pop', 10]) #nambahin isi di list jadi 2 element

List.append(['az', 4]) #nambahin satu element tapi jadi nested 
# [] buat aktif data atau akan melakukan sesuatu terhadap data tsbt
print(List)
#since list is mutable therefore it is liable to change so we can change its element
ABAA = ["disco", 10, 1.2]
print('Before change:', ABAA)
ABAA[0] = 'hard rock' #change the first element of list ABAA to hard rock
print('After change:', ABAA)
del(ABAA[0]) #delete the first element of list ABAA
print('After change:', ABAA)

BIBA = 'hard rock'
print(BIBA.split()) #split an element into two and turn it into a list
CICA = 'A,B,C,D'
print(CICA.split(','))

print(" ")
print("Dictionary operation")
print(" ")


release_year_dict = {"Thriller":"1982", "Back in Black":"1980", \
                    "The Dark Side of the Moon":"1973", "The Bodyguard":"1992", \
                    "Bat Out of Hell":"1977", "Their Greatest Hits (1971-1975)":"1976", \
                    "Saturday Night Fever":"1977", "Rumours":"1977"} #ini dictionary
                    #bisa contain tuple list sebagai value didalem dictionary
print(release_year_dict['Thriller'])  #buat nyari tau value nya thriller yaitu 19982
# print(release_year_dict[1]) ga bisa manggil kyk gini kalo dictionary
print(release_year_dict.keys())  #ngeprint semua keys, thriller back in black, dsb.
print(" ")
print(release_year_dict.values())  #ngeprint semua values kayak 1982, 1980 dsb
print(" ")
release_year_dict['Graduation']='2007' #ngeadd graduation : 2007 kedalam dictionary nya
print(" ")
print(release_year_dict)
del(release_year_dict['Thriller']) #delete keys didalam dictionary
del(release_year_dict['Graduation'])
print(" ")
print(release_year_dict)
print('The Bodyguard' in release_year_dict) #ngecheck keys ini ada ga di dictionary jawabannya true or false