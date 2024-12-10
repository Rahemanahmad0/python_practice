# print("hello")

# def sum():
#     print(4+5)
# sum()


# CODE FOR THIS OUTPUT
# *
# **
# ***
# ****
# *****

# for x in range(5):
#     for y in range(5):
#         if x >= y :
#             print("* ",end="")
#     print()
    
    
    # *****
    # *   *
    # *   *
    # *****
    
val=5
for x in range(val):
        if x==0 or x==val-1:
          print("* " * val) 
        else :
         for k in range(val):
             if k==0 or k==val-1:
                print("*",end=" ")
             else:
                print(" ", end=" ")
         print()

# [optimised code of it]
val = 5

# for x in range(val):
#     if x == 0 or x == val - 1:
#         print("* " * val)  # Print the entire line of stars for the first and last rows
#     else:
#         print("*" + " " * (2 * (val - 1) - 3) + "*")  # Print '*' with spaces in between for middle rows



# 1 2 3 4
# 1 2 3
# 1 2
# 1

# val=4
# for i in range(val):
#   for j in range(val-i):
#     print(j+1,end=" ")
#   print()
    

val = 5  # Example value, change as needed

for i in range(val):
    if (i + 1) % 2 != 0:  # Check if row is odd (1-based index)
        for j in range(val - i):
            print(i + j + 1, end=" ")
        print()
    else:  # For even rows
        print(" " * i, end="")  # Indentation for even rows
        for k in range(val - i):
            print(i + k + 1, end=" ")
        print()
