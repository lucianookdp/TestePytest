# flyup.py

paris = []
novayork = []
londres = []
passageiros = {}
pagamentos_abertos = {}
pagamentos_efetuados = {}
contador = 0

print("\n"
      "------------------------------------------------------\n"
      "Bem vindo(a) ao FlyUP Pacotes De Viagens! (BETA 3.O)\n"
      "------------------------------------------------------\n\n"
      "Alunos:\n"
      "Henrique Padilha Duda\n"
      "Luciano Kubiak Dal Pai\n"
      "Jhonnatan M. Cora Da Luz\n")

def menu():
    while True:
        print('----------------------------\n'
              'MENU PRINCIPAL:\n'
              '----------------------------\n'
              '1- Comprar passagem\n'
              '2- Ver destinos disponíveis\n'
              '3- Consultar valores\n'
              '4- Menu do administrador\n'
              '0- Sair\n'
              '----------------------------')

        continuar = int(input("Escolha uma opção: "))
        if continuar == 1:
            comprar()
        elif continuar == 2:
            mostrar()
        elif continuar == 3:
            valores()
        elif continuar == 4:
            admin()
        elif continuar == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")

def compra_paris(item):
    global paris
    for _ in range(item):
        paris.append(1)

def passagem_paris():
    global paris
    print('VOCÊ ESCOLHEU PARIS')
    if sum(paris) < 10:
        pacotesparis = int(input('Digite o número de pacotes: '))
        if pacotesparis <= (10 - sum(paris)):
            compra_paris(pacotesparis)
            for _ in range(pacotesparis):
                nome_passageiro_paris()
        else:
            novo_paris()
    else:
        print('Todos os pacotes para essa viagem já foram vendidos!!')
        comprar()

def nome_passageiro_paris():
    global passageiros, pagamentos_abertos
    nomepassageiro = input("Digite seu nome completo: ")
    if nomepassageiro.isdigit():
        print(f"Erro: Esperado um nome, mas recebido um número: {nomepassageiro}")
    else:
        nome = nomepassageiro.upper()
        passageiros.setdefault(nome, "PARIS")
        pagamentos_abertos.setdefault(nome, "Pagamento em aberto")

def novo_paris():
    global paris
    print('Número de pacotes inválido')
    print("Ainda restam", (10 - sum(paris)), "pacote(s) restante(s)")
    num = int(input('Digite:\n'
                    '1- Novo número de pacotes\n'
                    '2- Menu\n'))
    if num == 1:
        passagem_paris()
    elif num == 2:
        menu()
    else:
        novo_paris()

def novo_londres():
    global londres
    print('Número de pacotes inválido')
    print("Ainda restam", (10 - sum(londres)), "pacote(s) restante(s)")
    num1 = int(input('Digite:\n'
                     '1- Novo número de pacotes\n'
                     '2- Menu\n'))
    if num1 == 1:
        passagem_londres()
    elif num1 == 2:
        menu()
    else:
        novo_londres()

def compra_londres(item):
    global londres
    londres.append(item)

def passagem_londres():
    global londres
    print('VOCÊ ESCOLHEU LONDRES')
    if sum(londres) < 10:
        pacoteslondres = int(input('Digite o número de pacotes: '))
        if pacoteslondres <= 10 - sum(londres):
            compra_londres(pacoteslondres)
            for _ in range(pacoteslondres):
                nome_passageiro_londres()
        else:
            novo_londres()
    else:
        print('Todos os pacotes para essa viagem já foram vendidos!!')
        menu()

def nome_passageiro_londres():
    global passageiros, pagamentos_abertos
    nomepassageiro = input("Digite seu nome completo: ")
    nome = nomepassageiro.upper()
    passageiros.setdefault(nome, "LONDRES")
    pagamentos_abertos.setdefault(nome, "Pagamento em aberto")

def novo_novayork():
    global novayork
    print('Número de pacotes inválido')
    print("Ainda restam", (10 - sum(novayork)), "pacote(s) restante(s)")
    num2 = int(input('Digite:\n'
                     '1- Novo número de pacotes\n'
                     '2- Menu\n'))
    if num2 == 1:
        passagem_novayork()
    elif num2 == 2:
        menu()
    else:
        novo_novayork()

def compra_novayork(item):
    global novayork
    novayork.append(item)

def passagem_novayork():
    global novayork
    print('VOCÊ ESCOLHEU NOVA YORK')
    if sum(novayork) < 10:
        pacotesnovayork = int(input('Digite o número de pacotes: '))
        if pacotesnovayork <= 10 - sum(novayork):
            compra_novayork(pacotesnovayork)
            for _ in range(pacotesnovayork):
                nome_passageiro_novayork()
            print("Parabéns, você já reservou sua viagem!!")
        else:
            novo_novayork()
    else:
        print('Todos os pacotes para essa viagem já foram vendidos!!')
        menu()

