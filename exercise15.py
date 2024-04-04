
l1 = int(input("Indique o lado 1 do triangulo: "))
l2 = int(input("Indique o lado 2 do triangulo: "))
l3 = int(input("Indique o lado 3 do triangulo: "))

if l1 == l2 == l3:
    print("É um triangulo equilatero")
    
elif l1 == l2 !=l3:
    print("É um triangulo isóceles")
elif l2 == l3 !=l1:
    print("É um triangulo isóceles")
elif l3 == l1 !=l2:
    print("É um triangulo isóceles")

else:
    print("O triangulo é escaleno")