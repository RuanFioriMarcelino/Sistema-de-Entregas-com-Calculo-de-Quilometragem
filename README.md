# 📦 Sistema de Cadastro de Produtos e Cálculo de Frete

Este é um sistema simples em Python, feito para terminal, que permite:

- 📌 Cadastrar produtos com dimensões e peso.
- 🔍 Visualizar todos os produtos cadastrados.
- 🚚 Calcular o valor de entrega com base no peso ou volume e na distância.
- ❌ Encerrar o programa de forma segura.

---

## 🛠 Funcionalidades

### 1. Cadastro de Produto

O usuário pode inserir:

- Nome do produto
- Peso (Kg)
- Altura (cm)
- Largura (cm)
- Profundidade (cm)

O sistema valida os campos para garantir que todos sejam preenchidos corretamente.

---

### 2. Visualização de Produtos

Mostra todos os produtos cadastrados, com as seguintes informações:

- Código do produto
- Nome
- Peso
- Dimensões (altura, largura e profundidade)

---

### 3. Cálculo de Entrega

A entrega é calculada com base no **peso real** ou **peso cúbico** (utilizando o fator 4000 para transporte rodoviário).

Regras de frete:

- Até 5kg: R$ 20,00
- Até 10kg: R$ 35,00
- Até 20kg: R$ 50,00
- Acima de 20kg: R$ 80,00

O valor final é ajustado com base na distância percorrida:  
**frete_total = frete_base \* (1 + (distância / 100))**

---

## ▶️ Como usar

1. Execute o script com Python 3:

```bash
python nome_do_arquivo.py
```

2. Siga as instruções no menu interativo:

```
1 - Cadastrar produto
2 - Visualizar produtos
3 - Calcular entrega
4 - Sair do programa
```

---

## 📋 Exemplo de uso

```plaintext
Qual nome do produto a ser cadastrado? Celular
Digite o peso do produto em Kg: 0.3
Digite a altura do produto em CM: 15
Digite a largura do produto em CM: 7
Digite a profundidade do produto em CM: 1
Produto cadastrado com sucesso!
```

---

## 🧠 Lógica de Cálculo de Frete

```python
volume = altura * largura * profundidade
peso_cubado = volume / 4000
peso_final = max(peso, peso_cubado)
```

---

## ✅ Requisitos

- Python 3.x
- Terminal ou ambiente compatível com entrada via `input()`

---

## 📄 Licença

Este projeto é de uso educacional e livre para adaptações.
