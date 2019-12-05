from Screens import tela_3
from Screens import editora
from Screens import tela_2
from Screens import tela_1
import os
def interface(lista):
    cont=0
    
    for elem in lista:
        
        elem=elem[:-1]
        
        elem=elem.split("/")
        
        cont+=1
        
        print(cont,"=",elem[0],"--",elem[1],end="\n")
    
    verify=0
    while verify == 0:
        choice=input("Escolha uma opção invocador, para ver o save digite o seu número, para editar digite (-) e para voltar digite (=), para apagar um save digite(*) >> ")
        linha()
        
        if choice == "*":
            
            dic={"rota":elem[0],"nome":"delete"} 
            print("digite o numero do save a ser apagado>> ")
            try:
                line = int(input("linha>> "))
                linha()
                
                editora.editarquivo(dic,line,lista)
                print("*[save apagado com suscesso, invocador]*")
                verify = 1
                return "*"
            
            except:
                print("*[erro ao procurar]*")
                verify=0
        
        if choice == "=":
            
            return "*"

        if choice == "-":
            
            os.system("clear")
            print("*[entrando no menu de edição...]*")
            
            cont=0
            for elem in lista:

                elem=elem[:-1]
    
                elem=elem.split("/")

                cont+=1

                print(cont,"=",elem[0],"--",elem[1],end="\n")
    
            verify = 0
            while verify == 0:
                try: 
                    linha()
                    line=int(input("digite o numero do save a ser editado ,invocador>> "))
                    linha()
                except:
                    print("*[use os números invocador :)]*")
                    verify=0

                if line > cont:
                    
                    print("*[não existe esse save]*")
                    verify = 0
                if line <= cont:
                    verify=1 
                    editora.edit(lista,line)
                    return "*"
                    verify=1

        if choice != "*" and choice != "=" and choice != "-":
            
            try :        
                
                save=lista[int(choice)-1] 
                os.system("clear")
                verify=1
                return save
            
            except:
                
                print("*[opção inexistente invocador]*")
        
    return "*"
def linha():
    print("-="*40)
def view():
    linha()   
    print("-="*20,"VIEW","-="*20)
    #linha()
    verify = 0
    while verify == 0:
        print("*[escolha uma dessas rotas invocador top, mid, adcarry, suport, jungler.]*")
        print("*[Para sair invocador , digite = ]*")
        linha()
        response =input("Qual a lane você deseja ver os saves invocador ?>>")
        linha()
        if response == '=':
            return '*'
            verify = 1
        else:
            if response != "top" and response != "mid" and response != "adcarry" and response != "suport" and response != "jungler" and response != '=':
                verify = 0
                print("*[invocador essa lane não existe , tente novamente :)]*")
                linha()

            else:
                print('olá', response)
                verify = 1
    
    if response == "adcarry":
        
        arq=open("adcarry.txt","r")
        adlist=arq.readlines()
        return interface(adlist)
    
    if response == "mid":
        
        arq=open("mid.txt","r")
        midlist=arq.readlines()
        return interface(midlist)

    if response == "top":
        
        arq=open("top.txt","r")
        toplist=arq.readlines()        
        return interface(toplist)

    if response == "jungler":

        arq=open("jungler.txt","r")    
        junglerlist=arq.readlines()
        return interface(junglerlist)

    if response == "suport" :
        
        arq=open("suport.txt", "r")
        suportlist=arq.readlines()
        return interface(suportlist)


