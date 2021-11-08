fajl = open("alaprajz1.txt", "r")
elso_sor = fajl.readline()
szavak = elso_sor.split(" ")
sorok_szama = int(szavak[0])
tempor_sor = -1
tempor_oszlop = -1
tablazat = []


def keres(tablazat):
    for s in tablazat:
        temporar_sor = -1
        temporar_sor += 1
        temporar_oszlop = -1
        for o in s:
            temporar_oszlop += 1
            if o == '1':
                check = 0
                for c in range(0, 3):
                    if temporar_sor != 0:
                        temporar_sor -= 1
                    for d in range(0, 3):
                        if temporar_oszlop != 1:
                            temporar_oszlop -= 1
                            keresett = tablazat[temporar_sor][temporar_oszlop]
                            if keresett == '1':
                            if keresett == '0':
                                check += 1

                temporar_sor += 1
            elif b == '0':
                pass


for a in range(sorok_szama):
    temp_sor = fajl.readline()
    sor = []
    for kar in temp_sor:
        if kar == '0' or kar == '1':
            sor.append(kar)
    tablazat.append(sor)

print(tablazat)


for a in tablazat:
    tempor_sor += 1
    tempor_oszlop = -1
    for b in a:
        tempor_oszlop += 1
        if b == '0':
            tablazat[tempor_sor][tempor_oszlop] = "."
        elif b == '1':
            tablazat[tempor_sor][tempor_oszlop] = "*"
print(tablazat)

"""
oszlopok_szam=14
for oszlop_index in range(oszlopok_szam):
    for sor_index in range(sorok_szama):
        szam = tablazat[oszlop_index][sor_index]
        if szam == '0':
            tablazat[sor_index][oszlop_index] = "."
        elif szam == '1':
            tablazat[sor_index][oszlop_index] = "*"
"""
# tablazat[sor_index][oszlop_index] = '.' if tablazat[sor_index][oszlop_index] == "0" else "*"
