class Telepules:
    lista = []
    def __init__(self, az, ne, ra, kb, th, nep, tllsz):
        self.azonosito = az
        self.nev = ne
        self.rang = ra
        self.kister_bes = kb
        self.terulet = th
        self.nepesseg = nep
        self.lakossag = tllsz
        Telepules.lista.append(self)

with open("input.txt","r",encoding="utf8") as f:
	for sor in f:
		s = sor.strip().split("\t")
		t = Telepules(int(s[0]), s[1], s[2], s[3], int(s[4]), int(s[5]), int(s[6]))