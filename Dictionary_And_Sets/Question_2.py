# Exercise 14.2
# Write a program that first produces three sets of numbers between 1 and
# 1000, the first all those numbers that are dividable by 3, the second all those numbers that
# are dividable by 7, and the third all those numbers that are dividable by 11. It is easiest
# to do that with list comprehension, but it is not necessary. Now produce sets of all the
# numbers between 1 and 1000 that
# (a) are dividable by 3, 7, and 11,
# (b) are dividable by 3 and 7, but not by 11,
# (c) that are not dividable by 3, 7, or 11. The shortest solution has only one line of code for each of the six sets.
comprehensionList = [i for i in range(1,1001) if i%3==0 ]       # This way of creating list is called comprehension list


numbersDivisibleByThree = set(comprehensionList)
numbersDivisibleBySeven = set([i for i in range(1, 1001) if i % 7 == 0])
numbersDivisibleByEleven = set([i for i in range(1, 1001) if i % 11 == 0])

print(numbersDivisibleByThree.intersection(numbersDivisibleBySeven.intersection(numbersDivisibleByEleven)))

print((numbersDivisibleByThree.intersection(numbersDivisibleBySeven)).difference(numbersDivisibleByEleven))

print((((((numbersDivisibleByEleven.union(numbersDivisibleByThree).union(numbersDivisibleByEleven)))
       .difference(numbersDivisibleByThree)).difference(numbersDivisibleBySeven)).difference(numbersDivisibleByEleven)))


