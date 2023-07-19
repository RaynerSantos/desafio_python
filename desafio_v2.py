menu = """
============  MENU  ============

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair

=> """

def depositar(saldo, valor, extrato, /):    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
        print(f"Número de saques realizados no dia: {numero_saques}")
    
    else:
        print("\nOperação falhou! O valor informado é inválido")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n============ EXTRATO ============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=================================")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = int(input("Informe o CPF completo (somente números): "))
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com este CPF!")
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla do estado): ")

        usuarios.append({"nome": nome, "cpf": cpf, "data de nascimento": data_nascimento, "endereço": endereco})

        print("\nUsuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Informe o CPF completo (somente números): "))
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    else:
        print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(usuarios, contas):
    cpf = int(input("Informe o CPF completo (somente números): "))
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        for conta in contas:
            if conta["usuario"]["cpf"] == cpf:
                linha = f"""
            Agência:\t{conta["agencia"]}
            C/c:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}"""
                print(linha)
    else:
        print("\nUsuário ainda não existente! Favor criar usuário e conta.")




def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES)
        
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta += 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(usuarios, contas)

        elif opcao == 6:
            criar_usuario(usuarios)

        elif opcao == 0:
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()



