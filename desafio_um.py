menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input("Digite o valor que deseja depositar:\n"))
        if valor > 0:
         saldo += valor
         print("Valor depositado com sucesso!")
         extrato += (f"Deposito: R${valor:.2f}\n")
        else :
            print("Favor depositar um valor válido!")
            exit(1)
    elif opcao == 's':
        saque = float(input("Informe o valor que deseja sacar:\n"))
        if saque <= limite and numero_saques < LIMITE_SAQUES and saldo >= saque:
            saldo -= saque 
            numero_saques += 1
            extrato += (f"Saque: R${saque:.2f}\n")
            print("Saque feito com sucesso!")
        elif numero_saques > LIMITE_SAQUES:
            print("Número de Saques excedido, tente novamente amanhã!")
        elif saque > limite or numero_saques > LIMITE_SAQUES:
            print("Não é permitido saque acima do seu limite diário!")
        elif saque > saldo:
            print("Saldo insuficiente!")
        else :
            print("Ação não permitida, tente novamente!")
    elif opcao == 'e':
        print("*****Extrato*****")
        if extrato:
           print(extrato)
        else:
            print(f"Não Houve movimentações.")
        print(f"Seu saldo é de: R${saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Opção inválida, por favor selecione novamente.")
