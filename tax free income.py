import local as l
def TF_income():
    print(f'{l.text_tax_free_income}')
    tax_free_amount = 0
    for i in range(0, 12):
        tax_free_value = float(input(f'{l.data_tax_free_income} {l.month[i]} {l.currency}'))
        tax_free_amount += tax_free_value
    return tax_free_amount
