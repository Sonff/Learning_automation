# # row = 5
# # for i in range (row):
# #     for j in range (row):
# #         print("*", end=" ")
# #     print()
    
# # * * * * * 
# # * * * * * 
# # * * * * * 
# # * * * * * 
# # * * * * * 

# # row = 5
# # for i in range (1, row+1 ):
# #     print ("*" * i)

# # *
# # **
# # ***
# # ****
# # *****

# row = 5
# for i in range (row, 0, -1):
#     print ("*" * i)

# # *****
# # ****
# # ***
# # **
# # *


rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):

    # Print spaces
    for j in range(rows - i):
        print(" ", end="")

    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()