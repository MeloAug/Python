produto1 = {"nome": "feijao", "preço": 5.20}
produto2 = {"nome": "arroz", "preço": 7.80}
produto3 = {"nome": "batata", "preço": 2.50}

produtos = [produto1, produto2, produto3]

nome =(input("Digite o nome do produto: "))
for produto in produtos:
    if produto["nome"] == nome:
        print(produto ["preço"])
        break
if produto["nome"] != nome:
    print("Produto inexistente")