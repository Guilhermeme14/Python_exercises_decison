p1 = input("Telefonou para a vítima? ")
p2 = input("Esteve no local do crime? ")
p3 = input("Mora perto da vítima? ")
p4 = input("Devia para a vítima? ")
p5 = input("Já trabalhou com a vítima? ")

ponto = 0

if p1 == "sim":
    ponto += 1
else: 
    ponto += 0

if p2 == "sim":
    ponto += 1
else: 
    ponto += 0

if p3 == "sim":
    ponto += 1
else: 
    ponto += 0
    
if p4 == "sim":
    ponto += 1
else: 
    ponto += 0
    
if p5 == "sim":
    ponto += 1
else: 
    ponto += 0
    
print(ponto)

if ponto <=2:
    print("Suspeita")

elif 3 <= ponto <= 4:
    print("Cúmplice")

elif ponto == 5:
    print("Assassino")