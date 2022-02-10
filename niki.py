from main import Telepules

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
nN = max(Telepules.lista, key= lambda x: x.nepesseg)
print(f"{nN.nepesseg} fő")
print("16)	Mennyi a legalacsonyabb népességű település lélekszáma?")
kN = min(Telepules.lista, key= lambda x: x.nepesseg)
print(f"{kN.nepesseg} fő")

print("17)	Melyik a legnépesebb település? Írja ki a település nevét és lélekszámát!")
print(f"{nN.nev}: {nN.nepesseg} fő")
print("18)	Melyik a legalacsonyabb népességű település? Írja ki a település nevét és lélekszámát!")
print(f"{kN.nev}: {kN.nepesseg} fő")

print("37)	Melyik településen a legrosszabb a lakáshelyzet? (Egy lakásra a legtöbb lakos jut.)")
print(max(Telepules.lista, key= lambda x: x.nepesseg / x.lakossag).nev)

#20-32

print("20) Melyik a Szegedi kistérség legkisebb területű települése(i)?")
_20 = [x for x in Telepules.lista if x.kister_bes == "Szegedi"]
for elem in [x for x in _20 if x.terulet == min(_20, key = lambda x: x.terulet).terulet]:
    print(elem.nev)
print("21) Melyik a Szentesi kistérség legkisebb területű települése(i)?")
_21 = [x for x in Telepules.lista if x.kister_bes == "Szentesi"]
for elem in [x for x in _21 if x.terulet == min(_21, key = lambda x: x.terulet).terulet]:
    print(elem.nev)
print("22) Melyik a Makói kistérség legnépesebb települése(i)?")
_22 = [x for x in Telepules.lista if x.kister_bes == "Makói"]
for elem in [x for x in _22 if x.nepesseg == max(_22, key = lambda x: x.nepesseg).nepesseg]:
    print(elem.nev)
print("23) Melyik a Szegedi kistérség legnépesebb települése(i)?")
_23 = [x for x in Telepules.lista if x.kister_bes == "Szegedi"]
for elem in [x for x in _23 if x.nepesseg == max(_23, key = lambda x: x.nepesseg).nepesseg]:
    print(elem.nev)
print("24) Melyik a Szentesi kistérség legnépesebb települése(i)?")
_24 = [x for x in Telepules.lista if x.kister_bes == "Szentesi"]
for elem in [x for x in _24 if x.nepesseg == max(_24, key = lambda x: x.nepesseg).nepesseg]:
    print(elem.nev)

print("25) Írja ki a Makói kistérség településeinek népsűrűségét!")
for elem in [x for x in Telepules.lista if x.kister_bes == "Makói"]:
    print(round(elem.nepesseg / elem.terulet, 2))
print("26) Írja ki a Szegedi kistérség településeinek népsűrűségét!")
for elem in [x for x in Telepules.lista if x.kister_bes == "Szegedi"]:
    print(round(elem.nepesseg / elem.terulet, 2))
print("27) Írja ki a Szentesi kistérség településeinek népsűrűségét!")
for elem in [x for x in Telepules.lista if x.kister_bes == "Szentesi"]:
    print(round(elem.nepesseg / elem.terulet, 2))
print("28) Írja ki a Kisteleki kistérség településeinek népsűrűségét!")
for elem in [x for x in Telepules.lista if x.kister_bes == "Kisteleki"]:
    print(round(elem.nepesseg / elem.terulet, 2))

print("29) Igaz-e, hogy minden Makói kistérségű település lélekszáma nagyobb, mint 1000?")
print("30) Igaz-e, hogy minden Szentesi kistérségű település lélekszáma kisebb, mint 10000?")
print("31) Igaz-e, hogy minden Szegedi kistérségű település lélekszáma nagyobb, mint 2000?")
print("32) Igaz-e, hogy minden Kisteleki kistérségű település lélekszáma kisebb, mint 10000?")