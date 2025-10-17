def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def calcular_tmb(peso, altura, idade, sexo):
    if sexo == 'M':
        return 9.99 * peso + 6.25 * altura * 100 - 4.92 * idade + 5
    else:
        return 9.99 * peso + 6.25 * altura * 100 - 4.92 * idade - 161

pacientes = []
quantidade = int(input("Quantos pacientes serão cadastrados? "))

for i in range(quantidade):
    print(f"\nPaciente {i + 1}")
    nome = input("Nome: ")
    peso = float(input("Peso (kg): "))
    sexo = input("Sexo (M/F): ").upper()
    altura = float(input("Altura (m): "))
    idade = int(input("Idade: "))
    
    imc = calcular_imc(peso, altura)
    tmb = calcular_tmb(peso, altura, idade, sexo)
    
    pacientes.append({
        'nome': nome,
        'IMC': imc,
        'TMB': tmb
    })

print("\nOpções:")
print("1 - Maior IMC")
print("2 - Maior TMB")
print("3 - Menor IMC")
print("4 - Menor TMB")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    valor = max(p['IMC'] for p in pacientes)
    resultado = [p for p in pacientes if p['IMC'] == valor]
elif opcao == 2:
    valor = max(p['TMB'] for p in pacientes)
    resultado = [p for p in pacientes if p['TMB'] == valor]
elif opcao == 3:
    valor = min(p['IMC'] for p in pacientes)
    resultado = [p for p in pacientes if p['IMC'] == valor]
elif opcao == 4:
    valor = min(p['TMB'] for p in pacientes)
    resultado = [p for p in pacientes if p['TMB'] == valor]
else:
    print("Opção inválida!")
    resultado = []

for p in resultado:
    print(f"\nNome: {p['nome']}")
    print(f"IMC: {p['IMC']:.2f}")
    print(f"TMB: {p['TMB']:.2f}")
