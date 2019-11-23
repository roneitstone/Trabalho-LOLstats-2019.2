import Screens
from Screens import tela_1
from Screens import tela_2
from Screens import tela_3
from Screens import tela_4
def main ():
    tela_1.inicial()
    response = tela_2.menu()
    if response == 'jungler':
        save = tela_3.primeiros_dados()
        print('chegamos ate aqui')
        print(save)
    if response == 'top':
        save = tela_3.primeiros_dados()
        print('chegamos ate aqui')
        print(save)
    if response == 'adcarry':
        save = tela_3.primeiros_dados()
        print('chegamos ate aqui')
        print(save)
    if response == 'suport':
        save = tela_3.primeiros_dados()
        print('chegamos ate aqui')
        print(save)
    if response == 'midlaner':
        save = tela_3.primeiros_dados()
        print('chegamos ate aqui')
        print(save)
    if response != 'jungler' and response != 'top' and response != 'adcarry' and response !='suport' and response !='midlaner' and response != '~' and response != '^' and response != '=':
        print(' nao é uma resposta valida, tente novamente XP')
        main()
    if response ==  '=':
        print ('Até logo!')
main()