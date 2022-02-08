from main import Telepules

def Hany(lista, rang, filt):
    res = 0
    for elem in lista:        
        if filt(elem) and elem.rang == rang: res+=1
    return res

def Nep(lista, rang, filt):
    for elem in lista:
        if filt(elem) and elem.rang == rang:
            print(f"{elem.nev}: {elem.nepesseg} fő")

def Leg(lista, filt):
    leg = lista[0]
    for elem in lista:
        if filt(elem, leg): leg = elem
    return(leg)

def Bad(lista):
    worst = lista[0]
    for elem in lista:
        if (worst.nepesseg / worst.lakossag) < (elem.nepesseg / elem.lakossag):
            worst = elem
    return worst

print("1)	Hány település található az input fájlban?")
print(len(Telepules.lista))

print("2)	Hány község rangú település található?")
print(Hany(Telepules.lista, "község", lambda x: True))
print("3)	Hány város rangú település található?")
print(Hany(Telepules.lista, "város", lambda x: True))
print("4)	Van-e falu rangú település?")
print("Van" if 0 < Hany(Telepules.lista, "falu", lambda x: True) else "Nincs")

print("5)	Hány község rangú település található a Makói kistérségben?")
print(Hany(Telepules.lista, "község", lambda x: x.kister_bes == "Makói"))
print("6)	Hány község rangú település található a Szegedi kistérségben?")
print(Hany(Telepules.lista, "község", lambda x: x.kister_bes == "Szegedi"))
print("7)	Hány község rangú település található a Szentesi kistérségben?")
print(Hany(Telepules.lista, "község", lambda x: x.kister_bes == "Szentesi"))
print("8)	Hány város rangú település található a Makói kistérségben?")
print(Hany(Telepules.lista, "város", lambda x: x.kister_bes == "Makói"))
print("9)	Hány város rangú település található a Szegedi kistérségben?")
print(Hany(Telepules.lista, "város", lambda x: x.kister_bes == "Szegedi"))
print("10)	Hány város rangú település található a Szentesi kistérségben?")
print(Hany(Telepules.lista, "város", lambda x: x.kister_bes == "Szentesi"))

print("11)	Írja ki a község rangú települések közül az 1000 főnél népesebb települések nevét és népességét!")
Nep(Telepules.lista, "község", lambda x: x.nepesseg > 1000)
print("12)	Írja ki a város rangú települések közül az 10000 főnél népesebb települések nevét és népességét!")
Nep(Telepules.lista, "város", lambda x: x.nepesseg > 1000)
print("13)	Írja ki a község rangú települések közül az 1000 főnél alacsonyabb népességű települések nevét és népességét!")
Nep(Telepules.lista, "község", lambda x: x.nepesseg < 1000)
print("14)	Írja ki a város rangú települések közül az 5000 főnél alacsonyabb népességű települések nevét és népességét!")
Nep(Telepules.lista, "város", lambda x: x.nepesseg < 5000)

print("15)	Mennyi a legnépesebb település lélekszáma?")
nagyN = Leg(Telepules.lista, lambda x,y: x.nepesseg > y.nepesseg)
print(f"{nagyN.nepesseg} fő")
print("16)	Mennyi a legalacsonyabb népességű település lélekszáma?")
kisN = Leg(Telepules.lista, lambda x,y: x.nepesseg < y.nepesseg)
print(f"{kisN.nepesseg} fő")

print("17)	Melyik a legnépesebb település? Írja ki a település nevét és lélekszámát!")
print(f"{nagyN.nev}: {nagyN.nepesseg} fő")
print("18)	Melyik a legalacsonyabb népességű település? Írja ki a település nevét és lélekszámát!")
print(f"{kisN.nev}: {kisN.nepesseg} fő")

print("37)	Melyik településen a legrosszabb a lakáshelyzet? (Egy lakásra a legtöbb lakos jut.)")
print(Bad(Telepules.lista).nev)