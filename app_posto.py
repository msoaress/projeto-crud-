import mysql.connector # type: ignore
import os
#import tkinter as tk
########################################################################################################################################

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='ERP_POSTO'
)
 
cursor = conexao.cursor()

## função inserir dados
 
def inserir_dados(tab):
    
    c_1 = 0
    c_2 = 0
    c_3 = 0
    c_4 = 0
    c_5 = 0
    c_6 = 0
    c_7 = 0
    c_8 = 0
    
    if tab == 1:
      
        c_1=input("digite o indice login: ")
        c_2=input("digite a senha: ")
        c_3=input("digite o cnpj: ")
        sql = "INSERT INTO LOGIN (ID, SENHA_APP ,CNPJ  ) VALUES (%s, %s, %s)"
        val = (c_1,c_2,c_3)
        cursor.execute(sql, val)
        conexao.commit()
        print("Dados inseridos com sucesso.")
    
    if tab == 2:
       
        c_1=input("digite o indice da tabela estoque_saida: ")
        c_2=input("digite codigo da bomba: ")
        c_3=input("digite o disel: ")
        sql = "INSERT INTO ESTOQUE_SAÍDA (ID,  CÓD_BOMBA ,DIESEL  ) VALUES (%s, %s, %s)"
        val = (c_1,c_2,c_3)
        cursor.execute(sql, val)
        conexao.commit()
        print("Dados inseridos com sucesso.")
    
    if tab == 3:
        
        c_1=input("digite o indice da tabela vendas: ")
        c_2=input("digite a bomba: ")
        c_3=input("digite a data: ")
        c_4=input("digite o codigo da bomba: ")
        c_5=input("digite a diesel: ")
        c_6=input("digite a alcool: ")
        c_7=input("digite a gasolina: ")
        c_8=input("digite a gnd: ")
        sql = "INSERT INTO VENDAS (ID,BOMBAS_POSTO,DATA_HORAS,CÓD_BOMBA,DIESEL,ÁLCOOL,GASOLINA, GNV) VALUES (%s, %s, %s,%s, %s, %s,%s,%s)"
        val = (c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8)
        cursor.execute(sql, val)
        conexao.commit()
        print("Dados inseridos com sucesso.")
    
    if tab == 4:
        
        c_1=input("digite o indice da tabela custos: ")
        c_2=input("digite custo funcionario: ")
        c_3=input("digite custo produto: ")
        c_4=input("digite o codigo da bomba: ")
        c_5=input("digite custo  alcool: ")
        sql = "INSERT INTO CUSTOS (ID, FUNCIONÁRIOS,PRODUTOS, CÓD_BOMBA,ALCOOL) VALUES (%s, %s, %s, %s, %s)"
        val = (c_1,c_2,c_3,c_4,c_5)
        cursor.execute(sql, val)
        conexao.commit()
        print("Dados inseridos com sucesso.")
        
    if tab == 5:
        
        c_1=input("digite o indice tabela lucro mensal: ")
        c_2=input("digite a data: ")
        c_3=input("digite lucro: ")
        c_4=input("digite custos: ")
        c_5=input("digite o codigo da bomba: ")
        sql = "INSERT INTO LUCRO_MENSAL (ID,DATA_MÊS,LUCRO_REAL,CUSTOS,CÓD_BOMBA) VALUES (%s, %s, %s, %s, %s)"
        val = (c_1,c_2,c_3,c_4,c_5)
        cursor.execute(sql, val)
        conexao.commit()
        print("Dados inseridos com sucesso.")
    
    
    
    
#_________________fim função imserir dados___________#
    
    
########################################################################################################################################
 
 
 #________leitura de dados____________#
 
def ler_dados(tab):
    
    if tab == 1:
        cursor.execute("SELECT * FROM LOGIN ")
        resultados = cursor.fetchall()
        print("LOGIN")
        for resultado in resultados:
         print(resultado) 
               
    if tab == 2:  
        cursor.execute("SELECT * FROM ESTOQUE_SAÍDA ")
        resultados = cursor.fetchall()
        print("ESTOQUE_SAÍDA")
        for resultado in resultados:
         print(resultado)
        
    if tab == 3:  
        cursor.execute("SELECT * FROM VENDAS ")
        resultados = cursor.fetchall()
        print("VENDAS")
        for resultado in resultados:
         print(resultado)
        
    if tab == 4:  
        cursor.execute("SELECT * FROM CUSTOS ")
        resultados = cursor.fetchall()
        print("CUSTOS")
        for resultado in resultados:
         print(resultado)
        
        
    if tab == 5:  
        cursor.execute("SELECT * FROM LUCRO_MENSAL ")
        resultados = cursor.fetchall()
        print("LUCRO_MENSAL")
        for resultado in resultados:
         print(resultado)
         
         
   #fim função leitura de dados   
      
 ########################################################################################################################################
      

 #  _____________________função para alteração de dados ____________#
 
