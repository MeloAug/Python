pacientes = []
quantidade = int(input("Quantos pacientes serão cadastrados? "))
IMCs = []
TMBs =[]
for i in range (1):
    print(f"\nPaciente {i+1}")
    paciente = {
        'nome':input('Digite o nome: '),
        'peso':float(input('Digite o peso(kg): ')),
        'sexo':input('Digite o sexo(M-masculino, F-feminino): '),
        'altura':float(input('Digite a altura(metros): ')),
        'idade':int(input('Digite a idade: '))
    }
    pacientes.append(paciente)
    
for paciente in pacientes:
    paciente ['IMC'] = paciente ['peso'] / (paciente['altura'] **2)
    IMCs.append(paciente['IMC'])
    if paciente['sexo'] =='M':
        paciente['TMB'] = 9,99*paciente['peso'] + 6,25*paciente['altura']*100 - 4,92*paciente['idade'] + 5
    else:
        paciente['TMB'] = 9,99*paciente['peso'] + 6,25*paciente['altura']*100 - 4,92*paciente['idade'] + 161
    TMBs.append(paciente['TMB'])
        
    
print ('Opções: ')  
print ('1 – maior IMC')
print ('2 – maior TMB ')
print ('3 – menor IMC')
print ('4 – menor TMB ')

opcao= input('Digite a opção: ')

maior_IMC = max(IMCs)
maior_TMB = max(TMBs)
menor_IMC = min(IMCs)
menor_TMB = min(TMBs)
        
if opcao =='1':
    for paciente in pacientes:
        if paciente['IMC'] == maior_IMC:
            print(paciente)
            
if opcao =='2':
    for paciente in pacientes:
        if paciente['TMB'] == maior_TMB:
            print(paciente)
            
if opcao =='3':
    for paciente in pacientes:
        if paciente['IMC'] == menor_IMC:
            print(paciente)
            
if opcao =='4':
    for paciente in pacientes:
        if paciente['TMB'] == menor_TMB:
            print(paciente)
            
