def bank(x, y): # x - сумма вклада, y - кол-во лет
    proc = 0.1 # 10% годовых
    for a in range(y):
        x += (x * proc)
    return x

x = 100000
y = 5
print(round(bank(x, y), 2))