def alterar_dados(tab):
    
    if tab == 1:    
        
              
        sql = "UPDATE LOGIN SET CNPJ = %s, SENHA_APP = %s WHERE ID = %s"
        id_login = input("digite o id a ser alterados: ")        
        novo_CNPJ = input("digite o cnpj ser alterados: ")        
        nova_SENHA = input("digite a senha a ser alterados: ")
        val =(novo_CNPJ, nova_SENHA,id_login)
        cursor.execute(sql,val)
        conexao.commit()
        print("Dados alterados com sucesso.")
    
    if tab == 2:    
        
              
        sql = "UPDATE ESTOQUE_SAÍDA SET DIESEL = %s,  CÓD_BOMBA = %s WHERE ID = %s"
        id = input("digite o id a ser alterados: ")        
        novo_cod = input("digite o cód_bomba ser alterados: ")        
        novo_combustivel = input("digite a diesel a ser alterados: ")
        val =(novo_combustivel, novo_cod,id)
        cursor.execute(sql,val)
        conexao.commit()
        print("Dados alterados com sucesso.")
        
    if tab == 3:   
        
              
        sql = """UPDATE VENDAS SET BOMBAS_POSTO = %s,  
        DATA_HORAS = %s,  
        CÓD_BOMBA = %s,  
        DIESEL = %s,  
        ÁLCOOL = %s,  
        GASOLINA = %s,
        GNV = %s WHERE ID = %s"""
        id = input("digite o id a ser alterados: ")        
        novo_data= input("digite o data ser alterados: ")        
        nova_cod_bomba = input("digite  cód_bomba a ser alterados: ")
        diesel= input("digite o disel a ser alterados: ")        
        alcool= input("digite o alcool ser alterados: ")        
        gasolina = input("digite a gasolina a ser alterados: ")
        gnd = input("digite a gnd a ser alterados: ")
        bombas = input("digite a bombas a ser alterados: ")
        val =(bombas,novo_data,nova_cod_bomba,diesel,alcool,gasolina, gnd,id)
        cursor.execute(sql,val)
        conexao.commit()
        print("Dados alterados com sucesso.")
    
    if tab == 4:    
        
              
        sql = """UPDATE CUSTOS SET FUNCIONÁRIOS = %s,  
         PRODUTOS = %s,  
         CÓD_BOMBA = %s ,  
         ALCOOL = %s WHERE ID = %s"""
        id_ = input("digite o id a ser alterados: ")        
        alcool = input("digite o custo alcool ser alterados: ")        
        nova_cod_bomba = input("digite cod_bomba a ser alterados: ")
        funcionario = input("digite func_custo a ser alterados: ")
        produtos = input("digite a produto_custo a ser alterados: ")
        val =(funcionario,produtos,nova_cod_bomba, alcool,id)
        cursor.execute(sql,val)
        conexao.commit()
        print("Dados alterados com sucesso.")
        
    if tab == 5:    
        
              
        sql = """UPDATE LUCRO_MENSAL SET DATA_MÊS = %s,  
        LUCRO_REAL = %s,  
        CUSTOS = %s,  
        CÓD_BOMBA = %s WHERE ID = %s"""
        id_login = input("digite o id a ser alterados: ")        
        nova_cod_bomba = input("digite cod_bomba a ser alterados: ")   
        novo_data= input("digite o data ser alterados: ")   
        nova_lucro = input("digite lucro a ser alterados: ")
        nova_custos = input("digite custo a ser alterados: ")
        val =(novo_data,nova_lucro,nova_custos,nova_cod_bomba,id_login)
        cursor.execute(sql,val)
        conexao.commit()
        print("Dados alterados com sucesso.")
        
        
 #fim função alterar dados     
 
 
 
 ########################################################################################################################################
  
   
        
#___________________________deletar dados________________________________#        
        
def deletar_dados(tab):
    
    if tab == 1:
        id_=input("digite o indice  a ser deletador: ")
        sql = "DELETE FROM LOGIN WHERE ID = %s"
        val = (id_)
        cursor.execute(sql, (val,))
        conexao.commit()
        print("Dados deletados com sucesso.")
        
    if tab == 2:
        id_=input("digite o indice a ser deletador: ")
        sql = "DELETE FROM ESTOQUE_SAÍDA WHERE ID = %s"
        val = (id_)
        cursor.execute(sql, (val,))
        conexao.commit()
        print("Dados deletados com sucesso.")
        
        
    if tab == 3:
        id_=input("digite o indice a ser deletador: ")
        sql = "DELETE FROM VENDAS WHERE ID = %s"
        val = (id_)
        cursor.execute(sql, (val,))
        conexao.commit()
        print("Dados deletados com sucesso.")
        
        
    if tab == 4:
        id_=input("digite o indice a ser deletador: ")
        sql = "DELETE FROM CUSTOS WHERE ID = %s"
        val = (id_)
        cursor.execute(sql, (val,))
        conexao.commit()
        print("Dados deletados com sucesso.")
    
    
    if tab == 5:
        id_aluno=input("digite o indice a ser deletador: ")
        sql = "DELETE FROM LUCRO_MENSAL WHERE ID = %s"
        val = (id_aluno)
        cursor.execute(sql, (val,))
        conexao.commit()
        print("Dados deletados com sucesso.")
        
    
