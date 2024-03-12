# Case-study #3
# Developers: General Popov, Egor A.

import local


print(local.tax_cat)
tax_var = int(input())
match tax_var:
    case 1:
        single()
    case 2:
        duo()
    case 3:
        one_parent()
    case _:
        print(local.choice_error)


