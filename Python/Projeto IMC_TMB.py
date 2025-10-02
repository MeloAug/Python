pacientes = []
quantidade = int(input("Quantos pacientes serão cadastrados? "))
for i in range (3):
    print(f"\nPaciente {i+1}")
    paciente = {
        'nome':input('Digite o nome: '),
        'peso':float(input('Digite o peso(kg): ')),
        'sexo':input('Digite o sexo(M-masculino, F-feminino): '),
        'altura':float(input('Digite a altura(metros): ')),
        'idade':int(input('Digite a idade: '))
    }
    IMC = paciente['peso'] / (paciente['altura'] ** 2)
    if paciente ['peso'] == 'M':
        TMB = 9.99 * paciente['peso'] + 6.25 * (paciente['altura'] *100)- 4.92 * paciente['idade'] + 5
    else:
        TMB = 9.99 * paciente['peso'] + 6.25 * (paciente['altura'] *100) - 4.92 * paciente['idade'] - 161    
        
    
    print("\nOpções:")
    print("1  Maior IMC")
    print("2  Maior TMB")
    print("3  Menor IMC")
    print("4  Menor TMB")        
    
    opção = int(input("Digite um numero das opções: "))
    
    pacientes.append(paciente)
for paciente in pacientes:
    paciente
    
print(pacientes)
