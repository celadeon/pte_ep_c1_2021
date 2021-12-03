def rendez(lista: list[int]) -> list[int]:
    rendezett_lista = lista.copy()
    for i in range(1, len(lista)):
        for j in range(len(lista) - i):
            if rendezett_lista[j] > rendezett_lista[j + 1]:
                seged = rendezett_lista[j]
                rendezett_lista[j] = rendezett_lista[j + 1]
                rendezett_lista[j + 1] = seged
    return rendezett_lista


def minimum(lista: list[int], hanyadik: int) -> int:
    return rendez(lista)[hanyadik]

def osszeg(lista: list[int]) -> int:
    oszzeg = 0
    for i in range(len(lista)):
        oszzeg += lista[i]
    return osszeg

def atlag(lista: list[int]) -> float:
    return osszeg(lista)/len(lista)

lista = [43, 12, 34, 2, 75, 23 ,77 ,23 ,99]
print(lista)
print(rendez(lista))
print(minimum(lista, 3))
print(osszeg(lista))
print(atlag(lista))