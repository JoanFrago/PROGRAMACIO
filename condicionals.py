# If ----------------------------------------------------------------------
a = 3+9
if a == 12:
    print("'a' és igual a 12")
else:
    print("'a' és diferent de 12")

# Elif --------------------------------------------------------------------
a = 10+3
if a == 4:
    print("El valor 'a' és 4")
elif a == 13:
    print("El valor 'a' és 13")
elif a == 5:
    print("El valor 'a' és 5")
else:
    print("No es compleix cap condició")

# Problema ---------------------------------------------------------------

#0-1 any nou
#1-5 mitjana edat
#>5 antic

anys = float(input("Quants anys té l'ordinador? "))

if anys == 0 and anys < 1:
    print("El teu ordinador és nou")
elif anys >= 1 and anys <= 5:
    print("El teu ordinador és de mitjana edat")
elif anys > 5:
    print("El teu ordinador és antic")
else:
    print("Aquest número no és vàlid")

# ------------------------------------------------------------------------

# Condicionals Anidades --------------------------------------------------
edat = int(input("Introdueix la teva edat "))
if edat >= 0 and edat < 100:
    if edat >= 18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat")
else:
    print("Vosté ja ha superat els 100 anys")

#Problema ----------------------------------------------------------------
contrasenya = ('Ibanus2022')
contrasenya_u = str(input("Introdueix la contrasenya correcta "))
if len(contrasenya_u) >= 8:
    print("La contrasenya és prou llarga")
    if contrasenya_u == contrasenya:
        print("La contrasenya és correcte")
    else:
        print("La contrasenya ha de contenir 8 o més caràcters")
else:
    print("La contrasenya és incorrecte.")

# -----------------------------------------------------------------------

#While-------------------------------------------------------------------
i = 1
while i <= 1:
    print(i)
    i += 1
print("Programa acabat.")

#------------------------------------------------------------------------
dia = 0
setmana = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge"]
#falta acabar

#For ---------------------------------------------------------------------
nums = [13, 33, 440, 3, 393939]
for i in nums:
    print(i)

#-------------------------------------------------------------------------
for i in range (1, 1000+1, 4):
    print(i)

