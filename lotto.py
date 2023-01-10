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


def get_yn(msg, default=""):
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
    print("Choose six different numbers from 1 to 49.")
    for i in range(1, 7):
        while i != len(result):
            result |= {get_number(f"Number {i}: ",
                                  nmin=1, nmax=49)}
    return result


def get_number_of_draws():
    """Get number > 0 or 0 for loop until hit 6 numbers

    :rtype: int
    :return: number of draws
    """
    return get_number("Choose number of draws (default=1): ",
                      nmin=0, default=1)


def get_stop_number():
    """Get number from 1 to 6.
    The number of hits which stop iterate.

    :rtype: int
    :return: number of hits to stop the loop
    """
    return get_number("Choose number of hits to stop draw (default=6):",
                      nmin=1, nmax=6, default=6)


def print_numbers(msg, numbers, hits=frozenset()):
    """Print given message and numbers

    :param str msg: Message before numbers.
    :param list numbers: Numbers to print.
    :param frozenset hits: Set of numbers to colorize.
    """
    print(msg + ", ".join(f"\033[93m{_}\033[00m" if _ in hits
                          else str(_) for _ in numbers))


def lotto():
    """Main function.

    :rtype: dict
    :return: keys - number of hits and values being count of occurrences.
    """
    user_numbers = get_numbers()
    number_of_draws = get_number_of_draws()
    stop_number = -1 if number_of_draws else get_stop_number()
    show_draw = get_yn("Show lotto numbers", default="n")
    count = min_hit = 0
    if show_draw and get_yn("Show only win draws", default="y"):
        min_hit = 3
    draw_range = [*range(1, 50)]
    # keys from 0 to 6, value hit counter
    results = dict([(i, 0) for i in range(7)])
    print_numbers("Your numbers: ", sorted(user_numbers))
    while not number_of_draws or count < number_of_draws:
        count += 1
        shuffle(draw_range)
        draw_numbers = set(draw_range[:6])
        common = check(user_numbers, draw_numbers)
        results[len(common)] += 1
        if show_draw and (n := len(common)) >= min_hit:
            print_numbers(f"({count}) " +
                          "\033[9%smLotto numbers:\033[0m " %
                          ("0" if n < 3 else
                           "4251"[n - 3]),
                          sorted(draw_numbers),
                          common)
        else:
            print(" | ".join("{} : {}".format(k, v) for k, v in results.items()), end="\r")
        if len(common) == stop_number and not number_of_draws:
            print("\nNumber of draws:", count)
            break
    return results


if __name__ == "__main__":
    res = lotto()
    for i in range(3, 7):
        print(f"{i} hits: {res[i]}")
