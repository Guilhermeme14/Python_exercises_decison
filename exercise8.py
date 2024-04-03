banana = input("Qual o preço da banana? ")
maca = input("Qual o preço da maca? ")
limao = input("Qual o preço do limao? ")

menor_preco = banana 

if banana < maca and banana < limao:
    print("Compre a banana!")
elif maca < banana and maca < limao:
    print("Compre a maçã!")
else:
    print("Compre o limão!")
    