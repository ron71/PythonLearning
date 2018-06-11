#
# Bob and K - Subset
# Max. Marks: 100
#
# You are given an array
# of size  consisting of integers. Now, you need to find the number of distinct integers x,
# such that there exists a sequence of distinct indices i1<i2<....<im and a[i1] or a[i2] or ....or a[im] = x
#
# Here or represents the bitwise OR operator.
#
# Input
#
# First line of the each input will contain two space seperated integers n and k
# denoting the size of the array and maximum size of the subset, respectively.
#
# Next line will contain n spaced integers denoting elements of the array.
#
# Constraint
#
# 1 <= n <= 1000
# 1 <= k <= 20
# 1 <= a[i] < 2^11
#
# Output
#
# Output will consists of a single integer denoting the number of unique integers
#  that can be formed by taking Bitwise OR of every subset of size less than or equal to k.
#
# SAMPLE INPUT
#
# 3 2
# 1 2 4
#
# SAMPLE OUTPUT
#
# 6
#
# Explanation
#
# Array is having 3 integers: 1, 2 and 4.
# Subsets having size less than or equal to 2 is {{1},{2},{4},{1,2},{1,4},{2,4}}
# .
# Bitwise OR of the subsets thus obtained is {1,2,3,4,5,6} .
# Thus total unique intgers formed by taking bitwise OR of all subsets of size less than or equal to 2 is 6.


input1 = input()
input1 += " "
nk = list()

num = ''
for i in input1:
    if i == ' ':
        nk.append(int(num))
        num = ""
    else:
        num += i
# print(nk)

input2 = input()
input2 += " "
arrayOfNumbers = list()

if (nk[0] >= 1 and nk[1] >= 1) and (nk[0] < 1001 and nk[1] < 21):

    count = 0
    for i in input2:
        if count <= nk[0]:
            if i == ' ':
                arrayOfNumbers.append(int(num))
                num = ''
                count += 1
            else:
                num += i

    # print(arrayOfNumbers)

    subset = list()
    for i in arrayOfNumbers:
        subset.append([i])
    # print(subset)

    for i in arrayOfNumbers:
        for j in arrayOfNumbers:
            if i < j:
                subset.append([i, j])
    # print(subset)

    subsetAfterBitwiseOROperator = list()
    for i in subset:
        if len(i) == 2:
            subsetAfterBitwiseOROperator.append(i[0] | i[1])            # Bitwise Operation
        elif len(i) != 2:
            subsetAfterBitwiseOROperator.append(i[0])

    subsetAfterBitwiseOROperator.sort()
    newSubsetAfterBitwiseOROperator = list()
    for i in subsetAfterBitwiseOROperator:
        if i in newSubsetAfterBitwiseOROperator:
            continue
        else:
            newSubsetAfterBitwiseOROperator.append(i)
    #print(newSubsetAfterBitwiseOROperator)
    print(len(newSubsetAfterBitwiseOROperator))


# 5 3
# 3 8 5 6 1
# Output : 11