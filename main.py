# Case-study #3
# Developers: General Popov, Egor A.

import local as l
from income import income
from TF_income import TF_income


def single(x):
    if x < 9076:
        sum_tax = x * 0.1
    if x >= 9076 and x <= 36900:
        sum_tax = 9075 * 0.1 + 0.15 * (x - 9075)
    else:
        sum_tax = 9075 * 0.1 + 0.15 * (x - 9075 - (x - 36900)) + 0.25 * (x - 36900)
    return sum_tax


def duo(x):
    if x < 18151:
        sum_tax = x * 0.1
    if x >= 18151 and x <= 73800:
        sum_tax = 18150 * 0.1 + 0.15 * (x - 18150)
    else:
        sum_tax = 18150 * 0.1 + 0.15 * (x - 18150 - (x - 73800)) + 0.25 * (x - 73800)
    print(sum_tax)


def main():
    print(l.tax_cat)
    tax_var = int(input())
    sum = income()
    print(l.sum_income, sum)
    sum -= TF_income()
    print(l.sum_TF_income, sum)
    match tax_var:
        case 1:
            single(sum)
        case 2:
            duo(sum)
        # case 3:
        #     one_parent()
        case _:
            print(l.choice_error)


main()
