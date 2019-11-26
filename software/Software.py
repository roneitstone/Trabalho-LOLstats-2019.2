import os
from Screens import tela_1
from Screens import tela_2
from Screens import tela_3
from Screens import tela_4
def linha():
    print("-="*40)
def main ():
    baselist=[]
    tela_1.inicial()
    verify=0
    while verify == 0:
        response = tela_2.menu()
        if response != 'jungler' and response != 'top' and response != 'adcarry' and response !='suport' and response !='mid' and response != '~' and response != '^' and response != '=':
            print(' nao é uma resposta valida, tente novamente XP')
            verify=0
        else:
            verify = 1
    
    if response == 'jungler':
        save = tela_3.primeiros_dados(baselist)
        print('chegamos ate aqui')
        print(save)
    if response == 'top':
        save = tela_3.primeiros_dados(baselist)
        print('chegamos ate aqui')
        print(save)
    if response == 'adcarry':
        save = tela_3.primeiros_dados(baselist)
        print('chegamos ate aqui')
        print(save)
    if response == 'suport':
        save = tela_3.primeiros_dados(baselist)
        print('chegamos ate aqui')
        print(save)
    if response == 'mid':
        save = tela_3.primeiros_dados(baselist)
        print('chegamos ate aqui')
        print(save)
    if response == '~':
        print("recuperando dados ...")
         
        response=tela_4.view()
        
        if response!= "=":
            tela_3.primeiros_dados(response)

    if response != 'jungler' and response != 'top' and response != 'adcarry' and response !='suport' and response !='mid' and response != '~' and response != '^' and response != '=':
        print(' nao é uma resposta valida, tente novamente XP')
        main()
    
    if response ==  '=':
        print ('Até logo!')
        return 
    os.system("clear")
    return main()

main()
