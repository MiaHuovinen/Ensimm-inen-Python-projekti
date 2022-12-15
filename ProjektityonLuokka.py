#Tässä luokassa on määritelty eri lisien määrät/kertoimet.
#metodit tallentavat määreitä myös listaan talteen.
# __init__ alustuksen alla on muuttujia joihin metodit tallettavat tietoja ja käyttävät niitä uudestaan laskelmissa
#Vakioarvot/kertoimet metodien laskukaavoissa on sote-alan tessin mukaiset kertoimet
class SOTEpalkka:
    def __init__(self):
        self.palkka = 0
        self.palkkatunnissa = 0
        self.lista = []
    
    def tuntipalkka(self,tuntipalkanMaara):
        self.palkkatunnissa = tuntipalkanMaara
        self.lista.extend(("Tuntipalkka:",tuntipalkanMaara))
        return self.palkkatunnissa
    
    def tyotunnit(self, tuntienMaara):
        self.tunnit = self.palkkatunnissa*tuntienMaara
        self.palkka += self.tunnit
        self.lista.extend(("Tehdyt tunnit:",tuntienMaara))
        
    def iltalisat(self, tuntienMaara):
        self.iltalisa = self.palkkatunnissa*0.15*tuntienMaara
        self.palkka += self.iltalisa
        self.lista.extend(("Tehdyt iltatunnit:",tuntienMaara))
        
    def lauantailisat(self, tuntienMaara):
        self.lauantailisa = self.palkkatunnissa*0.25*tuntienMaara
        self.palkka += self.lauantailisa
        self.lista.extend(("Tehdyt lauantaitunnit:",tuntienMaara))
        
    def sunnuntailisat(self, tuntienMaara):
        self.sunnuntailisa = self.palkkatunnissa*tuntienMaara
        self.palkka += self.sunnuntailisa
        self.lista.extend(("Tehdyt sunnuntaitunnit:", tuntienMaara))

    def yolisat(self, tuntienMaara):
        self.yolisa = self.palkkatunnissa*0.4*tuntienMaara
        self.palkka += self.yolisa
        self.lista.extend(("Tehdyt yötunnit:", tuntienMaara))

    def palkkalaskelma(self):
        self.palkka = round(self.palkka, 2)
        print(f"Bruttopalkkasi on yhteensä {self.palkka} euroa")
    
    def lomakorvaus(self):
        määrä = round(self.palkka*1.09, 2)
        print(f"Bruttopalkkasi lomakorvauksen kanssa on yhteensä: {määrä} euroa.")

