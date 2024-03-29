# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru

MAX_MONTH = 12


def annual_income():
    """
    The function determines the amount of annual income.
    """
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.INCOME} {ru.NAME[month]} [USD]: '))
        amount += value
    return amount


def free_tax():
    """
    The function determines the annual tax-free amount.
    """
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.TEXT_FREE_TAX} {ru.NAME[month]} [USD]: '))
        amount += value
    return amount


def subject(revenue_tax):
    """
    The function determines tax of subject.
    """
    if revenue_tax < 9076:
        tax = 0.1 * revenue_tax
        return tax
    elif revenue_tax < 36901:
        tax = 0.1 * 9075 + 0.15 * (revenue_tax - 9076)
        return tax
    elif revenue_tax < 89351:
        tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * (revenue_tax - 36901)
        return tax
    elif revenue_tax < 186351:
        tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * 52450 + 0.28 * (revenue_tax - 89351)
        return tax
    elif revenue_tax < 405101:
        tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * 52450 + 0.28 * 97000 + 0.33 * (revenue_tax - 186351)
        return tax
    elif revenue_tax < 406751:
        tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * 52450 + 0.28 * 97_000 + 0.33 * 218750 + 0.35 * (
                    revenue_tax - 405101)
        return tax
    else:
        tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * 52450 + 0.28 * 97000 + 0.33 * 218750 + 0.35 * 1650 + 0.396 * (
                revenue_tax - 406751)
        return tax


def couple(revenue_tax):
    """
    The function determines tax of couple.
    """
    if revenue_tax < 18151:
        tax = 0.1 * revenue_tax
        return tax
    elif revenue_tax < 73801:
        tax = 0.1 * 18150 + 0.15 * (revenue_tax - 18151)
        return tax
    elif revenue_tax < 148851:
        tax = 0.1 * 18150 + 0.15 * 55650 + 0.25 * (revenue_tax - 73801)
        return tax
    elif revenue_tax < 226851:
        tax = 0.1 * 18150 + 0.15 * 55650 + 0.25 * 75050 + 0.28 * (revenue_tax - 148851)
        return tax
    elif revenue_tax < 405101:
        tax = 0.1 * 18150 + 0.15 * 55650 + 0.25 * 75050 + 0.28 * 78000 + 0.33 * (revenue_tax - 226851)
        return tax
    elif revenue_tax < 457601:
        tax = 0.1 * 18_150 + 0.15 * 55650 + 0.25 * 75050 + 0.28 * 78000 + 0.33 * 178250 + 0.35 * (revenue_tax - 405101)
        return tax
    else:
        tax = (0.1 * 18150 + 0.15 * 55650 + 0.25 * 75050 + 0.28 * 78000 + 0.33 * 178250 + 0.35 * 52500 + 0.396 * (
                revenue_tax - 457601))
        return tax


def parent(revenue_tax):
    """
    The function determines tax of parent.
    """
    if revenue_tax < 12951:
        tax = 0.1 * revenue_tax
        return tax
    elif revenue_tax < 49401:
        tax = 0.1 * 12950 + 0.15 * (revenue_tax - 12951)
        return tax
    elif revenue_tax < 127551:
        tax = 0.1 * 12950 + 0.15 * 36450 + 0.25 * (revenue_tax - 49401)
        return tax
    elif revenue_tax < 206601:
        tax = 0.1 * 12950 + 0.15 * 36450 + 0.25 * 78150 + 0.28 * (revenue_tax - 127551)
        return tax
    elif revenue_tax < 405101:
        tax = 0.1 * 12950 + 0.15 * 36450 + 0.25 * 78150 + 0.28 * 79050 + 0.33 * (revenue_tax - 206601)
        return tax
    elif revenue_tax < 432201:
        tax = 0.1 * 12950 + 0.15 * 36450 + 0.25 * 78150 + 0.28 * 79050 + 0.33 * 198500 + 0.35 * (
                revenue_tax - 405101)
        return tax
    else:
        tax = (0.1 * 12950 + 0.15 * 36450 + 0.25 * 78150 + 0.28 * 79050 + 0.33 * 198500 + 0.35 * 27100 + 0.396 * (
                revenue_tax - 432201))
        return tax


def main():
    """
    Main function.
    :return: None
    """

    grade = int(input(f'{ru.CATEGORY}\n1.{ru.ALONE}\n2.{ru.FAMILY}\n3.{ru.SINGLE}\n{ru.GRADE}'))
    print(ru.ANNUAL_INCOME)
    revenue = annual_income()
    print(f'{ru.ANNUAL_INCOME_SUM} ${revenue}')
    print(ru.FREE_TAX)
    revenue_no_tax = free_tax()
    revenue_tax = revenue - revenue_no_tax
    print(f'{ru.FINAL_FREE_TAX} ${revenue_no_tax}\n{ru.TAXABLE} ${revenue_tax}')
    if grade == 1:
        tax = subject(revenue_tax)
        print(f'{ru.TAX} ${round(tax, 2)}')
        print(f'{ru.MOUNTHLY_TAX} ${round((tax / 12), 2)}')
    elif grade == 2:
        tax = couple(revenue_tax)
        print(f'{ru.TAX} ${round(tax, 2)}')
        print(f'{ru.MOUNTHLY_TAX} ${round((tax / 12), 2)}')
    else:
        tax = parent(revenue_tax)
        print(f'{ru.TAX} ${round(tax, 2)}')
        print(f'{ru.MOUNTHLY_TAX} ${round((tax / 12), 2)}')


if __name__ == '__main__':
    main()
