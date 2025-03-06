# Listas para armazenar usuários e contas
usuarios = []
contas = []

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return
    # Adiciona novo usuário à lista
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário cadastrado com sucesso.")

def criar_conta_corrente(cpf):
    # Verifica se o CPF está cadastrado
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break
    if usuario is None:
        print("Usuário não encontrado.")
        return
    # Cria nova conta
    numero_conta = len(contas) + 1
    nova_conta = {
        'agencia': '0002',
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(nova_conta)
    print(f"Conta criada com sucesso. Agência: 0002, Conta: {numero_conta}.")

# Funções existentes separadas

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo, extrato
    if numero_saques >= limite_saques:
        print("Limite de saques atingido.")
        return saldo, extrato
    saldo -= valor
    extrato.append(f"Saque: -{valor}")
    numero_saques += 1
    return saldo, extrato

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato.append(f"Depósito: +{valor}")
    return saldo, extrato

def extrato(saldo, *, extrato):
    print("\nExtrato:")
    for item in extrato:
        print(item)
    print(f"Saldo atual: {saldo}")

# Funções adicionais

def listar_contas():
    for conta in contas:
        usuario = conta['usuario']
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Usuário: {usuario['nome']}")

# Exemplo de uso
cadastrar_usuario("Maria Silva", "01/01/1980", "12345678900", "Rua A, 123 - Bairro - Cidade/PE")
cadastrar_usuario("João Souza", "02/02/1990", "98765432100", "Av B, 456 - Bairro - Cidade/PE")

criar_conta_corrente("12345678900")
criar_conta_corrente("98765432100")

saldo = 1000
extrato_lista = []
saldo, extrato_lista = depositar(saldo, 200, extrato_lista)
saldo, extrato_lista = sacar(saldo=saldo, valor=150, extrato=extrato_lista, limite=500, numero_saques=1, limite_saques=3)
extrato(saldo, extrato=extrato_lista)
listar_contas()
