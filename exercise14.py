n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))

nota = (n1 + n2)/2

if nota < 4.0:
    conceito = "E"
elif nota < 6.0:
    conceito = "D"
elif nota < 7.5:
    conceito = "C"
elif nota < 9.0:
    conceito = "B"
elif nota < 10.0:
    conceito = "A"
    
situacao = "aprovado" if conceito in ["A","B","C"] else "reprovado"

print(f'O aluno tirou {nota:.2f} ficou com o conceito {conceito}, sendo assim ele está {situacao}')