# Case-study #3
# Developers: General Popov, Egor A.

import local as l
from income import income
from TF_income import TF_income


def single(x):
    if x < 9076:
        sum_tax = x * 0.1  # сумма налога.
    if x >= 9076 and x <= 36900:
        sum_tax = 9075 * 0.1 + 0.15 * (x - 9075)
    else:
        sum_tax = 9075 * 0.1 + 0.15 * (x - 9075 - (x - 36900)) + 0.25 * (
                    x - 36900)  # доп налог только на сумму, что выше предыдущей границы.
        # Поэтому когда нахожу налог 15% беру % сверх верхней границы первого и <= верхней границы второго.
    return sum_tax


def duo(x):  # Аналогично с single(), только границы налогообложения другие.
    if x < 18151:
        sum_tax = x * 0.1
    if x >= 18151 and x <= 73800:
        sum_tax = 18150 * 0.1 + 0.15 * (x - 18150)
    else:
        sum_tax = 18150 * 0.1 + 0.15 * (x - 18150 - (x - 73800)) + 0.25 * (x - 73800)
    print(sum_tax)


def main():
    print(l.tax_cat)  # предлагаю варианты нологооблажения
    tax_var = int(input())  # прошу выбрать тип налогооблажения
    sum = income()  # общая сумма. Сначала приравниваю ее к годовому доходу.
    print(l.sum_income, sum)  # вывожу доход за год
    sum -= TF_income()  # отнимаю из общей суммы необлагаемые налогом суммы
    print(l.sum_TF_income, sum)  # вывожу сумму, облагаемую доходом

    match tax_var:  # можно заменить на | if tax_var == 1: \n single(sum) |
        case 1:
            single(
                sum)  # сумма налога при выборе цифры 1 (субъект). sum в скобках это х в duo(x). От этой суммы считаем налог.
        case 2:
            duo(sum)
        # case 3:
        #     one_parent()
        case _:
            print(l.choice_error)


main()  # вызываю основную функцию, чтобы все заработало
