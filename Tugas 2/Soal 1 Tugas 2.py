print("Selamat Datang!")

print("---Menu--- \n 1. Daftar Kontak \n 2. Tambah Kontak \n 3. Keluar")

print(" ")

a = input("Pilih Menu: ")

nama_kontak = []
nomor_kontak = []


while True:
    if a == "Keluar" or a == "3":
        print("Program Selesai, Sampai Jumpa!")
        print(" ")
        break
    elif a == "Daftar Kontak" or a == "1":
        if len(nama_kontak) >= 1: #misalnya for duluan baru if, else nya ga berfungsi karena statement for nya cuman ke define di if awalnya aja tapi ga ke else
            for ii in range(len(nama_kontak)): #jadi logicnya itu dikasi kondisi dulu jika len nama kontak lebih dari satu maka ngelooping
                print("Nama : {} \nNomor : {} \n".format(nama_kontak[ii], nomor_kontak[ii]))
        else:
            print("Daftar Kontak Kosong")
        print(" ")
    elif a == "Tambah Kontak" or a == "2":
        count = int(input("Berapa Kontak Baru Yang Diinput: "))
        for i in range(count):
            print("Data ke {}".format(i+1))
            nama = input("Nama : ")
            nomor = int(input("Umur : "))
            nama_kontak.append(nama)
            nomor_kontak.append(nomor)
            print(" ")
    else:
        print("Menu Tidak Tersedia")
        print(" ")
    a = input("Pilih Menu yang lain: ")

    






