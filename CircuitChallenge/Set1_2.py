# Plus Plus
# Max. Marks: 100
#
# You are given a two dimensional grid A of size n x m ( n rows and m columns).
# Your task is to select two non overlapping Plus signs from the grid and do multiplication with corresponding elements
# and find out summation. What is the maximum summation.
#
# Note: The Plus sign will be formed by 5 cells which have coordinates of form(x,y),(x-1,y),(x+1,y),(x,y-1),(x,y+1).
# The center of the Plus sign cannot lie on boundary of the grid.Over lapping Plus signs would have at least one cell in
# common. Please, see the explanation below for exact figure.
#
# INPUT
#
# First line contains two space separated integers n and m, denoting size of array A.
# Next n lines contains m space separated integers.
#
# OUTPUT
#
# Print the required maximum value.
#
# Constraints:
#
# 6<=n and m<=50
# 0<=a[i,j]<=9
#
# SAMPLE INPUT
#
# 6 6
# 4 0 8 4 3 0
# 7 8 3 4 7 4
# 9 2 6 0 5 8
# 2 0 6 3 9 7
# 1 5 0 5 6 3
# 5 0 0 0 4 1
#
# SAMPLE OUTPUT
#
# 166
#
# Explanation
#
# Maximum value can be obtained if we select two Plus signs centered at (2,3) and (5,5),
# which are represented by yellow and green color in following diagram. Note, these plus signs are non overlapping
# because every no cell is shared by different color's plus sign.
#
# 3 * 6 + 8 * 9 + 6 * 4 + 8 * 5 + 8 * 3 = 178
# Summation: 8.9+8.5+3.6+4.3+6.4 =  166.


dimension = input()
dimension = dimension.split(" ")

print(dimension)

matrix = list()

for i in range(int(dimension[0])):
    dataOfOneRowInFormOfString = input()
    matrix.append(list(dataOfOneRowInFormOfString.split(" ")))
    #dataOfOneRowInFormOfString = dataOfOneRowInFormOfString.split(" ")
    #dataOfOneRow = list()
    # print(dataOfOneRow)
    #for j in dataOfOneRowInFormOfString:
     #   dataOfOneRow.append(int(j))
    #matrix.append(dataOfOneRow)
#print(matrix)
sum = 0

for i in range(1, (len(matrix)-1)):
    for j in range(1, len(matrix[i])-1):

        firstPlus = [[i, j], [i-1, j], [i+1, j], [i, j-1], [i, j+1]]             #   (x,y),(x-1,y),(x+1,y),(x,y-1),(x,y+1)

        for ii in range(1, (len(matrix)-1)):
            for jj in range(1, len(matrix[i])-1):

                secondPlus = [[ii, jj], [ii-1, jj], [ii+1, jj], [ii, jj-1], [ii, jj+1]]

                check = False
                for k in firstPlus:                 # Checking for Non Overlapping
                    if k not in secondPlus:
                        check = True
                    else:
                        check = False
                        break

                if check:
                   # print("\n\nFIRST PLUS : {0}\nSECOND PLUS : {1}\n".format(firstPlus, secondPlus))
                    tempSum = int(matrix[i][j]) * int(matrix[ii][jj]) + int(matrix[i-1][j]) * int(matrix[ii-1][jj]) + int(matrix[i+1][j]) * int(matrix[ii+1][jj]) + int(matrix[i][j-1]) * int(matrix[ii][jj-1]) + int(matrix[i][j+1]) * int(matrix[ii][jj+1])
                  #  print("{0} * {1} + {2} * {3} + {4} * {5} + {6} * {7} + {8} * {9} = {10}"
                        #  .format(matrix[i][j], matrix[ii][jj], matrix[i-1][j], matrix[ii-1][jj], matrix[i+1][j], matrix[ii+1][jj], matrix[i][j-1], matrix[ii][jj-1],  matrix[i][j-1], matrix[ii][jj+1], tempSum))

        if tempSum > sum:
            sum = tempSum

print(sum)