# ********************************************************************************************************************************************** #
# Program: SRIHARI-MOHD_EMADELDIN-KISHENDHRA-JIA_XIAN.py                                                                                         #
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN                                                                                             #
# Class: TT04                                                                                                                                    #
# Year: 2020/21 Trimester 1                                                                                                                      #
# Names:   SRIHARI NAIDU A/L VENKATASH   | MOHAMMED EMADELDIN AHMED TAHA ELMOGY | KISHENDHRA A/L KANNATHASAN    | WONG JIA XIAN                  #
# IDs:     1201100182                    | 1191102751                           | 1201100207                    | 1201100886                     #
# Emails:  1201100182@student.mmu.edu.my | 1191102751@student.mmu.edu.my        | 1201100207@student.mmu.edu.my | 1201100886@student.mmu.edu.my  #
# Phones:  +6010-667 7569                | +966 50 160 1369                     | +6016-243 6197                | +6017-375 0529                 #
# ********************************************************************************************************************************************** #

#modules/libs
import random
import string
import psphelper

#gameSetup
psphelper.clearScreen() #clear-the-screen
quotes = psphelper.readQuotesFromFile("quotes.txt") #read-quote-from-file
gameQuote = random.choice(quotes) #randomly-select-quote

#modify the game quote ---> #alpha-to-underscore
alphaQuote_list = list(gameQuote) #for reference
screenQuote_list = [] #to show on main-interface

for ele in alphaQuote_list:
    screenQuote_list.append(psphelper.alphaToUnderscore(ele))
    screenQuote = ''.join(screenQuote_list)

#gameFunctions
def repQuote(): #check-and-replace/update-letter ---> #underscoreToAlpha
    for i in range(len(alphaQuote_list)):
        if alphaQuote_list[i] == guess.upper():
            screenQuote_list[i] = guess.upper()
    global screenQuote
    screenQuote = ''.join(screenQuote_list)

#player-dictionary 
money = {"Player 1": 0, "Player 2": 0, "Player 3": 0} #player-money
cheat = {"Player 1": 1, "Player 2": 1, "Player 3": 1} #player-cheats

winner = [] #game-winner

#player-reference
players = [1,2,3] #3-players
playerIndex = 0 #player-reference

#game-mechanics-reference
vowels = ['a','e','i','o','u']
dice = ["RM500", "RM600", "RM700", "RM800", "RM900", "RM1000", "Bankrupt","Lose A Turn"]
guess_keyword = ['cheat', '/']

