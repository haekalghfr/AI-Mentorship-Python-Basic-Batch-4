print("Selamat Datang!")

print("---Menu--- \n 1. Daftar Kontak \n 2. Tambah Kontak \n 3. Keluar")

print(" ")

a = input("Pilih Menu: ")

daftar_kontak = []
# nomor_kontak = []

def tambah_kontak(nama, nomor):
    b = {
        "nama" : nama, 
        "nomor" : nomor
        }
    daftar_kontak.append(b)
    # nomor_kontak.append(b)

def tampilkan_kontak ():
    for i in daftar_kontak:
        print('Nama : ' + i["nama"])
        print('Nomor Telpon : ' + i["nomor"])
        return daftar_kontak


while True:
    if a == "Keluar" or a == "3":
        print("Program Selesai, Sampai Jumpa!")
        print(" ")
        break
    elif a == "Daftar Kontak" or a == "1":
        if len(daftar_kontak) >= 1: #misalnya for duluan baru if, else nya ga berfungsi karena statement for nya cuman ke define di if awalnya aja tapi ga ke else
                tampilkan_kontak()
        else:
            print("Daftar Kontak Kosong")
        print(" ")
    elif a == "Tambah Kontak" or a == "2":
            nama = input("Nama : ")
            nomor = (input("Umur : "))
            kontak = tambah_kontak(nama, nomor)
            daftar_kontak.append(kontak)
            print('Kontak berhasil ditambahkan')
            print('')
    else:
        print("Menu Tidak Tersedia")
        print(" ")
    a = input("Pilih Menu yang lain: ")

    






