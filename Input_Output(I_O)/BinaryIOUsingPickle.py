# Concept of Serialization:
# In Java it is used to store an object in file using 'Serializable' keyword.
# In Python same concept is known as if Pickling to serialize an object:
# So when an object is pickled it is written in file in format that contains object data together
# with sufficient information (metadata) to allow that object to be re-created when it is loaded back in.
import pickle

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4,"Kentish Town Waltz"))
even = list(range(0,21,2))
odd = list(range(1,21,2))
# To write the object in pickle file File dump(object, pickleFile) method is used and it is a static method
with open('imelda.pickle','bw') as pickleFile:
    pickle.dump(imelda,pickleFile, 0)
    pickle.dump(even,pickleFile,protocol= pickle.HIGHEST_PROTOCOL)
    pickle.dump(odd,pickleFile, protocol= pickle.DEFAULT_PROTOCOL)

# To restore we use load(pickle Filename) method, and it as also static method

with open('imelda.pickle','br') as pickleFile:
    imelda2 = pickle.load(pickleFile)
    even = pickle.load(pickleFile)
    odd = pickle.load(pickleFile)

print(imelda2)
print(even)
print(odd)

# Protocols are the set rule rules using which we want to keep our object in file.
# The most update protocol in python in version 4 in Python 3.4
# Important :  newer protocols cannot be used by older versions of Python
#
# ImportWarning : donot work with pickle files fronm unknown sources for example
# internet it can cause damage to file system
