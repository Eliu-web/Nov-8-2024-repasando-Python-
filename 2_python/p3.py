print (" ")
print ("Velazquez Mares Jesus Eliu")
print (" ")

q = str(input("Ingresa el nombre correspondiente: "))
w = str(input("Ingresa el apellido correspondiente: "))

if q == "Daniel" and w == "Ramos":
    print ("Nombre y apellido correctos")
elif q == "Daniel" and w != "Ramos":
    print ("Apellido incorrecto")
elif q != "Daniel" and w == "Ramos":
    print ("Usuario desconocido")
    