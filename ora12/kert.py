def menu_opciok():
    print("valaszon a menupontok kozul: \n\t0 - kilepes"
          "\n\t1 - uj fa"
          "\n\t2 - fafajta lekerdezese")

def egesz_szam_bekerese(koordinata: int):
    szam = ""
    while szam == "":
        try:
            szam = int(input(f"adja meg {koordinata} koordinatat"))
        except ValueError:
            print("nem egesz szam")
    return szam

def fa_regisztralasa(fak):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely in fak:
        print("itt mar van fa")
    else:
        fak[hely] = input("adja mega a fajtajat")
        print("sikeres regisztracio")

def szotar_kiiratasa(szotar, filepath):
    fileobject = open(filepath, "w")
    for kulcs in szotar:
        fileobject.write(str(kulcs[0]))
        fileobject.write("\t")
        fileobject.write(str(kulcs[1]))
        fileobject.write("\t")
        fileobject.write(szotar[kulcs])
        fileobject.write("\n")
    fileobject.close()

def szotar_betoltes(filepath: str):
    szotar = {}
    file = open(filepath, "r")
    for sor in file:
        adat = sor.strip().split("\t")
        szotar[adat[0], int(adat[1])] = adat[2]
    file.close()
    return szotar

def fafajta_lekerdezese(fak):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely in fak:
        print(fak[hely])
    else:
        print("nincs ezen a helyen fa")

menu = ""
fak_szotar_filepath = "fak.csv"
fak = szotar_betoltes(fak_szotar_filepath)
while menu != "0":
    menu_opciok()
    menu = input()
    if menu == "1":
        fa_regisztralasa(fak)
    elif menu == "2":
        fafajta_lekerdezese(fak)

szotar_kiiratasa(fak, fak_szotar_filepath)
