from itertools import product

from utils import check_for_false, calculate_value


def rule_1(expected, fp, fk):
    rule_check = [True if expected[i] == fp[i] else False for i in range(len(expected))]
    return check_for_false(rule_check)


def rule_2(expected, fp, fk):
    rule_check = [True if expected[i] == (fp[i] * (not(fk[i]))) else False for i in range(len(expected))]
    return check_for_false(rule_check)


def rule_3(expected, fp, fk):
    rule_check = []
    for i in range(len(expected)):
        if expected[i] == fp[i] * 0:
            rule_check.append(True)
        elif expected[i] == fp[i] * 1:
            rule_check.append(True)
        else:
            rule_check.append(False)

    return check_for_false(rule_check)


def rule_4(expected, fp, fk):
    value = lambda f_pi, f_ki, J_j: (not(f_ki)) * J_j
    return True == calculate_value(expected, value, fp, fk, 1)


def rule_5(expected, fp, fk):
    value = lambda f_pi,  f_ki, y_i: (f_pi or y_i) and (not(f_ki))
    return True == calculate_value(expected, value, fp, fk, 1)


def rule_6(expected, fp, fk):
    value = lambda f_pi, f_ki, J_j: f_pi * (not(f_ki)) * J_j
    return True == calculate_value(expected, value, fp, fk, 1)


def rule_7(expected, fp, fk):
    value = lambda f_pi, f_ki, J_j: f_pi * ((not(f_ki)) + J_j)
    return True == calculate_value(expected, value, fp, fk, 1)


def rule_8(expected, fp, fk):
    value = lambda f_pi, f_ki, y_i, J_j: (f_pi or y_i) and ((not(f_ki)) or J_j)
    return True == calculate_value(expected, value, fp, fk, 2)
    #return (f_pi + y_i) * ((not(f_ki)) + J_j)


def rule_9(expected, fp, fk):
    rule_check = []
    for i in range(len(expected)):
        if expected[i] == (fp[i] + 0) * (not (fk[i])) * 0:
            rule_check.append(True)
        elif expected[i] == (fp[i] + 0) * (not (fk[i])) * 1:
            rule_check.append(True)
        elif expected[i] == (fp[i] + 1) * (not (fk[i])) * 0:
            rule_check.append(True)
        elif expected[i] == (fp[i] + 1) * (not (fk[i])) * 1:
            rule_check.append(True)
        else:
            rule_check.append(False)
    return check_for_false(rule_check)
    #return (f_pi + y_i) * (not(f_ki)) * J_j


def rule_10(expected, fp, fk):
    value = lambda f_pi,J_j,y_i,f_ki: (f_pi * J_j + y_i) * (not(f_ki))
    rule_check = []
    for i in range(len(expected)):
        if expected[i] == value(fp[i], 0, 0, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 0, 1, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 1, 0, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 1, 1, fk[i]):
            rule_check.append(True)
        else:
            rule_check.append(False)
    return check_for_false(rule_check)


def rule_11(expected, fp, fk):
    value = lambda f_pi, J_j, y_i, J_k,f_ki: (f_pi * J_j + y_i) * (not (f_ki)) * J_k
    rule_check = []
    for i in range(len(expected)):
        if expected[i] == value(fp[i], 0, 0, 0, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 0, 1, 0, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 1, 0, 0, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 1, 1, 0, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 0, 1, 1, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 1, 0, 1, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 1, 1, 1, fk[i]):
            rule_check.append(True)
        elif expected[i] == value(fp[i], 0, 0, 1, fk[i]):
            rule_check.append(True)
        else:
            rule_check.append(False)

    return check_for_false(rule_check)
    #return (f_pi * J_j + y_i) * (not(f_ki)) * J_k


def rule_12(expected, fp, fk):
    pass
    #return check_for_false(rule_check)
    #return (f_pi * J_j + y_i) * ((not(f_ki)) + J_k)


def rule_13(expected, fp, fk):
    return False
    #return check_for_false(rule_check)
    #return (f_pi * (not(m)), (f_ki + m) * J_j)


def rule_14(expected, fp, fk):
    return False
    #return check_for_false(rule_check)
    #return (f_pi * J_j * (not(m)), (f_ki + m) * J_k)


def rule_15(expected, fp, fk):
    return False
    #return check_for_false(rule_check)
    #return (f_pi * (not(m)), (f_ki * J_j + m) * J_k)


def rule_16(expected, fp, fk):
    return False
    #return check_for_false(rule_check)
    #return ((f_pi + y_i) * (not(m)), (f_ki + m) * J_j)


def rule_17(expected, fp, fk):
    return False
    #return check_for_false(rule_check)
    #return ((f_pi + y_i) * (not(m)), (f_ki * J_j + m ) * J_k)


def rule_18(expected, fp, fk):
    return False
    #return check_for_false(rule_check)
    #return (f_pi * J_j * (not(m)), (f_ki * J_k + m) * J_l)


def rule_19(expected, fp, fk):
    return False
    #return check_for_false(rule_check)
    #return ((f_pi * J_j + y_i) * (not(m)), (f_ki + m) * J_k)


def rule_20(expected=0, f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    value = lambda f_pi,J_j,y_i,m,J_k,J_l,f_ki: [((f_pi * J_j + y_i) * (not(m))), (f_ki * J_k + m) * J_l]

    #perm = list(product([0, 1], repeat=7))
    # if f_pi == 2 and f_ki == 2:
    #     for i in perm:
    #         val = value(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    #         if expected == val[0] or expected == val[1]:
    #             return True
    # elif f_pi == 2:
    #     for i in perm:
    #         val = value(i[0], i[1], i[2], i[3], i[4], i[5], f_ki)
    #         if expected == val[0] or expected == val[1]:
    #             return True
    # elif f_ki == 2:
    #     for i in perm:
    #         val = value(f_pi, i[1], i[2], i[3], i[4], i[5], i[6])
    #         if expected == val[0] or expected == val[1]:
    #             return True
    # else:
    #     for i in perm:
    #         val = value(f_pi, i[1], i[2], i[3], i[4], i[5], f_ki)
    #         if expected == val[0] or expected == val[1]:
    #             return True
    #return check_for_false(rule_check)
    return False


Rules = {
    1: rule_1,
    2: rule_2,
    3: rule_3,
    4: rule_4,
    5: rule_5,
    6: rule_6,
    7: rule_7,
    8: rule_8,
    9: rule_9,
    10: rule_10,
    11: rule_11,
    12: rule_12,
    13: rule_13,
    14: rule_14,
    15: rule_15,
    16: rule_16,
    17: rule_17,
    18: rule_18,
    19: rule_19,
    20: rule_20,
}
