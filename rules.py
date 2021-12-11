from enum import Enum
from itertools import product

def rule_1(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    return f_pi == expected


def rule_2(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    pass
    return f_pi * (not(f_ki))


def rule_3(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    pass
    return f_pi * J_j


def rule_4(expected=0, f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    value = lambda f_ki, J_j: (not(f_ki)) * J_j
    if expected != value(f_ki, J_j):
        J_j = 1
        return expected == value(f_ki, J_j)
    else:
        return expected == value(f_ki, J_j)

def rule_5(expected=0, f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    value = lambda f_pi,y_i,f_ki: (f_pi + y_i) * (not(f_ki))
    if expected != value(f_pi,y_i,f_ki):
        y_i = 1
        return value(f_pi,y_i,f_ki) == expected
    else:
        return True

def rule_6(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    pass
    return f_pi * (not(f_ki)) * J_j


def rule_7(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    pass
    return f_pi * ((not(f_ki)) * J_j)


def rule_8(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    pass
    return (f_pi + y_i) * ((not(f_ki)) + J_j)


def rule_9(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    pass
    return (f_pi + y_i) * (not(f_ki)) * J_j


def rule_10(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    value = lambda f_pi,J_j,y_i,f_ki: (f_pi * J_j + y_i) * (not(f_ki))
    for i in range(2):
        for j in range(2):
            if f_pi == 2:
                for k in range(2):
                    if expected != value(k,i,j,f_ki):
                        return value == expected
    return False



def rule_11(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    pass
    return (f_pi * J_j + y_i) * (not(f_ki)) * J_k


def rule_12(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    pass
    return (f_pi * J_j + y_i) * ((not(f_ki)) + J_k)


def rule_13(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    return False
    return (f_pi * (not(m)), (f_ki + m) * J_j)


def rule_14(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    return False

    return (f_pi * J_j * (not(m)), (f_ki + m) * J_k)


def rule_15(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    return False
    return (f_pi * (not(m)), (f_ki * J_j + m) * J_k)


def rule_16(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    return False
    return ((f_pi + y_i) * (not(m)), (f_ki + m) * J_j)


def rule_17(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    return False
    return ((f_pi + y_i) * (not(m)), (f_ki * J_j + m ) * J_k)


def rule_18(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    return False
    return (f_pi * J_j * (not(m)), (f_ki * J_k + m) * J_l)


def rule_19(expected=0,f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    return False
    return ((f_pi * J_j + y_i) * (not(m)), (f_ki + m) * J_k)


def rule_20(expected=0, f_pi=0, J_j=0, y_i=0, m=0, f_ki=0, J_k=0, J_l=0):
    value = lambda f_pi,J_j,y_i,m,J_k,J_l,f_ki: [((f_pi * J_j + y_i) * (not(m))), (f_ki * J_k + m) * J_l]

    perm = list(product([0, 1], repeat=7))
    if f_pi == 2 and f_ki == 2:
        for i in perm:
            val = value(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
            if expected == val[0] or expected == val[1]:
                return True
    elif f_pi == 2:
        for i in perm:
            val = value(i[0], i[1], i[2], i[3], i[4], i[5], f_ki)
            if expected == val[0] or expected == val[1]:
                return True
    elif f_ki == 2:
        for i in perm:
            val = value(f_pi, i[1], i[2], i[3], i[4], i[5], i[6])
            if expected == val[0] or expected == val[1]:
                return True
    else:
        for i in perm:
            val = value(f_pi, i[1], i[2], i[3], i[4], i[5], f_ki)
            if expected == val[0] or expected == val[1]:
                return True
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