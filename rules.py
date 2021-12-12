from enum import Enum
from itertools import product

def rule_1(expected, fp, fk):
    rule_check = [True if expected[i] == fp[i] else False for i in range(len(expected))]
    if False in rule_check:
        return False
    return True



def rule_2(expected, fp, fk):
    pass
    #return f_pi * (not(f_ki))


def rule_3(expected, fp, fk):
    pass
    #return f_pi * J_j


# "Y": [0, 1, 1, 0, 0],
# "fp": [0, 1, 1, 0, 0],
# "fk": [0, 0, 0, 1, 0],
def rule_4(expected, fp, fk):
    value = lambda f_ki, J_j: (not(f_ki)) * J_j
    bool_check = True

    count_0 = fk.count(0)
    count_1 = fk.count(1)
    for i in range(len(expected)):
        if count_0:
            J_j = 0
            lol = value(fk[i], J_j)
        if expected[i] == value(fk[i], J_j):
            count_0 -= 1
            pass
        else:
            if count_1:
                J_j = 1
            if expected[i] == value(fk[i], J_j):
                count_1 -= 1
                pass
            else:
                bool_check = False
    if bool_check is False:
        return bool_check
    return True

def rule_5(expected, fp, fk):
    value = lambda f_pi,y_i,f_ki: (f_pi + y_i) * (not(f_ki))
    bool_check = True
    for i in range(len(expected)):
        if 0 in fp:
            y_i = 0
        if expected[i] == value(fp[i], fk[i], expected[i]):
            pass
        else:
            bool_check = False
            break
    for i in range(len(expected)):
        if 1 in fp:
            y_i = 1
        if expected[i] == value(fp[i], fk[i], expected[i]):
            pass
        else:
            return False
    return bool_check


def rule_6(expected, fp, fk):
    pass
    #return f_pi * (not(f_ki)) * J_j


def rule_7(expected, fp, fk):
    pass
    #return f_pi * ((not(f_ki)) * J_j)


def rule_8(expected, fp, fk):
    pass
    #return (f_pi + y_i) * ((not(f_ki)) + J_j)


def rule_9(expected, fp, fk):
    pass
    #return (f_pi + y_i) * (not(f_ki)) * J_j


def rule_10(expected, fp, fk):
    value = lambda f_pi,J_j,y_i,f_ki: (f_pi * J_j + y_i) * (not(f_ki))
    pass



def rule_11(expected, fp, fk):
    pass
    #return (f_pi * J_j + y_i) * (not(f_ki)) * J_k


def rule_12(expected, fp, fk):
    pass
    #return (f_pi * J_j + y_i) * ((not(f_ki)) + J_k)


def rule_13(expected, fp, fk):
    return False
    #return (f_pi * (not(m)), (f_ki + m) * J_j)


def rule_14(expected, fp, fk):
    return False
    #return (f_pi * J_j * (not(m)), (f_ki + m) * J_k)


def rule_15(expected, fp, fk):
    return False
    #return (f_pi * (not(m)), (f_ki * J_j + m) * J_k)


def rule_16(expected, fp, fk):
    return False
    #return ((f_pi + y_i) * (not(m)), (f_ki + m) * J_j)


def rule_17(expected, fp, fk):
    return False
    #return ((f_pi + y_i) * (not(m)), (f_ki * J_j + m ) * J_k)


def rule_18(expected, fp, fk):
    return False
    #return (f_pi * J_j * (not(m)), (f_ki * J_k + m) * J_l)


def rule_19(expected, fp, fk):
    return False
    #return ((f_pi * J_j + y_i) * (not(m)), (f_ki + m) * J_k)


def rule_20(expected=0, f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    value = lambda f_pi,J_j,y_i,m,J_k,J_l,f_ki: [((f_pi * J_j + y_i) * (not(m))), (f_ki * J_k + m) * J_l]

    # perm = list(product([0, 1], repeat=7))
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

#Realizacja pamieci z przerzutnikami