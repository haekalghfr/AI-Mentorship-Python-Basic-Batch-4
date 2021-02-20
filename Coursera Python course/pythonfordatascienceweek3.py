print('boolean operation')
print(' ')

# '!=' means not equal to
# jadi misal i=6 
#  i!=6 
#jawabannya false karena i equal to 6

age=int(input("input your age "))
if age>18:
    
    print("you can enter" )
elif age==18:
    print("go see Pink Floyd")
else: #misalnya ga memenuhi kondisi yang diatas
    print("go see Meat Loaf" )
    
print("move on")

print(" ")

album_year = int(input("Input Album Year "))
if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

print(" ")

photo_year = int(input("Input Photo Year "))
if(photo_year > 1979) and (photo_year < 1990):
    print ("Album year was in between 1981 and 1989")
else:
    print("The Album was made in the 1980's ")

print(" ")
single_year = int(input("Input Single Year "))

if not (single_year == '1984'):
    print ("Album year is not 1984")
else:
    print ("Album year is  1984")

print(' ')
print('Loop operation')
print(' ')

dates = [1982,1980,1973]

for date in dates:
     
    print(date)  

print(' ')

datess = [1982,1980,1973]
N =len(datess)

for i in range(N):
     
    print(datess[i])  

print(' ')

squares=['red','yellow','green','purple','blue ']

for c in range(0,5):
    print("Before Loop square ",c, 'is',  squares[c])
    
    squares[c]='Light'
    
    print("After Loop square ",c, 'is',  squares[c])

colours = ['red','yellow','green','purple','blue ']

print(' ')

for d,colour in enumerate(colours):
    print(d,colour)

print(' ')

tanggal2 = [1982,1980,1973,2000]

n=0
tahun=0
while(tahun!=1973): #loop bakal muter terus sampe nemu kondisi yang gasesuai syarat yaitu tahun ga boleh = 1973
    tahun=tanggal2[n]
    n=n+1
    print(tahun)
    
    
print("it took ", n ,"repetitions to get out of loop")

