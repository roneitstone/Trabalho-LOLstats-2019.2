import os
from Screens import tela_1
from Screens import tela_2
from Screens import tela_3
from Screens import tela_4
from Screens import editora
def linha():
    print("-="*40)
def main ():
    baselist=[]
    
    tela_1.inicial()
    
    response = tela_2.menu()

    if response == 'new':
        os.system("clear")
        save = tela_3.primeiros_dados(baselist)
        print('chegamos ate aqui')
        print(save)

    if response == '~':
        print("recuperando dados ...")
         
        response=tela_4.view()
        
        if response!= "=" and response != "-":
            os.system("clear")
            tela_3.primeiros_dados(response)
    if response != 'new' and response != '~' and response != '=':
        print(' nao é uma resposta valida, tente novamente XP')
        
    if response ==  '=':
        print ('Até logo!')
        return 
    os.system("clear")
    return main()

main()
