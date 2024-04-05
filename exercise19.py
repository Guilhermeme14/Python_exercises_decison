num = int(input('Digite o numero: '))

if num > 99:
    num_str = str(num)
    print(f'O número possuí {num_str[0]} centenas, {num_str[1]} dezenas e {num_str[2]} unidades')
elif 100 > num > 9:
    num_str = str(num)
    print(f'O número possuí {num_str[0]} dezenas e {num_str[1]} unidades')
elif 10 > num >= 0:
    num_str = str(num)
    print(f'O número possuí {num_str[0]} unidades')
else: 
    print('Numero inválido')
    