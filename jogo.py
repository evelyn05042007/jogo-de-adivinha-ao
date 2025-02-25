print("*******************")
print("Bem vindo ao jogo de Adivinhação!")
print("*******************")
numero_secreto = 65
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativas {} de {}".format(rodada, total_de_tentativas))

chute_str = input("Digite o seu número:")
print("Você digitou:", chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = Chute < numero_secreto

if (acertou)
    print ("Parabéns Você acertou!")
else:
    if (maior):
        print("O seu chute foi maior do que o numero secreto!")
    elif(menor):
    print ("O seu chute foi menor do que o numero secreto!")

rodada = rodada + 1
print("Fim de Jogo!")