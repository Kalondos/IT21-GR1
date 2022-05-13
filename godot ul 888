extends Node

var kivi = 1
var kaarid = 2
var paber = 3
var voidud = 0
var kaotused = 0
var uusMang





func _ready():
	pass
	
	

func _process(delta):
	$voidud.text = str(voidud)
	$kaotused.text = str(kaotused)

func _on_Kivi_pressed():
	$omaValik.text = "Kivi"
	kivi = 1
	var arvutiValik = RandomNumberGenerator.new()
	arvutiValik.randomize()
	var vordub = arvutiValik.randi_range(1, 3)
	 
	if vordub == 1:
		$arvutiTegu.text = "Kivi"
		print("Viik")
		
	elif vordub == 2:
		$arvutiTegu.text = "Paber"
		print("Arvuti võit")
		kaotused += 1
	
	else:
		$arvutiTegu.text = "Käärid"
		print("Teie võit")
		voidud += 1
		
func _on_Paber_pressed():
	paber = 2
	$omaValik.text = "Paber"
	var arvutiValik = RandomNumberGenerator.new()
	arvutiValik.randomize()
	var vordub = arvutiValik.randi_range(1, 3)
	 
	if vordub == 1:
		$arvutiTegu.text = "Kivi"
		print("Teie võit")
		voidud += 1
		
	elif vordub == 2:
		$arvutiTegu.text = "Paber"
		print("Viik")
		
	
	else:
		$arvutiTegu.text = "Käärid"
		print("Arvuti võit")
		kaotused += 1

func _on_Kaarid_pressed():
	kaarid = 3
	$omaValik.text = "Käärid"
	
	var arvutiValik = RandomNumberGenerator.new()
	arvutiValik.randomize()
	var vordub = arvutiValik.randi_range(1, 3)
	 
	if vordub == 1:
		$arvutiTegu.text = "Kivi"
		print("Arvuti võit")
		kaotused += 1
		
	elif vordub == 2:
		$arvutiTegu.text = "Paber"
		print("Teie võit")
		voidud += 1
	
	else:
		$arvutiTegu.text = "Käärid"
		print("viik")
		pass
		
	if voidud >= 10:
		$kaotus_voit.text = "Võitsite Mängu"
		print("Võitsite mängu")
	elif kaotused <= 10:
		$kaotus_voit.text = "Kaotasite Mängu"
		print("Kaotasite mängu")
		


func _on_uusMang_pressed():
	get_tree().reload_current_scene()
		
		
