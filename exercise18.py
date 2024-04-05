dia = int(input("digite o dia: "))
mes = int(input("digite o mes: "))
ano = int(input("digite o ano: "))

if 0 < dia <= 31 and 0 < mes <= 12 and 0 < ano <= 2024:
    print(f'{dia}/{mes}/{ano}')

else: 
    print('Data incorreta')