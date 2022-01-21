from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton

from rules import Rules


class RuleChecker(QPushButton):
    get_values = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("WYNIK")
        self.values = None


    def mousePressEvent(self, e) :
        self.get_values.emit()
        print("values", self.values)
        self.check_for_rules(values=self.values)

    def check_for_rules(self, values):
        rozwiazanie = []
        for steps in values:
            for i in range(1, 21):
                if Rules[i](steps["Y"], steps["fp"], steps["fk"]):
                    rozwiazanie.append(Rules[i].__name__)
                    break
        self.setText(f"{values}\n{rozwiazanie}")


class ProcessAlgorithmMaker:
    def __init__(self, buttons):
        self.buttons = buttons

    def make_algorithm(self):
        pistons = []
        valves = []

        for i in self.buttons:
            if "piston" in i.image_path:
                pistons.append(i)
            if "valve" in i.image_path:
                valves.append(i)

        pairs = []
        for i in range(len(pistons)):
            pairs.append((pistons[i], valves[i]))

        steps = len(valves)*2
        crocs = {}
        #check for pair, bo musze wiedzic ktore
        # warunki fpi i fki z pistona
        # dla ktorego valve
        # Rozpatruje kazdy zawor jako osobny krok, wiec fp i fk sa to wartosci przed i po sygnale z zaworu
        # TODO OBLICZANIE ROWNANIA SCHEMATOWEGO DLA KAZDEGO Z SYGNALOW
                    #POdziel stepy na takty i wstrzykuj 3artosci logiczne
                    # dla kazdego z sygnalow

                    # WAZNE - WSKAZNIKI POLOZENIA INNYCH PISTONOW TEZ MUSZA MIEC
                    # 1 albo 0 az do momentu zmiany stanu, czyli gdy nadejdzie ich kolej

        algorithm = dict()
        groups = []

        for i in range(len(pairs)):
            temp_table = dict()
            valve = pairs[i][1]
            piston = pairs[i][0]
            temp_table[f"Y{valve.second_title}"] = [valve.state]
            temp_table[f"X{piston.left_index}"] = [piston.left_state]
            temp_table[f"X{piston.right_index}"] = [piston.right_state]
            groups.append(temp_table)

        print(groups)
        for i in range(steps*2-1):
            current_group = 0
            for j in groups:
                try:
                    j[f"Y{current_group}"].append(pairs[current_group][1].state)
                    j[f"X{current_group*2+1}"].append(pairs[current_group][0].left_state)
                    j[f"X{current_group*2+2}"].append(pairs[current_group][0].right_state)
                except KeyError:
                    for k, l in j.items():
                        j[k].append(l[0])
        print(groups)
        return crocs
