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

        self.pairs = []
        for i in range(len(pistons)):
            self.pairs.append((pistons[i], valves[i]))

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

        algorithm = []
        bi_valves = []
        for i in range(len(self.pairs)):
            temp_table = dict()
            valve = self.pairs[i][1]
            piston = self.pairs[i][0]

            temp_table[f"Y{valve.second_title}"] = [valve.state]
            temp_table[f"X{piston.left_index}"] = [piston.left_state]
            temp_table[f"X{piston.right_index}"] = [piston.right_state]
            if i != 0:
                temp_table[f"Y{valve.second_title}"] = [valve.state] + [valve.state] * i
                temp_table[f"X{piston.left_index}"] = [piston.left_state] + [piston.left_state] * i
                temp_table[f"X{piston.right_index}"] = [piston.right_state] + [piston.right_state] * i
#            if "bi" in valve.image_path:
#                bi_valves.append(f"Y{valve.second_title}")
            algorithm.append(temp_table)

        print(algorithm)
        current_group = 0
        for i in range(len(algorithm)):
            self.process_group(algorithm, current_group)
            for j in range(current_group+1, len(algorithm)):
                print(algorithm[j])
                for k in range(len(algorithm[j])):
                    algorithm[j][f"Y{j}"].append(self.pairs[j][1].state)
                    algorithm[j][f"X{j * 2 + 1}"].append(self.pairs[j][0].left_state)
                    algorithm[j][f"X{j * 2 + 2}"].append(self.pairs[j][0].right_state)

            for l in range(0, current_group):
                for m in range(len(algorithm[l])+1):
                    algorithm[l][f"Y{l}"].append(self.pairs[l][1].state)
                    algorithm[l][f"X{l * 2 + 1}"].append(self.pairs[l][0].left_state)
                    algorithm[l][f"X{l * 2 + 2}"].append(self.pairs[l][0].right_state)

            current_group += 1
        print("algorithm_finall")
        for i in algorithm:
            print(i)
        print("bi",bi_valves)
    #    if len(bi_valves):
    #        print("ZMIENIAM ZAWOR BI STABILNY")
    #        self.update_algorithm_with_bi_stable_valve(algorithm, bi_valves)
        return crocs

    def process_group(self, algorithm, current_group):
        group_to_be_processed = algorithm[current_group]

        if len(group_to_be_processed[f"Y{current_group}"]) > 3:
            self.pairs[current_group][1].change_state()
            group_to_be_processed[f"Y{current_group}"][-1] = self.pairs[current_group][1].state
            group_to_be_processed[f"X{current_group * 2 + 1}"][-1] =(self.pairs[current_group][0].left_state)
            group_to_be_processed[f"X{current_group * 2 + 2}"][-1] =(self.pairs[current_group][0].right_state)

        for i, j in group_to_be_processed.items():
            if group_to_be_processed[f"X{current_group*2+1}"][-1] == 1: # 1 step
                self.pairs[current_group][0].change_state("left")
                group_to_be_processed[f"X{current_group*2+1}"].append(self.pairs[current_group][0].left_state)
                group_to_be_processed = self.append_to_group(algorithm, current_group, f"X{current_group*2+1}")
            elif group_to_be_processed[f"X{current_group*2+1}"][-1] == 0 and group_to_be_processed[f"X{current_group*2+2}"][-1] == 0: # 2 step
                self.pairs[current_group][1].change_state()
                self.pairs[current_group][0].change_state("right")
                group_to_be_processed[f"X{current_group*2+2}"].append(self.pairs[current_group][0].right_state)
                group_to_be_processed = self.append_to_group(algorithm, current_group, f"X{current_group*2+2}")
            elif group_to_be_processed[f"X{current_group*2+2}"][-1] == 1 and group_to_be_processed[f"X{current_group*2+1}"][-1] == 0: # 3 step
                group_to_be_processed[f"X{current_group*2+1}"].append(self.pairs[current_group][0].left_state)
                self.pairs[current_group][0].change_state("right")
                group_to_be_processed = self.append_to_group(algorithm, current_group, f"X{current_group*2+1}")
                self.pairs[current_group][0].change_state("left")
        return group_to_be_processed

    def append_to_group(self, algorithm, current_group, *not_append):
        if f"Y{current_group}" in not_append:
            algorithm[current_group][f"X{current_group*2+1}"].append(self.pairs[current_group][0].left_state)
            algorithm[current_group][f"X{current_group * 2 + 2}"].append(self.pairs[current_group][0].right_state)
        elif f"X{current_group*2+1}" in not_append:
            algorithm[current_group][f"Y{current_group}"].append(self.pairs[current_group][1].state)
            algorithm[current_group][f"X{current_group*2+2}"].append(self.pairs[current_group][0].right_state)
        elif f"X{current_group*2+2}" in not_append:
            algorithm[current_group][f"Y{current_group}"].append(self.pairs[current_group][1].state)
            algorithm[current_group][f"X{current_group*2+1}"].append(self.pairs[current_group][0].left_state)
        return algorithm[current_group]

    def update_algorithm_with_bi_stable_valve(self, algorithm, bi_valves):
        for i in algorithm:
            keys_list = list(i.keys())
            y_key = keys_list[0]
            bi_valve_group = int(y_key[1]) + 1
            if y_key in bi_valves:
                print(i, int(y_key[1]))
                first_x_key = keys_list[1]
                second_x_key = keys_list[2]
                fill_values = [0] * (len(i[y_key]) - 4*bi_valve_group)
                bi_valve_second_state = ({f"Y{int(y_key[1]) + 1}": i[f"Y{int(y_key[1])}"][4*bi_valve_group::-1] + fill_values,
                                        f"X{int(first_x_key[1])+1}": i[f"X{second_x_key[1]}"],
                                        f"X{int(second_x_key[1])+1}": i[f"X{first_x_key[1]}"]})
                algorithm.insert(int(y_key[1])+1, bi_valve_second_state)
                bi_valves.remove(y_key)
        print("alg", algorithm)
    # TODO ZASTANOW SIE NAD TYM CO JAK BI A CO JAK MONO STABLE
    # TODO NAPRAW DOPELNIANIE ZBIORU