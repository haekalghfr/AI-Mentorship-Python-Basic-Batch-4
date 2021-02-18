NilaiTeori= float(input("Please input Nilai Teori Siswa "))
NilaiPraktek= float(input("Please input Nilai Praktek Siswa "))

if (NilaiTeori>=70) and (NilaiPraktek>=70):
    print("Selamat anda lulus")
elif (NilaiTeori<70) and (NilaiPraktek>=70):
    print("Anda Harus Mengulang Ujian Praktek")
elif (NilaiTeori>=70) and (NilaiPraktek<70):
    print("Anda Harus Mengulang Ujian Teori")
else:
    print("Anda Harus Mengulang Ujian Teori dan Praktek")

print(" ")