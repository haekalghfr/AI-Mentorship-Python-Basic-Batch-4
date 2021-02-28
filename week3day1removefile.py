#harus import library os buat ngapus file

import os 
file_path = "file.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(" ")
    print("File " + file_path + " has been deleted")
    print(" ")
else:
    print(" ")
    print("file does not exsist")
    print(" ")

os.remove('file.txt')
