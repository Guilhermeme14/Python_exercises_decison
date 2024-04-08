carne = input(
    "Qual o tipo de carne? \n"
    "D - File duplo \n"
    "A - Alcatra \n"
    "P - Picanha \n"
)

kg = float(input("Qual a quantidade de kg da carne: "))

pagamento = input(
    "Qual o metodo de pagamento? \n"
    "T - Tabajara \n"
    "N - Normal \n"
)

if carne == "D":
    if kg <= 5:
        preco = kg * 4.9
    else:
        preco = kg * 5.8
    carne = "File duplo"
elif carne == "A":
    if kg <= 5:
        preco = kg * 5.9
    else:
        preco = kg * 6.8
    carne = "Alcatra"
elif carne == "P":
    if kg <= 5:
        preco = kg * 6.9
    else:
        preco = kg * 7.8
    carne = "Picanha"
if pagamento == "T":
    desconto = preco * 0.05
    preco_total = preco - desconto
    pagamento = "Cartão Tabajara"
else:
    desconto = "Não possui"
    preco_total = preco
    pagamento = "Cartão normal"

print(
    "Nota fiscal: \n"
    f"Carne : {carne} \n"
    f"Quantidade : {kg}kg \n"
    f"Preço : {preco}R$ \n"
    f"Tipo de pagamento : {pagamento} \n"
    f"Desconto : {desconto} \n"
    f"Total a pagar : {preco_total:.2f}R$ \n"
)
