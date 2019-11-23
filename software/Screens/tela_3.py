def primeiros_dados ():
   name = input('Nome do campeão: ')
   saida_b = ''
   itens = []
   itens_b = []
   i_tens = 'a'
   i_tens_b = 'b'
   saida = ''
    
   if name == '=':
       print('saindo...')
       return '='
   else:
    route = input('Rota: ')
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
                                Dict = {
                                    'Nome': name,
                                    'Rota': route,
                                    'Itens_Padroes': itens,
                                    'Itens_Alternativos': itens_b,
                                    'Skill.Q': skill_Q,
                                    'Skill.E': skill_E,
                                    'Skill.W': skill_W,
                                    'Skill.R': skill_R
                                    }
                                return Dict 
