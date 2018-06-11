# Iterator is an object that represents a stream of data.
# It returns the actual data in the stream on at a time.

sentence = "Harry and Meghan got married."
for i in sentence:
    print(i)
# Here string sentence implicitly creates a iterator object which is used by for loop
# For loop uses this iterator to call elements of sentence one at a time.
# At the end of the loop Iterator creates an Error which is implicitly handelled by for loop
# Therefore we don't see any error in our o/p
# We can call this iterator object at our will for instance

s = iter(sentence)
print(s)        # O/P-->    <str_iterator object at 0x01A17310>

# Actually s has stored an iterator object which is stored at memory location : '0x01A17310'

print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
# After this if we print , it will cause error.

#   print(next(s))      O/P--> ERROR:StopIteration

# NOTE : Following coed do same:

for i in sentence:
    print(i)
print("*************************")
for i in iter(sentence):
    print(i)

print("*************************")
list1 = list(sentence)
it = iter(list1)
for i in range(len(list1)):
    print(next(it))

