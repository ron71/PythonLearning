# Exercise 12.4
# Count how often each letter occurs in a string (case-insensitively). You can
# ignore every character that is not a letter. Print the letters with their counts, in order from
# highest count to lowest count.

letters = list()
for i in range(65,91):
    letters.append([0, chr(i).upper()])

for i in range(65,91):
    letters.append([0, chr(i).lower()])          # chr()---> converts ascii into letters

userData = input("Enter your Text")

for char in userData:
    for letter in letters:
        if char in letter:
            letter[0] +=1
print(sorted(letters, reverse=True))