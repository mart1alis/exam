import string

with open('password.txt', 'r') as file:
    password = file.read()

def check(password):
    if not any(c in string.ascii_uppercase for c in password):
        print("Пароль должен содержать хотя бы одну заглавную букву")
        return False
    if not any(c in string.ascii_lowercase for c in password):
        print("Пароль должен содержать хотя бы одну строчную букву")
        return False
    if not any(c in string.digits for c in password):
        print("Пароль должен содержать хотя бы одну цифру")
        return False
    if not any(c in string.punctuation for c in password):
        print("Пароль должен содержать хотя бы один спецсимвол")
        return False
    if len(password) < 8:
        print("Пароль должен быть длиной не менее 8 символов")
        return False
if check(password) != False:
    print("Пароль соответствует требованиям")




