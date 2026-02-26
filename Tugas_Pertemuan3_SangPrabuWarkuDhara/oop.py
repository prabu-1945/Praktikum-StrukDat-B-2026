class Spiderman:
    def __init__(self, Jaring, Baju, Topeng):
        self.Jaring = Jaring
        self.Baju = Baju
        self.Topeng = Topeng

    def getPeter(self):
        return self.Jaring

    def getAgus(self):
        return self.Baju

    def getMail(self):
        return self.Topeng

    def ubahtopeng(self, Kairil):
        self.Topeng = Kairil



hero1 = Spiderman("Panjang", "hitam", "hitam")
hero2 = Spiderman("Kuat", "merah", "merah")
hero3 = Spiderman("pendek", "biru", "biru")

print(hero1.getPeter())
print(hero2.getAgus())
print(hero3.getMail())
hero3.ubahtopeng("terserah")
print(hero3.getMail())