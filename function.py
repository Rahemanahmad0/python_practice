import math as m
#[function using parameters]
# def sum(a,b):
#  return a+b

# a=int(input("Enter value in a="))
# b=int(input("Enter value in b=23"))

# c=sum(a,b)
# print(c)


# [function using polymorphism]

# def sum(a,b):
#  return a+b

# a=input("Enter value in a=")
# b=input("Enter value in b=")

# c=sum(a,b)
# print(c)
# c1=sum('a',b)
# print(c1)


#[retutn multiple value in python]

# def area_circum(rad):
#     area = m.pi * rad * rad
#     circum = 2 * m.pi * rad

#     return area,circum


# rad=int(input("Enter radius of cirle="))
# area,circum=area_circum(rad)

# print(area,circum)


#[write a function if it will pass it will show or else it will show default answer]

# def display(name="raheman"):

#  return ("hello" +" " +name)

# print(display("chai"))
# print(display())


#[lambda fucntion or (anonymous function)]   
# ==> Its useful when we are writing some complex function 
# and we want to write a function in short we can use this

# cube=lambda  x,y:x *y*2

# print(cube(3,4))

# we can do the same work using function as well 
# but lambda usecase normally happen in frameworks like django
 
 
#  kwargs[keywords_arguments]


# def kw_args(name,power):
#     print(f"Hello {name} your power is {power}")
    

# kw_args(power="laser",name="Raheman")
                                                       
# its not professional way
   
#[ normally we use positional arguments but here we are using keyword arguments]
 
# { better way for kwargs}

def kw_args(**kwargs):
   for key,value in kwargs.items():
       print(f"{key}: {value}")
       
    

kw_args(power="laser",name="Raheman")

# generate range and print it

# for i in range(1,10,2):   
    #here 1 is starting value,
    # 10 will be end limiut it will go upto 10-1
    # and 2 will be gap means 1+2=3,3+2=5 will print like this
    
    # print(i)
    
    # difference between yield and return 
    
    # After returning a value it exit fom the function
    
    # but yield we use to return series of value from a function over a time and 
    # we use it to conserve a memory
    
    
def even_gen(num):
        for i in range(num):
         if(i%2==0):
            yield i
            

for num in even_gen(10):           
 print(num)
 
 
 
