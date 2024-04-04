import math

a = float(input("Digite o a: "))
b = float(input("Digite o b: "))
c = float(input("Digite o c: "))

delta = b**2 - 4*a*c

if a == 0:
    print("A equação é de 1º grau")
    
elif delta < 0:
    print("Não possui raízes reais")
else:
    delta = b**2 - 4*a*c
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)
    
    if delta == 0:
        print(f"A equação possui uma raiz x: {x1}")
    else:
        print(f"A equação possui as raízes x1: {x1} e x2: {x2}")