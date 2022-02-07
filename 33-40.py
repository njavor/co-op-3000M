from main import Telepules

"""
33)	Írja ki a Makói kistérség településeinek egy lakásra jutó népesség számát!
34)	Írja ki a Szentesi kistérség településeinek egy lakásra jutó népesség számát!
35)	Írja ki a Szegedi kistérség településeinek egy lakásra jutó népesség számát!
36)	Írja ki a Kisteleki kistérség településeinek egy lakásra jutó népesség számát!
37)	Melyik településen a legrosszabb a lakáshelyzet? (Egy lakásra a legtöbb lakos jut.)
38)	Készítsen kimutatást kistérségi bontásban, amelyben megadja az egyes kistérségek településeinek a számát!
39)	Készítsen kimutatást kistérségi bontásban, amelyben megadja az egyes kistérségek összlakosságának a számát!
40)	Készítsen kimutatást kistérségi bontásban, amelyben megadja az egyes kistérségek összterületének a nagyságát!
"""

#33-36

def térségek_lakására_jutók(lista, bekistérség):
    népesség_ered=0
    lakások=0
    for elem in lista:
        if elem.kister_bes==bekistérség:
            népesség_ered+=elem.nepesseg
            lakások+=elem.lakossag
    print (népesség_ered, lakások)
    népesség_ered/=lakások
    print (népesség_ered)
print(térségek_lakására_jutók(Telepules.lista,"Makói"))
#37

#38-40

def kimutatások(lista, adat):
    első=lista[0].kister_bes
    kisterseg={}
    i =1
    while i<len(lista):

        i+=1   
        


