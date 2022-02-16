
'''
Karl Eerik Kotter
ulesanne 08
16.02.2022
'''

class Auto:
#atribuudid
    mark = 'Kadunud'
    aasta = 0
    hind = 0
    kiirus = 0
    varv  = 'puudub'

    def lisamark(self,x):
        self.mark = x
    def lisaaasta(self,x):
        self.aasta = x
    def lisahind(self,x):
        self.hind = x
    def lisavarv(self,x):
        self.varv = x
    def lisakiirus(self,x):
        self.kiirus = x

    def kuva(self):
        print(f"{self.mark} {self.aasta} {self.varv} {self.kiirus} {self.hind}")
        
uusObjekt = Auto() 
uusObjekt.lisamark('Nissan')
uusObjekt.lisavarv('Sinine')
uusObjekt.lisaaasta(2000)
uusObjekt.lisahind('420€')
uusObjekt.lisakiirus('300km/h')
uusObjekt.kuva()


uusAuto = Auto()
uusAuto.lisamark('BMW')
uusAuto.lisaaasta(2007)
uusAuto.lisavarv('Punane')
uusAuto.lisahind('2300€')
uusAuto.lisakiirus('255km/h')
uusAuto.kuva()
