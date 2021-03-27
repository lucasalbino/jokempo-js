from random import randint
from time import sleep

jogar = "S"

itens = ()
itens = ('','PEDRA','PAPEL','TESOURA')
pontos_usuario = 0
pontos_computador = 0

while jogar == "S":
    jogada_computador = randint(1,3)
    print('')
    print('''---------JOKEMPO---------
Escolha sua jogada:

  [ 1 ] PEDRA 
  [ 2 ] PAPEL
  [ 3 ] TESOURA''')
    
    jogada = int(input('''
Qual a sual jogada? '''))
    try:
        print('''
        JO''')
        sleep(1)
        print('''
        KEM''')
        sleep(1)
        print('''
        PO!''')
        sleep(1)
        print('')
        print('Você jogou: {}' .format(itens[jogada]))
        print('Computador jogou: {}' .format(itens[jogada_computador]))
        print('-'*30)
    
    except:
        if jogada != 1 or jogada != 2 or jogada != 3:
            print('Digite uma opção valida! (1/2/3')
            print('Tente Novamente!')
            continue
    
    try:
        if jogada == 1:
            if jogada_computador == 1:
                print('Empate!')
                print('')
                print('------------PLACAR------------')
                print('')
                print('Jogador: {}' .format(pontos_usuario))
                print('Computador: {}' .format(pontos_computador))
            elif jogada_computador == 2:
                print('Papel ganha de Pedra!')
                print('-'*30)
                print('Vitória do Computador!')
                print('')
                pontos_computador = pontos_computador + 1
                print('------------PLACAR------------')
                print('')
                print('Jogador: {}' .format(pontos_usuario))
                print('Computador: {}' .format(pontos_computador))
            elif jogada_computador == 3:
                print('Pedra ganha de Tesousa!')
                print('-'*30)
                print('Vitória do Jogador!')
                print('')
                pontos_usuario = pontos_usuario + 1
                print('------------PLACAR------------')
                print('')
                print('Jogador: {}' .format(pontos_usuario))
                print('Computador: {}' .format(pontos_computador))
            else:
                print('Jogada Invalida!')
        
        elif jogada == 2:
            if jogada_computador == 1:
                print('Papel ganha de Pedra!')
                print('-'*30)
                print('Vitória do Jogador!')
                print('')
                pontos_usuario = pontos_usuario + 1
                print('------------PLACAR------------')
                print('')
                print('Jogador: {}' .format(pontos_usuario))
                print('Computador: {}' .format(pontos_computador))
            elif jogada_computador == 2:
                print('Empate!')
                print('')
                print('------------PLACAR------------')
                print('')
                print('Jogador: {}' .format(pontos_usuario))
                print('Computador: {}' .format(pontos_computador))
            elif jogada_computador == 3:
                print('Tesoura ganha de Papel')
                print('-'*30)
                print('Vitoria do Computador')
                print('')
                pontos_computador = pontos_computador + 1
                print('------------PLACAR------------')
                print('')
                print('Jogador: {}' .format(pontos_usuario))
                print('Computador: {}' .format(pontos_computador))
            else:
                print('Jogada Invalida!')
                
        elif jogada == 3:
            if jogada_computador == 1:
                print('Pedra Ganha de Tesoura!')
                print('-'*30)
                print('Vitoria do Computador!')
                print('')
                pontos_computador = pontos_computador + 1
                print('------------PLACAR------------')
                print('')
                print('Jogador: {}' .format(pontos_usuario))
                print('Computador: {}' .format(pontos_computador))
            elif jogada_computador == 2:
                print('Tesoura ganha de Papel!')
                print('-'*30)
                print('Vitoria do Jogador!')
                print('')
                pontos_usuario = pontos_usuario + 1
                print('------------PLACAR------------')
                print('')
                print('Jogador: {}' .format(pontos_usuario))
                print('Computador: {}' .format(pontos_computador))
            elif jogada_computador == 3:
                print('Empate!')
                print('')
                print('------------PLACAR------------')
                print('Jogador: {}' .format(pontos_usuario))
                print('Computador: {}' .format(pontos_computador))
            else:
                print('Jogada Invalida!')
    except:
        pass

    jogar = str(input('Deseja Jogar Novamente? [S/N]')).upper().strip()[0]
    print('')

    while jogar not in "SN":
        jogar = str(input('Digite um dado válido. Deseja continuar a jogar? [S/N] ')).upper().strip()[0]
        print('')

else:
    if pontos_usuario > pontos_computador:
        print('-'*30)
        print('---------FIM DE JOGO----------')
        print('Você venceu o Computador de {} a {}'.format(pontos_usuario, pontos_computador))
    elif pontos_usuario < pontos_computador:
        print('-'*30)
        print('---------FIM DE JOGO---------')
        print('Você perdeu para o Computador de {} a {}'.format(pontos_computador, pontos_usuario))
    elif pontos_usuario == pontos_computador:
        print('-'*30)
        print('---------FIM DE JOGO----------')
        print('O jogo empatou!')

