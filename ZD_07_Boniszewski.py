import random

def figurki(iteracje):
    wyjscie = 0
    for x in range(iteracje):
        k = 20  
        m = 1000  

        paczki = [0] * m 

        for i in range(m):
            paczki[i] = random.randint(1, k)

        znalezione = []
        for j in range(len(paczki)):
            if paczki[j] not in znalezione:
                znalezione.append(paczki[j])
            if len(znalezione) == 20:
                break
        wyjscie+=j+1

    return wyjscie

iteracje = 1000

print(f"Średnio potrzeba kupić {figurki(iteracje)/iteracje} paczek")

