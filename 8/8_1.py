import random
import string

symbols = string.ascii_letters + string.digits + string.punctuation
password = []

for i in range(1, 12):
    password.append(random.choice(symbols))

password = ''.join(password)

with open('password.txt', 'w') as file:
    file.write(password)
