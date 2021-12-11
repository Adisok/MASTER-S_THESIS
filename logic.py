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

# n-liczba zmiennych wyjsciowych
# l_st liczba stanow stabilnych
# l_reg liczba regul = 20
# k liczba zmiennych wejsciowych
# l liczba zmiennych pomocniczcyh
# i,j,R,a,b indeksy pomocniczne
# I_we = k+1
# J_a, J_b, J_j = (X_1, X_2, ..., X_k)u(M_1,M_2,...,M_l)
# J_j to albo zmienna wejsciowa albo element pamieci
# I_reg obecna regula
# R regula

NUMBER_OF_RULES = 20
def main(n, i_in, **kwargs):
    Y = kwargs["Y"]
    X = kwargs["X"]
    fp = kwargs["fp"]
    fk = kwargs["fk"]
    Y_prim = 0
    R=0
    rozwiazanie = []
    # Y_prim musi zwraca rozwiazanie i regule
    for i in range(n):
        R += 1
        j = 0
        if R != NUMBER_OF_RULES+1:
            j += j+1
            if j != i_in+1:
                Y_prim = find_rule(j)
                if Y_prim != Y[i]:
                    rozwiazanie.append(Y_prim)
                    continue
            else:
                for a in range(i_in):
                    b = 0
                    if a != i_in+1:
                        b += 1
                        if b != i_in+1:
                            M = (J_a+m)*J_b
                            Y_prim = find_rule(M)
                            if Y_prim != Y_i:
                                rozwiazanie.append(Y_prim)
                                i_in = i_in + 1
                                break
                                #GO TO i += 1
                        else:
                            continue
                            #GO TO a += 1
                    else:
                        continue
                        #GO TO R=R+1
                        print("Should go to first else")
        else:
            return("Brak rozwiazan")
    print(rozwiazanie)

if __name__ == "__main__":
    main(n=1, i_in=5, **{"Y": [0,1,1,1,0], "fp": [0,1,0,0,0], "fk": [0,0,0,1,0]})
