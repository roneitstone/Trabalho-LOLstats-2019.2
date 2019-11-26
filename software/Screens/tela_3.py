import os
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
                                                                        'Itens_Padroes': itens,
                                                                        'Itens_Alternativos': itens-b,
                                                                        'Skill.Q': skill_q,
                                                                        'Skill.E': skill_e,
                                                                        'Skill.W': skill_w,
                                                                        'Skill.R': skill_r,
                                                                        'passive': passive,
                                                                        'taticas_ING':tatic,
                                                                        'win_rate': wr,
                                                                        'dificuldade':dificult,
                                                                        'weak_again':wa,
                                                                        "win_rate_elo":wrelo
                                                                        }

                                                                save+=dic.values()
                                                                return  save
    else:
        
        lista=[]
        lista.append(save[0])
        
        print(lista)
        lista.split("/")
        dic = {'Rota': lista[0],
                'Nome': lista[1],
                'dicas':lista[2],
                'Itens_Padroes':lista[3] ,
                'Itens_Alternativos':lista[4],
                'Skill.Q':lista[5],
                'Skill.E': lista[6],
                'Skill.W': lista[7],
                'Skill.R': lista[8],
                'passive':lista[9],
                'taticas_ING':lista[10],
                'win_rate': lista[11],
                'dificuldade':lista[12],
                'weak_again':lista[13],
                "win_rate_elo":lista[14]
                }
        print(logo())
        print("CHAMPION >>>>",dic["Nome"],end="\n")
        print(linha())
        print("ROTA >>>>",dic["Rota"],end="\n")
        print(linha())
        print("dicas >>>>",dic["dicas"],end="\n")
        print(linha())
        print("CORE BUILD >>>>>>",dic["Itens_Padrões"],end="\n")
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
        print("Tatics in game>>>>",dic["taticas ING"],END="\n")
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
