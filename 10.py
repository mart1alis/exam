s = input("Введите строку: ")

n = len(s)
t = ''

for i in range(n):
    symbol = s[i]
    symbol_count = s.count(s[i])
    if symbol not in t:
        t = t + symbol
        print(symbol, ' - ', symbol_count)
