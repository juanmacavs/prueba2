n1 = int(input('ingrese primer numero: '))
n2 = int(input('ingrese segundo numero: '))
n3 = int(input('ingrese tercer numero: '))
menor = min(n1, n2, n3)
mayor = max (n1, n2, n3)
valormedio = (n1 + n2 + n3) - menor - mayor
print ("Mayor: ")
print (mayor)
print ("Medio: ")
print (valormedio)
print ("Menor: ")
print (menor)
