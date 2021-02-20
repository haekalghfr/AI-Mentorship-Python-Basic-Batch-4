print(" ")
print("For Loop Function")
print(" ")
namabuah = ["apel", "jeruk ", "mangga"]

for buah in namabuah:
    print(buah)

print(" ")
print("Range Function")
print(" ")

for ind in range(0,6,2): #range(angka mula, sebelum angka akhir (panjang), step)
    print(ind)

print(" ")
print("Loop Program")
print(" ")

countt = int(input("Number of Data: "))

nama_pelanggan = []
umur_pelanggan = []

for i in range(countt):
    print("Data ke {}".format(i+1))
    nama = input("Nama : ")
    umur = int(input("Umur : "))

    nama_pelanggan.append(nama)
    umur_pelanggan.append(umur)

print(nama_pelanggan)
print(umur_pelanggan)

for ii in range(len(nama_pelanggan)):
    print("Pelanggan {} Berumur {}".format(nama_pelanggan[ii], umur_pelanggan[ii]))

print(" ")
print("While Loop Function")
print(" ")

a = 1

while a < 6:
    print(a)
    a = a + 1

print(" ")
print("Continue Loop Function")
print(" ")

for n in range(5):
    if n ==1: #nilai index = 1 ga keluar langsung diskip
        continue
    print(n)

for nn in range(10): #buat memfilter bilangan genap
    if nn %2 == 0:
        continue
    print(nn)

print(" ")
print("Break Loop Function")
print(" ")

for m in range(5):
    if m ==3:
        break
    print(m)

print(" ")

text = input("input text : ")

while True:
    if text == "stop":
        print("program has stopped")
        break
    print("text : {}".format(text))
    text = input("input another text : ")

