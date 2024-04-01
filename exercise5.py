n1 = float(input("Digite a n1: "))
n2 = float(input("Digite a n2: "))

media = (n1 + n2)/2

print(media)

if media >= 7.0:
    print("Aprovado")
elif media < 7.0 :
    print("Reprovado")
elif media == 10.0:
    print("nerd")