#Function Definition   
def square(a):
    """Square the input and add one  
    """
    #Local variable 
    b=1
    c=a*a+b
    print(a, "if you square +1 ",c) 
    return(c)

#Initializes Global variable  

x=3
#Makes function call and return function a y
z=square(x)

#If there is no return statement, the function returns None. The following two functions are equivalent

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

print(MJ())
print(MJ1())

def Equation(a,b):
    c=a+b+2*a*b-1
    if(c<0):
        c=0
        
    else:
        c=5
    return(c) 

l=Equation(2,4)
print(l)

def type_of_album(artist,album,year_released):
    if year_released > 1980:
        print(artist,album,year_released)
        return "Modern"
    else:
        print(artist,album,year_released)
        return "Oldie"
    
xx = type_of_album("Michael Jackson","Thriller",1980)
print(xx)


def PrintList(the_list):
    for element in the_list:
        print(element)

PrintList(['1',1,'the man',"abc"])