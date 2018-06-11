# Binary file are used to store image files, videos etc
# Therefore Any thing to be stored must be converted into format called 'Bytes' first
with open('binary','bw') as binaryFile:
    for i in range(17):
        binaryFile.write(bytes([i]))        # NOTE bytes() take list as argument

with open('binary','br') as binaryFile:
    for bin in binaryFile:
        print(bin)
# b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'
# b'\x0b\x0c\r\x0e\x0f\x10'

# here above we can see all output is in hexadecimal as Python 3 supports UNICODE characters
# We can observe number in when converted in bytes returns '\t', no 10 gives '\n'.
# NOte: \x07 is a bell character, we can observe by typing--> type <filename> in cmd OR cat <filename> in linux

a = 65534           # FF FE
b = 65535           # FF FF
c = 65536           # 00 01 00 00
d = 2998302         # 02 2D C0 1E

with open('binary2','bw') as binFile:
    binFile.write(a.to_bytes(2, 'big'))
    binFile.write(b.to_bytes(2, 'big'))
    binFile.write(c.to_bytes(4, 'big'))
    binFile.write(d.to_bytes(4, 'big'))
    binFile.write(d.to_bytes(4, 'little'))

# to_bytes(size, architecture) :
# This function is used to convert integers into bytes. It has two parameter size, architecture
# size specifies no of bytes so largest no that can be stored in 16 bit(2 bytes) is 65535
# architecture: 'big' represents Big Endian i.e. highest significant byte will be stored first
#               'little' represents little Endian i.e. lowest significant byte will be stored first

with open('binary2','br') as binFile:
    e = int.from_bytes(binFile.read(2),'big')           # O/P--> 65534
    print(e)
    f = int.from_bytes(binFile.read(2),'big')           # O/P--> 65535
    print(f)
    g = int.from_bytes(binFile.read(4),'big')           # O/P--> 65536
    print(g)
    h = int.from_bytes(binFile.read(4),'big')           # O/P--> 2998302
    print(h)
    i = int.from_bytes(binFile.read(4),'big')           # O/P--> 515910912
    print(i)        # We can observe the no is not same,
    # this is because we stored no in little endian and retrieving it in big endian

