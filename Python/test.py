pacientes = []

# Cadastro de 3 pacientes
for i in range(3):
    print(f"\nPaciente {i+1}")
    nome = input('Nome: ')
    peso = float(input('Peso (kg): '))
    sexo = input('Sexo (M/F): ').upper()
    altura = float(input('Altura (m): '))
    idade = int(input('Idade: '))

    imc = round(peso / (altura ** 2), 2)
    if sexo == 'M':
        tmb = round(9.99 * peso + 6.25 * altura * 100 - 4.92 * idade + 5, 2)
    else:
        tmb = round(9.99 * peso + 6.25 * altura * 100 - 4.92 * idade - 161, 2)

    pacientes.append({
        'nome': nome, 'peso': peso, 'sexo': sexo,
        'altura': altura, 'idade': idade,
        'IMC': imc, 'TMB': tmb
    })

# Menu
print("\nOpções:\n1 - Maior IMC\n2 - Maior TMB\n3 - Menor IMC\n4 - Menor TMB")
opcao = int(input("Escolha uma opção: "))

# Função para buscar paciente(s)
def filtrar(chave, maior=True):
    valor = max(p[chave] for p in pacientes) if maior else min(p[chave] for p in pacientes)
    return [p for p in pacientes if p[chave] == valor]

# Processa a opção
if opcao == 1:
    resultado = filtrar('IMC', True)
elif opcao == 2:
    resultado = filtrar('TMB', True)
elif opcao == 3:
    resultado = filtrar('IMC', False)
elif opcao == 4:
    resultado = filtrar('TMB', False)
else:
    print("Opção inválida.")
    resultado = []

# Exibe resultado
for p in resultado:
    print(f"\nNome: {p['nome']}, IMC: {p['IMC']}, TMB: {p['TMB']}")
