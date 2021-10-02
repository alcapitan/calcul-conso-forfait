from datetime import date, time, datetime
from calendar import monthrange

print("Calculateur de consommation de forfait")
print("Version 1.0.0 ; 30/09/21")
print("Créateur : @alcapitan (sur github : www.github.com/alcapitan)")
print("\n")


# Paramètres utilisateur

print("Données utilisateur : ")

	# Entrées utilisateur
	
dataCapacity = int("20000")
dayReset = int("13")

	# Receuil des informations
	
		# Capacité du forfait
		
if dataCapacity == "0":
	dataCapacity = input("\tCapacité du forfait (en Mo) : ")
else:
	print("\tCapacité du forfait (en Mo) : ",dataCapacity)

		# Date de réinitialisation
		
if dayReset == "0" or dayReset > 31:
	dayReset = input(" \tDate de réinitialisation du forfait : ")
else:
	print("\tDate de réintialisation : ", dayReset)

		# Informations liés à la date
		
dateNow = date.today()
dayNow = int(dateNow.day)
monthNow = int(dateNow.month)
yearNow = int(dateNow.year)
print("\tDate d'aujourd'hui (JJ/MM/AA) : ",dayNow,"/",monthNow,"/",yearNow)

			# Algorithme de recul de mois et année selon le jour
			
if dayReset < dayNow:
	monthReset = int(monthNow)
	yearReset = int(yearNow)
elif monthNow == 1:
	monthReset = int(12)
	yearReset = int(yearNow - 1)
else:
	monthReset = int(monthNow - 1)
	yearReset = int(yearNow)

print("\n")

# Traitement des informations

print("Données complémentaires : ")

	# Nombre de jours depuis le reset du forfait (aujourd'hui non compris)
	
dateReset = date(yearReset,monthReset,dayReset)
numberDays = dateNow - dateReset
print("\tNombre de jours depuis le reset (sans compter aujourd'hui) : ",numberDays.days)

	# Nombre de jours d'utilisation du forfait

nextReset = date(yearReset,monthReset + 1,dayReset)
print("\tProchain jour de réinitialisation du forfait (JJ/MM/AA) : ",nextReset.day,"/",nextReset.month,"/",nextReset.year)
daysUse = nextReset - dateReset
daysUse = daysUse.days
print("\tNombre de jours d'utilisation du forfait : ",daysUse)

	# Consommation maximale par jour
	
dataDaily = dataCapacity // daysUse
print("\tConsommation maximale de données en 1 jour : ",dataDaily,"Mo")
roundError = dataCapacity - (dataDaily * daysUse)
print("\tMarge d'erreur à cause de l'arrondissement des chiffres : ",roundError,"Mo")

print("\n")

# Résultat

print("Résultats : ")

	# Data maximale consommé (sans compter aujourd'hui)
	
dataUsed = dataDaily * numberDays.days
print("\tSans compter votre consommation d'aujourd'hui, vous devriez avoir utilisé au maximum",dataUsed,"Mo. Si vous avez dépassé cette limite, vous risquez d'être à 0 avant la fin du forfait.")

	# Data minimale restante (sans compter aujourd'hui)

dataResidual = dataCapacity - dataUsed
print("\tSans compter votre consommation d'aujourd'hui, il devrait vous rester au minimum",dataResidual,"Mo. Si vous avez dépassé cette limite, vous risquez d'être à 0 avant la fin du mois.")

