import random

cardlist = [11,2,3,4,5,6,7,8,9,10,10,10,10]
playercards = [random.choice(cardlist), random.choice(cardlist) ]
print(f"Your Cards are {playercards}")
computercards = [random.choice(cardlist)]
print(f"Computer's First Card is {computercards}")
compscore = sum(computercards)

def compscoreadj():
    #computercards.append(random.choice(cardlist))
    computerscore = sum(computercards)
    while computerscore < 17:
        computercards.append(random.choice(cardlist))
        computerscore = sum(computercards) 
    #print(f"Computer's Cards are {computercards}, score is {computerscore}")
    return computerscore


def elevenconverter(cards): # MAKE SURE TO GENERALIZE IT FOR BOTH, PLAYER AND COMPUTER      elevenconverter(variable = playercards/computercards), then replace playercards by that variable
    for x in range(len(cards)):
        if cards[x] == 11:
            cards[x] = 1
            return True


situation = True
while situation == True:
    conti = input("Type 'y' to get another card, type 'n' to pass ")
    if conti == "y":
        playercards.append(random.choice(cardlist))
        playerscore = sum(playercards)
        print(f"Your Cards are {playercards}, current score is {playerscore}")
        if playerscore > 21 and elevenconverter(playercards) == True:
            print("You have an Ace")
        elif playerscore > 21:
            print("Bust")
            computerscore = compscoreadj()
            if compscore > 21 and elevenconverter(computercards) == True :
                compscore = compscoreadj()
            print(f"Computer's Cards are {computercards}, score is {compscore}")
            situation = False

        elif playerscore < 21:
            compscore = sum(computercards)
            if compscore < 17:
                compscore = compscoreadj()

            if compscore <= 21:

                if playerscore > compscore :
                    print(f"Computer's Cards are {computercards}, score is {compscore}")
                    print("You Win")
                    situation = False
                elif playerscore == compscore :
                    print(f"Computer's Cards are {computercards}, score is {compscore}")
                    print("Draw")
                    situation = False
                elif playerscore < compscore :
                    #print("Dealer Wins")
                    # have to complete but for the time being
                    situation = True
            elif compscore > 21 and elevenconverter(computercards) == True:
                if playerscore > compscore :
                    print(f"Computer's Cards are {computercards}, score is {compscore}")
                    print("You Win")
                    situation = False
                elif playerscore == compscore :
                    print(f"Computer's Cards are {computercards}, score is {compscore}")
                    print("Draw")
                    situation = False
                elif playerscore < compscore :
                    #print("Dealer Wins")
                    # have to complete but for the time being
                    situation = True
            else:
                print(f"Computer's Cards are {computercards}, score is {compscore}")
                print("You Win")
                situation = False

        else:


            compscore = compscoreadj()

            if playerscore == compscore :
                print(f"Computer's Cards are {computercards}, score is {compscore}")
                print("Draw")
            else:
                print("!!BlackJack!!")

            situation = False

    else:
        playerscore = sum(playercards)
        if playerscore >= 21 and elevenconverter(playercards) == True:
            print("You have an Ace")
            situation = True
        else:
            playerscore = sum(playercards)
            print(f"Your Cards are {playercards}, current score is {playerscore}")
            if compscoreadj() < 17:
                computercards.append(random.choice(cardlist))

            compscore = compscoreadj()

            if playerscore > compscore and playerscore < 21:
                print(f"Computer's Cards are {computercards}, score is {compscore}")
                print("You Win")
            elif playerscore == compscore and playerscore < 21:
                print(f"Computer's Cards are {computercards}, score is {compscore}")
                print("Draw")
            elif playerscore < compscore and compscore > 21:
                print(f"Computer's Cards are {computercards}, score is {compscore}")
                print("You Win")
            else:
                print(f"Computer's Cards are {computercards}, score is {compscore}")
                print("Dealer Wins")
            situation = False
























