# HW1: 5x5 Drawing THIS
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

rows = 5
num = 1

while num <= rows:
    space = num
#   printing space before stars
    while space < rows:
        print(" ", end =" ")
        space += 1
    l = 1
    # print stars
    while l <= num:
        print("*", end =" ")
        l += 1
    print()
    num += 1

   



    