#fim função deletar


 
 ########################################################################################################################################



#bloco de codigo para interação com banco de dados



#___________________autenticação_______________________

i=1

while i==1:
    cont=1
    opcao=0
    senha=0
    login=0
    lista=[]
    x=0
    cursor.execute("SELECT * FROM LOGIN ")
    resultados = cursor.fetchall()
    print("para acesso a ao sistema digite seu login e senha: ")
    login=input("digite seu cnpj:  ")
    senha=input("digite sua senha: ")
    for resultado in resultados:
        lista=resultado 
             
        if (login == str(lista[0])) and (senha ==  str(lista[1])):  
        
                 x = 1  
                 i = 0
                 break  
                              
        
        else:  
            print("senha ou login invalidos")      

    if i == 1:   
        i=int(input("""
                    digite as opções a seguir: 
                    (1) continuar
                    (2) encerra sistema
                    # digite a opção: """))
    

    #__________________fim autenticação_________________________________________________
    
    

while x == 1: 
    os.system('cls')     
   
    print("liberado acesso: true \a" )
    
    import winsound

    # Emite um bip com frequência de 1000 Hz e duração de 100 milissegundos
    winsound.Beep(1000, 500)

 
     
    while cont == 1:     
        x=0
        
        print("""\n
        digite oque quer fazer, as opções disponiveis são: 
               (1)ler dados
               (2)altera dados
               (3)inserir dados
               (4)deletar dados""")
        opcao= int (input("digite a opção: "))
        
        
        
        os.system('cls') 
    
        
            # leitura de dados
        if opcao == 1:
                print("\ndigite qual tabela você quer ler digite as seguintes opções: ")
                print("""
                (1) LOGIN
                (2) ESTOQUE_SAÍDA
                (3) VENDAS 
                (4) CUSTOS
                (5) LUCRO_MENSAL
                    """)
                tab = int (input("digite a opção: "))
                ler_dados(tab)
                
            #alteração de dados
            
        if opcao == 2:
                print("\ndigite qual tabela você quer altera os dados digite as seguintes opções: ")
                print("""
                (1) LOGIN
                (2) ESTOQUE_SAÍDA
                (3) VENDAS 
                (4) CUSTOS
                (5) LUCRO_MENSAL
                    """)
                tab = int (input("digite a opção: "))
                alterar_dados(tab)
        
            #inserir dados    
            
        if opcao == 3:
                print("\ndigite qual tabela você quer inserir dados digite as seguintes opções: ")
                print("""
                (1) LOGIN
                (2) ESTOQUE_SAÍDA
                (3) VENDAS 
                (4) CUSTOS
                (5) LUCRO_MENSAL
                    """)
                tab = int (input("digite a opção: "))
                inserir_dados(tab)
        
            #deletar dados
        
        if opcao == 4:
                print("\ndigite qual tabela você quer deletar os dados digite as seguintes opções: ")
                print("""
            (1) LOGIN
            (2) ESTOQUE_SAÍDA
            (3) VENDAS 
            (4) CUSTOS
            (5) LUCRO_MENSAL
                """)
                tab = int (input("digite a opção: "))
                deletar_dados(tab)  
                
                
            
        print("""
                digite as opções a seguir: 
                (1) continuar
                (2) encerra sistema:  """)
        cont= int (input("digite a opção: "))
       

    
 
import winsound

# Emite um bip com frequência de 1000 Hz e duração de 100 milissegundos
winsound.Beep(700, 500)
    
cursor.close()
conexao.close()
print("""\n
      cursor.close
      conexao.close""")

########################################################################################################################################


"""janela = tk.Tk()

janela.title("Posição de botão")

janela.geometry("300x200")



botao1 = tk.Button(janela, text="Botão 1")

botao1.place(x=50, y=50)



botao2 = tk.Button(janela, text="Botão 2")

botao2.place(x=500, y=50)



botao3 = tk.Button(janela, text="Botão 3")

botao3.place(x=50, y=100)



botao4 = tk.Button(janela, text="Botão 4")

botao4.place(x=0, y=0)



janela.mainloop()"""

########################################################################################################################################
