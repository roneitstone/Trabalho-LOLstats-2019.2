import os
def arquive(dic):
    
    cont=0
    for value in dic.values():
        
        if dic["Rota"] == "top": 
            arq=open("top.txt","a")
            
            for empty in value:
                if empty == " ":
                    cont+=1
                    if cont>=2:
                        arq.write("x.x")
                        arq.write("/")

            if value == "" or value == " ": 
                arq.write("x.x")
                arq.write("/")

            else:

                arq.write(value)
                arq.write("/")    
        
        if dic["Rota"] == "mid":
        
            arq=open("mid.txt","a")
            
            for empty in value:
                if empty == " ":
                    cont+=1
                    if cont>=2:
                        arq.write("x.x")
                        arq.write("/")

            if value == "" or value == " ":
                arq.write("x.x")
                arq.write("/")

            else:

                arq.write(value)
                arq.write("/")  

        if dic["Rota"] == "jungler":
        
            arq=open("jungler.txt","a")
            
            for empty in value:
                if empty == " ":
                    cont+=1
                    if cont>=2:
                        arq.write("x.x")
                        arq.write("/")
    
            if value == "" or value == " ": 
                arq.write("x.x")
                arq.write("/")

            else:
                arq.write(value)
                arq.write("/")

        if dic["Rota"] == "suport":
        
            arq=open("suport.txt","a")
            
            
            for empty in value:
                if empty == " ":
                    cont+=1
                    if cont>=2:
                        arq.write("x.x")
                        arq.write("/")
            if value == "" or value == " ": 
                arq.write("x.x")
                arq.write("/")
            else:
                arq.write(value)
                arq.write("/")

        if dic["Rota"] == "adcarry":
        
            arq=open("adcarry.txt","a")
            
            
            for empty in value:
                if empty == " ":
                    cont+=1
                    if cont>=2:
                        arq.write("x.x")
                        arq.write("/")
            
            if value == "" or value == " ": 
                arq.write("x.x")
                arq.write("/")
            else:
                arq.write(value)
                arq.write("/")

    arq.write("\n")        
    arq.close()
    return 

def logo():
    return "#"*20,"LOLSTATS","#"*20
def linha():
    return "-="*40
