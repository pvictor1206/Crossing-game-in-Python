""""
Programa feito para treinar a linguagem de programação Python.
O programa é simples e se trata de um jogo.
Existem 3 sapos vermelhos e 3 sapos azuis antes da ponte, ajude a atravessar
a cor do sapo azul para o outro lado da ponte...
by: Paulo Victor Santos Magalhães
"""

from os import system

def linha(): # Função para representar linhas
    print('-'*40)
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'azul':'\033[34m'}

linha()
print('JOGO DA TRAVESSIA')
linha()

cont = 0

saposVermelhos = [1,1,1] # Sapos vermelhos antes da ponte
saposAzuis = [2,2,2] # Sapos azuis antes da ponte
saposVermelhos2 = [0,0,0] # Sapos vermelhos depois da ponte
saposAzuis2 = [0,0,0] #Sapos azuis depois da ponte

try:
    print('Existem 3 sapos vermelhos e 3 sapos azuis antes da ponte, ajude a atravessar a cor do sapo azul para o outro lado da ponte...')
    # Pergunta se o usuário quer continuar jogando
    palavra = str(input('Se estiver preparado para jogar. digite SIM, se não estiver. digite NAO: ')).strip().upper()
    while True:
        if palavra != 'NAO' and palavra != 'SIM':
            # Laço infinito até o usuario decidir se quer continuar jogando
            palavra = str(input('Se estiver preparado para jogar. digite SIM, se não estiver. digite NAO: ')).strip().upper()
        else:
            break
    if palavra == 'SIM':
        while True:
            # Condições da regra do jogo para sapos antes da ponte
            if saposAzuis[0] == 0 and saposAzuis[1] == 0 and saposAzuis[2] == 2 and saposVermelhos[0] == 1 and saposVermelhos[1] == 1 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0,3):
                    saposVermelhos[c] = 1
                for c in range(0,3):
                    saposAzuis[c] = 2
                for c in range(0,3):
                    saposVermelhos2[c] = 0
                for c in range(0,3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 0 and saposAzuis[1] == 2 and saposAzuis[2] == 0 and saposVermelhos[0] == 1 and saposVermelhos[1] == 1 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 2 and saposAzuis[1] == 0 and saposAzuis[2] == 0 and saposVermelhos[0] == 1 and saposVermelhos[1] == 1 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0

            if saposAzuis[0] == 0 and saposAzuis[1] == 2 and saposAzuis[2] == 2 and saposVermelhos[0] == 1 and saposVermelhos[1] == 1 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 2 and saposAzuis[1] == 0 and saposAzuis[2] == 2 and saposVermelhos[0] == 1 and saposVermelhos[1] == 1 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
                saposAzuis2[2] = 0
            if saposAzuis[0] == 2 and saposAzuis[1] == 2 and saposAzuis[2] == 0 and saposVermelhos[0] == 1 and saposVermelhos[1] == 1 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 0 and saposAzuis[1] == 0 and saposAzuis[2] == 2 and saposVermelhos[0] == 1 and saposVermelhos[1] == 1 and saposVermelhos[2] == 0:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 0 and saposAzuis[1] == 2 and saposAzuis[2] == 0 and saposVermelhos[0] == 1 and saposVermelhos[1] == 1 and saposVermelhos[2] == 0:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 2 and saposAzuis[1] == 0 and saposAzuis[2] == 0 and saposVermelhos[0] == 1 and saposVermelhos[1] == 1 and saposVermelhos[2] == 0:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 0 and saposAzuis[1] == 0 and saposAzuis[2] == 2 and saposVermelhos[0] == 1 and saposVermelhos[1] == 0 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 0 and saposAzuis[1] == 0 and saposAzuis[2] == 2 and saposVermelhos[0] == 1 and saposVermelhos[1] == 0 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 0 and saposAzuis[1] == 0 and saposAzuis[2] == 2 and saposVermelhos[0] == 1 and saposVermelhos[1] == 0 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 0 and saposAzuis[1] == 0 and saposAzuis[2] == 2 and saposVermelhos[0] == 0 and saposVermelhos[1] == 1 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 0 and saposAzuis[1] == 0 and saposAzuis[2] == 2 and saposVermelhos[0] == 0 and saposVermelhos[1] == 1 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0
            if saposAzuis[0] == 0 and saposAzuis[1] == 0 and saposAzuis[2] == 2 and saposVermelhos[0] == 0 and saposVermelhos[1] == 1 and saposVermelhos[2] == 1:
                print('EXISTEM MAIS SAPOS VERMELHOS DO QUE SAPOS AZUIS ANTES DA PONTE... JOGO REINICIADO...')
                for c in range(0, 3):
                    saposVermelhos[c] = 1
                for c in range(0, 3):
                    saposAzuis[c] = 2
                for c in range(0, 3):
                    saposVermelhos2[c] = 0
                for c in range(0, 3):
                    saposAzuis2[c] = 0


            linha()
            print('REGRA: Não poder ter mais sapos vermelhos do que sapos azuis antes da ponte\nTodos os sapos azuis devem está depois da ponte.')
            print('Jogo atual:')
            print('{}Sapos vermelhos antes da ponte: {}'.format(cores['vermelho'],cores['limpa']),end=' ')
            for c in range(0,3):
                print('{}{}{}'.format(cores['vermelho'],saposVermelhos[c],cores['limpa']),end=' ')
            print('\n{}Sapos azuis antes da ponte: {}'.format(cores['azul'],cores['limpa']),end=' ')
            for c in range(0, 3):
                print('{}{}{}'.format(cores['azul'],saposAzuis[c],cores['limpa']),end=' ')
            print('\n{}Sapos vermelhos depois da ponte: {}'.format(cores['vermelho'],cores['limpa']),end=' ')
            for c in range(0, 3):
                print('{}{}{}'.format(cores['vermelho'],saposVermelhos2[c],cores['limpa']),end=' ')
            print('\n{}Sapos azuis depois da ponte: {}'.format(cores['azul'],cores['limpa']),end=' ')
            for c in range(0, 3):
                print('{}{}{}'.format(cores['azul'],saposAzuis2[c],cores['limpa']),end=' ')
            print(' ')
            linha()
            if saposAzuis2[0] == 2 and saposAzuis2[1] == 2 and saposAzuis2[2] == 2:
                break
            # Decisão se o usuário quer atravessar ou trazer o sapo
            sapos = int(input("\nDigite [1] para atravessar os sapos e [2] para trazer os sapos de volta: "))
            while True:
                # laço infinito até usuário decidir se quer atravessar ou trazer o sapo
                if sapos != 1 and sapos != 2:
                    sapos = int(input("Digite [1] para atravessar os sapos e [2] para trazer os sapos de volta: "))
                else:
                    break
            if sapos == 1:
                # Pergunta ao usuário a cor do sapo para travessia
                travessia = int(input('Para atravessar um sapo da cor vermelho digite [1] e para atravessar um sapo da cor azul digite [2]:   '))
                while True:
                    # Laço infinito até o usuário decidir a cor do sapo para travessia
                    if travessia != 1 and travessia != 2:
                        travassia = int(input('Para atravessar um sapo da cor vermelho digite [1] e para atravessar um sapo da cor azul digite [2]:   '))
                    else:
                        break
                # Comandos para travessia do sapo vermelho
                if travessia == 1:
                    while True:
                        if saposVermelhos[0] == 0 and saposVermelhos[1] == 0 and saposVermelhos[2] == 0:
                            system('cls')
                            print('Não existem sapos vermelhos para atravessar...')
                            break
                        if saposVermelhos2[cont] == 0:
                            saposVermelhos2[cont] = 1
                            saposVermelhos[cont] = 0
                            cont = 0
                            system('cls')
                            break
                        else:
                            cont += 1
                # Comandos para travessia do sapo azul
                if travessia == 2:
                    while True:
                        if saposAzuis[0] == 0 and saposAzuis[1] == 0 and saposAzuis[2] == 0:
                            system('cls')
                            print('Não existem sapos azuis para atravessar...')
                            break
                        if saposAzuis2[cont] == 0:
                            saposAzuis2[cont] = 2
                            saposAzuis[cont] = 0
                            system('cls')
                            cont = 0
                            break
                        else:
                            cont += 1
            if sapos == 2:
                    # Pergunta ao usuário a cor do sapo para retorno
                retorno  = int(input('Para trazer um sapo da cor vermelho digite [1] e para trazer um sapo da cor azul digite [2]:   '))
                while True:
                        # Laço infinito até o usuário decidir a cor do sapo para retorno
                    if retorno != 1 and retorno != 2:
                        retorno = int(input('Para trazer um sapo da cor vermelho digite [1] e para trazer um sapo da cor azul digite [2]:   '))
                    else:
                        break
                if retorno == 1:
                # comandos para o retorno do sapo vermelho
                        while True:
                            if saposVermelhos2[0] == 0 and saposVermelhos2[1] == 0 and saposVermelhos2[2] == 0:
                                system('cls')
                                print('Não existem sapos vermelhos para o retorno...')
                                break
                            if saposVermelhos2[cont] == 1:
                                saposVermelhos2[cont] = 0
                                saposVermelhos[cont] = 1
                                system('cls')
                                cont =  0
                                break
                            else:
                                cont += 1
                if retorno == 2:
                # Comandos para o retorno do sapo azul
                        while True:
                            if saposAzuis2[0] == 0 and saposAzuis2[1] == 0 and saposAzuis2[2] == 0:
                                system('cls')
                                print('Não existem sapos azuis para o retorno...')
                                break
                            if saposAzuis2[cont] == 2:
                                saposAzuis2[cont] = 0
                                saposAzuis[cont] = 2
                                system('cls')
                                cont = 0
                                break
                            else:
                                cont += 1
except Exception as erro:
    print(f'HOUVE UM ERRO: {erro.__class__}') # Mensagem que informa se tiver ocorrido algum erro

else:
    if palavra == 'NAO': # Se o usuário digitar NAO, o programa ira ser finalizado
        linha()
        print('ATE LOGO')
    else: # Se o usuário digitar SIM, e finalizar o desafio, ira apresentar está mensagem
        linha()
        print('JOGO FINALIZADO, OBRIGADO POR JOGAR')

print('...')

