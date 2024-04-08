combustivel = input("Qual o tipo de combustível:\n"
                    " A - Alcool \n G - Gasolina")

litros = float(input("Qauntos litros de gasolina: "))

alcool = 1.9
gasolina = 2.5

if combustivel == "A":

    if litros <= 20:
        preco = alcool * litros
        desconto = preco * 0.03
        preco_atual = preco - desconto
        print(f"O preço total com alcool é: {preco_atual}")

    elif litros > 20:
        preco = alcool * litros
        desconto = preco * 0.05
        preco_atual = preco - desconto
        print(f"O preço total com alcool é: {preco_atual}")

elif combustivel == "G":

    if litros <= 20:
        preco = gasolina * litros
        desconto = preco * 0.04
        preco_atual = preco - desconto
        print(f"O preço total com gasolina é: {preco_atual}")

    elif litros > 20:
        preco = gasolina * litros
        desconto = preco * 0.06
        preco_atual = preco - desconto
        print(f"O preço total com gasolina é: {preco_atual}")

else: 
    print("Dado incorreto")