def primeiros_dados (save):
    if len(save) == 0: 
        name = input('Nome do campeão: ')
        saida_b = ''
        itens = []
        itens_b = []
        i_tens = 'a'
        i_tens_b = 'b'
        saida = ''
        print("invocador escreva os dados que você quer armazenar agora e não esqueça , caso queira sair é só apertar = em qualquer pergunta ")
        if name == '=':
            print('saindo...')
            return '='
        else:
            verify=0
            while verify == 0 :
                print("Lembrando invocador , as unicas rotas aceitas são (top , jungler , mid , adcarry e suport) tilta não XD")
                route = input('Rota: ')
                if route == "=":
                    verify=1
                if route != "jungler" and route != "top" and route != "mid" and route != " adcarry" and route != "suport":
                    verify=0
                    print("digite uma rota existente, invocador :/")
                else:
                    verify=1
            
            
            if route == '=':
                print('saindo...')
                return '='
            else:
                while i_tens != 'sair': 
                    print("agora se quiser sair dos (itens indicados) é so escrever sair")
                    i_tens =  input('Itens indicados: ')
                    if i_tens == '=':
                        saida = '='
                        i_tens = 'sair'
                    itens.append(i_tens)
                if saida == '=':
                    print('saindo...')
                    return '='
                else:
                    itens.pop()
                    print('digite os itens e quando acabar digite sair para continuar')
                    print('para sair do programa ainda vale digitar =')
                    while i_tens_b != 'sair': 
                        i_tens_b =  input('Itens alternativos: ')
                        if i_tens_b == '=':
                            saida_b = '='
                            i_tens_b = 'sair'
                        itens_b.append(i_tens_b)
                    if saida_b == '=':
                        print('saindo...')
                        return '='
                    else:
                        itens_b.pop()
                        skill_Q = input('Skill Q: ')
                        if skill_Q == '=':
                            print('saindo...')
                            return  '=' 
                        else:
                            skill_W = input('Skill W: ')
                            if skill_W == '=':
                                print('saindo...')
                                return '='
                            else:
                                skill_E = input('Skill E: ')
                                if skill_E == '=':
                                    print('saindo...')
                                    return '='
                                else:
                                    skill_R = input('Skill R: ')
                                    if skill_R == '=':
                                        print('saindo...')
                                        return '='
                                    else:
                                        
                                        dica=input("dicas early-game >> ")
                                        if dica == '=':
                                            print('saindo...')
                                            return '='
                                        else:
                                            tatic=input("diga qual tática recomenda >> ")
                                            if tatic == '=':
                                                print('saindo...')
                                                return '='
                                            else:
                                                wr=input("diga o winrate desse tipo de game >>")
                                                if wr == '=':
                                                    print('saindo...')
                                                    return '='
                                                else:
                                                    dificult=input("diga a dificuldade >>")
                                                    if dificult == '=':
                                                        print('saindo...')
                                                        return '='
                                                    else:

                                                        wa=input("diga os counters nesse match >>")
                                                        if wa == '=':
                                                            print('saindo...')
                                                            return '='
                                                        else:
                                                            wrelo=input("diga o winrate no seu elo >>")
                                                            if wrelo == '=':
                                                                print('saindo...')
                                                                return '=' 
                                                            else:
                                                                passive=input("diga a passiva do champion>>")
                                                                if passive == "=":
                                                                    print("saindo...")
                                                                    return '='
                                                                os.system("clear")
                                                                print("Parábens invocador , agora você tem um save :)")

                                                                dic = {'Rota': route,
                                                                        'Nome': name,
                                                                        'dicas':dica,
                                                                        'Itens_Padroes': "".join(itens),
                                                                        'Itens_Alternativos': "".join(itens_b),
                                                                        'Skill.Q': skill_Q,
                                                                        'Skill.E': skill_E,
                                                                        'Skill.W': skill_W,
                                                                        'Skill.R': skill_R,
                                                                        'passive': passive,
                                                                        'taticas_ING':tatic,
                                                                        'win_rate': wr,
                                                                        'dificuldade':dificult,
                                                                        'weak_again':wa,
                                                                        "win_rate_elo":wrelo
                                                                        }
                                                                
                                                                save+=dic.values()
                                                                arquive(dic)
                                                                return  save
    else:
        
        save=[save]
        for elem in save:
            elem=elem[:-1]
            save=elem.split("/")
        
        
        
        dic = {'Rota': save[0],
                'Nome': save[1],
                'dicas':save[2],
                'Itens_Padroes':save[3] ,
                'Itens_Alternativos':save[4],
                'Skill.Q':save[5],
                'Skill.E': save[6],
                'Skill.W': save[7],
                'Skill.R': save[8],
                'passive':save[9],
                'taticas_ING':save[10],
                'win_rate': save[11],
                'dificuldade':save[12],
                'weak_again':save[13],
                "win_rate_elo":save[14]
                }
        print(logo())
        print("CHAMPION >>>>",dic["Nome"],end="\n")
        print(linha())
        print("ROTA >>>>",dic["Rota"],end="\n")
        print(linha())
        print("dicas >>>>",dic["dicas"],end="\n")
        print(linha())
        print("CORE BUILD >>>>>>",dic["Itens_Padroes"],end="\n")
        print(logo())
        print("Side Build >>>>>>",dic["Itens_Alternativos"],end="\n")
        print(linha())
        print("Skill [Q] ____",dic["Skill.Q"],"____",end="\n")
        print(linha())
        print("Skill [w]____",dic["Skill.W"],"____",end="\n")
        print(linha())
        print("Skill [E]____",dic["Skill.E"],"____",end="\n")
        print(linha())
        print("Skill [R]____",dic["Skill.R"],"____",end="\n")
        print(logo())
        print("Skill [passiva]____",dic["passive"],"____",end="\n")
        print(linha())
        print("Tatics in game>>>>",dic["taticas_ING"],end="\n")
        print(linha())
        print("WIN RATE geral",dic["win_rate"],end="\n")
        print(linha())
        print("Dificuldade de jogar",dic["dificuldade"],end="\n")
        print(linha())
        print("Weak agains --",dic["weak_again"],end="\n")
        print(linha())
        print("Win rate no seu elo >>>",dic["win_rate_elo"],"<<<",end="\n")
        print(logo())
        espace=input("presione qualquer tecla para voltar ao menu :)")
        return ''
