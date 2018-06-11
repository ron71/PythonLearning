# for i in range(17):
#     print("{0:2} in binary : {0:>02x}".format(i))
#
# # binary
# binaryNumber = 0b0101010111
# print(binaryNumber)
#
# octalNumber = 0o1234567
# print(octalNumber)
#
# hexadecimal = 0xfeabcd
# print(hexadecimal)
#
# a = hex(13)
# b = hex(2)
# print(a-b)          # Error aas the both return hexadecimal values in 0x format


# Challenge : decimal to binary

decimalNumber = int(input("Please enter no less than 65535"))
num = decimalNumber
powers = []
for i in range(15, -1, -1):
    powers.append(2**i)
print(powers)

# WE will divide (Integer division) the no by the greatest power of 2 and then continue this on remainder of it.
binary = ''

for power in powers:
    binary += str(decimalNumber // power)
    decimalNumber %= power

print("{0} in binary : {1}".format(num, binary))

# Challenge : decimal to octal

decimalNumber = num
powers = []
for i in range(7, -1, -1):
    powers.append(8**i)
print(powers)

octal = ""
for power in powers:
    octal += str(decimalNumber // power)
    decimalNumber %= power

print("{0} in octal : {1}".format(num, octal))

# Challenge : Decimal to Hexadecimal

decimalNumber = num

powers = []
for i in range(3, -1, -1):
    powers.append(16**i)
print(powers)

code = ['a', 'b', 'c', 'd', 'e', 'f']

hexadecimal = ''

for power in powers:
    c = decimalNumber // power
    if c > 9:
        hexadecimal += code[c-10]
    else:
        hexadecimal += str(c)
    decimalNumber %= power

print("{0} in Hexadecimal : {1}".format(num, hexadecimal))


