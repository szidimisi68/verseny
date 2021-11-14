fajl = open("alaprajz1.txt", "r")
elso_sor = fajl.readline()
szavak = elso_sor.split(" ")
sorok_szama = int(szavak[0])
tablazat = []
oszlopok_szam = 14


def minim(so):  # az so helyére sor vagy oszlop kerül
    if so != 0:
        return so - 1
    else:
        return so


def maxim(so, maxi):
    if so != maxi:
        return so + 2
    else:
        return so + 1


for a in range(sorok_szama):
    temp_sor = fajl.readline()
    sor = []
    for kar in temp_sor:
        if kar == '0' or kar == '1':
            sor.append(kar)
    tablazat.append(sor)

print(tablazat)

oszlopok_szam = 14
sorok_szama = 11
szekek = 0
kanapek = 0
kanape_keresett_szama = 2
kanape_kordinata = [0, 0]
already_checked_kanape = [0, 0]
check_so = [0, 0]

for sor_index in range(0, sorok_szama):
    for oszlop_index in range(0, oszlopok_szam):
        szam = tablazat[sor_index][oszlop_index]
        if szam == '1':  # csak akkor vizsgálja meg a számot ha 1
            check_szek = 0  # a check minden karakternek külön nézi hogy megvan-e a 8 0-karakter körülötte
            check_kanape = 0
            for sor_index_2 in range(minim(sor_index), maxim(sor_index, 10)):
                for oszlop_index_2 in range(minim(oszlop_index), maxim(oszlop_index, 13)):  # ez a 2 darab 2 for felel a karakter körüljárásáért.
                    keresett = tablazat[sor_index_2][oszlop_index_2]  # egyesével nézi körbe a karakter körüli mezőket
                    if keresett == '0':  # ha nulla akkor hozzá egyet a checkhez amiből 8 esetén végig nulla van körülötte.
                        check_szek += 1
                        if check_szek == 8:
                            szekek += 1  # ha kigyűlt a 8 check azt jelenti, hogy a mező egy szék
                    if keresett == '1':
                        if already_checked_kanape[0] != sor_index_2 and already_checked_kanape[1] != oszlop_index_2:
                            check_kanape += 1
                            kanape_kordinata = [sor_index_2, oszlop_index_2]
                            already_checked_kanape = [sor_index_2, oszlop_index_2]
            if check_kanape == 1:
                while check_kanape == 1 and already_checked_kanape[0] != check_so[0] and already_checked_kanape[1] != check_so[1]:
                    kanape_keresett_szama = 0
                    for sor_index_3 in range(minim(kanape_kordinata[0]), maxim(kanape_kordinata[0], 10)):
                        for oszlop_index_3 in range(minim(kanape_kordinata[1]), maxim(kanape_kordinata[1], 13)):  # ez a 2 darab 2 for felel a karakter körüljárásáért.
                            if tablazat[sor_index_3][oszlop_index_3] == "1":
                                kanape_keresett_szama += 1
                                already_checked_kanape = [sor_index_3, oszlop_index_3]
                    kanape_kordinata = [already_checked_kanape[0], already_checked_kanape[1]]
                    check_so = [already_checked_kanape[0], already_checked_kanape[1]]
                    if kanape_keresett_szama == 2 or kanape_keresett_szama == 5:
                        kanapek += 1
                        check_kanape = 0
                    else:
                        check_kanape = 0

print(szekek)
print(kanapek)
"""
for sor_index in range(0, sorok_szama):
    for oszlop_index in range(0, oszlopok_szam):
        szam = tablazat[sor_index][oszlop_index]
        if szam == '0':
            tablazat[sor_index][oszlop_index] = "."
        elif szam == '1':
            tablazat[sor_index][oszlop_index] = "*"
print(tablazat)
"""
# tablazat[sor_index][oszlop_index] = '.' if tablazat[sor_index][oszlop_index] == "0" else "*"

"""
def keres(tabla):
    oszlopok_szam = 14
    sorok_szama = 11
    szekek = 0
    for sor_index in range(0, sorok_szama):
        for oszlop_index in range(0, oszlopok_szam):
            szam = tablazat[sor_index][oszlop_index]
            if szam == '1':
                check = 0
                for sor_index_2 in range(min(sor_index), max(sor_index, 10)):
                    for oszlop_index_2 in range(min(oszlop_index), max(oszlop_index, 13)):
                        if sor_index_2 != sor_index and oszlop_index_2 != oszlop_index:
                            keresett = tabla[sor_index_2][oszlop_index_2]
                            if keresett == '1':
                                pass
                            elif keresett == '0':
                                check += 1
                                if check == 8:
                                    szekek += 1
    return szekek
"""
