total = 0
saques=[]
while True:
    valor = float( input("Digite um valor: "))
    if valor == 0:
     break
    saques.append(valor)
    total += valor
    print(f"Sacado: R${total:.2f}")