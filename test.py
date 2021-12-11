from rules import Rules
import pytest

def test_rules_being_defined_properly():
    for i in range(1, 21):
        assert Rules[i].__name__ == f"rule_{i}"


class TestRules:

    def test_for_rule_one_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
            "fp": [0, 1, 1, 0, 0],
            "fk": [0, 0, 0, 1, 0],
        }
        for i in range(1, 6):
            rozwiazanie = []
            for j in range(len(test_values["Y"])):
                print(Rules[i](expected=test_values["Y"][j], f_pi=test_values["fp"][j], f_ki=test_values["fk"][j]))
                rozwiazanie.append(
                    Rules[i](expected=test_values["Y"][j], f_pi=test_values["fp"][j], f_ki=test_values["fk"][j]))
                if isinstance(rozwiazanie[-1], tuple):
                    rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"][j]
            if False in rozwiazanie:
                continue
            else:
                print(i)
                print(Rules[i].__name__)

    def test_for_rule_five_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
             "fp": [0, 1, 0, 0, 0],
             "fk": [0, 0, 0, 1, 0],
        }
        for i in range(1, 6):
            rozwiazanie = []
            for j in range(len(test_values["Y"])):
                print(Rules[i](expected=test_values["Y"][j], f_pi=test_values["fp"][j], f_ki=test_values["fk"][j]))
                rozwiazanie.append(Rules[i](expected=test_values["Y"][j], f_pi=test_values["fp"][j], f_ki=test_values["fk"][j]))
                if isinstance(rozwiazanie[-1], tuple):
                    rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"][j]
            if False in rozwiazanie:
                continue
            else:
                print(i)
                print(Rules[i].__name__)



    def test_for_rule_ten_and_twenty_being_used(self):
        test_values = {
            "Y": [0, 0, 1, 1, 0],
             "fp": [2, 1, 0, 0, 0],
             "fk": [2, 0, 0, 1, 0],
        }
        for i in range(1, 21):
            rozwiazanie = []
            for j in range(len(test_values["Y"])):
                rozwiazanie.append(Rules[i](expected=test_values["Y"][j], f_pi=test_values["fp"][j], f_ki=test_values["fk"][j]))
                if isinstance(rozwiazanie[-1], tuple):
                    rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"][j]
            if False in rozwiazanie:
                continue
            else:
                print(Rules[i].__name__)


    def test_for_rule_one_and_four(self):
        test_values = {
            "Y": [0, 0, 1, 1, 1],
             "fp": [0, 1, 1, 0, 0],
             "fk": [0, 0, 0, 1, 1],
        }
        for i in range(1, 21):
            rozwiazanie = []
            for j in range(len(test_values["Y"])):
                rozwiazanie.append(Rules[i](expected=test_values["Y"][j], f_pi=test_values["fp"][j], f_ki=test_values["fk"][j]))
                if isinstance(rozwiazanie[-1], tuple):
                    rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"][j]
            if False in rozwiazanie:
                continue
            else:
                print(Rules[i].__name__)
            print("4 i 1")