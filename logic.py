from rules import Rules

NUMBER_OF_RULES = 20

def main(**kwargs):
    Y = kwargs["Y"]
    fp = kwargs["fp"]
    fk = kwargs["fk"]
    rozwiazanie = dict()
    for i in range(1, NUMBER_OF_RULES + 1):
        rozwiazanie[Rules[i].__name__] = Rules[i](Y, fp, fk)
    print({i: j for i, j in rozwiazanie.items() if j is True})

if __name__ == "__main__":
    main(**{"Y": [0, 1, 1, 1, 0], "fp": [0, 1, 0, 0, 0], "fk": [0, 0, 0, 1, 0]})
