""" 
• Cadastro e visualização de produtos.
• Cadastro de entregas com cálculo da distância percorrida.
• Cálculo automático do valor médio gasto por quilometragem.
• Verificações com condicionais if para evitar erros como campos
vazios ou dados incorretos.
• Uso de laços while e for para percorrer listas de produtos e
entregas, automatizando os cálculos e exibições.

"""
products = {}

def menu():
    option = int(input("O que você deseja realizar?\n\n1 - Para cadastrar um produto\n2 - Para visualizar os produtos\n3 - Para calcular uma entrega\n"))
    if option == 1:
        option_One()
    elif option == 2:
        option_Two()
    elif option == 3:
        option_Three()
    else:
        print("Opção digitada é invalida, tente novamente!\n")
        menu()

    return option

def option_One():
    name = input("Qual nome do produto a ser cadastrado? ")
    weight = str(input("Digite o peso do produto em Kg: "))
    height = str(input("Digite a altura do produto em CM: "))
    width = str(input("Digite a largura do produto CM: "))
    profundity = str(input("Digite a profundidade do produto em CM: "))
    products[len(products)+1] = {"nome": name, "peso": weight, "altura": height, "largura": width, "profundidade": profundity}
    menu()

    

def option_Two():
    if len(products) == 0:
        print("Nenhum produto encontrado!")
    elif len(products) < 2: 
        print("1 Produto encontrado!")
    else:
        print(len(products),"Produtos encontrados! ")
    print("")

    for id, produto in products.items():
        produto = products[id]
        print(f"Produto: {id}\n Nome: {produto['nome']}\n Peso: {produto['peso']}\n Altura: {produto['altura']}\n Largura: {produto['largura']}\n Profundidade: {produto['profundidade']}\n")
    
    
    menu()



def option_Three():
    pass
''

while True:
    print("_"*93)
    print("Seja Bem-Vindo ao Sistema de Entregas com Informações de Produtos e Cálculo de Quilometragem!")
    print("_"*93,"\n")

    menu()

    break