# criando matriz
valores = []

# entrada de dados
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input("Digite um valor: "))
        linha.append(n)
    valores.append(linha)

# variáveis
soma_linha1 = 0
qtd_maior5 = 0
menor = valores[0][0]

print("\nMatriz:")

# mostrando e calculando
for i in range(3):
    for j in range(3):
        print(valores[i][j], end=" ")
        
        # soma da primeira linha
        if i == 0:
            soma_linha1 += valores[i][j]
        
        # contando números maiores que 5
        if valores[i][j] > 5:
            qtd_maior5 += 1
        
        # menor valor da matriz
        if valores[i][j] < menor:
            menor = valores[i][j]
    print()

print("\nResultados:")
print("Soma da primeira linha:", soma_linha1)
print("Quantidade > 5:", qtd_maior5)
print("Menor valor:", menor)