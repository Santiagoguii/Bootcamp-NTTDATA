# Menu interativo
menu = """
        -----BEM-VINDO-----
    [1] Realizar depósitos
    [2] Realizar saques
    [3] Ver extratos
    [4] Criar usuário
    [5] Criar conta corrente
    [6] Sair do sistema
"""

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (apenas números): ")
    nome = input("Digite o nome do usuário: ")
    dt_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite o endereço: ")

    # Verifica o CPF 
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado.")
        return usuarios

    usuarios.append({ 'nome': nome, 'dt_nascimento': dt_nascimento, 'cpf': cpf,  'endereco': endereco})

    print("Usuário criado com sucesso!")
    return usuarios


def criar_contacorrente(contas, usuarios):
    cpf = input("Digite o CPF do usuário para vincular a conta (apenas números): ")
    
    if not any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário não encontrado. Por favor, é necessário criar um usuário antes de criar uma conta.")
        return contas

    numero_conta = len(contas) + 1
    
    # Número fixo de agência
    AGENCIA = "0001"
    
    conta = { 'numero_conta': numero_conta, 'agencia': AGENCIA,'cpf_usuario': cpf }

    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}, Agência: {AGENCIA}")
    return contas


def deposito(saldo, valor, extrato, contas, usuarios, cpf_usuario, /):
    if not any(conta['cpf_usuario'] == cpf_usuario for conta in contas):
        print("Usuário invalido. Crie uma conta antes de realizar depósitos.")
        return saldo, extrato

    if valor <= 0:
        print("Valor incorreto, adicione um valor positivo.")
    else:
        saldo += valor
        conta = next(conta for conta in contas if conta['cpf_usuario'] == cpf_usuario)
        nome_usuario = next(usuario['nome'] for usuario in usuarios if usuario['cpf'] == cpf_usuario)
        extrato += (f"Depósito: R$ {valor:.2f}\n"
                    f"Conta: {conta['numero_conta']} - Agência: {conta['agencia']}\n"
                    f"Nome: {nome_usuario}\n"
                    "\n")
        print("\n Depósito realizado com sucesso!\n")
    
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saque, LIMITE_SAQUE, contas, usuarios, cpf_usuario):
    if not any(conta['cpf_usuario'] == cpf_usuario for conta in contas):
        print("Usuário invalido. Crie uma conta antes de realizar saques.")
        return saldo, extrato, numero_saque

    if numero_saque >= LIMITE_SAQUE:
            print("Limite de saques diários excedido! Tente novamente amanhã.\n")
       
    elif valor > limite:
            print("O limite máximo para saques diários é de R$ 500,00.\n")
        
    elif saldo < valor:
            print("Saque não realizado. Saldo insuficiente.\n")
       
    elif valor <= 0:
            print("Valor inválido, por favor insira um valor positivo.\n")    
            
    else:
        saldo -= valor
        conta = next(conta for conta in contas if conta['cpf_usuario'] == cpf_usuario)
        nome_usuario = next(usuario['nome'] for usuario in usuarios if usuario['cpf'] == cpf_usuario)
        extrato += (f"Saque: R$ {valor:.2f}\n"
                    f"Conta: {conta['numero_conta']} - Agência: {conta['agencia']}\n"
                    f"Nome: {nome_usuario}\n"
                    "\n")
        print("Saque realizado com sucesso!\n")
        numero_saque += 1

    return saldo, extrato, numero_saque


def extrato(saldo, /, *, extrato):
    print("# Extrato da conta #".center(20, "-"))
    print("\nNenhuma movimentação registrada." if not extrato else extrato)    
    print(f"\nSaldo total: R$ {saldo:.2f}\n")
    print("## ## ##".center(36,"-"))


# Execução do menu 
def main():
    # Inicializando variáveis
    saldo = 0
    limite = 500
    extrato_banco = ""
    numero_saque = 0
    LIMITE_SAQUE = 3
    usuarios = [] 
    contas = []    

    while True:
        opcao = input(menu())
        
        if opcao == "1":
            cpf_usuario = input("Digite o CPF do usuário (apenas números): ")
            cpf_usuario = ''.join(filter(str.isdigit, cpf_usuario))
            saldo, extrato_banco = deposito(
                saldo,
                float(input("Qual a quantia que você deseja depositar? ")),
                extrato_banco,
                contas,
                usuarios,
                cpf_usuario
            )

        elif opcao == "2":
            cpf_usuario = input("Digite o CPF do usuário (apenas números): ")
            cpf_usuario = ''.join(filter(str.isdigit, cpf_usuario))
            saldo, extrato_banco, numero_saque = saque(
                saldo=saldo,
                valor=float(input("Qual a quantia que você deseja sacar? ")),
                extrato=extrato_banco,
                limite=limite,
                numero_saque=numero_saque,
                LIMITE_SAQUE=LIMITE_SAQUE,
                contas=contas,
                usuarios=usuarios,
                cpf_usuario=cpf_usuario
            )
        
        elif opcao == "3":
            extrato(saldo, extrato=extrato_banco)
        
        elif opcao == "4":
            usuarios = criar_usuario(usuarios)
        
        
        elif opcao == "5":
            contas = criar_contacorrente(contas, usuarios)
        
        elif opcao == "6":
            print("Saindo do sistema. Até breve!")
            break
         
        else:
            print("Opção inválida. Por favor, selecione novamente a opção desejada.\n")

main()