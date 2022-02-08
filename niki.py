from main import Telepules

def Bad(lista):
    worst = lista[0]
    for elem in lista:
        if (worst.nepesseg / worst.lakossag) < (elem.nepesseg / elem.lakossag):
            worst = elem
    return worst

print("1)	Hány település található az input fájlban?")
print(len(Telepules.lista))

print("2)	Hány község rangú település található?")
print(len(list(filter(lambda x: x.rang == "község",Telepules.lista))))
print("3)	Hány város rangú település található?")
print(len(list(filter(lambda x: x.rang == "város",Telepules.lista))))
print("4)	Van-e falu rangú település?")
print("Van" if 0 < len(list(filter(lambda x: x.rang == "falu" and x.kister_bes == "Makói",Telepules.lista))) else "Nincs")

print("5)	Hány község rangú település található a Makói kistérségben?")
print(len(list(filter(lambda x: x.rang == "község" and x.kister_bes == "Makói",Telepules.lista)))) #Farkasról copy-zva
print("6)	Hány község rangú település található a Szegedi kistérségben?")
print(len(list(filter(lambda x: x.rang == "község" and x.kister_bes == "Szegedi",Telepules.lista))))
print("7)	Hány község rangú település található a Szentesi kistérségben?")
print(len(list(filter(lambda x: x.rang == "község" and x.kister_bes == "Szentesi",Telepules.lista))))
print("8)	Hány város rangú település található a Makói kistérségben?")
print(len(list(filter(lambda x: x.rang == "város" and x.kister_bes == "Makói",Telepules.lista))))
print("9)	Hány város rangú település található a Szegedi kistérségben?")
print(len(list(filter(lambda x: x.rang == "város" and x.kister_bes == "Szegedi",Telepules.lista))))
print("10)	Hány város rangú település található a Szentesi kistérségben?")
print(len(list(filter(lambda x: x.rang == "város" and x.kister_bes == "Szentesi",Telepules.lista))))

print("11)	Írja ki a község rangú települések közül az 1000 főnél népesebb települések nevét és népességét!")
eleven = [x for x in Telepules.lista if x.rang == "község" and x.nepesseg > 1000]
for elem in eleven: print(f"{elem.nev}: {elem.nepesseg}")
print("12)	Írja ki a város rangú települések közül az 10000 főnél népesebb települések nevét és népességét!")
twelwe = [x for x in Telepules.lista if x.rang == "város" and x.nepesseg > 1000]
for elem in twelwe: print(f"{elem.nev}: {elem.nepesseg}")
print("13)	Írja ki a község rangú települések közül az 1000 főnél alacsonyabb népességű települések nevét és népességét!")
thirteen = [x for x in Telepules.lista if x.rang == "község" and x.nepesseg < 1000]
for elem in thirteen: print(f"{elem.nev}: {elem.nepesseg}")
print("14)	Írja ki a város rangú települések közül az 5000 főnél alacsonyabb népességű települések nevét és népességét!")
fourteen = [x for x in Telepules.lista if x.rang == "város" and x.nepesseg < 5000]
for elem in fourteen: print(f"{elem.nev}: {elem.nepesseg}")

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