# Case-study #3
# Developers: General Popov, Egor A.

import local as l
from income import income
from TF_income import TF_income


def single(x):
    sum_tax = 0
    if x <= 9075:
        sum_tax = x * 0.1
    elif 9076 >= x <= 36900:
        sum_tax = 9075 * 0.1 + (x - 9076) * 0.15
    elif 36901 >= x <= 89350:
        sum_tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (x - 36901) * 0.25
    elif 89351 >= x <= 186350:
        sum_tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 36901) * 0.25 + (x - 89351) * 0.28
    elif 186351 >= x <= 405100:
        sum_tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 36901) * 0.25 + (186350 - 89351) * 0.28 + (
                x - 186351) * 0.33
    elif 405101 >= x <= 406750:
        sum_tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 36901) * 0.25 + (186350 - 89351) * 0.28 + (
                405100 - 186351) * 0.33 + (x - 405101) * 0.35
    elif x >= 406751:
        sum_tax = 9075 * 0.1 + (36900 - 9076) * 0.15 + (89350 - 36901) * 0.25 + (186350 - 89351) * 0.28 + (
                405100 - 186351) * 0.33 + (406750 - 405101) * 0.35 + (x - 406751) * 0.396
    print(l.sum_tax, sum_tax, l.currency)
    print(l.m_sum_tax, sum_tax / 12, l.currency)


def duo(x):
    sum_tax = 0
    if x <= 18150:
        sum_tax = x * 0.1
    elif 18151 >= x <= 73800:
        sum_tax = 18150 * 0.1 + (x - 18151) * 0.15
    elif 73801 >= x <= 148850:
        sum_tax = 18150 * 0.1 + (73800 - 18151) * 0.15 + (x - 73801) * 0.25
    elif 148851 >= x <= 226850:
        sum_tax = 18150 * 0.1 + (73800 - 18151) * 0.15 + (148850 - 73801) * 0.25 + (x - 148851) * 0.28
    elif 226851 >= x <= 405100:
        sum_tax = 18150 * 0.1 + (73800 - 18151) * 0.15 + (148850 - 73801) * 0.25 + (226850 - 148851) * 0.28 + (
                x - 226851) * 0.33
    elif 405101 >= x <= 457600:
        sum_tax = 18150 * 0.1 + (73800 - 18151) * 0.15 + (148850 - 73801) * 0.25 + (226850 - 148851) * 0.28 + (
                405100 - 226851) * 0.33 + (x - 405101) * 0.35
    elif x >= 457601:
        sum_tax = 18150 * 0.1 + (73800 - 18151) * 0.15 + (148850 - 73801) * 0.25 + (226850 - 148851) * 0.28 + (
                405100 - 226851) * 0.33 + (457600 - 405101) * 0.35 + (x - 457601) * 0.396
    print(l.sum_tax, sum_tax, l.currency)
    print(l.m_sum_tax, sum_tax / 12, l.currency)


def one_parent(x):
    sum_tax = 0
    if x <= 12950:
        sum_tax = x * 0.1
    elif 12951 >= x <= 49400:
        sum_tax = 12950 * 0.1 + (x - 12951) * 0.15
    elif 49401 >= x <= 127550:
        sum_tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (x - 49401) * 0.25
    elif 127551 >= x <= 206600:
        sum_tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (x - 127551) * 0.28
    elif 206601 >= x <= 405100:
        sum_tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (206600 - 127551) * 0.28 + (
                x - 206601) * 0.33
    elif 405101 >= x <= 432200:
        sum_tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (206600 - 127551) * 0.28 + (
                405100 - 206601) * 0.33 + (x - 405101) * 0.35
    elif x >= 432201:
        sum_tax = 12950 * 0.1 + (49400 - 12951) * 0.15 + (127550 - 49401) * 0.25 + (206600 - 127551) * 0.28 + (
                405100 - 206601) * 0.33 + (432200 - 405101) * 0.35 + (x - 432201) * 0.396
    print(l.sum_tax, sum_tax, l.currency)
    print(l.m_sum_tax, sum_tax / 12, l.currency)


def main():
    print(l.tax_cat)
    tax_var = int(input())
    sum = income()
    print(l.sum_income, sum)
    a = int(TF_income())
    sum -= a
    print(l.sum_TF_income, a)
    print(l.sum_t, sum)

    match tax_var:
        case 1:
            single(sum)
        case 2:
            duo(sum)
        case 3:
            one_parent(sum)
        case _:
            print(l.choice_error)


main()
