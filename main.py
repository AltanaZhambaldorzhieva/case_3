# Case_3
# Developers: Zhambaldorzhieva A., Ryaguzova D., Zaitseva D.
#
import ru_local as ru
MAX_MONTH = 12


def main():
    """
        Main function.
        :return: None
    """

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

    grade = int(input(f'{ru.CATEGORY}\n1.{ru.ALONE}\n2.{ru.FAMILY}\n3.{ru.SINGLE}\n{ru.GRADE}'))
    print(ru.ANNUAL_INCOME)
    print(f'{ru.ANNUAL_INCOME_SUM} ${annual_income()}')
    print(ru.FREE_TAX)
    print(f'{ru.FINAL_FREE_TAX} ${free_tax()}')


if __name__ == '__main__':
    main()
