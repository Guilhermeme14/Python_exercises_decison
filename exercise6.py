n1 = input("Insira 1 numero: ")
n2 = input("Insira 1 numero: ")
n3 = input("Insira 1 numero: ")

maior_numero = n1

if n2 > maior_numero:
    maior_numero = n2
if n3 > maior_numero:
    maior_numero = n3

print("O maior número é:", maior_numero)