#26
class Oqish:
    def __init__(self, ism):
        self.ism = ism

    def oynash(self):
        print("O'ynayapti", end=" ")


class Geymer(Oqish):
    def oynash(self):
        super().oynash()
        print(", Video o'yin o'ynayapti")


o1 = Oqish("Ali")
g1 = Geymer("Vali")

o1.oynash()
g1.oynash()


#27
class Suv:
    def __init__(self, hajm):
        self.hajm = hajm

    def ichish(self):
        print("Ichildi", end=" ")


class IchimlikSuv(Suv):
    def ichish(self):
        super().ichish()
        print(", Toza suv ichildi")


s1 = Suv(1.5)
i1 = IchimlikSuv(2.5)

s1.ichish()
i1.ichish()
