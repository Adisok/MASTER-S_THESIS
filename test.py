from rules import Rules

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
        assert 'rule_1' in rozwiazanie

    def test_for_rule_two_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
            "fp": [0, 1, 1, 1, 1],
            "fk": [0, 0, 0, 1, 1],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_2' in rozwiazanie

    def test_for_rule_three_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
            "fp": [0, 1, 1, 1, 1],
            "fk": [0, 0, 0, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)

    def test_for_rule_four_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
            "fp": [0, 1, 0, 0, 0],
            "fk": [0, 0, 0, 1, 1],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_4' in rozwiazanie

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
        assert 'rule_5' in rozwiazanie


    def test_for_rule_six_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
             "fp": [0, 1, 1, 1, 1],
             "fk": [0, 0, 0, 1, 2],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)

    def test_for_rule_seven_being_used(self):
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

    def test_for_rule_eight_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
             "fp": [0, 1, 0, 0, 0],
             "fk": [0, 0, 2, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_8' in rozwiazanie


    def test_for_rule_nine_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
             "fp": [0, 1, 0, 0, 2],
             "fk": [0, 0, 0, 1, 2],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_9' in rozwiazanie


    def test_for_rule_ten_being_used(self):
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
        assert 'rule_10' in rozwiazanie


    def test_for_rule_eleven_being_used(self):
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
        assert 'rule_11' in rozwiazanie


    def test_for_rule_twelve_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
             "fp": [0, 1, 0, 0, 2],
             "fk": [0, 0, 2, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_12' in rozwiazanie


    def test_for_rule_thirteen_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
             "fp": [0, 1, 1, 1, 1],
             "fk": [0, 0, 0, 1, 2],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_13' in rozwiazanie


    def test_for_rule_fourteen_being_used(self):
        test_values = {
            "Y": [1, 1, 1, 0, 0],
             "fp": [2, 1, 1, 1, 2],
             "fk": [0, 0, 0, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_14' in rozwiazanie


    def test_for_rule_fifteen_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 1],
             "fp": [0, 1, 1, 1, 1],
             "fk": [0, 0, 2, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_15' in rozwiazanie


    def test_for_rule_sixteen_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 1],
             "fp": [0, 1, 2, 1, 2],
             "fk": [0, 0, 0, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_16' in rozwiazanie

    def test_for_rule_seventeen_being_used(self):
        test_values = {
            "Y": [0, 1, 0, 0, 0],
             "fp": [0, 1, 2, 0, 0],
             "fk": [0, 0, 2, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_17' in rozwiazanie

    def test_for_rule_eighteen_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 0],
             "fp": [0, 1, 1, 1, 1],
             "fk": [0, 0, 2, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_18' in rozwiazanie

    def test_for_rule_nineteen_being_used(self):
        test_values = {
            "Y": [0, 1, 1, 0, 1],
             "fp": [0, 1, 2, 1, 1],
             "fk": [0, 0, 0, 1, 2],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_19' in rozwiazanie

    def test_for_rule_twenty_being_used(self):
        test_values = {
            "Y": [0, 0, 1, 1, 0],
             "fp": [2, 1, 0, 0, 0],
             "fk": [2, 0, 0, 1, 0],
        }
        rozwiazanie = []

        for i in range(1, 21):
            if Rules[i](test_values["Y"], test_values["fp"], test_values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
            # if isinstance(rozwiazanie[-1], tuple):
            #     rozwiazanie[-1] = rozwiazanie[-1][0] * rozwiazanie[-1][1] == test_values["Y"]
        print(rozwiazanie)
        assert 'rule_20' in rozwiazanie

