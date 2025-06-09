with open('text.txt', 'r') as file:
    words = file.read()
count = len(words.split())
print(count)
