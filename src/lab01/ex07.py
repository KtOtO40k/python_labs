s = input()

# 1. первая заглавная буква — первый символ оригинала
start = next(i for i, ch in enumerate(s) if ch.isupper())
# 3. второй символ стоит сразу после первой цифры
second = next(i for i, ch in enumerate(s) if ch.isdigit()) + 1
# 2. символы расположены с фиксированным шагом
step = second - start

result = ""
for ch in s[start::step]:
    result += ch
    # 4. последний символ оригинала — точка
    if ch == ".":
        break
print(result)
