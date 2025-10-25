
text = "Python Programming Is {Great }"
text = text.lower()

alphabets = [0] * 26
base_number = ord('a')

for letter in text:
    index = ord(letter) - base_number
    if 0 <= index < len(alphabets):
        alphabets[index] += 1

print(alphabets)
for i in range(len(alphabets)):
    char = chr(i + base_number)
    print(f"{char}: {alphabets[i]}")

