# Menu interativo
menu = """
        -----BEM-VINDO-----
       [1] Realizar depósitos
       [2] Realizar saques
       [3] Ver extratos
       [4] Sair do sistema
"""

# Inicializando variáveis
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3 
 
while True:
    print(menu)
    opcao = input("Escolha uma opção: ".center(25))

    # Depósito
    if opcao == "1":
        adicao_valor = float(input("Qual a quantia que você deseja depositar? "))
        if adicao_valor <= 0:
            print("Valor inválido, por favor insira um valor positivo.")
        else:
            saldo += adicao_valor
            extrato += f"Depósito: R$ {adicao_valor:.2f}\n"
            print("Depósito realizado com sucesso!\n")

    # Saque 
    elif opcao == "2":
        valor_retirada = float(input("Qual a quantia que você deseja sacar? "))
       
        if numero_saque >= LIMITE_SAQUE:
            print("Limite de saques diários excedido! Tente novamente amanhã.\n")
       
        elif valor_retirada > limite:
            print("O limite máximo para saques diários é de R$ 500,00.\n")
        
        elif saldo < valor_retirada:
            print("Saque não realizado. Saldo insuficiente.\n")
       
        elif valor_retirada <= 0:
            print("Valor inválido, por favor insira um valor positivo.\n")    
            
        else:    
            saldo -= valor_retirada 
            extrato += f"Saque: R$ {valor_retirada:.2f}\n"
            print("Saque realizado com sucesso!\n")
            numero_saque += 1

    # Verificação do extrato 
    elif opcao == "3":
       print("# Extrato da conta #".center(20, "-"))
       print("\nNenhuma movimentação registrada." if not extrato else extrato)    
       print(f"\nSaldo total: R$ {saldo:.2f}\n")
       print("## ## ##".center(36,"-"))
    elif opcao == "4":
        print("Saindo do sistema. Até breve!")
        break    

    # Opção que não contém no menu 
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")