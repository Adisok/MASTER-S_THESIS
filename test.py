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
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)

    def test_for_rule_five_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
             "fp": [0, 1, 0, 0, 0],
             "fk": [0, 0, 0, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)



    # def test_for_rule_ten_and_twenty_being_used(self):
    #     test_values = {
    #         "Y": [0, 0, 1, 1, 0],
    #          "fp": [2, 1, 0, 0, 0],
    #          "fk": [2, 0, 0, 1, 0],
    #     }
    #     rozwiazanie = []
    #
    #     for i in range(1, 21):
    #         if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
    #             rozwiazanie.append(Rules[i].__name__)
    #         # if isinstance(rozwiazanie[-1], tuple):
    #         #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
    #     print(rozwiazanie)

    def test_for_rule_one_and_four(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
             "fp": [0, 1, 1, 0, 0],
             "fk": [0, 0, 0, 1, 1],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)


            # KUURWA LICZ NAJPIERW RULE DLA CALEJ LISTY DLA JEDNEJ ZMIENNEJ POMOCNICZEJ
            # POTEM JAK NIE PYKNIE TO LICZ TO KURWA DLA DRUGIEJ ZMIENNEJ POMOCNICZEJ
            # ALE ZEBY CIE KURWA NIE PODKUSILO ROBIC JEGO JEDNOSTKOWO TYLKO PIERDOLISZ
            # PO CALOSCI Z OSOBNA DLA KAZDEJ ZMIENNEJ POMOCNICZEJ KUUUUUURWAAAAA
            # CZYLI F(YI) = NOT(F_KI) * J DLA J = 0
            # I LECIMY DLA fk[0](J=0) potem fk[1](J=0) i tak do konca i jak nie pyknie
            # TO LECISZMY TAK fk[0](J=1) potem fk[1](J=1) i tak dokonca i wtedy jak nie pyknie
            # to lecimy next i chuj