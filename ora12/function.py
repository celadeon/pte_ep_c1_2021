def megtalal(karakter: str, szoveg: str) -> int:
    """
    karakter poziciojanak megkeresese a szovegben
    :param karakter: adott karakter
    :param szoveg: adott szoveg
    :return: a karakter pozicioja a szovegben, -1 ha nincs benne
    """
    for i in range(len(szoveg)):
        if szoveg[i] == karakter:
            return i
    return -1

def kacsanevek(prefixes='JKLMNOPQ', suffix='ack') -> list[str]:
    nevek = []
    for kezdo_betu in prefixes:
        nevek.append(kezdo_betu + suffix)
    return nevek

print(megtalal("x", "Indul a pap aludni"))
print("Indul a pap aludni".find("x"))
print(kacsanevek())