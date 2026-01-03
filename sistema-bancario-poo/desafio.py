import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


# ===================== MENU =====================
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


# ===================== HISTÓRICO =====================
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )


# ===================== TRANSAÇÃO =====================
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar(self)
            print("\n=== Depósito realizado com sucesso! ===")


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar(self)
            print("\n=== Saque realizado com sucesso! ===")


# ===================== CONTA =====================
class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor inválido! @@@")
            return False

        if valor > self.saldo:
            print("\n@@@ Saldo insuficiente! @@@")
            return False

        self.saldo -= valor
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor inválido! @@@")
            return False

        self.saldo += valor
        return True


# ===================== CONTA CORRENTE =====================
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        quantidade_saques = len(
            [t for t in self.historico.transacoes if t["tipo"] == "Saque"]
        )

        if valor > self.limite:
            print("\n@@@ Limite de saque excedido! @@@")
            return False

        if quantidade_saques >= self.limite_saques:
            print("\n@@@ Número máximo de saques excedido! @@@")
            return False

        return super().sacar(valor)


# ===================== CLIENTE =====================
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


# ===================== PESSOA FÍSICA =====================
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# ===================== MAIN =====================
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "nu":
            cpf = input("Informe o CPF: ")

            if any(cliente.cpf == cpf for cliente in clientes):
                print("\n@@@ Usuário já cadastrado! @@@")
                continue

            nome = input("Informe o nome completo: ")
            nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço: ")

            cliente = PessoaFisica(nome, cpf, nascimento, endereco)
            clientes.append(cliente)

            print("\n=== Usuário criado com sucesso! ===")

        elif opcao == "nc":
            cpf = input("Informe o CPF do usuário: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)

            if not cliente:
                print("\n@@@ Usuário não encontrado! @@@")
                continue

            numero = len(contas) + 1
            conta = ContaCorrente(cliente, numero)
            cliente.adicionar_conta(conta)
            contas.append(conta)

            print("\n=== Conta criada com sucesso! ===")

        elif opcao == "d":
            numero = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor do depósito: "))

            conta = contas[numero - 1]
            conta.cliente.realizar_transacao(conta, Deposito(valor))

        elif opcao == "s":
            numero = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor do saque: "))

            conta = contas[numero - 1]
            conta.cliente.realizar_transacao(conta, Saque(valor))

        elif opcao == "e":
            numero = int(input("Informe o número da conta: "))
            conta = contas[numero - 1]

            print("\n================ EXTRATO ================")
            if not conta.historico.transacoes:
                print("Não foram realizadas movimentações.")
            else:
                for t in conta.historico.transacoes:
                    print(f"{t['tipo']}:\tR$ {t['valor']:.2f} - {t['data']}")

            print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
            print("========================================")

        elif opcao == "lc":
            for conta in contas:
                print("=" * 40)
                print(f"Agência:\t{conta.agencia}")
                print(f"Conta:\t\t{conta.numero}")
                print(f"Titular:\t{conta.cliente.nome}")

        elif opcao == "q":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\n@@@ Operação inválida! @@@")


main()
