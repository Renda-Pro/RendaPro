import mysql.connector as ProjetoFinanceiro

conexao = ProjetoFinanceiro.connect(host='localhost', database='banco_financeiro', user='root', password='2004')

cursor = conexao.cursor() 


email = "admin123@gmail.com"
hashed_senha = "admin123"
cpf = "12345678910"
tel = "40028922"
data = "2000-01-01"
nome = "administrador"
#Primeira tela após o login do usuario
'''
saldo = float(input("Insira quanto você tem disponivel em seu saldo: "))

comand = 'INSERT INTO tbl_usuario (email_usuario, senha_usuario,cpf_usuario,telefone_usuario,data_nasc_usuario,nome_usuario,saldo_atual_usuario,status_usuario) VALUES (%s, %s,%s,%s,%s,%s,%s,true)'
valores = (email, hashed_senha,cpf,tel,data,nome,saldo)
cursor.execute(comand, valores)
conexao.commit()



print("\nAgora vamos adicionar os seus principais meios de rendas! \n")

salario = float(input("Insira o seu salário: "))
pensao = float(input("\nQuanto recebe de pensão? Caso não receba informe o valor 0: "))
auxilio = float(input("\nQuanto recebe de auxilio? Caso não receba informe o valor 0: "))
investimentos = float(input("\nInsira seu retorno de investimento, você tem? Se não, informe o valor 0: "))

nome_renda_mensal = ""
desc_renda_mensal = ""
valor_renda_mensal = 0

comand = 'insert into tbl_renda_mensal (nome_renda_mensal, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s)'
valores =	("Salario", salario, "1")
cursor.execute(comand, valores)
conexao.commit()

comand = 'insert into tbl_renda_mensal (nome_renda_mensal, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s)'
valores =	("Pensao", pensao, "1")
cursor.execute(comand, valores)
conexao.commit()

comand = 'insert into tbl_renda_mensal (nome_renda_mensal, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s)'
valores =	("Auxilio", auxilio, "1")
cursor.execute(comand, valores)
conexao.commit()

comand = 'insert into tbl_renda_mensal (nome_renda_mensal, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s)'
valores =	("Investimentos", investimentos, "1")
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
            
            comand = 'insert into tbl_renda_mensal (nome_renda_mensal, desc_renda_mensal_, valor_renda_mensal, fk_id_usuario) values (%s, %s, %s, %s)'
            valores =	(nome_renda_mensal, desc_renda_mensal, valor_renda_mensal, "1")
            cursor.execute(comand, valores)
            conexao.commit()

        if outrasRendas != 'N' and  outrasRendas != 'n' and outrasRendas != 'nao' and outrasRendas != 'Não':
            condicaoR = True

   
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
valores =	("Aluguel", aluguel, "1")
cursor.execute(comand, valores)
conexao.commit()

comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
valores =	("Conta de luz", conta_de_luz, "1")
cursor.execute(comand, valores)
conexao.commit()

comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
valores =	("Conta de água", conta_de_agua, "1")
cursor.execute(comand, valores)
conexao.commit()

comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
valores =	("Internet", internet, "1")
cursor.execute(comand, valores)
conexao.commit()

comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
valores =	("Mercado", mercado, "1")
cursor.execute(comand, valores)
conexao.commit()

comand = 'insert into tbl_despesa_mensal (nome_despesa_mensal, valor_despesa_mensal, fk_id_usuario) values (%s, %s, %s)'
valores =	("Escola", escola, "1")
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
            valores =	(nome_despesa_mensal, desc_despesa_mensal, valor_despesa_mensal, "1")
            cursor.execute(comand, valores)
            conexao.commit()
            
        if outrasDespesas != 'N' and  outrasDespesas != 'n' and outrasDespesas != 'nao' and outrasDespesas != 'Não':
            condicaoD = True

if conexao.is_connected():
    cursor.close()
    conexao.close()
    print("A conexão foi encerrada")


print("\n\n\n\n\n\nObrigado por adicionar essas informações!")

print("\nAqui está sua rendas e despesas mensais!: \n")

print("\n\n\n######Rendas Mensais######")
print("\nSalário: R$", salario)
print("Pensão: R$", pensao)
print("Auxilio: R$", auxilio)
print("Investimentos: R$", investimentos)


print(nome_renda_mensal,": R$", valor_renda_mensal)
print(desc_renda_mensal)

somaRenda = salario+pensao+auxilio+investimentos+valor_renda_mensal
print("\nSua Renda por mês: ",somaRenda)

print("\n\n\n######Despesas Mensais######")
print("\nAluguel: R$", aluguel)
print("Conta de luz: R$", conta_de_luz)
print("Conta_de_agua: R$", conta_de_agua)
print("Internet: R$", internet)
print("Mercado: R$", mercado)
print("Escola: R$", escola)

print(nome_despesa_mensal,": R$", valor_despesa_mensal)
print(desc_despesa_mensal)

subtrDespesas = aluguel+conta_de_luz+conta_de_agua+internet+mercado+escola+valor_despesa_mensal
print("\nO Total das suas despesas no mês é: R$",subtrDespesas)

diferenca = somaRenda - subtrDespesas
if diferenca >0:
    print("\nNo mês, você ficou positivo! sobraria: R$",diferenca, "em seu saldo")

elif diferenca <0:
    print("\nNo mês, você ficou negativo! seu saldo seria: R$", diferenca)

else:
    print("\nNo mês, você zerado saldo seria: R$", diferenca)

print("\nE seu saldo é: R$",saldo)
'''



'''

opition_menu1 = int(input("Qual opção deseja?:\n 1- ADICIONAR RENDAS \n 2- ADICIONAR DESPESAS \n 3- OLHAR RENDAS E DESPESAS "))
if opition_menu1 == 3:
    cursor.execute("SELECT id_usuario FROM tbl_usuario WHERE email_usuario=%s", (email,))
    registro = cursor.fetchone()

    cursor.execute("SELECT nome_renda_mensal, valor_renda_mensal FROM tbl_renda_mensal WHERE fk_id_usuario=%s", (registro))
    registro = cursor.fetchone()
    print(registro)
else:
    print("deu errado")

'''

            #para pegar o id, para usarmos nas fk
cursor.execute("SELECT id_usuario FROM tbl_usuario WHERE email_usuario=%s", (email,))
registroFK_ID = cursor.fetchone()

print(registroFK_ID)