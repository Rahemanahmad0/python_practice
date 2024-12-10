# a=input("enter a number")
# print(f"{a}")
# print(type(a))

# print("hello")
# a,b=map(int,input("enter a number").split())

# print(f"first number={a},second number {b}")


# list1=list(map(int,input("enter number in list").split())) 
# print(list1)


#[remove spaces at start and at the end of the string]
# str= "    hello bro how are you ?    "
# print(str.strip())
# we can split a string using split method

size=[1,2,3,4,6]

# for i in size:
#     print(i)
    
# for i in range(len(size)):
#         print(size[i])

list1=[1,2,3,4,4,5,77,77,3]

my_set=set()

for i in list1:
 if i in my_set:
    # print("Duplicate number",i)
    continue
 my_set.add(i)

print(my_set)


list11=[1,2,3,4]
 
#  print(max(list1))
max_nm=max(list11)