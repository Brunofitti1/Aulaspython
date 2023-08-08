#dicionario
"""tabela = {"alface": 0.45, "batata": 1.2 , "tomate": 2.3 , "feijão": 1.5}
while True:
    produto = input("digite o nome do produto ou  fim para terminar")
    if produto = "fim":
        break
    if produto in tabela:
        print(f"preço: R$ {tabela[produto]:.2f}")
    else:
        print("produto nao encontrado.")"""


carros = {"Jimmy": 75000.00, "Toro": 120000.00, "Amarok": 180000.00, "Audi A3": 215000.00, "Urus": 1200000.00,
          "Maverick": 200000.00,}
print(carros.keys())
carros = {"Jimmy": 75000.00, "Toro": 120000.00, "Amarok": 180000.00, "Audi A3": 215000.00, "Urus": 1200000.00,
          "Maverick": 200000.00,}
while True:
    carro = input("digite o nome do carro de sua escolha ou difite fim para terimnar.")
    if carro == "fim":
        break
    if carro in carros:
        print(f"Preço: R${carros[carro]:.2f}")
    else:
        print("carro nâo encontrado")
