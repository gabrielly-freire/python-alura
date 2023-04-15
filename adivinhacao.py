import random
def jogar():
    print("#####################################")
    print("# Bem-vindo ao jogo de adivinhação! #")
    print("#####################################")

    numero_secreto = round(random.random()*100)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("(1) Fácil (2) Médio (3) Díficil")
    nivel = int(input("Escolha um nível de dificuldade: "))

    if(nivel ==1):
        total_tentativas = 20
    elif(nivel==2):
        total_tentativas =10
    else:
        total_tentativas = 5

    while(rodada <= total_tentativas):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite o seu número entre 1 e 100: "))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute<1 or chute>100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        if(acertou):
            print("Você acertou!")
            print("Sua pontuação foi de: {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("O número que você digitou é maior que o número secreto")
            elif(menor):
                print("O número que você digitou é menor que o número secreto")
        pontos_perdidos = abs(numero_secreto-chute)
        pontos = pontos - pontos_perdidos
        rodada= rodada+1

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()
