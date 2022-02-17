'''
Karl Eerik helikopter helikopter
ulesanne nein
17.02.2022
'''

import datetime

#kuud
kuud = ["Jaanuar","Veebruar","Märts"]
#Praegune kuupaev
kuup = datetime.date.today()
#kuu
kuu = int(kuup.month)
kuup2 = datetime.date(kuup.year, kuu , kuup.day)
print(kuup2.strftime("%d")+". "+str(kuud[kuu-1])+" "+kuup2.strftime("%Y"))





#isikukood


ikood = "50509266969"
aasta = int("20"+ikood[1]+ikood[2])
kuu = int(ikood[3]+ikood[4])
paev = int(ikood[5]+ikood[6])

sunnipaev = datetime.date(aasta, kuu, paev)
print(sunnipaev)

#praegune vanus päevades, kuna yolo
vanus = (kuup2 - sunnipaev)
print(vanus)

#def vanus(sund):
 #   kuup3 = date.today()
  #  vanus = kuup3.aasta - sund.aasta - ((kuup3.kuu, kuup3.paev) < (sund.kuu, sund.paev))    
   
   #print(vanus)










	
