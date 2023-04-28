# Parte de importações, definições de valores e variaveis

import random, time, emoji

AttemptsCounter = 0

while True:
    MachineChoice = random.randrange(0, 6)
    print('\n\033[1;33mBem-vindo! \033[0;0meste arquivo python é um joguinho de adivinhação feito por \033[1;36mG.Felix!\033[0;0m\n')
    time.sleep(3.5)

    # Parte 2: Definição do input e ajustes para possiveis erros

    while True:
        print('\033[H\033[J')
        UserGuess = input('~-' * 58 + '\n\n\033[1;31mVamos dar inicio ao jogo!\033[0;0m\n\nEscolha \033[1;31muma\033[0;0m das opções abaixo para o seu palpite e tente adivinhar em que número eu estou pensando...\n\n\033[1;36m[0]\033[0;0m \033[1;35m[1]\033[0;0m \033[1;34m[2]\033[0;0m \033[1;33m[3]\033[0;0m \033[1;32m[4]\033[0;0m \033[1;30m[5]\033[0;0m\n\n' + '~-' * 58 + '\n\n\033[1;32m---> \033[0;0m').strip()

        if UserGuess.isnumeric() and int(UserGuess) in range(6):

            break

        else:
            time.sleep(2)
            print('\n\033[1;33mAlgo deu errado. Analisando...\033[0;0m')
            time.sleep(1.6)
            print('\n\033[1;31mEntrada inválida\033[0;0m! Digite apenas os números entre \033[1;31m0\033[0;0m e \033[1;31m5.\033[0;0m')
            time.sleep(2.5)

            # Limpa o console após a mensagem de erro

            print('\033[H\033[J')

    # Parte para resultados
    print(emoji.emojize('\n\033[1;33mVamos ver se seu palpite está correto...\033[0;0m :thinking_face:\n'))

    time.sleep(2)

    if int(UserGuess) != MachineChoice:
        AttemptsCounter += 1

    if int(UserGuess) == MachineChoice:
        print(emoji.emojize('\033[1;32mUaau... De primeira\033[0m!!! :face_with_peeking_eye:'))
        print(emoji.emojize('\nVocê \033[1;32macertou\033[0;0m!! Dessa vez você me pegou... :person_shrugging:'))
        time.sleep(5.2)
        print('\033[H\033[J')

    # Aqui abaixo mostrará que o usuário errou e pedirá novamente o input do mesmo, assim fazendo a contagem pela variável 'cont', enquanto o usuario não atender o requisito do while o programa continuará pedindo um novo palpite e contando quantas vezes ele erra

    else:
        time.sleep(0.9)
        print(emoji.emojize('\033[1;31mParece que você errou, tente novamente! :confused_face:'))
        while MachineChoice != UserGuess:
            UserGuess = input('\n\033[1;35mQual é o seu novo palpite?\033[1;35m\n---> \033[1;32m')


            # Se o input atender aos requisitos do loop while, as próximas verificações irão ocorrer abaixo.
            if UserGuess.isnumeric() and int(UserGuess) in range(6):
                pass

            # Caso não atenda os requisitos do if acima o input caira nesse else e será exibida a seguinte mensagem de erro e pedirá novamente para que o usuário digite um número válido.
            else:
                time.sleep(1.2)
                print('\n\033[1;31mEntrada inválida\033[0;0m! Digite apenas os números entre \033[1;31m0\033[0;0m e \033[1;31m5.\033[0;0m')
                time.sleep(1.1)
                continue

            # Verificando se o palpite do jogador é maior ou menor ou igual ao número escolhido pelo computador.
            if MachineChoice > int(UserGuess):
                time.sleep(0.7)
                print(emoji.emojize('\n\033[1;33mMais... :smirking_face: Tente o seu palpite novamente\033[0m'))
                AttemptsCounter += 1

            if MachineChoice < int(UserGuess):
                time.sleep(0.7)
                print(emoji.emojize('\n\033[1;34mMenos... :sad_but_relieved_face: Tente o seu palpite novamente\033[0m'))
                AttemptsCounter += 1
                
                # Aqui será exibida a mensagem de acerto e fora deste loop nos será mostrado a quantidade de tentativas que foram usadas até chegar no resultado final.
            if int(UserGuess) == MachineChoice:
                print(emoji.emojize('\nVocê \033[1;32macertou\033[0;0m!! É, rsrs... Dessa vez você me pegou :face_holding_back_tears:'))
                AttemptsCounter += 1
                break

        # Exibição das tentativas juntamente com o clear do console
        time.sleep(2)
        print(f'\n\033[1;34mVocê levou \033[43;1;30m{AttemptsCounter}\033[0;0m \033[1;34mtentativas para acertar o número escolhido.\033[0m')
        time.sleep(4)
    print('\033[H\033[J')

    # Nessa parte eu desejo saber se o usuário deseja jogar novamente para que fique um jogo interessante a se jogar.
    jogar_novamente = input('\nJogar \033[1;32mnovamente\033[0;0m? (S/N): ').lower().strip()[0]

    # Validação da resposta do input 'jogar_novamente'
    while jogar_novamente not in ['s', 'n']:
        jogar_novamente = input('\n\033[1;31mOpção inválida\033[0;0m. Quer jogar novamente? (S/N): ').lower().strip()[0]
        continue

    # Verifica a resposta do usuário do primeiro ou segundo input caso ele tenha digitado errado e reproduz os seguintes comandos, sendo eles continue ou break.
    if jogar_novamente == 's':
        AttemptsCounter = 0
        print('\033[H\033[J')
        continue

    if jogar_novamente == 'n':
        break
