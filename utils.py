from itertools import product


def check_for_false(rule_list):
    return not(False in rule_list)


def calculate_value(expected, func, fp, fk, params):
    perm = list(product([0, 1], repeat=params))
    check = []
    for j in perm:
        for i in range(len(expected)):
            if isinstance(fp[i], int) and isinstance(fk[i], int):
                if expected[i] == func(1, 1, *j):
                    pass
                elif expected[i] == func(0, 1, *j):
                    pass
                elif expected[i] == func(1, 0, *j):
                    pass
                elif expected[i] == func(0, 0, *j):
                    pass
                else:
                    check.append(False)
                    break
            if isinstance(fp[i], int):
                if expected[i] == func(1, fk[i], *j):
                    pass
                elif expected[i] == func(0, fk[i], *j):
                    pass
                else:
                    check.append(False)
                    break
            if isinstance(fk[i], int):
                if expected[i] == func(fp[i], 1, *j):
                    pass
                if expected[i] == func(fp[i], 0, *j):
                    pass
                else:
                    break
            if expected[i] == func(fp[i], fk[i], *j):
                pass
            else:
                check.append(False)
        if check_for_false(check) == True:
            return True
        else:
            check = []
    return False
