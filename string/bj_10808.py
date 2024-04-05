alphabet = []
for i in range(26):
    alphabet.append(0)
    
word = input()

for letter in word:
    alphabet[ord(letter) - ord('a')] += 1
    
print(' '.join(map(str, alphabet)))