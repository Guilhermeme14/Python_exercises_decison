n1 = float(input("Digite o numero 1: "))
n2 = float(input("Digite o numero 2: "))

decisao = int(input("Qual operação voce quer usar: \n"
      "1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão \n"))

if decisao == 1:
    resultado = n1 + n2

elif decisao == 2:
    resultado = n1 - n2
    
elif decisao == 3:
    resultado = n1 * n2

elif decisao == 4:
    resultado = n1 / n2

if resultado % 2 == 0:
    print("É par")

else:
    print("É impar")

if resultado > 0:
    print("O numero é postivo")
    
else: 
    print("O numero é negativo")

inteiro = round(resultado)

if resultado == inteiro:
    print("É um numero inteiro")

else:
    print("É um numero decimal")


