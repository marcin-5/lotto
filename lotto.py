from random import shuffle


def parse(line):
    """
    :param str line:
    :return: list of numbers or error message
    """
    if not line.strip():
        return "No numbers!"
    allowed_chars = tuple([str(_) for _ in range(10)] + [" "])
    for char in line:
        if char not in allowed_chars:
            return f"Not allowed char: '{char}'!"
    line = [int(_) for _ in line.strip().split()]
    tmp = line[:]
    if not len(line) == 6:
        return "Wrong amount of numbers!"
    for i in line[:-1]:
        tmp.pop(0)
        if i in tmp:
            return f"Repeated number: {i}!"
    if min(line) < 1 or max(line) > 49:
        return "Number out of range!"
    return sorted(line)


def check(l1, l2):
    """
    :param list l1:
    :param list l2:
    :return: tuple of common part
    """
    return tuple(i for i in l1 if i in l2)


def lotto():
    """Main function."""
    user_numbers = ""
    number_of_draws = 0
    while not user_numbers:
        user_numbers = parse(input("Enter six numbers from 1 to 49 space separated:\n"))
        if type(user_numbers) is not list:
            print(user_numbers)
            user_numbers = ""
    while not number_of_draws:
        try:
            number_of_draws = int(input("How many draws? "))
        except ValueError:
            print(f"{number_of_draws} is not a number!")
            number_of_draws = 0
        else:
            if not number_of_draws:
                print("Must be > 0!")
    draw_range = [*range(50)]
    # keys from 0 to 6, value hit counter
    results = dict([(i, 0) for i in range(7)])
    for i in range(number_of_draws):
        shuffle(draw_range)
        draw_numbers = sorted(draw_range[:6])
        number_of_hits = len(check(user_numbers, draw_numbers))
        results[number_of_hits] += 1

    for i in range(3, 7):
        print(f"{i} hits: {results[i]}")


if __name__ == "__main__":
    lotto()