def nome_passageiro_novayork():
    global passageiros, pagamentos_abertos
    nomepassageiro = input("Digite seu nome completo: ")
    nome = nomepassageiro.upper()
    passageiros.setdefault(nome, "NOVA YORK")
    pagamentos_abertos.setdefault(nome, "Pagamento em aberto")

def admin():
    print("-----------------------------\n"
          "MENU DO ADMINISTRADOR: \n"
          "-----------------------------")
    senha = 2022
    senha2 = input("Digite a senha: ")
    if senha2.isdigit() and int(senha2) == senha:
        pagamentos()
    else:
        print("Senha incorreta!")
        admin()

def comprar():
    dest = int(input("-----------------------------------\n"
                     "Selecione o seu destino dos sonhos!!\n"
                     "São os destinos disponíveis:\n"
                     '1- PARIS\n'
                     '2- LONDRES\n'
                     '3- NOVA YORK\n'
                     '-----------------------------------\n'))

    if dest == 1:
        passagem_paris()
    elif dest == 2:
        passagem_londres()
    elif dest == 3:
        passagem_novayork()

def mostrar():
    global paris, londres, novayork
    print('-----------------------------------------------------')
    print('Paris ainda tem', (10 - sum(paris)), 'lugares disponíveis')
    print('Londres ainda tem', (10 - sum(londres)), 'lugares disponíveis')
    print('Nova York ainda tem', (10 - sum(novayork)), 'lugares disponíveis')
    print('------------------------------------------------------------------')

def valores():
    print('Pacote para Paris = R$ 3.499,90')
    print('Pacote para Londres = R$ 3.699,90')
    print('Pacote para Nova York = R$ 3.299,90')

def lista_passageiros():
    busca = int(input('Digite:\n'
                      '1- Exibir lista de passageiros\n'
                      '2- Buscar passageiro\n'
                      '3- Pagamentos\n'
                      '4- Menu\n'))
    if busca == 1:
        if passageiros:
            for a in passageiros:
                print('Nome:', a, ", destino:", passageiros[a])
            pagamentos()
        else:
            print("Ainda não há nenhum passageiro")
            pagamentos()
    elif busca == 2:
        busca_passageiro = input("Digite o nome do passageiro: ")
        nome = busca_passageiro.upper()
        if passageiros.get(nome):
            print("Nome:", nome, ", Destino:", passageiros[nome])
            pagamentos()
        else:
            print("Passageiro não encontrado")
            pagamentos()
    elif busca == 3:
        pagamentos()
    elif busca == 4:
        menu()
    else:
        print("Dígito inválido")
        lista_passageiros()

def pagamentos():
    while True:
        try:
            pag = int(input('1- Ver pagamentos em aberto \n'
                            '2- Consultar lista de passageiros\n'
                            '3- Consultar valores totais\n'
                            '4- Retornar ao menu\n'
                            '----------------------------\n'
                            'Escolha uma opção: '))
            if pag == 1:
                for nome, status in pagamentos_abertos.items():
                    print(f'Nome: {nome} = {status}')
            elif pag == 2:
                lista_passageiros()
            elif pag == 3:
                valorestotais()
            elif pag == 4:
                confirmar_pagamento()
            elif pag == 0:
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

def confirmar_pagamento():
    global pagamentos_abertos, pagamentos_efetuados
    nome = input("Digite o nome do passageiro à confirmar o pagamento: ").upper()
    if nome in pagamentos_abertos:
        pagamentos_efetuados[nome] = 'Pagamento efetuado'
        del pagamentos_abertos[nome]
        print(f"O pagamento de {nome} foi confirmado!")
        print(f"{nome} = Pagamento efetuado")
    else:
        print("Passageiro não encontrado ou pagamento já efetuado.")

def valorestotais():
    valort = int(input('1- Valores totais de Paris\n'
                       '2- Valores totais de Londres\n'
                       '3- Valores totais de Nova York\n'
                       '4- Pagamentos\n'))
    if valort == 1:
        print(sum(paris), "passagens para Paris vendidas")
        x = int(input("Digite a quantidade de pacotes vendidos: "))
        if sum(paris) == x:
            total = somaparis(x)
            print(total, "R$")
        else:
            print("Números divergem")
            valorestotais()
    elif valort == 2:
        print(sum(londres), "passagens para Londres vendidas")
        x = int(input("Digite a quantidade de pacotes vendidos: "))
        if sum(londres) == x:
            total = somalondres(x)
            print(total, "R$")
        else:
            print("Números divergem")
            valorestotais()
    elif valort == 3:
        print(sum(novayork), "passagens para Nova York vendidas")
        x = int(input("Digite a quantidade de pacotes vendidos: "))
        if sum(novayork) == x:
            total = somany(x)
            print(total, "R$")
        else:
            print("Números divergem")
            valorestotais()
    elif valort == 4:
        pagamentos()
    else:
        print("Dígito inválido!!")
        valorestotais()

def somalondres(n):
    return n * 3699.90

def somany(n):
    return n * 3299.90

def somaparis(n):
    return n * 3499.90

if __name__ == "__main__":
    menu()

