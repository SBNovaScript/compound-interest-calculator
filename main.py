from pprint import pprint


def calculate_declining_funds(starting_amount, interest_rate, stipend_amount):
    """
    If I want to take out a big chunk every year, how many years will it last?
    :param starting_amount: The amount of money the bank has to start with.
    :type starting_amount: double
    :param interest_rate: The rate that interest is being added into the bank.
    :type interest_rate: float
    :param stipend_amount: The amount taken out each year for a stipend.
    :type stipend_amount: float
    :return: The amount of years until funds deplete, the last stipend amount.
    """

    # We are not losing anything.
    if stipend_amount <= 0:
        return -1, -1

    current_amount = starting_amount
    last_stipend_amount = 0
    years = 0
    while current_amount > 0:

        # Funds are taken out at the beginning of each year, to accrue interest regardless.
        current_amount += (current_amount * interest_rate)

        # if we are on the last iteration
        if current_amount - stipend_amount <= 0:
            last_stipend_amount = stipend_amount - current_amount

        years += 1
        current_amount -= stipend_amount

    return years, last_stipend_amount


def calculate_recurrent_stipend(starting_amount, interest_rate):
    """
    If I have X amount in the bank, how much can I make a year?
    :param starting_amount: The amount of money the bank has to start with.
    :type starting_amount: double
    :param interest_rate: The rate that interest is being added into the bank.
    :type interest_rate: float
    :return: The recurrent stipend.
    """

    recurrent_stipend = starting_amount * interest_rate
    return recurrent_stipend


def calculate_interest_amount_lump_sum(starting_amount, number_of_years, interest_rate):
    """
    After X number of years, how much would I have in the bank?
    :param starting_amount: The amount of money the bank has to start with.
    :type starting_amount: double
    :param number_of_years: The amount of time to accrue interest.
    :type number_of_years: int
    :param interest_rate: The rate that interest is being added into the bank.
    :type interest_rate: float
    :return: The amount in the bank.
    """

    current_amount = starting_amount
    for year in range(number_of_years):
        current_amount += (current_amount * interest_rate)

    return current_amount


def calculate_interest_amount_in_years(starting_amount, number_of_years, interest_rate, stipend_rate):
    """
    After X number of years, how much would I have in the bank?
    :param starting_amount: The amount of money the bank has to start with.
    :type starting_amount: double
    :param number_of_years: The amount of time to accrue interest.
    :type number_of_years: int
    :param interest_rate: The rate that interest is being added into the bank.
    :type interest_rate: float
    :param stipend_rate: The amount taken out each year for a stipend.
    :type stipend_rate: float
    :return: The amount in the bank, and the yearly stipends.
    """

    # Money is not gained. Can be calculated, but not here.
    if stipend_rate >= interest_rate:
        return -1, -1

    current_amount = starting_amount
    stipend = {}
    for year in range(number_of_years):
        current_amount += (current_amount * interest_rate)

        # We take the stipend out after adding new interest.
        new_stipend_amount = current_amount * stipend_rate
        current_amount -= new_stipend_amount
        stipend[year+1] = round(new_stipend_amount, 2)

    return current_amount, stipend


def calculate_interest_amount_stipend(starting_amount, interest_rate):
    """
    After X number of years, how much would I have in the bank?
    :param starting_amount: The amount of money the bank has to start with.
    :type starting_amount: double
    :param interest_rate: The rate that interest is being added into the bank.
    :type interest_rate: float
    :return: The yearly stipend.
    """

    return starting_amount * interest_rate


def calculate_interest_years(starting_amount, requested_amount, interest_rate, stipend_rate):
    """
    If I want X in the bank, how long will it take?
    :param starting_amount: The amount of money the bank has to start with.
    :type starting_amount: double
    :param requested_amount: The amount requested in the bank.
    :type requested_amount: double
    :param interest_rate: The rate that interest is being added into the bank.
    :type interest_rate: float
    :param stipend_rate: The amount taken out each year for a stipend.
    :type stipend_rate: float
    :return: The amount of years it will take to accrue, the yearly stipend amounts.
    """

    # Money is not gained. Can be calculated, but not here.
    if stipend_rate >= interest_rate:
        return -1, -1

    # We start on the first year.
    years = 1
    current_amount = starting_amount
    stipend = [0]
    while current_amount < requested_amount:
        current_amount += (current_amount * interest_rate)

        # We take the stipend out after adding new interest.
        new_stipend_amount = current_amount * stipend_rate
        current_amount -= new_stipend_amount
        stipend.append(new_stipend_amount)
        years += 1

    # If we want to calculate stipend, return the full stipend sheet.
    return years, stipend if stipend_rate > 0 else [0]


def calculate_years_until_amount(starting_amount, requested_amount, interest_rate, stipend_rate):
    """
    If I want X in the bank, how long will it take?
    :param starting_amount: The amount of money the bank has to start with.
    :type starting_amount: double
    :param requested_amount: The amount requested in the bank.
    :type requested_amount: double
    :param interest_rate: The rate that interest is being added into the bank.
    :type interest_rate: float
    :param stipend_rate: The amount taken out each year for a stipend.
    :type stipend_rate: float
    :return: The amount of years it will take to accrue, the yearly stipend amounts.
    """

    # Money is not gained. Can be calculated, but not here.
    if stipend_rate >= interest_rate:
        return -1, -1

    # We start on the first year.
    years = 1
    current_amount = starting_amount
    stipend = [0]
    while current_amount < requested_amount:
        current_amount += (current_amount * interest_rate)

        # We take the stipend out after adding new interest.
        new_stipend_amount = current_amount * stipend_rate
        current_amount -= new_stipend_amount
        stipend.append(new_stipend_amount)
        years += 1

    # If we want to calculate stipend, return the full stipend sheet.
    return years, stipend if stipend_rate > 0 else [0]


if __name__ == '__main__':
    starting_amount_input = 3750000
    interest_rate_input = 0.025

    print('\nOption A:')

    stipend_amount_A = 100000

    years, final_stipend = calculate_declining_funds(starting_amount_input, interest_rate_input, stipend_amount_A)
    print(f'You get a standard ${stipend_amount_A} per year until year {years}, '
          f'with your final stipend being ${round(final_stipend, 2)}')

    print('\nOption B:')

    result_amount = calculate_recurrent_stipend(starting_amount_input, interest_rate_input)
    print(f'You get a recurring ${round(result_amount, 2)} per year.')

    print('\nOption C:')

    number_of_years_C = 69
    stipend_rate_C = 0.02

    result_amount, stipends = calculate_interest_amount_in_years(
        starting_amount_input,
        number_of_years_C,
        interest_rate_input,
        stipend_rate_C)

    print(f'In {number_of_years_C} years, you would have ${round(result_amount, 2)} in the bank. Here would be '
          f'your historical recurring, increasing stipends:')
    pprint(stipends)

    print('\nOption D:')

    number_of_years_D = 69

    result_amount = calculate_interest_amount_lump_sum(starting_amount_input, number_of_years_D, interest_rate_input)

    print(f'In {number_of_years_D} years with no stipend, you would have ${round(result_amount, 2)} in the bank.')
