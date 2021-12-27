from rules import Rules
# f_pi i f_ki i F(Y_i) <- podstawy do wyznacznia rownania schematowego
# przedstawia to w przejrzysty sposob zmiany stanow wejscia i wyjscia ukladu sterowania
# WYKORZYSTUJEMY TYLKO STANY STABILNE


# ZASDA DZIALANIA:
# 1. Wyznaczanie zaleznosci f_pi i f_ki okreslajacych funkcji F(Y_i)
# 2. Przedstawienie w sposob graficzny zaleznosci f_pi * f_ki
# 3. Analiza zaleznozci f_pi, f_ki oraz f_pi * f_ki, co daje
#    regule realizacji pamieci, ktora spelnia postulaty wznaczone przez iloczyn f_pi * f_ki
# 4. Wyznaczenie zaleznosci f_pi' i f_ki' ktore spelnia zaleznosc:
#    F_1(Y_i) = f_pi' * f_ki'
# 5. Powtorzenie 1-4 co da funkcje zmiennych wyjsciowych F_1(Y_i) i pomocniczych F_2(M_j)

# REGUlA REALIZACJI PAMIECI
# 1. Czas przed realizacjia etapu Z_n
# 2. Rozpoczecie realizacji stanu Z_n,
# f_pi zmienia stan 0 -> 1
# 3. Czas trwania stanu Z_n, f_pi = 1
# 4. Zakonczenie stanu Z_n,
# f_ki zmienia sie 1 -> 0
# 5. Czas po realizacji etapu Z_n
# W etapach 1,3,5 iloczyn f_pi i f_ki = {0,1,P}
# gdzie, P jest to na zmianne 0 lub 1
# W przediale 2 f_pi = 1, a w 4 0 lub 1
# W przedziale 4 f_ki = 1, a w 2 0 lub 1 dla obu zmiennych


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
