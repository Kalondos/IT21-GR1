extends Node

func parameeter():
	
	#tunnid
	var tunnid = 50
	#tunnitasi
	var tunnitasu = 5
	#palk/tasu
	var tasu = 0
	#kui tunde on 40 v siis rohkem, siis korrutatakse tunnid ka tunnitasu kokku
	if tunnid > 40:
		tasu = tunnid * tunnitasu
		print("teie tasu: ", tunnid*tunnitasu)
	else:
		#kui on vähem kui 40h siis korrutatakse teistmoodi
		print("Teie tasu: ", 40*tunnitasu+(tunnid-40)*1.5*tunnitasu)
		
		
		
		
		
		
func eksam():
	#punktid
	var punktid = [7,28,64,51,81,40,21,73,34,98,39,17,33,85,35,44]	
	#iga punkt funktsioonis punktid
	for punkt in punktid:
		#kui on rohkem kui 90 punktii saab 5
		if punkt > 90:
			print(punkt,"p", " - 5")
			#kui on 75 v rohkem punkte saab 4
		elif punkt > 75:
			print(punkt,"p", " - 4")
			#kui on 50 v rohkem punkte saab 3 
		elif punkt > 50:
			print(punkt,"p", " - 3")
			#kui on alla 50 punkti saab hindeks 2
		else:
			print(punkt,"p", " - 2")

# ma ei taju kuidas neid väljastada


