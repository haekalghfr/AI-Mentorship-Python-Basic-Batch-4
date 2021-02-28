print(" ")
print("File Handling Operation")
print(" ")

"r" # ini read digunakan untuk menjalankan program file dengan menggunakan argumen
"a" # ini append untuk menambahin sesuatu yang baru ke sebuah file
"w" # ini write kalo dipake ini data disebuah file bakal di overwrite dgn argumen yg dituliskan
"c" # 

print(" ")
print("Append file Operation")
print(" ")

f = open("file.txt", "a") #parameter pertama nama file nya, kedua operasi yg dilakukan
#ini misalnya kita run bakal ngebuat file dgn nama file dengan format .txt
#ngebuat file.txt soalnya belom ada di file kita kalo udah ada lgsg
#masuk ke argumen selanjutnya
f.write("Added new text \n") #ini adalah text yang ada didalam file 
#yang baru dibuat
f.close() #ini untuk menutup argumen diatas
#kayak kita buka buku makanya argumen pertama open
#lalu yang terakhir musti kasih argumen close karena kita nutup buku trsbt

