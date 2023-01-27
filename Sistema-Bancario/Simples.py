def Menu(): #MENU A SER EXIBIDO
    print("1- Saque")
    print("2- Deposito")
    print("3- Extrato")

    opcao = int(input("Digite a opcao desejada: "))
    return opcao #retorna a opcao desejada

#Variaveis Globais
saldo = 0.00
extrato = []
saque = 0
operacao = []

def Saque(saldo): #Função responsável por sacar
    valor = float(input("Digite o valor que deseja sacar: ")) #valor a ser sacado

    global saque

    if (valor <= saldo and valor < 500.00 and saque < 3 and valor > 0): #se o valor a ser sacado for menor ou igaul ao saldo E menor que 500 E se ainda tiver disponivel algum saque (limite 3)
        saldo = saldo-valor #decremento

        extrato.append(valor) #vetor de valores incrementados ou decrementados ao saque
        operacao.append("Saque") #vetor de operacoes realizadas
        saque = saque + 1 #contador de saques (limite 3) VARIAVEL GLOBAL
        print("Saque realizado com sucesso! (" + str(saque) + "/3)")
        return saldo

    else:
        print("Saque indisponivel!")
        return saldo

def Deposito(saldo): #Função responsável por depositar
    valor = float(input("Digite o valor que deseja depositar: ")) #valor a ser depositado

    if (valor < 0):#tem que ser um valor positivo
        print("Não é possível depositar um valor negativo!")
        return 0

    saldo = saldo + valor #incrementa ao montante
    extrato.append(valor) #vetor de valores incrementados ou decrementados ao saque
    operacao.append("Deposito") #vetor de operacoes realizadas
    print("Deposito efetuado com sucesso!")

    return saldo

def Extrato():#Função responsável por mostrar o extrato
    for i in range(len(extrato)): #loop de 0 até o total de operações realizadas
        print(str(operacao[i])+": R$" + str(extrato[i])) #imprime a operação e o valor operado
    print("Total: R$"+str(saldo))#imprime o total

while True: #loop infinito (main)
    opcao = Menu() #mostra o menu
    print("_______________________________________________")

    if opcao == 1:#se o valor digitado for 1, ocorre o saque
        saldo=Saque(saldo)
        print("_______________________________________________")

    elif opcao == 2:#se o valor digitado for 2, ocorre o depósito
        saldo=Deposito(saldo)
        print("_______________________________________________")

    elif opcao == 3:#se o valor digitado for 3, ocorre a impressao do extrato
        Extrato()
        print("_______________________________________________")

    else:
        break
