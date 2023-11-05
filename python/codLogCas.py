import mysql.connector as ProjetoFinanceiro
import bcrypt
import random
import string
from datetime import datetime,timedelta
import re
import funcoes

conexao = ProjetoFinanceiro.connect(host='localhost', database='banco_financeiro', user='root', password='Victor@12')

cursor = conexao.cursor()
acabar = False

while(acabar == False):
    try:
        print("\n---------------\nBEM VINDO AO DEFINIR NOME\n")

        opition = int(input("QUAL OPÇÃO VOCÊ DESEJA?\n1- LOGIN\n2- CADASTRO\n3-RECUPERAR SENHA\n"))

        if opition == 1:
            email = input("DIGITE SEU EMAIL:\n")
            senha = input("DIGITE SUA SENHA:\n")

            cursor.execute("SELECT * FROM tbl_usuario WHERE email_usuario=%s", (email,))
            
            registro = cursor.fetchone()

            #para pegar o id, para usarmos nas fk
            cursor.execute("SELECT id_usuario FROM tbl_usuario WHERE email_usuario=%s", (email,))
            registroFK_ID = cursor.fetchone()

            if registro:
                senha_armazenada = registro[6]
                
                if bcrypt.checkpw(senha.encode('utf-8'), senha_armazenada.encode('utf-8')):
                    print(f"\nLOGIN BEM SUCEDIDO\n---------------\n")
                    menu = True
                    while(menu == True):
                        print(f"BEM-VINDO(A) {registro[1]}\nVOCÊ TEM R$ {registro[7]}\n")
                        try:
                            
                            opition_menu = int(input("Qual opção você deseja?\n 1- RENDAS E DESPESAS\n 2- BOLETOS\n 3- CALENDÁRIO\n 4- CARTÃO DE CRÉDITO"))
                            if  opition_menu == 1:
                                
                                opition_menu1 = int(input("Qual opção deseja?:\n 1- ADICIONAR RENDAS \n 2- ADICIONAR DESPESAS \n 3- ALTERAR RENDAS \n 4- ALTERAR DESPESAS\n 5- EXCLUIR RENDA\n 6- EXCLUIR DESPESA\n"))
                                if opition_menu1 == 1:

                                    print("\nAgora vamos adicionar os seus principais meios de rendas! \n")

                                    salario = float(input("Insira o seu salário: "))
                                    pensao = float(input("\nQuanto recebe de pensão? Caso não receba informe o valor 0: "))
                                    auxilio = float(input("\nQuanto recebe de auxilio? Caso não receba informe o valor 0: "))
                                    investimentos = float(input("\nInsira seu retorno de investimento, você tem? Se não, informe o valor 0: "))

                                    nome_renda_mensal = ""
                                    desc_renda_mensal = ""
                                    valor_renda_mensal = 0

                                    comand = 'insert into tbl_renda_mensal (nome_renda_mensal, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Salario", salario, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()

                                    comand = 'insert into tbl_renda_mensal (nome_renda_mensal, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Pensao", pensao, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()

                                    comand = 'insert into tbl_renda_mensal (nome_renda_mensal, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Auxilio", auxilio, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()

                                    comand = 'insert into tbl_renda_mensal (nome_renda_mensal, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Investimentos", investimentos, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()


                                    condicaoR = True
                                    while (condicaoR == True):
                                            outrasRendas = str(input("\nFaltou alguma renda que queira especificar? Adicione ela! :)\n\nDigite 'S' para 'Sim', e 'N' para 'Não': "))
                                            
                                            if outrasRendas != 'S' and outrasRendas != 'Sim' and outrasRendas != 's' and outrasRendas != 'sim':
                                                condicaoR = False

                                            else:
                                                nome_renda_mensal = str(input("\nInsira o nome da sua renda: "))
                                                desc_renda_mensal = str(input("\ninsira uma descrição dessa renda: "))
                                                valor_renda_mensal = float(input("\nInsira quanto você recebe dessa renda: "))
                                                
                                                comand = 'insert into tbl_renda_mensal (nome_renda_mensal, desc_renda_mensal, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s, %s)'
                                                valores =	(nome_renda_mensal, desc_renda_mensal, valor_renda_mensal, registroFK_ID[0])
                                                cursor.execute(comand, valores)
                                                conexao.commit()

                                            if outrasRendas != 'N' and  outrasRendas != 'n' and outrasRendas != 'nao' and outrasRendas != 'Não':
                                                condicaoR = True
                                
                                elif opition_menu1 == 2:       
                                                      
                                    print("\nAgora vamos adicionar os seus principais despesas! \n")

                                    aluguel = float(input("Quanto você paga de aluguel?, se não, digite o valor 0: "))
                                    conta_de_luz = float(input("\nQuanto você paga em usa energia elétrica?: "))
                                    conta_de_agua = float(input("\nQuanto você gasta de água?: "))
                                    internet = float(input("\nQuanto você paga na sua internet?: "))
                                    mercado = float(input("\nEm média, quanto você gasta no mês em compras?: "))
                                    escola = float(input("\nVocê paga escola pro seu filho? se não digite o valor 0: "))

                                    nome_despesa_mensal = "Outros"
                                    desc_despesa_mensal = ""
                                    valor_despesa_mensal = 0

                                    comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Aluguel", aluguel, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()

                                    comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Conta de luz", conta_de_luz, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()

                                    comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Conta de água", conta_de_agua, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()

                                    comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Internet", internet, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()

                                    comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Mercado", mercado, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()

                                    comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
                                    valores =	("Escola", escola, registroFK_ID[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()

                                    condicaoD = True
                                    while (condicaoD == True):
                                            outrasDespesas = str(input("\nFaltou alguma despesa que queira especificar? Adicione ela! :)\n\nDigite 'S' para 'Sim', e 'N' para 'Não': "))
                                            
                                            if outrasRendas != 'S' and outrasDespesas != 'Sim' and outrasDespesas != 's' and outrasDespesas != 'sim':
                                                condicaoD = False

                                            else:
                                                nome_despesa_mensal = str(input("\nInsira o nome da sua despesa: "))
                                                desc_despesa_mensal = str(input("\ninsira uma descrição dessa despesa: "))
                                                valor_despesa_mensal = float(input("\nInsira quanto você paga despesa: "))

                                                comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, desc_despesa_mensal_, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s, %s)'
                                                valores =	(nome_despesa_mensal, desc_despesa_mensal, valor_despesa_mensal, registroFK_ID[0])
                                                cursor.execute(comand, valores)
                                                conexao.commit()
                                                
                                            if outrasDespesas != 'N' and  outrasDespesas != 'n' and outrasDespesas != 'nao' and outrasDespesas != 'Não':
                                                condicaoD = True

                                elif opition_menu1 == 3:
                                    
                                        print("VOCÊ QUER ALTERAR SUAS RENDAS, OK!")

                                        nome_renda_alter = str(input("Digite o nome da renda que quer alterar: \n"))
                                        valor_renda_alter = float(input("Digite o novo valor dessa renda: \n"))

                                        comand = 'UPDATE tbl_renda_mensal SET valor_renda_mensal = %s WHERE nome_renda_mensal = %s and fk_id_usuario = %s' 
                                        valores = (valor_renda_alter, nome_renda_alter,registroFK_ID[0])
                                        cursor.execute(comand,valores)
                                        conexao.commit()

                                elif opition_menu1 == 4:
                                    
                                        print("VOCÊ QUER ALTERAR SUAS DESPESAS, OK!")

                                        nome_despesa_alter = str(input("Digite o nome da despesa que quer alterar: \n"))
                                        valor_despesa_alter = float(input("Digite o novo valor dessa despesa: \n"))

                                        comand = 'UPDATE tbl_despesa_mensal SET valor_despesa_mensal = %s WHERE nome_despesa_mensal = %s and fk_id_usuario = %s' 
                                        valores = (valor_despesa_alter, nome_despesa_alter,registroFK_ID[0])
                                        cursor.execute(comand,valores)
                                        conexao.commit()

                                elif opition_menu1 == 5:
                                    
                                        print("VOCÊ QUER EXCLUIR RENDAS , OK!")

                                        nome_renda_delet = str(input("Digite o nome da renda que quer excluir: \n"))

                                        comand = 'delete from tbl_renda_mensal WHERE nome_renda_mensal = %s and fk_id_usuario = %s' 
                                        valores = (nome_renda_delet,registroFK_ID[0])
                                        cursor.execute(comand,valores)
                                        conexao.commit()

                                elif opition_menu1 == 6:
                                    
                                        print("VOCÊ QUER EXCLUIR DESPESAS , OK!")

                                        nome_despesa_delet = str(input("Digite o nome da despesa que quer excluir: \n"))

                                        comand = 'delete from tbl_despesa_mensal WHERE nome_despesa_mensal = %s and fk_id_usuario = %s' 
                                        valores = (nome_despesa_delet,registroFK_ID[0])
                                        cursor.execute(comand,valores)
                                        conexao.commit()

                            elif opition_menu == 2:
                                datacerta = False
                                valorcorreto = False
                                descricaoboleto = False
                                print("\n---------------\nADICIONAR BOLETOS\n")
                                descricao = input("DESCRIÇÃO DO BOLETO: ")
                                while (valorcorreto ==False):
                                    try:
                                        saldo = float(input("VALOR DO BOLETO: R$ "))
                                        if(saldo > 0):
                                            valorcorreto = True
                                        else:
                                            print("SALDO INVÁLIDO")
                                    except ValueError:
                                        print("INVÁLIDO\n")
                                        
                                while (datacerta == False):
                                    dt = input("DIGITE A DATA DE VENCIMENTO DO BOLETO. (DD/MM/AAAA)")
                                    try:
                                        data = datetime.strptime(dt, '%d/%m/%Y')
                                        data_inserida = data.date()
                                        data_atual = datetime.now().date()
                                        if data_inserida < data_atual:
                                            print("DATA DE VENCIMENTO NÃO PODE SER ANTERIOR A DATA ATUAL\n")
                                        else:
                                            datacerta = True
                                    except ValueError:
                                        print("FORMATO DE DATA INCORRETO. CERTIFIQUE-SE DE USAR O FORMATO 'DD/MM/AAAA'.")
                                

                                comand = 'INSERT INTO tbl_pagamentos (desc_pagamento,valor_pagamento,data_vencimento_pagamento,fk_id_usuario) values (%s,%s,%s,%s)'
                                valores = (descricao,saldo,data,registro[0])
                                cursor.execute(comand, valores)
                                conexao.commit()
                                print("BOLETO ADICIONADO COM SUCESSO!!")

                            elif opition_menu == 3:
                                consulta_calendario = False
                                while(consulta_calendario == False):
                                    data_calendario = input("DIGITE A DATA QUE VOCÊ DESEJA CONSULTAR NO CALENDÁRIO. (DD/MM/AAAA): ")
                                    try:
                                        data = datetime.strptime(data_calendario, '%d/%m/%Y')
                                        data_inserida = data.date()
                                        data_atual = datetime.now().date()
                                        if data_inserida < data_atual:
                                            print("DATA DE CONSULTA NÃO PODE SER ANTERIOR A DATA ATUAL\n")
                                        else:
                                            cursor.execute("SELECT  u.saldo_atual_usuario - SUM(p.valor_pagamento) AS total_valor FROM tbl_pagamentos p INNER JOIN tbl_usuario u ON p.fk_id_usuario = u.id_usuario WHERE u.id_usuario = %s and p.data_vencimento_pagamento < %s and p.data_vencimento_pagamento > %s", (registro[0],data_inserida,data_atual))
                                            saldo_futuro = cursor.fetchone()

                                            print(saldo_futuro[0])
                                            consulta_calendario = True
                                    except ValueError:
                                        print("FORMATO DE DATA INCORRETO. CERTIFIQUE-SE DE USAR O FORMATO 'DD/MM/AAAA'.")

                            elif opition_menu == 4:
                                option_cartao = int(input("QUAL OPÇÃO VOCÊ DESEJA?\n 1- CADASTRAR UM CARTÃO DE CRÉDITO\n 2-ADICIONAR COMPRA NO CARTÃO DE CRÉDITO\n 3- CONSULTAR CARTÕES"))
                                if(option_cartao == 1):
                                    print("\nCADASTRAR CARTÃO DE CRÉDITO\n")
                                    nomecerto = False
                                    limitecerto= False
                                    datavencimentocerta = False
                                    while(nomecerto ==False):
                                        nome_cartao = input("NOME DO CARTÃO DE CRÉDITO: ")
                                        cursor.execute("SELECT * FROM tbl_cartao_de_credito WHERE nome_cartao=%s", (nome_cartao,))
                                        cartaonome = cursor.fetchone()
                                        if(len(nome_cartao) >20):
                                            print("\nNOME INVÁLIDO\n")
                                        elif(cartaonome):
                                            print("\nCARTÃO JÁ REGISTRADO NA NOSSA BASE DE DADOS\n")
                                        else:
                                            nomecerto = True
                                    while(limitecerto == False):
                                        try:
                                            limite_cartao = float(input("QUAL O LIMITE DO SEU CARTÃO? "))
                                            if(limite_cartao >1):
                                                limitecerto = True
                                            else:
                                                print("\nVALOR INCORRETO\n")
                                        except ValueError:
                                            print("\nVALOR INCORRETO\n")
                                    while(datavencimentocerta == False):
                                        try:
                                            datavencimento = int(input("EM QUAL DIA VENCE O SEU CARTÃO? "))
                                            if(datavencimento <1 or datavencimento>31):
                                                print("DATA INVÁLIDA. (DIGITE DE 1 À 31)")
                                            else:
                                                datavencimentocerta = True
                                        except ValueError:
                                            print("DATA INVÁLIDA. (DIGITE DE 1 À 31)")
                                    comand = 'INSERT INTO tbl_cartao_de_credito (nome_cartao,limite,fk_id_usuario,cartaoativo) values (%s,%s,%s,true)'
                                    valores = (nome_cartao,limite_cartao,registro[0])
                                    cursor.execute(comand, valores)
                                    cursor.execute("SELECT * FROM tbl_cartao_de_credito WHERE nome_cartao=%s", (nome_cartao,))
                                    cartao = cursor.fetchone()
                                   
                                    
                                    data_atual = datetime.now()

                                    # Configure o dia desejado para o próximo mês
                                    data_insercao = data_atual.replace(day=datavencimento)
                                    meses_com_31 = {1, 3, 5, 7, 8, 10, 12}
                                    if data_insercao.month in meses_com_31:
                                            data_insercao + timedelta(days=31)
                                    elif data_insercao.month == 2:
                                        if (data_insercao.year % 4 == 0 and data_insercao.year % 100 != 0) or (data.year % 400 == 0):
                                            data_insercao + timedelta(days=29)
                                        else:
                                            data_insercao + timedelta(days=28)
                                    else:
                                        data_insercao + timedelta(days=30)

                                    
            
                                    # Crie uma lista para armazenar as datas dos próximos 6 meses com o dia especificado
                                    datas_a_inserir = [data_insercao]

                                    for i in range(12):
                                        # Adicione 30 dias para cada mês subsequente
                                        if data_insercao.month in meses_com_31:
                                            data_insercao += timedelta(days=31)
                                        elif data_insercao.month == 2:
                                            if (data_insercao.year % 4 == 0 and data_insercao.year % 100 != 0) or (data.year % 400 == 0):
                                                data_insercao += timedelta(days=29)
                                            else:
                                                data_insercao += timedelta(days=28)
                                        else:
                                            data_insercao += timedelta(days=30)
                                        datas_a_inserir.append(data_insercao)


                                    for data in datas_a_inserir:
                                        comand = 'INSERT INTO tbl_pagamentos (desc_pagamento, valor_pagamento, data_vencimento_pagamento, fk_id_usuario,fk_id_cartao) VALUES (%s, %s, %s, %s,%s)'
                                        valores = (nome_cartao, 0.0, data, registroFK_ID[0],cartao[0])  # Substitua os valores de descrição, valor e fk_id_usuario conforme necessário
                                        cursor.execute(comand, valores)
                                        conexao.commit()
                                    print("CARTÃO DE CRÉDITO CADASTRADO COM SUCESSO!!\n")
                                elif(option_cartao ==2):
                                    nomecompracerto = False
                                    valorcompracerto = False
                                    parcelascompracerto = False
                                    cartaoexistente = False
                                    while cartaoexistente == False:
                                        comand='SELECT * FROM tbl_cartao_de_credito where cartaoativo = true and fk_id_usuario = %s'
                                        valores = (registroFK_ID[0],)
                                        cursor.execute(comand, valores)
                                        cartoes = cursor.fetchall()
                                        count = 0
                                        print("EM QUAL CARTÃO VOCÊ DESEJA ADICIONAR A COMPRA?\n")
                                        while(len(cartoes) > count):
                                            print(count+1,'- ',cartoes[count][1])
                                            count +=1
                                        escolha = int(input("Digite o número do cartão desejado: "))
                                        if 1 <= escolha <= len(cartoes):
                                            cartao_escolhido = cartoes[escolha - 1]
                                            print("Você escolheu o cartão:", cartao_escolhido[1])
                                            cartaoexistente = True
                                        else:
                                            print("Escolha inválida. Por favor, digite um número válido.")

                                    while(nomecompracerto == False):
                                        nome_compra = input("DESCRIÇÃO DA COMPRA: ")
                                        if(len(nome_compra) < 300):
                                            nomecompracerto = True
                                        else:
                                            print("\nDESCRIÇÃO INVÁLIDA\n")
                                    while(valorcompracerto == False):
                                        valor_compra = float(input("VALOR TOTAL DA COMPRA: "))
                                        if(valor_compra > 0):
                                            valorcompracerto = True
                                        else:
                                            print("\nVALOR INVÁLIDO\n")
                                    while(parcelascompracerto == False):
                                        parcelas = int(input("EM QUANTAS PARCELAS FOI DIVIDIDA A COMPRA? "))
                                        if(parcelas > 0):
                                            parcelascompracerto = True
                                        else:
                                            print("\nVALOR INVÁLIDO\n")

                                    comand="UPDATE tbl_pagamentos SET valor_pagamento = valor_pagamento + %s WHERE fk_id_cartao = %s AND data_vencimento_pagamento >= CURDATE() LIMIT %s"
                                    valores = (valor_compra/parcelas,cartao_escolhido[0],parcelas)
                                    cursor.execute(comand, valores)
                                    conexao.commit()


                                    comand="INSERT INTO tbl_compras_cartoes (desc_pagamento, valor_compra, data_registro_compra, parcelas, fk_id_cartao) VALUES (%s, %s, %s, %s,%s)"
                                    valores = (nome_compra,valor_compra,datetime.now(),parcelas,cartao_escolhido[0])
                                    cursor.execute(comand, valores)
                                    conexao.commit()
                                elif(option_cartao == 3):

                                    cartaoexistente = False
                                    while cartaoexistente == False:
                                        comand='SELECT * FROM tbl_cartao_de_credito where cartaoativo = true and fk_id_usuario = %s'
                                        valores = (registroFK_ID[0],)
                                        cursor.execute(comand, valores)
                                        cartoes = cursor.fetchall()
                                        count = 0
                                        print("EM QUAL CARTÃO VOCÊ DESEJA ADICIONAR A COMPRA?\n")
                                        while(len(cartoes) > count):
                                            print(count+1,'- ',cartoes[count][1])
                                            count +=1
                                        escolha = int(input("Digite o número do cartão desejado: "))
                                        if 1 <= escolha <= len(cartoes):
                                            cartao_escolhido = cartoes[escolha - 1]
                                            print("Você escolheu o cartão:", cartao_escolhido[1])
                                            cartaoexistente = True
                                        else:
                                            print("Escolha inválida. Por favor, digite um número válido.")
                                    option_cartao2 = int(input("1- Consultar parcelas\n 2- Consultar compras"))
                                    if(option_cartao2 == 1):
                                        comand='SELECT * FROM tbl_pagamentos where fk_id_cartao = %s and fk_id_usuario = %s and valor_pagamento != 0'
                                        valores = (cartao_escolhido[0],registroFK_ID[0],)
                                        cursor.execute(comand, valores)
                                        parcelas_cartao = cursor.fetchall()
                                        for i in parcelas_cartao:
                                            print("Data:",i[3].strftime("%d/%m/%Y"),"| Valor:",i[2],"| Limite Restante: ",cartao_escolhido[2]-i[2])
                                    if(option_cartao2 ==2):
                                        comand='SELECT * FROM tbl_compras_cartoes where fk_id_cartao = %s'
                                        valores = (cartao_escolhido[0],)
                                        cursor.execute(comand, valores)
                                        compras_cartao = cursor.fetchall()
                                        for i in compras_cartao:
                                            print("Data e horário:",i[3].strftime("%d/%m/%Y %H:%M:%S"),"| Descrição:",i[4],"| Valor: ",i[1],"| Parcelas: ",i[2])



                                


                        except ValueError:
                            print("ALGO DEU ERRADO\n")
                else:
                    print("\n SENHA INCORRETA\n")
            else:
                print('\nEMAIL INCORRETO\n')


            

        elif opition == 2:
            emailcerto=False
            datacerta = False
            senhasiguais = False
            nomevalido = False
            cpfvalido = False
            telvalido = False
            saldocorreto = False

            while(emailcerto ==False):
                email = input("DIGITE O EMAIL:\n")
                regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                if re.match(regex, email):
                    cursor.execute("SELECT * FROM tbl_usuario WHERE email_usuario=%s", (email,))
                    registro = cursor.fetchone()
                    if registro:
                        print("EMAIL JÁ REGISTRADO EM NOSSA BASE DE DADOS\n")
                    else: 
                        emailcerto= True
                else:
                    print("EMAIL INVÁLIDO\n")
                    
            while(senhasiguais ==False):
                senha = input("DIGITE A SENHA: ")
                confsenha = input("DIGITE A CONFIRMAÇÃO DE SENHA SENHA: ")

                if(senha == confsenha):
                    if funcoes.verificar_senha(senha):
                        senhasiguais = True
                    else:
                        print("SENHA DEVE CONTER: NO MÍNIMO 8 CARACTERES, UM CARACTER ESPECIAL, UM NÚMERO E UMA LETRA MAIÚSCULA\n")
                else:
                    print("SENHAS NÃO CONFEREM\n")

            while(nomevalido==False):
                regex = r'^[A-Za-z\s]{2,50}$'
                nome = input("DIGITE O NOME: ")
                if re.match(regex, nome):
                    nomevalido= True
                else:
                    print("NOME INVÁLIDO\n")

            while (datacerta == False):
                dt = input("DIGITE SUA DATA DE NASCIMENTO (DD/MM/AAAA): ")
                try:
                    data = datetime.strptime(dt, '%d/%m/%Y')
                    print("DATA INSERIDA:", data)
                    datacerta = True
                except ValueError:
                    print("FORMATO DE DATA INCORRETO. CERTIFIQUE-SE DE USAR O FORMATO 'DD/MM/AAAA'.\n")
            
            while(cpfvalido == False):
                cpf = input("DIGITE SEU CPF: ")
                if funcoes.validar_cpf(cpf):
                    cpfvalido = True
                else:
                    print("CPF INVÁLIDO\n")
                    
            while(telvalido ==  False):
                tel = input("TELEFONE DO USUÁRIO (COM DD): ")
                if funcoes.validar_telefone(tel):
                    telvalido = True
                else:
                    print("TELEFONE INVÁLIDO\n")

            while(saldocorreto == False):
                try:
                    saldo = float(input("SALDO ATUAL: R$ "))
                    if(saldo >= 0):
                        saldocorreto = True
                    else: 
                        print("SALDO INVÁLIDO")
                except ValueError:
                    print("INVÁLIDO\n")

        
            salt = bcrypt.gensalt(12)
            hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), salt)

            comand = 'INSERT INTO tbl_usuario (email_usuario, senha_usuario,cpf_usuario,telefone_usuario,data_nasc_usuario,nome_usuario,saldo_atual_usuario,status_usuario) VALUES (%s, %s,%s,%s,%s,%s,%s,true)'
            valores = (email, hashed_senha,cpf,tel,data,nome,saldo)
            cursor.execute(comand, valores)
            conexao.commit()


                
        elif opition == 3:
            email = input("DIGITE O EMAIL:\n")
        
            cursor.execute("SELECT senha_usuario FROM tbl_usuario WHERE email_usuario=%s", (email,))
            registro = cursor.fetchone()

            if(registro):
                letras = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
                numeros = ''.join(random.choice(string.digits) for _ in range(3))
                codigo = letras + numeros
                print(f"Seu código é:\n---------\n{codigo}\n---------\n")
                cod = input("DIGITE O CÓDIGO:\n")
                if cod == codigo:
                    
                    senhasiguais = False
                    while(senhasiguais == False):
                        novasenha = input("DIGITE A NOVA SENHA")
                        confnovasenha = input("CONFIRME A NOVA SENHA")
                        if(novasenha == confnovasenha):
                            salt = bcrypt.gensalt(12)
                            hashed_novasenha = bcrypt.hashpw(novasenha.encode('utf-8'), salt)
                            if funcoes.verificar_senha(novasenha):
                                comand = 'UPDATE tbl_usuario SET senha_usuario = %s WHERE email_usuario = %s'
                                valores = (hashed_novasenha,email)
                                cursor.execute(comand,valores)
                                conexao.commit()
                                senhasiguais = True
                            else:
                                print("SENHA DEVE CONTER: NO MÍNIMO 8 CARACTERES, UM CARACTER ESPECIAL, UM NÚMERO E UMA LETRA MAIÚSCULA\n")
                        else:
                            print("SENHAS NÃO CONFEREM")
                    else:
                        print("CÓDIGO INCORRETO")
            else:
                print("EMAIL NÃO ENCONTRADO")

    except ValueError:

        print("\n ALGO DEU ERRADO\n")
    

   

#nome_produto = "banana"
#valor = 0.5

# Use placeholders para evitar injeção de SQL
#comando = 'INSERT INTO product (NAME_PRODUCT, VALUE) VALUES (%s, %s)'
#valores = (nome_produto, valor)

#cursor.execute(comando, valores)
#conexao.commit()

#conexao.commit()
conexao.close()