from datetime import datetime

def valida_transacao(funcao_original):
    def wrapper(self, valor, *args, **kwargs):
        if valor <= 0:
            print("\n❌ Operação negada: Valor deve ser maior que 0.")
            return self.saldo
        else:
            print(f"📝 [AUDITORIA] Processando transação de R$ {valor}...")
            return funcao_original(self, valor, *args, **kwargs)
    return wrapper

class Conta:
    def __init__(self, nome, id, senha, saldo=0):
        self.nome = nome
        self.id = id
        self.saldo = saldo
        self.senha = senha
        self.historico = []

    def __str__(self):
        return f"ID: {self.id} | Titular: {self.nome} | Saldo: R$ {self.saldo:.2f}"

    @valida_transacao
    def deposito(self, valor) -> float:
        self.saldo += valor
        hora_dep = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.historico.append(f"DEPOSITO {valor:.2f} {hora_dep}")
        return self.saldo

    @valida_transacao
    def saque(self, valor) -> float:
        if valor > self.saldo:
            print("\n❌ Operação negada: Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso.")
            hora_saque = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.historico.append(f"SAQUE {valor:.2f} {hora_saque}")
        return self.saldo

    def transferencia(self, id, valor):
        pass

    def exportar_historico(self):
        print("\n" + "="*40)
        print("          EXPORTANDO EXTRATO")
        print("="*40)

        with open(f"extrato{self.nome}.txt", "w") as arquivo:
            arquivo.write("EXTRATO BANCÁRIO:\n")
            for linha in self.historico:
                arquivo.write(f"{linha} \n")
            arquivo.write("EXPORTAÇÃO COMPLETA")

        print("EXPORTAÇÃO COMPLETA")
        return None


class Banco:
    def __init__(self, id_inicial=0):
        self.id = id_inicial
        self.contas = {}

    def __iter__(self):
        return iter(self.contas.values())

    def listar_contas(self):
        print("\n" + "="*40)
        print("          RELATÓRIO DE CONTAS")
        print("="*40)

        if not self.contas:
            print("Nenhuma conta cadastrada no momento.")
            return

        for conta in self:
            print(conta)
            print("-" * 40)

    def criar_conta(self):
        print("\n" + "="*40)
        print("          ABERTURA DE CONTA")
        print("="*40)
        
        nome = input("👉 Digite seu nome: ")
        senha = input("👉 Crie sua senha: ")

        self.id += 1
        saldo_inicial = 0

        nova_conta = Conta(nome, self.id, senha, saldo_inicial)
        self.contas[nova_conta.id] = nova_conta

        print(f"\n✅ Conta criada com sucesso!")
        print(f"Bem-vindo(a), {nome}. O ID da sua conta é: {self.id}")
        print("="*40)

    def excluir_conta(self):
        print("\n" + "="*40)
        print("           EXCLUIR CONTA")
        print("="*40)
        
        # O ID deve ser capturado como inteiro (int) para buscar no dicionário
        id_conta = int(input("👉 Digite o ID da conta que deseja excluir: "))

        # Lógica corrigida de busca direta no dicionário
        if id_conta in self.contas:
            conta_removida = self.contas[id_conta]
            del self.contas[id_conta]
            print(f"\n✅ Conta de {conta_removida.nome} (ID: {id_conta}) removida com sucesso!")
        else:
            print("\n❌ Erro: Conta não encontrada no sistema.")

    def login(self):
        print("\n" + "="*40)
        print("          ACESSO AO SISTEMA")
        print("="*40)
        
        id_conta = int(input("👉 Digite seu ID: "))
        senha = input("👉 Digite sua senha: ")
    
        if id_conta in self.contas:
            conta_encontrada = self.contas[id_conta]
            if senha == conta_encontrada.senha:
                print(f"\n🔓 Acesso liberado. Olá, {conta_encontrada.nome}!")
                return conta_encontrada
            else:
                print("\n❌ Erro: Senha incorreta.")
                return None
        else:
            print("\n❌ Erro: Conta não localizada.")
            return None


class Menu:
    banco = Banco()
    
    print("\n" + "#"*40)
    print("💰 BEM-VINDO AO BANCO PYTHON 💰")
    print("#"*40)
    
    while True:
        print("\n" + "-"*40)
        print("           MENU PRINCIPAL")
        print("-"*40)
        print("1 - Acessar conta (Login)")
        print("2 - Criar uma nova conta")
        print("3 - Excluir conta")
        print("4 - Listar contas")
        print("5 - Sair do sistema")
        print("-"*40)

        opcao_escolhida = int(input("👉 Escolha uma operação (1-4): "))

        if opcao_escolhida == 1:
            login = banco.login()
            
            if isinstance(login, Conta):
                while True:
                    print("\n" + "-"*40)
                    print(f"    PAINEL DA CONTA | Saldo: R$ {login.saldo:.2f}")
                    print("-"*40)
                    print("1 - Depositar")
                    print("2 - Sacar")
                    print("3 - Transferência")
                    print("4 - Exportar extrato")
                    print("5 - Voltar (Deslogar)")
                    print("-"*40)

                    opcoes_escolhida_conta = int(input("👉 Escolha uma operação (1-4): "))
                    
                    if opcoes_escolhida_conta == 1:
                        valor = float(input("\n👉 Valor que deseja depositar: R$ "))
                        novo_saldo = login.deposito(valor)
                        print(f"✅ Depósito realizado! Novo saldo: R$ {novo_saldo:.2f}")
                    
                    elif opcoes_escolhida_conta == 2:
                        valor = float(input("\n👉 Valor do Saque: R$ "))
                        novo_saldo = login.saque(valor)

                    elif opcoes_escolhida_conta == 3:
                        print("\n🚧 Transferência em desenvolvimento...")

                    elif opcoes_escolhida_conta == 4:
                        exportar_extrato = login.exportar_historico()

                    elif opcoes_escolhida_conta == 5:
                        print("DESLOGANDO...")
                        break

        elif opcao_escolhida == 2:
                    banco.criar_conta()
                    
        elif opcao_escolhida == 3:
            banco.excluir_conta()

        elif opcao_escolhida == 4:
            banco.listar_contas()
            
        elif opcao_escolhida == 5:
            print("\n👋 Obrigado por usar o Banco Python. Até logo!\n")
            break
            
        else:
            print("\n❌ Opção inválida. Escolha um número de 1 a 5.")