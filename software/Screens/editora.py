import os
from Screens import tela_4
from tela_3 import anti_crash
def editarquivo(dic,line,dados):
    cont=0
    save=[]
    
    for value in dic.values():
        if value == "" or value == " ": 
            save.append("x.x")
            save.append("/")
        else:
            value = tela_3.anti_crash(value)
            save.append(value)
            save.append("/")
    if dic["nome"] != "":    
        save.append("\n")
        dados[line-1]=''.join(save)
    
    if dic["rota"] == "adcarry":

        arq=open("adcarry.txt","w")
        arq.write("")
    
    if dic["rota"] == "mid":

        arq=open("mid.txt","w")
        arq.write("")    
    if dic["rota"] == "top":

        arq=open("top.txt","w")
        arq.write("")

    if dic["rota"] == "jungler":

        arq=open("jungler.txt","w")
        arq.write("")

    if dic["rota"] == "suport" :

        arq=open("suport.txt", "w")
        arq.write("")
    arq.close()
    if dic["nome"] == "delete":
        dados.pop(line-1)
        
    for elem in dados: 
        
        string=elem
        
        if dic["rota"] == "adcarry":

            arq=open("adcarry.txt","a")
            adlist=string
            arq.write(adlist)

        if dic["rota"] == "mid":

            arq=open("mid.txt","a")
            midlist=string
            arq.write(midlist)

        if dic["rota"] == "top":

            arq=open("top.txt","a")
            toplist=string
            arq.write(toplist)
    
        if dic["rota"] == "jungler":

            arq=open("jungler.txt","a")
            junglerlist=string
            arq.write(junglerlist)

        if dic["rota"] == "suport" :

            arq=open("suport.txt", "a")
            suportlist=string
            arq.write(suportlist)

    arq.close()
    return 
def logo():
    print("-="*20 ,"EDIT","-="*20)
def linha():
    print("-="*40)

def edit(dados,line):
    
    dado=(dados[line-1]) 
    dado=dado.split("/")
          
    dic = {'rota': dado[0],
            'nome': dado[1],
            'dicas':dado[2],
            'itens_padroes':dado[3] ,
            'itens_alternativos':dado[4],
            'skill.q':dado[5],
            'skill.e': dado[6],
            'skill.w': dado[7],
            'skill.r': dado[8],
            'passive':dado[9],
            'taticas_ing':dado[10],
            'win_rate': dado[11],
            'dificuldade':dado[12],
            'weak_again':dado[13],
            "win_rate_elo":dado[14]
            }
    verify = 0
    logo()
    print("dicionario",dic)
    linha()
    print("keys usaveis >>>",dic.keys())
    
    while verify == 0:
        logo()
        print()
        print("*[não se esqueça de digitar igual ao mostrado para acessar o local e para sair digite (=), invocador]*")
        print()
        linha()
        print()
        choice=input("digite o local que deseja editar >>>")
        print()
        linha()
        
        if choice == "=":
            break
        
        if choice != "rota" and choice!="nome" and choice!="dicas" and choice != "itens_padroes" and choice!="itens_alternativos" and choice!= "skill.e" and choice!= "skill.q" and choice!= "skill.w" and choice!="skill.r" and choice!= "passive" and choice!= "taticas_ing" and choice!="win_rate" and choice!="dificuldade" and choice!="weak_again" and choice!= "win_rate_elo" and choice!= "=":
            print()
            print("*[Esse local não existe invocador]*")
            print()
            verify=0
        
        else:
            logo()
            print()
            print('Lembrando que não poderá ser usadas / nos novos valores adicionados')
            print()
            mudanca=input("digite a nova mudança >>")
            mudanca =  tela_3.anti_crash(mudanca)
            print()
            linha()
            print()
            print("antigo>>>",dic[choice],"// novo>>>",mudanca)
            print()
            dic[choice]=mudanca
            

    os.system("clear")
    editarquivo(dic,line,dados)
    return
