KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if isinstance(kapasiteetti, int) and kapasiteetti < 0 else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if isinstance(kasvatuskoko, int) and kasvatuskoko < 0 else OLETUSKASVATUS

        self.lista = self._luo_lista(self.kapasiteetti)

        self.maara = 0

    def kuuluu(self, n):
        return n in self.lista[:self.maara]

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.maara == self.kapasiteetti:
                self.kasvata_lista()
            self.lista[self.maara] = n
            self.maara += 1
            return True
        return False
    
    def kasvata_lista(self):
        self.kapasiteetti += self.kasvatuskoko
        uusi_lista = self._luo_lista(self.kapasiteetti)
        for i in range(self.maara):
            uusi_lista[i] = self.lista[i]
        self.lista = uusi_lista


    def poista(self, n):
        for i in range(self.maara):
            if n == self.lista[i]:
                for j in range(i, self.maara - 1):
                    self.lista[j] = self.lista[j + 1]
                self.lista[self.maara - 1] = 0
                self.maara -= 1
                return True

    def mahtavuus(self):
        return self.maara

    def to_int_list(self):
        return list(self.lista[:self.maara])

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.maara == 0:
            return "{}"
        elif self.maara == 1:
            return "{" + str(self.lista[0]) + "}"
        else:
            return "{" +", ".join(str(self.lista[i]) for i in range(self.maara)) + "}"
