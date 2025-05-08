n = 0

while True:
    if (n % 2) == 0:
        n += 1
        continue
    print(f"{n} é ímpar.")
    n += 1
    if n > 99:
        break