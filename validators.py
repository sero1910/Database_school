def sprawdz_pesel(pesel):
    if not pesel.isdigit() or len(pesel) != 11:
        return False,  "PESEL musi składać się z 11 cyfr."
    # TODO: Tu później dodamy sprawdzanie sumy kontrolnej
    # TODO: Tu dodamy weryfikację daty i płci
    
    return True, "Pesek poprawny."

def sprawdz_plec(pesel, plec):
    #TODO: Zaimplementować logikę (cyfry parzyste/nieparzyste)
    return True