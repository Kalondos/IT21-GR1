# karl eerik kotter
# 13.04.22
# ul2

extends Node

func _ready():
	#isiku raha
	var raha = 5
	
	#toode
	var toode = "kandoss"
	var tootehind = 3.99
	
	#v2ljastab palju isikul on raha
	print("Teil on ",raha," eurot")
	#väljastab toote hinna ja nime
	print("Toode: ",toode," on ",tootehind," eurot")
	
	#prindib vastuse vastaval rahalisele olukorrale
	if raha >= tootehind:
		print("teil on piisavalt raha, et osta toode: ",toode,". Teil jääb üle ",raha - tootehind," eurot")
	else:
		print("Teil ei ole piisavalt raha, et osta toodet: ",toode,". Teil jääb puudu ",raha - tootehind," eurot")
	
	
