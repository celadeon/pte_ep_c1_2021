class Kutya:
    """
    kutyak oszatlya
    """
    def __init__(self, nev: str, fajta: str):
        self.nev = nev
        self.fajta = fajta

    def __str__(self):
        return "a {} nevu kutya {} fajtaju".format(self.nev, self.fajta)


kutya1 = Kutya("bodri", "kuvasz")
kutya2 = Kutya("buksi", "puli")

print(kutya1)
print(kutya2)
