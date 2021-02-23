print("Nested Loop Operation")
print(" ")

for i in range(2):
    print("i : {}".format(i))
    for j in range(4):
        print("j : {}".format(j))
    print('----')

for baris in range(2):
    for kolom in range(3):
        print("{}.{}".format(baris+1,kolom+1), end=" ") #kasih fungsi end biar hasilnya jadi horizontal buat bikin matrix
    print () #kasih end biar ga kebawah angkanya tapi kesamping angkanya
    #kalo ketik end = "-" nanti jadinya - yang misahin tapi kesamping gitu

print(" ")
print("Dictionary Loop Operation")
print(" ")

pelanggan = {"nama" : "Astuti", "umur" : 20}
pelanggan_2 = {"nama" : "Aba", "umur" : 25}
print("Nama : {} , Umur : {}".format(pelanggan["nama"],pelanggan["umur"]))
#pelanggan["nama"] buat ngakses value dari key itu

#ganti value dari key
pelanggan["umur"] = 21
print(" ")
for x in pelanggan:
    print(x) #key
    print(pelanggan[x]) #value dari key tersebut
    print(pelanggan_2[x])
print(" ")
daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)
print(" ")
print(daftar_pelanggan)
print(" ")
for pelanggan in daftar_pelanggan:
    print("Nama: {}".format(pelanggan['nama']))
    print("Umur: {}".format(pelanggan['umur']))

print(" ")
print("Function Operation")
print(" ")

def my_function(a,b):
    print("Halo " +a + " " + b)
my_function("haha","hihi")


print(" ")
print("Function Example")
print(" ")

nama_buah = []

def tambah_nama_buah(nama):
    nama_buah.append(nama)

def print_nama_buah():
    for buah in nama_buah:
        print(buah)
    print('----')

tambah_nama_buah("jeruk")
tambah_nama_buah("apel")
tambah_nama_buah("sirsak")

print_nama_buah()

print(" ")
print("Function Operation with default parameter")
print(" ")

def hai(first_name, last_name="abdul"):
    print("Halo " +first_name + " " +last_name)

hai("koko")

print(" ")
print("Function Operation with keyword parameter")
print(" ")



print(" ")
print("Function Return Value Operation")
print(" ")

def tambah(n,m):
    tambah = n + m
    return tambah

hasil = tambah(2,9)
print(hasil)