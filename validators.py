def sprawdz_sume_kontrolna(pesel):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0
    
    for i in range(10):
        suma += int(pesel[i]) * wagi[i]

    reszta = suma % 10
    if reszta == 0:
        cyfra_kontrolna = 0
    else:
        cyfra_kontrolna = 10 - reszta
    
    return cyfra_kontrolna == int(pesel[10])


def sprawdz_plec(pesel, plec):
    cyfra_plci = int(pesel[9])
    czy_kobieta = (cyfra_plci % 2 == 0)

    plec_input = plec.strip().upper()

    if plec_input == "K" :
        return czy_kobieta
    elif plec_input == "M":
        return not czy_kobieta
    else:
        return False
    



def sprawdz_pesel(pesel, plec=None):
    if not pesel.isdigit() or len(pesel) != 11:
        return False,  "PESEL musi składać się z 11 cyfr."
    
    if not sprawdz_sume_kontrolna(pesel):
        return False, "Nieprawidłowa suma kontrolna PESEL."
    
    if plec:
        if not sprawdz_plec(pesel, plec):
            return False, f"Płeć z PESELu nie zgadza się z podaną ({plec})."

    return True, "Pesek poprawny."