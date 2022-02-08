from main import Telepules

#33-36

def térségek_lakására_jutók(lista, bekistérség):
    népesség_ered=0
    lakások=0
    for elem in lista:
        if elem.kister_bes==bekistérség:
            népesség_ered+=elem.nepesseg
            lakások+=elem.lakossag
    népesség_ered/=lakások
    print (népesség_ered)
print("33)	Írja ki a Makói kistérség településeinek egy lakásra jutó népesség számát!")
térségek_lakására_jutók(Telepules.lista,"Makói")

print("34)	Írja ki a Szentesi kistérség településeinek egy lakásra jutó népesség számát!")
térségek_lakására_jutók(Telepules.lista,"Szentesi")

print("35)	Írja ki a Szegedi kistérség településeinek egy lakásra jutó népesség számát!")
térségek_lakására_jutók(Telepules.lista,"Szegedi")

print("36)	Írja ki a Kisteleki kistérség településeinek egy lakásra jutó népesség számát!")
térségek_lakására_jutók(Telepules.lista,"Kisteleki")

#38
def kisterseg_telepules(lista):
    kisterseg={}
    i =0
    while i<len(lista):
        if not lista[i].kister_bes in kisterseg.keys():
            kisterseg[lista[i].kister_bes] =1
        else:
            kisterseg[lista[i].kister_bes] +=1
        i+=1  
    print(kisterseg)
print("38)	Készítsen kimutatást kistérségi bontásban, amelyben megadja az egyes kistérségek településeinek a számát!")
kisterseg_telepules(Telepules.lista)

#39
def kisterseg_lakosok(lista):
    kisterseg={}
    i =0
    while i<len(lista):
        if not lista[i].kister_bes in kisterseg.keys():
            kisterseg[lista[i].kister_bes] =lista[i].nepesseg
        else:
            kisterseg[lista[i].kister_bes] +=lista[i].nepesseg
        i+=1  
    print(kisterseg) 
print("39)	Készítsen kimutatást kistérségi bontásban, amelyben megadja az egyes kistérségek összlakosságának a számát!")
kisterseg_lakosok(Telepules.lista)

#40
def kisterseg_terület(lista):
    kisterseg={}
    i =0
    while i<len(lista):
        if not lista[i].kister_bes in kisterseg.keys():
            kisterseg[lista[i].kister_bes] =lista[i].terulet
        else:
            kisterseg[lista[i].kister_bes] +=lista[i].terulet
        i+=1   
    print(kisterseg)
print("40)	Készítsen kimutatást kistérségi bontásban, amelyben megadja az egyes kistérségek összterületének a nagyságát!")
kisterseg_terület(Telepules.lista)

