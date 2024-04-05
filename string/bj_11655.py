string = input()
result = ""

for letter in string:
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        change = ord(letter) + 13
        if change > ord('z'):
            change = ord('a') + (change - ord('z')) - 1
    elif ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
        change = ord(letter) + 13
        if change > ord('Z'):
            change = ord('A') + (change - ord('Z')) - 1
    else:
        change = ord(letter)
        
    result += chr(change)
print(result)