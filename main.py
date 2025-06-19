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
    print('')
    if option == 1:
        option_One()
    elif option == 2:
        option_Two()
    elif option == 3:
        option_Three()
    else:
        print("Opção digitada é inválida, tente novamente!\n")
        menu()
    return option

def option_One():
    name = input("Qual nome do produto a ser cadastrado? ").strip()
    weight = input("Digite o peso do produto em Kg: ").strip()
    height = input("Digite a altura do produto em CM: ").strip()
    width = input("Digite a largura do produto em CM: ").strip()
    profundity = input("Digite a profundidade do produto em CM: ").strip()

    if name == "" or weight == "" or height == "" or width == "" or profundity == "":
        print("\nErro: Nenhum campo pode ficar vazio. Tente novamente.\n")
        option_One()
        return

    elif not weight.replace(".", "").isdigit() or not height.replace(".", "").isdigit() or not width.replace(".", "").isdigit() or not profundity.replace(".", "").isdigit():
        print("\nErro: Peso, altura, largura e profundidade devem conter apenas números. Tente novamente.\n")
        option_One()
        return

    weight = float(weight)
    height = float(height)
    width = float(width)
    profundity = float(profundity)

    products[len(products)+1] = {
        "nome": name,
        "peso": weight,
        "altura": height,
        "largura": width,
        "profundidade": profundity
    }

    print("\nProduto cadastrado com sucesso!\n")
    menu()

def option_Two():
    if len(products) == 0:
        print("Nenhum produto encontrado!")
    elif len(products) < 2:
        print("1 Produto encontrado!")
    else:
        print(len(products), "Produtos encontrados! ")
    print("")

    for id, product in products.items():
        print(f"Código do produto: {id}")
        print(f" Nome: {product['nome']}")
        print(f" Peso: {product['peso']} Kg")
        print(f" Altura: {product['altura']} cm")
        print(f" Largura: {product['largura']} cm")
        print(f" Profundidade: {product['profundidade']} cm\n")
    menu()

def calcular_frete(peso, altura, largura, profundidade):
    volume = altura * largura * profundidade  
    peso_cubado = volume / 4000  # fator padrão rodoviário
    peso_final = max(peso, peso_cubado)

    if peso_final <= 5:
        return 20.00
    elif peso_final <= 10:
        return 35.00
    elif peso_final <= 20:
        return 50.00
    else:
        return 80.00

def option_Three():
    distance = input("Digite a distância do percurso em Km: ").strip()
    nmrProduct = input("Digite o código do produto a ser calculado o frete: ").strip()

    if distance == "" or nmrProduct == "":
        print("\nErro: Nenhum campo pode ficar vazio. Tente novamente.\n")
        option_Three()
        return

    elif not distance.replace(".", "").isdigit() or not nmrProduct.replace(".", "").isdigit():
        print("\nErro: Digite apenas números válidos. Tente novamente.\n")
        option_Three()
        return

    distance = float(distance)
    nmrProduct = int(float(nmrProduct))
    product = products.get(nmrProduct)

    if product:
        print("Produto encontrado!")

        a = float(product['altura'])
        l = float(product['largura'])
        c = float(product['profundidade'])
        w = float(product['peso'])

        frete_base = calcular_frete(w, a, l, c)

        frete_total = frete_base * (1 + (distance / 100))

        print(f"\nResumo da Entrega:")
        print(f"Distância: {distance:.2f} km")
        print(f"Valor base do frete: R$ {frete_base:.2f}")
        print(f"Valor total com base na distância: R$ {frete_total:.2f}\n")

    else:
        print("Produto não encontrado! Tente novamente")
        option_Three()
        return

    menu()

while True:
    print("_"*93)
    print("Seja Bem-Vindo ao Sistema de Entregas com Informações de Produtos e Cálculo de Quilometragem!")
    print("_"*93,"\n")
    menu()
    break
