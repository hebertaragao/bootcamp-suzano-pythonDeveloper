from datetime import datetime
class contaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []
        self.saques_hoje = 0
        self.ultimo_saque = None
    
    def depositar(self, valor):
        if valor <= 0:
            print("Depósito falhou: valor negativo ou zero não é permitido.")
            self.extrato.append(f"Depósito falhado: R${valor:.2f} | Saldo: R${self.saldo:.2f}")
            return
        
        self.saldo += valor
        self.extrato.append(f"Depósito: +R${valor:.2f} | Saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        hoje = datetime.now().date()

        if self.ultimo_saque != hoje:
            self.saques_hoje = 0

        if self.saques_hoje >= 3:
            print("Limite diário de saques atingido!")
            self.extrato.append(f"Saque falhado (limite): R${valor:.2f} | Saldo: R${self.saldo:.2f}")
            return
        
        if valor > 500:
            print("Limite máximo de R$ 500,00 por saque!")
            self.extrato.append(f"Saque falhado (limite): R${valor:.2f} | Saldo: R${self.saldo:.2f}")
            return
        
        if valor > self.saldo:
            print("Saldo insuficiente!")
            self.extrato.append(f"Saque falhado (saldo): R${valor:.2f} | Saldo: R${self.saldo:.2f}")
            return
        
        self.saldo -= valor
        self.extrato.append(f"Saque: -R${valor:.2f} | Saldo: R${self.saldo:.2f}")
        self.saques_hoje += 1
        self.ultimo_saque = hoje

    def visualizar_extrato(self):
        print(f"Extrato da conta de {self.titular}:")
        for item in self.extrato:
            print(item)
        print(f"Saldo atual: R${self.saldo:.2f}")

# Criando uma conta bancária

minha_conta = contaBancaria("João", 1000.00)    

# Realizando operações
minha_conta.depositar(500.50)
minha_conta.sacar(200.25)
minha_conta.sacar(600.00)  # Saldo insuficiente
minha_conta.depositar(-100.00)  # Depósito inválido
minha_conta.sacar(300.00)
minha_conta.sacar(50.00)
minha_conta.sacar(30.00)  # Limite diário de saques atingido
minha_conta.visualizar_extrato()
