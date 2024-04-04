dias_da_semana = {
    1: "segunda-feira",
    2: "terça-feira",
    3: "quarta-feira",
    4: "quinta-feira",
    5: "sexta-feira",
    6: "sábado",
    7: "domingo"
}

dia = int(input("Digite um número: "))

if dia in dias_da_semana:
    print(dias_da_semana[dia])
else:
    print('Número inválido')
