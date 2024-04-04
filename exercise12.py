horas_trabalhadas = float(input("Horas que atuou no mes: "))

bruto = 10 * horas_trabalhadas

if bruto <= 900.00:
    inss = bruto * 0.10
    desconto = inss
    liquido = bruto - desconto

if 900.00 < bruto <= 1500.00:
    ir = bruto * 0.05
    inss = bruto * 0.10
    desconto = ir + inss
    liquido = bruto - desconto
 
if 1500.00 < bruto <= 2500.00:
    ir = bruto * 0.10
    inss = bruto * 0.10
    desconto = ir + inss
    liquido = bruto - desconto    

if bruto > 2500.00:
    ir = bruto * 0.20
    inss = bruto * 0.10
    desconto = ir + inss
    liquido = bruto - desconto
    
print(f'Salario bruto : {bruto}\n IR : {ir}\n INSS : {inss} \n Total de descontos : {desconto} \n Salario liquido : {liquido}')