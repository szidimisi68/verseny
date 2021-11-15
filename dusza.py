belepesi_valasz = input("belép vagy regisztrál? ")
karakter_ellenor = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9","0"]
szamok_lista = ["1","2","3","4","5","6","7","8","9","0"]
karakterek_szama = 0
felhasznalo_nevek = ["alma", "körte", "medve"]
jelszavak = ["fafafa", "szalma", "disznó"]
siker = False
n = 0


#Megnézi, hogy az általad megadott felhasználó névhez, az ahhoz tartozó jelszavat adtad-e meg.
def belepesteszt():
    global n
    n = 0
    while not siker:
        adatok = open("adatok", "w")
        felhasznalo_nev = input("Felhasznaló neved: ")
        jelszo = input("Jelszavad: ")
        for fel in felhasznalo_nevek:
            proba = False
            while not proba:
                a = str(adatok.readline())
                if a[-5] == " ":
                    temp_felhasznalo = a[0:-5]
                elif a[-3] in szamok_lista:
                    temp_jelszo = a[-4:-1]
                    proba = True
            if temp_felhasznalo == felhasznalo_nev and temp_jelszo == jelszo:
                belepes()
            n += 1
        if siker == False:
            sikertelen_belepes()


#Ha sikertelen a bejelntkezés, ezt írja ki. Ezután újra lehet próbálkozni.
def sikertelen_belepes():
    print("\nHibás felhasználónév és/vagy jelszó!\n\n")
    belepesteszt()

#Ha sikeresen bejelentkeztél, akkor ez történik.
def belepes():
    global siker
    print("Üdvözöllek " + str(felhasznalo_nevek[n]) + "!")
    siker = True


def regisztral():
    helyes_jelszo = False
    jelszo = input("jelszava: ")
    while not helyes_jelszo:
        for karakter in jelszo:
            if karakter == " ":
                print("nem tartalmazhat szóközt!")
                regisztral()
                break
            if karakter not in karakter_ellenor:
                print("csak szám, kis és nagy angol betü lehet!")
                regisztral()
                break
            karakterek_szama = len(jelszo)
            if karakterek_szama >= 11 or karakterek_szama <= 7:
                print("8 és 10 karakter hosszúság között lehet!")
                regisztral()
                break
        if len(jelszo) < 10:
            while len(jelszo) == 10:
                jelszo = jelszo + "d"
        helyes_jelszo = True
        return jelszo


if belepesi_valasz == "regisztrál":
    email_cim = input("email cím neve: ")
    """regisztral()"""
    jelszo = regisztral()
    jelszo_2 = input("jelvasza újra: ")
    felhasznalo_nev = "dusza.hu"
    while jelszo != jelszo_2:
        print("Nem egyeznek a jelszavak!")
        jelszo = regisztral()
        jelszo_2 = input("jelvasza újra: ")

    print("Sikeresen regisztrált egy felhasználót!")
    file = open("adatok" "w")
    file.write(felhasznalo_nev + " " + str(ord(jelszo)) + "\n")

if belepesi_valasz == "belép":
    belepesteszt()
