from Screens import tela_3
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
        choice=input("Qual save deseja ver,invocador?ou caso queira sair digite = >>")
        linha()
        if choice == "=":
            return "="
        else:
            try :        
                save=lista[int(choice)-1] 
                os.system("clear")
                verify=1
                return save
            except:
                print("opção inexistente invocador")
    
    
def linha():
    print("-="*40)
def view():
    linha()   
    verify = 0
    while verify == 0:
        linha()
        response =input("Qual a lane você deseja ver os saves invocador ?>>")
        linha()
        if response != "top" and response != "mid" and response != "adcarry" and response != "suport" and response != "jungler":
            verify = 0
            print("invocador essa lane não existe , tente novamente :)")
        else:
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
    

