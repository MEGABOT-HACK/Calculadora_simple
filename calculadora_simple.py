import os,time,sys
time.sleep(3)
limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
limpiar_consola()
print("\n\n\t\tc")
time.sleep(1)
print(" \n\n\t\t\ta")
time.sleep(1)
print("  \n\n\t\t\t\tl")
time.sleep(1)
print("   \n\n\t\t\t\t\tc")
time.sleep(1)
print("    \n\n\t\t\t\t\t\tu")
time.sleep(1)
print("     \n\n\t\t\t\t\t\t\tl")
time.sleep(1)
print("      \n\n\t\t\t\t\t\t\t\ta")
time.sleep(1)
print("       \n\n\t\t\t\t\t\t\t\t\td")
time.sleep(1)
print("        \n\n\t\t\t\t\t\t\t\t\t\to")
time.sleep(1)
print("         \n\n\t\t\t\t\t\t\t\t\t\t\tr")
time.sleep(1)
print("          \n\n\t\t\t\t\t\t\t\t\t\t\t\ta")
time.sleep(3)
limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
limpiar_consola()
preguntar_operación = print("\n\n\n\n\n\t\t\t\t¿Qué operación deseas realizar?")
time.sleep(3)
suma = print ("\n\n\n\n\n\t\t\t\t\t\t[01] suma")
time.sleep(3)
resta = print ("\n\n\n\n\n\t\t\t\t\t\t[02] resta")
time.sleep(3)
multiplicación = print ("\n\n\n\n\n\t\t\t\t\t\t[03] multiplicación")
time.sleep(3)
división = print ("\n\n\n\n\n\t\t\t\t\t\t[04] división")
time.sleep(3)
introducir_operación = input ("\n\n\n\n\n\t\t\t\telige una opción: ")
try:
	introducir_operación == "01"
	introducir_operación == "02"
	introducir_operación == "03"
	introducir_operación == "04"
	pass
except:
	sys.exit()
limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
limpiar_consola()
while True:
	numero_1 = input ("\n\n\n\n\n\t\t\t\tintroduce el primer numero: ")
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
	time.sleep(3)
	numero_2 = input ("\n\n\n\n\n\t\t\t\tintroduce el segundo numero: " )
	time.sleep(3)
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
	try:
		numero_1 = int (numero_1)
		numero_2 = int (numero_2)
		print ("\n\n\n\n\n\t\t\t\tnúmeros analizados correctamente")
		time.sleep(3)
		limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
		limpiar_consola()
		time.sleep(3)
	except:
		pass
	else: 
		numero_1 = numero_1
		numero_2 = numero_2
		break
if introducir_operación == "01":
	time.sleep(3)
	print ("\n\n\n\n\n\t\t\t\trealizando la suma, espere")
	time.sleep(3)
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
	time.sleep(3)
	sumar = numero_1 + numero_2
	time.sleep(3)
	sumar = str (sumar)
	numero_1 = str (numero_1)
	numero_2 = str (numero_2)
	sumando = ("\n\n\n\n\n\t\t\t\tel resultado de la suma de ( " + numero_1 + " )" + " mas ( " + numero_2 + " )" + " es igual a: " + sumar)
	print (sumando)
	time.sleep(5)
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
if introducir_operación == "02":
	time.sleep(3)
	print ("\n\n\n\n\n\t\t\t\trealizando la resta, espere")
	time.sleep(3)
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
	time.sleep(3)
	restar = numero_1 - numero_2
	restar = str (restar)
	numero_1 = str (numero_1)
	numero_2 = str (numero_2)
	restando = ("\n\n\n\n\n\t\t\t\tel resultado de la resta de ( " + numero_1 + ")" + " menos (" + numero_2 + ")" + " es igual a: " + restar)
	print (restando)
	time.sleep(5)
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
if introducir_operación == "03":
	multiplicar = numero_1 * numero_2
	print ("\n\n\n\n\n\t\t\t\trealizando la multiplicación, espere")
	time.sleep(3)
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
	time.sleep(3)
	multiplicar = str (multiplicar)
	numero_1 = str (numero_1)
	numero_2 = str (numero_2)
	multiplicando = ("\n\n\n\n\n\t\t\t\tel resultado de la multiplicación de ( " + numero_1 + ")" + " por ( " + numero_2 + ")" + " es igual a: " + multiplicar)
	print (multiplicando)
	time.sleep(5)
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
if introducir_operación == "04":
	dividir = numero_1 / numero_2
	print ("\n\n\n\n\n\t\t\t\trealizando la división, espere")
	time.sleep(3)
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
	time.sleep(3)
	dividir = str (dividir)
	numero_1 = str (numero_1)
	numero_2 = str (numero_2)
	dividiendo = ("\n\n\n\n\n\t\t\t\tel resultado de la división de ( " + numero_1 + ")" + " entre ( " + numero_2 + ")" + " es igual a: " + dividir)
	print (dividiendo)
	time.sleep(5)
	limpiar_consola = lambda : os.system ('cls' if os.name in ('nt', 'dos') else 'clear')
	limpiar_consola()
