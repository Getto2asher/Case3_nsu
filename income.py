import local as l

print(f'{l.text_income}')
amount = 0
for i in range(0, 12):
    value = float(input(f'{l.data_income} {l.month[i]} {l.currency}'))
    amount += value
print(amount)
