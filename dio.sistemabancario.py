menu = """
####### BEM VINDO ########

[D] - DEPOSITAR
[S] - SACAR
[E] - EXTRATO
[Q] - SAIR

Escolha uma opção acima: """

saldo = 0
limite_saque = 500
saques = 3
deposito = 0
extrato = ""
n_saques = 0

while True:

    opcao = input(menu).upper()

    if opcao == "D":
        depositado = float(input("Digite o valor a ser depositado: R$ "))

        if depositado > 0:
            saldo += depositado
            extrato += "Deposito realizado de R$ {:.2f}\n".format(depositado)
            #print("O valor depositado foi de R$ {:.2f}".format(depositado))
        else:
            print("Valor informado é inválido")
    elif opcao == "S":
        saque = float(input("Informe o valor a ser sacado: R$ "))

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite_saque
        excedeu_saques = n_saques >= saques

        if excedeu_saldo:
            print("Não foi possivel realizar o saque, saldo insuficiente.")
        elif excedeu_limite:
            print("Não foi possivel realizar o saque, você excedeu o limite de saque diário.")
        elif excedeu_saques:
            print("Não foi possivel realizar o saque, você excedeu o numero de saques diários.")
        elif saque > 0:
            saldo -= saque
            extrato += "Saque realidado de R$ {:.2f}\n".format(saque)
            n_saques += 1
        else:
            print("O Valor informado foi inválido")
    elif opcao == "E":
        print('''\n#################EXTRATO###################
Não foram realizados movimentações.''' if not extrato else extrato)
        print("Saldo: R$ {:.2f}".format(depositado-saque))
        print("################################################")
    elif opcao == "Q":
        break

    else:
        print("Digite uma opção válida!")







