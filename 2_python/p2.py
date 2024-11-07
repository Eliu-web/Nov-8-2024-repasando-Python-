print (" ")
print ("Velazquez Mares Jesus Eliu")
print (" ")

q = int(input("ingresa la calificacion de tu nota: "))

if q >= 0:
    print ("SUSPENSO")
elif q >= 5:
    print ("SUFICENTE")
elif q >= 6:
    print ("BIEN")
elif q >= 7:
    print ("NOTABLE")
elif q >= 9:
    print ("SOBRESALIENTE")
else:
    print ("Nota no valida")
