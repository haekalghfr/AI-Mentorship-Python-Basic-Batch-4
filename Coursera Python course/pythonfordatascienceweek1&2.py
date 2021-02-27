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
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2))) #tuple ga bisa diubah 
#tuple pake () kalo list pake [] kalo sets pake {}
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

print(" ")
print("Set operation")
print(" ")

set1={"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"} #walaupun ada beberapa item yang sama
#yang keluar bakal gaada yang sama
album_list =[ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]

album_set = set(album_list)    #conveert list to set (the duplicate from the list will be removed)
print(album_set)

Aset = set(["Thriller","Back in Black", "AC/DC"] )
Aset.add("NSYNC") #nambahin data ke dalam set (pakenya add bukan append)
Aset.remove("Thriller") #remove data di set (pakenya remove)
print("AC/DC" in Aset) #ngecheck value ada ga di set nya


album_set1 = set(["Thriller",'AC/DC', 'Back in Black'] )
album_set2 = set([ "AC/DC","Back in Black", "The Dark Side of the Moon"] )
album_set_3 = album_set1 & album_set2 #gabungin kedua set tapi set yang baru cuman 
#data yang ada di set3 itu data yang ada di kedua set1 dan set2
print(album_set_3)
print(" ")
print(album_set1.difference(album_set2))
print(" ")
print(album_set1.union(album_set2)) #nampilin semua data dialbum set1 dan 2
print(" ")
print(album_set_3.issubset(album_set1)) #ngecheck kalo album set 3 itu subset album set 1

print(len(List2[0]))