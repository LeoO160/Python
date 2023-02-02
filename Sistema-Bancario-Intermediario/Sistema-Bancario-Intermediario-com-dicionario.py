import textwrap


def Menu(): #MENU A SER EXIBIDO
    print("1- Saque")
    print("2- Deposito")
    print("3- Extrato")
    print("4- Criar usuario")
    print("5- Mostrar todos usuarios")
    print("6- Limpar todos usuarios e suas respectivas contas")
    print("7- Nova conta")
    print("8- Mostrar contas")
    print("_______________________________________________")

    opcao = int(input("Digite a opcao desejada: "))
    return opcao #retorna a opcao desejada

#Variaveis Globais
AGENCIA = "0001"
saldo = 0.00
extrato = []
saque = 0
operacao = []
usuarios=[]
contas=[]

def cadastrar_usuario(usuarios):
    cpf = input("Digite o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios) #verifica se há alguem com esse CPF já cadastrado

    if(usuario != None): #se houver
        print("Ja existe um usuario com esse CPF!")
        return
	
	#se nãao houver, a função pede as entradas
    nome = input("Digite o nome do usuario: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input ("Informe o endereco (longradouro, nro - bairro - cidade/UF estado): ")
	
	#guarda os dados dentro do vetor em forma de dicionario
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereço":endereco})
    print("USUARIO CRIADO COM SUCESSO!")


def filtrar_usuario(cpf,usuarios):
    usuario_filtrados = []
	
	#verifica se existe o CPF digitado nos usuarios cadastrados
    for usuario in usuarios:
        if usuario["cpf"]==cpf:
            usuario_filtrados = usuario
            return usuario_filtrados

    if usuario_filtrados == []: #se nao exitir, retorna None
        return None

def mostrar_usuarios(usuarios):#imprime os usuarios
    print(usuarios)

def limpar_usuarios(usuarios, conta):#limpa os vetores relacionados aos usuarios e as contas
    usuarios.clear()
    conta.clear()
    print("Usuarios e contas foram limpados com sucesso!!")

def cadastrarConta(agencia, numero_conta, usuarios): #cadastra uma nova conta
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios) #procura o cpf digitado

    if(usuario != None): #se houver
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} #retorna os valroes digitados para a variavel que chamou a função

    print("usuario nao encontrado!!")#se nao houver

def mostrar_contas(contas): #imprime os dados de todas as contas
    for conta in contas:
        linha = f"""\
           Agencia: \t{conta["agencia"]}
           C/C:\t\t{conta["numero_conta"]}
           Titular:\t{conta["usuario"]["nome"]}
        """
    print("=" * 100)
    print(textwrap.dedent((linha)))

def limpar_contas(contas): #apaga somente as contas
    contas.clear()
    print("Contas limpadas com sucesso!!")

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

    elif opcao == 4:
        cadastrar_usuario(usuarios)
        print("_______________________________________________")

    elif opcao == 5:
        mostrar_usuarios(usuarios)
        print("_______________________________________________")

    elif opcao == 6:
        limpar_usuarios(usuarios,contas)
        print("_______________________________________________")

    elif opcao == 7:
        numero_conta = len(contas) + 1
        conta = cadastrarConta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
        print("_______________________________________________")

    elif opcao == 8:
        mostrar_contas(contas)
        print("_______________________________________________")

    elif opcao == 9:
        limpar_contas(contas)
        print("_______________________________________________")

    else:
        print("_______________________________________________")
        break
