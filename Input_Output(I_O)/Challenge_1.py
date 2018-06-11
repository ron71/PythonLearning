# Append tables till 12 in 'sample.txt'

with open('sample', 'ta') as file1:
    print("\n", file = file1)
    for i in range(1,13):
        for j in range(1,11):
            print('{0} X {1} = {2}'.format(i,j,i*j),file=file1)
        print('*'*80, file=file1)



with open('sample', 'r') as file1:
    for lines in file1:
         print(lines,end='')
#
# for i in range(1,13):
#     for j in range(1,11):
#          print('{0} X {1} = {2}'.format(i,j,i*j))
#     print("jjj"*19)