#main-game-loop
endgame = False
while not endgame:

    #main-interface
    psphelper.clearScreen()
    title = "..:: C.O.V.I.D ::.."
    width = 46
    borderWidth = 4
    print(title.center(width + borderWidth))
    psphelper.showQuoteScreen(screenQuote, width)
    print()
    
    #money-screen
    for p in money:
        print(f'{p}: RM {money[p]}')
    
    #input-options
    print()
    print("Input Options:")
    print("   /           :- Solve the puzzle")
    print("   a vowel     :- Buy a vowel")
    print("   a consonant :- Guess a consonant")
    print()

    #current-player-reference
    current_player = players[playerIndex]    # if playerIndex = 0, players = 1, the player-turn system is explained in-depth below
    player = ["Player", str(current_player)]
    player = " ".join(player)
    
    #current-player-screen
    print(player)
    print('========')

    # Checks to see whether the quote has been solved (for each round)
    if screenQuote == gameQuote:
        engame = True

    # If so, it will declare the winner in a new screen (different format)
        #main-interface
        psphelper.clearScreen()
        width = 46
        borderWidth = 4
        psphelper.showQuoteScreen(screenQuote, width)
        print()

        #money-screen
        for p in money:
            print(f'{p}: RM {money[p]}')
        print()
        
        # Gets the player with the highest amount of money
        for player in money:
            if money[player] == max(money.values()):
                winner.append(player)

        if len(winner) == 1: # if only one player with the highest amount of money, the player is the only winner
            print(f'{winner[0]} Wins.')
        else:
            print("It's a tie.") # if there are multiple players with the same-highest amount of money, they all win so it's a tie
        print()

        print(f'Game Ends.')
        break

    #game-mechanics-loop
    while True:

        #input-prompt   
        guess = input("Input > ")
 
        # Checks for invalid inputs - initial filter layer to avoid invalid inputs that hinders other game mechanics
        if guess.isspace() or guess.isdigit() or guess == "" or not guess.lower().split()[0].isalpha() and guess != '/' or guess.lower().split()[0] != 'cheat' and len(guess) > 1:
            print("Invalid Input.")
            continue #continue with this game-mechanics-loop to continually ask for input without clearing/resetting the screen
        # Checks for letters that has been chosen/guessed/taken
        elif guess.upper() in screenQuote_list:
            print(f'Letter {guess.upper()} has been taken.')

            input("Press ENTER to continue play.")
            break


        #vowelMechanics
        elif guess.lower() in vowels: # did the player guess a vowel?

            letter_count = alphaQuote_list.count(guess.upper()) # Counts for how many guessed letter(s)/vowel(s) there are in the game quote
            vowel_cost = letter_count * 200 # Calculates the cost to buy the vowel
                
            if money[player] >= vowel_cost and money[player] > 0: # Checks to see if the player has enought money to buy the guessed vowel(s)
                
                #main_vowel_mechanics
                if guess.upper() in alphaQuote_list: #if the vowel guessed is in the quote, the player can continue
                    print(f'You found {letter_count} letter {guess.upper()}.')
                    print(f'You spent RM {vowel_cost}')
                    money[player] -= vowel_cost
                    repQuote() #underscoreToAlpha - replace _(blanks) with found letter

                    input("Press ENTER to continue play.")
                    break

                else:
                    print(f'Sorry. There is no letter {guess.upper()}.')
                    playerIndex = (playerIndex + 1) % len(players)  
                
                    ############## the mechanics of how the next consecutive player is referred from that equation ###############
                    #|            (0+1) % 3 = 1 |            (1+1) % 3 = 2 |            (2+1) % 3 = 0 |            (0+1) % 3 = 1 |
                    #| playerIndex ^   player ^ | playerIndex ^   player ^ | playerIndex ^   player ^ | playerIndex ^   player ^ |   
                    #         playerIndex = 0 --> 1 --> 2 --> 0 --> 1 --> 2...\ it goes infinitely,
                    # player[playerIndex] = 1 --> 2 --> 3 --> 1 --> 2 --> 3.../ in a cycle 
                    
                    input("Your turn ends. Press ENTER to end turn.") #the player's turn ends                    
                    break

            else: #player money < vowel cost
                print("Insufficient money.")

                input("Press ENTER to continue play.")
                break
                

        #consonantMechanics
        elif guess.lower().split()[0] not in guess_keyword and vowels: # did the player guess a consonant?

            #roll-the-dice
            diceRoll = random.choices(dice, weights=(2,2,2,2,2,2,1,1)) # this returns a list
            diceRoll = diceRoll[0] # hence this picks the roll value from the list

            if guess.upper() in alphaQuote_list: #if the consonant guessed is in the quote, the program continues
                print(f'You rolled "{diceRoll}".')

                if diceRoll == "Bankrupt":
                    print("Sorry, you lose all your money.")
                    money[player] = 0 
                    playerIndex = (playerIndex + 1) % len(players)

                    input("Your turn ends. Press ENTER to end turn.")
                    break

                elif diceRoll == "Lose A Turn":
                    playerIndex = (playerIndex + 1) % len(players)

                    input("Your turn ends. Press ENTER to end turn.")
                    break

                else: # if the dice rolls for money
                    letter_count = alphaQuote_list.count(guess.upper()) # Counts for how many guessed letter(s)/vowel(s) there are in the game quote
                    roll_value = int(diceRoll.split("RM")[1]) # Finds the prize money value
                    consonant_prize = roll_value * letter_count # Calculates how much the player earns

                    print(f'Found {letter_count} letter {guess.upper()}.')
                    print(f'You earned RM {letter_count * roll_value}.')
                    money[player] += consonant_prize # adds the prize money to the current player's dictionary
                    repQuote()

                    input("Press ENTER to continue play.")
                    break

            else: # if there are no guessed consonant
                print(f'Sorry. There is no letter {guess.upper()}.')
                playerIndex = (playerIndex + 1) % len(players)

                input("Your turn ends. Press ENTER to end turn.")
                break
                

        #solveMechanics
        elif guess == '/': # the player wants to solve

            guess = input('Solve It > ').upper()

            if guess == gameQuote:
                screenQuote = gameQuote 
                money[player] *= 2

                input("Congratulations! You have solved it. Your money is doubled.")
                break

            else:
                playerIndex = (playerIndex + 1) % len(players)

                input("WRONG SOLUTION!\nYour turn ends. Press ENTER to end turn.")
                break

        
        #cheatMechanics
        elif guess.lower().split()[0] == "cheat": # if the first word of input is cheat, run the cheatcode mechanics

            guess_split = guess.lower().split(' ') #split the cheatcode to get the money value 

            if len(guess_split) == 1: # the input is only 'cheat' code ----> letter cheat

                if guess_split[0] != "cheat": #or not guess_split[1].isdigit() and int(guess_split[1]) < 0:
                    print("Invalid Input.")
                    continue

                else:
                    if cheat[player] > 0: # checks to see if the player has cheats left

                        #letter-cheat-system
                        consonant_cheat = '' # stores the consonants found for the cheat c0de
                        max_count, max_conso = 0, None

                        # Finds for consonant in the game quote that has not been guessed and counts it
                        for letter in alphaQuote_list:
                            if letter.lower() not in vowels and letter not in screenQuote_list: # letter must be a consonant, and has not been guessed
                                if letter not in consonant_cheat: # letter must not have been found using cheat c0de
                                    consonant_cheat += letter # adds the consonant found to the "storage area"(consonant_cheat)
                                    freq = alphaQuote_list.count(letter)
                                    if freq > max_count: # highest frequeny consonant found in cheat c0de
                                        max_count, max_conso = freq, letter

                        if len(consonant_cheat) > 0: # means, if there are any values(consonants) in the cheated/found consonants
                            print(f'There are {max_count} letter {max_conso}.')
                            cheat[player] = 0 #player now has no more cheats

                            input("Press ENTER to continue play.")
                            break

                        else:
                            print(f'Sorry, no more consonants available.')

                            input("Press ENTER to continue play.")
                            break

                    else: # if cheat <= 0 / no cheats
                        print('No more cheat available.')

                        input("Press ENTER to continue play.")
                        break


            elif len(guess_split) == 2: #there's a value behind 'cheat' code -----> money cheat

                if not guess_split[1].isdigit() or guess_split[1].isdigit() and int(guess_split[1]) <= 0: #if it's not digit 'or' if it's digit but('and') lesser than zero
                    print("Invalid Input.")
                    continue
                
                else:
                    if cheat[player] > 0: # checks to see if the player has cheats left

                        cheatAmount = int(guess_split[1])

                        print(f'Money changed to RM {cheatAmount}.')
                        money[player] = cheatAmount
                        cheat[player] = 0 #player now has no more cheats

                        input("Your turn ends. Press ENTER to end turn.")
                        break

                    else: # if cheat <= 0
                        print('No more cheat available.')

                        input("Press ENTER to continue play.")
                        break
                    
            else: # if length of guess in more not 1 nor 2 making it something else, so it's invalid
                print("Invalid Input.")
                continue
        
        else: # final layer of filter for all the other invalid inputs
            print("Invalid Input.")
            continue