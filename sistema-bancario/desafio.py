# ==========================
# FUNÇÕES DE OPERAÇÕES
# ==========================

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(" Saldo insuficiente.")
    elif excedeu_limite:
        print(" Valor excede o limite.")
    elif excedeu_saques:
        print("Limite de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Valor inválido para saque.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Sem movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=============================")


# ==========================
# FUNÇÕES DE USUÁRIO 
# ==========================

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario_existente = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario_existente:
        print(" Usuário já cadastrado com esse CPF.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")

    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print(" Usuário não encontrado.")
        return

    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    })

    print(" Conta criada com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print(f"""
Agência: {conta['agencia']}
Conta: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
        """)


# ==========================
# PROGRAMA PRINCIPAL
# ==========================

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[l] Listar Contas
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        criar_conta(AGENCIA, numero_conta, usuarios, contas)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print(" Opção inválida.")
