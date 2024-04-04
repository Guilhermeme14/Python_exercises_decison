salario = float(input("Qual o seu salário: "))

if salario <= 280.00:
    aumento = salario * 0.2
    novo_salario = salario + aumento
    print(f'Este era o seu salario {salario} voce ganhou um aumento de 20% o seu aumentou foi de {aumento} e o seu novo salario é {novo_salario}')

if 280.00 < salario <= 700.00:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f'Este era o seu salario {salario} voce ganhou um aumento de 15% o seu aumentou foi de {aumento} e o seu novo salario é {novo_salario}')    
    
if 700.00 < salario <= 1500.00:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f'Este era o seu salario {salario} voce ganhou um aumento de 10% o seu aumentou foi de {aumento} e o seu novo salario é {novo_salario}')

if salario > 1500.00:
    aumento = salario * 0.05
    novo_salario = salario + aumento
    print(f'Este era o seu salario {salario} voce ganhou um aumento de 5% o seu aumentou foi de {aumento} e o seu novo salario é {novo_salario}')