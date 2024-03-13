def one_parent(x):
    if x < 18151:
        sum_tax = x * 0.1
    if x >= 18151 and x <= 73800:
        sum_tax = 18150 * 0.1 + 0.15 * (x - 18150)
    else:
        sum_tax = 18150 * 0.1 + 0.15 * (x - 18150 - (x - 73800)) + 0.25 * (x - 73800)
    print(sum_tax)