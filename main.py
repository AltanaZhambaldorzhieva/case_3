# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru
MAX_MONTH = 12


def free_tax():
    '''
    The function determines the annual tax-free amount.
    '''
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TEXT_FREE_TAX} {ru.NAME[month]} [USD]: '))
        amount += value
    return amount


if __name__ == '__main__':
    main()


