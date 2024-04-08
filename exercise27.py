kg_morango = float(input("Kg de morango: "))
kg_maca = float(input("Kg de maçã: "))

if kg_morango <= 5:
    preco_morango = kg_morango * 2.5
else:
    preco_morango = kg_morango * 2.25

if kg_maca <= 5:
    preco_maca = kg_maca * 1.8
else:
    preco_maca = kg_maca * 1.5

kg_frutas = kg_maca + kg_morango
preco_total = preco_maca + preco_morango

if kg_frutas > 8 or preco_total > 25:
    desconto = preco_total * 0.1
    preco_final = preco_total - desconto
    print(f"O valor a ser pago pelo cliente é {preco_final:.2f}")

else:
    print(f"O valor a ser pago pelo cliente é {preco_total:.2f}")