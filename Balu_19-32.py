from main import Telepules

with open("input.txt","r",encoding="utf8") as f:
	for sor in f:
		s = sor.strip().split("\t")
		t = Telepules(int(s[0]), s[1], s[2], s[3], int(s[4]), int(s[5]), int(s[6]))

def KistérségekLegebbTelepülései(kistérség, legebb):
    legebbtelep = []
    for település in Telepules.lista:
        if (település.kister_bes == kistérség):
            if ((len(legebbtelep) == 0) or (legebb == "legkisebb" and település.terulet < legebb[0].terulet)):
                print("ok")
                legebb.append(település)
            if (legebb == "legnagyobb" and település.terulet > legebb.terulet):
                legebb.append(település)
            if (település.terulet == legebb.terulet):
                legebbtelep += település
    for település in legebbtelep:
        print(f"{legebbtelep[település]}-nek van a {legebb} területe a {kistérség} kistérségben.")

print("19) Melyik a Makói kistérség legkisebb területű települése(i)?")

KistérségekLegebbTelepülései("Makó", "legkisebb")