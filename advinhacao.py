from random import randint
comp = randint(0, 10)
print("Hoje sou seu desafiante e quero ver se acerta o número que acabei de pensar.")
print("Será que você é bom? Let's Go!")
acertou = False
while not acertou:
    player = int(input("Escolha seu número: "))
    if player == comp:
        acertou = True
    else:
        if player < comp:
            print("Um pouco mais... Tente novamente.")
        elif player > comp:
            print("Um pouco menos... Tente novamente.")
print("Parabéns! Você é muito bom! O número foi {}".format(comp))

