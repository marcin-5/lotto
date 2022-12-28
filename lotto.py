from random import shuffle


def get_number(msg, nmin=None, nmax=None, default=None):
    """Get number from user.
    Try until user give proper number.

    :param str msg: message before input
    :param int nmin: lower range of number
    :param int nmax: upper range of number
    :param int default: return default value if no input
    :return: given number as int
    """
    while True:
        result = input(msg)
        if not result and default is not None:
            return default
        try:
            result = int(result)
        except ValueError:
            print("It's not a number")
        else:
            if nmin is not None and result < nmin:
                print(f"Number must be >= {nmin}")
            elif nmax is not None and result > nmax:
                print(f"Number must be <= {nmax}")
            else:
                return result


def check(l1, l2):
    """
    :param list l1:
    :param list l2:
    :return: tuple of common part
    """
    return tuple(i for i in l1 if i in l2)


def get_numbers():
    """Get 6 different numbers between 1 and 49.

    :return: list with 6 numbers provide by user
    """
    result = []
    print("Chose six different numbers from 1 to 49.")
    for i in range(1, 7):
        while True:
            n = get_number(f"Number {i}: ", nmin=1, nmax=49)
            if n not in result:
                break
            print("The number cannot be repeated.")
        result.append(n)
    return sorted(result)


def get_number_of_draws():
    """Get number > 0

    :rtype: int
    :return: number of draws
    """
    return get_number("Chose number of draws: ",
                      nmin=1, default=1)


def lotto():
    """Main function."""
    user_numbers = get_numbers()
    number_of_draws = get_number_of_draws()
    draw_range = [*range(50)]
    # keys from 0 to 6, value hit counter
    results = dict([(i, 0) for i in range(7)])
    print(f"Your numbers: {', '.join(map(str, user_numbers))}")
    for i in range(number_of_draws):
        shuffle(draw_range)
        draw_numbers = sorted(draw_range[:6])
        number_of_hits = len(check(user_numbers, draw_numbers))
        results[number_of_hits] += 1

    for i in range(3, 7):
        print(f"{i} hits: {results[i]}")


if __name__ == "__main__":
    lotto()
