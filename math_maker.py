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

        steps = len(valves)*2
        crocs ={}
        Y = []
        fp = []
        fk = []
        #check for pair, bo musze wiedzic ktore
        # warunki fpi i fki z pistona
        # dla ktorego valve
        # Rozpatruje kazdy zawor jako osobny krok, wiec fp i fk sa to wartosci przed i po sygnale z zaworu
        # TODO OBLICZANIE ROWNANIA SCHEMATOWEGO DLA KAZDEGO Z SYGNALOW
        current_valve = 0
        current_piston = 0
        current_left_state = 0
        current_right_state = 1
        for i in range(steps):

            fp.append(pistons[current_piston].state[current_left_state])
            Y.append(valves[current_valve].state[current_left_state])
            fk.append(pistons[current_piston].state[current_right_state])
            current_left_state += 1
            current_right_state -= 1

            if i % 2 == 1:
                crocs[current_valve] = {"Y": Y, "fp": fp, "fk": fk}
                Y = []
                fp = []
                fk = []
                current_valve += 1
                current_piston += 1
                current_left_state = 0
                current_right_state = 1
                if "bi" in valves[current_valve-1].image_path:
                    valves.insert(current_valve, valves[current_valve-1])
                    valves[current_valve].state = valves[current_valve].state[::-1]
                    for i in range(2):
                        fp.append(pistons[current_piston-1].state[current_left_state])
                        Y.append(valves[current_valve].state[current_left_state])
                        fk.append(pistons[current_piston-1].state[current_right_state])
                        current_left_state += 1
                        current_right_state -= 1
                    crocs[current_valve] = {"Y": Y, "fp": fp, "fk": fk}
                    Y = []
                    fp = []
                    fk = []
                    current_valve += 1
                    current_left_state = 0
                    current_right_state = 1
                    #POdziel stepy na takty i wstrzykuj 3artosci logiczne
                    # dla kazdego z sygnalow

                    # WAZNE - WSKAZNIKI POLOZENIA INNYCH PISTONOW TEZ MUSZA MIEC
                    # 1 albo 0 az do momentu zmiany stanu, czyli gdy nadejdzie ich kolej

        algorithm = []
        for i,j in crocs.items():
            pass
        return crocs
