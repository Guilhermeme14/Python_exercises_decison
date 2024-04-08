num = int(input('Digite o numero: '))

if num < 10 or num > 600:
    print("Valor de saque inválido. O valor mínimo é 10 reais e o máximo é 600 reais.")

else:
    cem = num // 100
    num %= 100

    cinquenta = num // 50
    num %= 50

    dez = num // 10
    num %= 10

    cinco = num // 5
    num %= 5
    
    um = num

    print("Imprimindo: ")
    if cem > 0:
        print(f"{cem} nota(s) de 100 reais")
    if cinquenta > 0:
        print(f"{cinquenta} nota(s) de 50 reais")
    if dez > 0:
        print(f"{dez} nota(s) de 10 reais")
    if cinco > 0:
        print(f"{cinco} nota(s) de 5 reais")
    if um > 0:
        print(f"{um} nota(s) de 1 real")
