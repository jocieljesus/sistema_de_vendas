estoque_produtos = {
    1 : {"nome": "Camisa do Brasil", "preco": 400.00, "quantidade": 60},
    2 : {"nome": "Camisa do Paraguai", "preco": 120.00, "quantidade": 15},
    3 : {"nome": "Camisa do Cabo Verde", "preco":200.00, "quantidade": 18}
}

carrinho = []

while True:

    print("*"*30)
    print(" Seja Bem Vindo a minha Loja  ")
    print("*"*30)
    print(" [1] Vizualizar estoque.")
    print(" [2] Adicionar item ao carrinho.")
    print(" [3] Vizualizar Carrinho.")
    print(" [4] Finalizar Compra.")
    print(" [0] Sair do sistema.")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(" Vizualizando Estoque!")
        for chave, valor in estoque_produtos.items():
            print(f"{chave}:{valor}")

    elif opcao == 2:
        print("Adicionando itens ao carrinho!")
        id_produto = int(input("Qual ID do produto você deseja comprar? "))
        if id_produto in estoque_produtos:
            qtd_produto = int(input("Quantas unidades voce deseja?"))
            if qtd_produto <= 0:
                print("Quantidade inválida!")
            elif qtd_produto <= estoque_produtos[id_produto]["quantidade"]:
                item = {
                    "qtd" : qtd_produto,
                    "nome" : estoque_produtos[id_produto]["nome"],
                    "preco": estoque_produtos[id_produto]["preco"],
                    "preco_total": qtd_produto * estoque_produtos[id_produto]["preco"]
                }
                carrinho.append(item)
                estoque_produtos[id_produto]["quantidade"] -= qtd_produto
                print(item)
            else:
                print(f"Quantidade indispon vel, temos apenas {estoque_produtos[id_produto]["quantidade"]} no estoque.")
        else:
            print("Id informado não existe no estoque!")

    elif opcao == 3:
        if carrinho:
            print(" Vizualizando Carrinho!")
            subtotal = 0
            for i in carrinho:
                print(f"{i["qtd"]}x {i["nome"]} no valor de R${i["preco"]}(cada)\nTotal R${i["preco_total"]}")
                subtotal += i["preco_total"]
            print(f"Subtotal da Compra R${subtotal}")
        else:
            print("Carrinho Vazio!")

    elif opcao == 4:
            print("Finalizando Compra!")

    elif opcao == 0:
        print("Saindo do sistema...")
        break
    else:
        print("Opçao inválida!")
