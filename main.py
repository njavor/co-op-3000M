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