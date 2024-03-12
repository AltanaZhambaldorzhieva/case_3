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
        global amount1
        amount1 = 0
        for month in range(1, MAX_MONTH + 1):
            value = float(input(f'{ru.INCOME} {ru.NAME[month]} [USD]: '))
            amount1 += value
        return amount1

    def free_tax():
        """
        The function determines the annual tax-free amount.
        """
        global amount2
        amount2 = 0
        for month in range(1, MAX_MONTH + 1):
            value = float(input(f'{ru.TEXT_FREE_TAX} {ru.NAME[month]} [USD]: '))
            amount2 += value
        return amount2

    revenue_tax = (amount1 - amount2)

    def subject(revenue_tax):
        """
            The function determines tax of subject.
        """
        if revenue_tax < 9076:
            tax = 0.1 * revenue_tax
            return tax
        elif revenue_tax < 36901:
            tax = 0.1 * 9075 + 0.15 * (revenue_tax - 9075)
            return tax
        elif revenue_tax < 89351:
            tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * (revenue_tax - 36900)
            return tax
        elif revenue_tax < 186351:
            tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * 52450 + 0.28 * (revenue_tax - 89350)
            return tax
        elif revenue_tax < 405101:
            tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * 52450 + 0.28 * 97000 + 0.33 * (revenue_tax - 186350)
            return tax
        elif revenue_tax < 406_751:
            tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * 52450 + 0.28 * 97_000 + 0.33 * 218750 + 0.35 * (
                        revenue_tax - 405100)
            return tax
        else:
            tax = 0.1 * 9075 + 0.15 * 27825 + 0.25 * 52450 + 0.28 * 97000 + 0.33 * 218750 + 0.35 * 1650 + 0.396 * (
                        revenue_tax - 406750)
            return tax

    def couple(revenue_tax):
        if revenue_tax < 18151:
            tax = 0.1 * revenue_tax
            return tax
        elif revenue_tax < 73801:
            tax = 0.1 * 18150 + 0.15 * (revenue_tax - 18150)
            return tax
        elif revenue_tax < 148851:
            tax = 0.1 * 18150 + 0.15 * 55650 + 0.25 * (revenue_tax - 73800)
            return tax
        elif revenue_tax < 226851:
            tax = 0.1 * 18150 + 0.15 * 55650 + 0.25 * 75050 + 0.28 * (revenue_tax - 148850)
            return tax
        elif revenue_tax < 405101:
            tax = 0.1 * 18150 + 0.15 * 55650 + 0.25 * 75050 + 0.28 * 78000 + 0.33 * (revenue_tax - 226850)
            return tax
        elif revenue_tax < 457601:
            tax = 0.1 * 18_150 + 0.15 * 55650 + 0.25 * 75050 + 0.28 * 78000 + 0.33 * 178250 + 0.35 * (
                        revenue_tax - 405100)
            return tax
        else:
            tax = (0.1 * 18150 + 0.15 * 55650 + 0.25 * 75050 + 0.28 * 78000 + 0.33 * 178250 + 0.35 * 52500
                   + 0.396 * (revenue_tax - 457600))
            return tax

    def parent(revenue_tax):
        if revenue_tax < 12951:
            tax = 0.1 * revenue_tax
            return tax
        elif revenue_tax < 49401:
            tax = 0.1 * 12950 + 0.15 * (revenue_tax - 12950)
            return tax
        elif revenue_tax < 127551:
            tax = 0.1 * 12950 + 0.15 * 36450 + 0.25 * (revenue_tax - 49400)
            return tax
        elif revenue_tax < 206601:
            tax = 0.1 * 12950 + 0.15 * 36450 + 0.25 * 78150 + 0.28 * (revenue_tax - 127550)
            return tax
        elif revenue_tax < 405101:
            tax = 0.1 * 12950 + 0.15 * 36450 + 0.25 * 78150 + 0.28 * 79050 + 0.33 * (revenue_tax - 206600)
            return tax
        elif revenue_tax < 432201:
            tax = 0.1 * 12950 + 0.15 * 36450 + 0.25 * 78150 + 0.28 * 79050 + 0.33 * 198500 + 0.35 * (
                        revenue_tax - 405100)
            return tax
        else:
            tax = (0.1 * 12950 + 0.15 * 36450 + 0.25 * 78150 + 0.28 * 79050 + 0.33 * 198500 + 0.35 * 27100
                   + 0.396 * (revenue_tax - 432200))
            return tax


    grade = int(input(f'{ru.CATEGORY}\n1.{ru.ALONE}\n2.{ru.FAMILY}\n3.{ru.SINGLE}\n{ru.GRADE}'))

    print(ru.ANNUAL_INCOME)
    print(f'{ru.ANNUAL_INCOME_SUM} ${annual_income()}')
    print(ru.FREE_TAX)
    print(f'{ru.FINAL_FREE_TAX} ${free_tax()}\n{ru.TAXABLE} ${revenue_tax}')




if __name__ == '__main__':
    main()
