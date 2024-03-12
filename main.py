# Case-study #3
# Developers: General Popov, Egor A.

import local as l
from income import income
from TF_income import TF_income


def single(x):
    sum = income()
    print(l.sum_income)
    sum -= TF_income()
    print(l.sum_TF_income)
    x = int(x)
    if x < 9076:
        sum_tax = x * 0.1
    if x >= 9076 and x <= 36900:
        sum_tax = 9075 * 0.1 + 0.15 * (x - 9075)
    else:
        sum_tax = 9075 * 0.1 + 0.15 * (x - 9075 - (x - 36900)) + 0.25 * (x - 36900)
    return sum_tax


# print(l.tax_cat)
# tax_var = int(input())
# match tax_var:
#     case 1:
#         single()
#     case 2:
#         duo()
#     case 3:
#         one_parent()
#     case _:
#         print(l.choice_error)
