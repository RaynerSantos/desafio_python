menu = """
         MENU

    [1] Depositar
    [2] Retirar
    [3] Extrato
    [0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if(opcao == 1):
        deposito = float(input("Informe o valor do depósito desejado: "))
        if(deposito > 0):
            saldo += deposito
            extrato = f"Depósito no valor de R$ {deposito:.2f}\n"
            print(extrato)
        else:
            print("Operação falhou! O valor informado é inválido, favor tentar novamente!")

    elif(opcao == 2):
        saque = float(input("Informe o valor desejado para saque: "))
        if(saque <= saldo):
            if(numero_saques >= LIMITE_SAQUES):
                print("Operação falhou! Você excedeu o número de saques diários!")
            elif(saque <= limite):
                if(saque > 0):
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"Saque no valor de R$ {saque:.2f}\n"
                    print(extrato)
                else:
                    print("Operação falhou! O valor informado é inválido, favor tentar novamente!")
            else:
                print("Operação falhou! Não é possível retirar mais do que R$500,00 por saque!") 
        else:
            print("Operação falhou! Não é possível retirar o dinheiro por falta de saldo.")

    elif(opcao == 3):
        print("\n============= EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual de R$ {saldo:.2f}")
        print("===================================")

    elif(opcao == 0):
        break

    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")
