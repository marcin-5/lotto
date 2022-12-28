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


def get_yn(msg, default=None):
    """Get answer yes or no from user.

    :param str msg: message before input
    :param default: Default answer when no input.
    :rtype: bool
    :return: True for yes and False for no.
    """
    while True:
        result = input(msg + " [y/n]: ".replace(default.lower(),
                                                default.upper()))
        if not result and default:
            result = default
        if result.lower() in ("y", "n"):
            return result.lower() == "y"


def check(s1, s2):
    """
    :param set s1:
    :param set s2:
    :return: frozenset of common elements
    """
    return frozenset(s1 & s2)


def get_numbers():
    """Get 6 different numbers between 1 and 49.

    :return: list with 6 numbers provide by user
    """
    result = set()
    print("Chose six different numbers from 1 to 49.")
    for i in range(1, 7):
        while i != len(result):
            result |= {get_number(f"Number {i}: ",
                                  nmin=1, nmax=49)}
    return result


def get_number_of_draws():
    """Get number > 0

    :rtype: int
    :return: number of draws
    """
    return get_number("Chose number of draws (default=1): ",
                      nmin=1, default=1)


def print_numbers(msg, numbers, hits=frozenset()):
    """Print given message and numbers

    :param str msg: Message before numbers.
    :param list numbers: Numbers to print.
    :param frozenset hits: Set of numbers to colorize.
    """
    print(msg + ", ".join(f"\033[93m {_}\033[00m" if _ in hits else str(_) for _ in numbers))


def lotto():
    """Main function."""
    user_numbers = get_numbers()
    number_of_draws = get_number_of_draws()
    show_draw = get_yn("Show lotto numbers", default="n")
    draw_range = [*range(1, 50)]
    # keys from 0 to 6, value hit counter
    results = dict([(i, 0) for i in range(7)])
    print_numbers("Your numbers: ", sorted(user_numbers))
    for i in range(number_of_draws):
        shuffle(draw_range)
        draw_numbers = set(draw_range[:6])
        common = check(user_numbers, draw_numbers)
        if show_draw:
            print_numbers("Lotto numbers: ",
                          sorted(draw_numbers),
                          common)
        results[len(common)] += 1
    return results


if __name__ == "__main__":
    res = lotto()
    for i in range(3, 7):
        print(f"{i} hits: {res[i]}")
