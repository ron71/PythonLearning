
usersInput = input("ENTER YOUR TEXT")

vowels = frozenset(['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U'])
# print(vowels)

usersInput = set(usersInput)

non_vowels = usersInput.difference(vowels)
if len(non_vowels) == 0:
    print("You entered only vowels, that so mean!")
else:
    output = ''
    for char in sorted(non_vowels):
        output+=char
    print(output)