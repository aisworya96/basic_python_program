# counting vowels in given words

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Aisworya panda"
count = 0
for character in word:
    if character in vowels:
        count += 1
print (count)

# counting consonent in given word
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Aisworya panda"
count = 0
for character in word:
    if character not in vowels:
        count += 1
print (count)
