
try:
    n1 = int(input('ingrese primer numero: '))
    n2 = int(input('ingrese segundo numero: '))
    n3 = int(input('ingrese tercer numero: '))
    n4 = int(input('ingrese cuarto numero: '))


    if n1 >= 0:
        if str(n1) == str(n1)[:: -1]:
            print('%i es capicua.' % n1)
        else:
            print('%i no es capicua.' % n1)
    else:
        print ('El numero debe ser positivo.')    

    if n2 >= 0:
        if str(n2) == str(n2)[:: -1]:
            print('%i es capicua.' % n2)
        else:
            print('%i no es capicua.' % n2)
    else:
        print ('El numero debe ser positivo.')    

    if n3 >= 0:
        if str(n3) == str(n3)[:: -1]:
            print('%i es capicua.' % n3)
        else:
            print('%i no es capicua.' % n3)
    else:
        print ('El numero debe ser positivo.')    

    if n4 >= 0:
        if str(n4) == str(n4)[:: -1]:
            print('%i es capicua.' % n4)
        else:
            print('%i no es capicua.' % n4)
    else:
        print ('El numero debe ser positivo.')      
except: 
        print ('Ingrese solo numeros enteros')




