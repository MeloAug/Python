#Inicializa a matriz 3x3 e variaveis de controle
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna3 = 0
soma_linha2 = 0

#Leitura dos dados e preenchimento
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        
#Processamento
print ("-=" * 20)
for l in range (0, 3):
    for c in range (0, 3):
        print (f"[{matriz [l][c]:^5}]", end="")
        if matriz [l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()
    
#Calculo das estatisticas
for l in range (0, 3):
    soma_coluna3 += matriz[l][2]
    
maior_linha2 = max(matriz[1])

print ("-=" * 20)
print (f"Soma dos valores pares é {soma_pares}")
print (f"Soma dos valores da terceira coluna é {soma_coluna3}")
print (f"O maior valor da segunda linha é {maior_linha2}")