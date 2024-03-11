import math

#inut du mode
print("mode 1: convertir un angle en degré en radiant")
print("mode 2: convertir un angle en radiant en degré")
mode = float(input("entrez le mode choisi: "))


if mode == 1:
	#input de la mesure de l'angle
	angle = float(input("entrez l'ouverture de l'angle: "))
	#calcul de l'angle en radiant
	angle = angle / 180
	#print du résultat
	print(f"l'angle possède une ouverture de {angle}π")
	
elif mode == 2:
	#input de la mesure de l'angle
	pi = float(input("entrez le nombre de π de l'angle: "))
	diviseur = float(input("entrez le nombre qui divise π: "))
	#calcul de l'angle en degré
	angle = pi/diviseur
	angle = angle * 180
	#print du résultat
	print(f"l'angle possède une ouverture de {angle}°")
else:
	print("mode sélectionné invalide, veuillez uniquement entrer 1 ou 2 en fonction du mode choisi")
