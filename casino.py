# casino
import random
import time
money = 100
playing = 0
while playing == 0:
    playing = 1
    print('Welcome to the Casino!')
    print('1 = BLACKJACK')
    print('2 = SLOTS')
    print('3 = ROULETTE')
    print('4 = POKER')
    print('5 = LEAVE')
    which_game = int(input('Where would you like to go? '))

    # BLACKJACK GAME CODE
    def bj_lose():
        global playing
        print('YOU LOSE')
        if money > 0:
            print('Returning to lobby...')
            time.sleep(2)
            playing = 0
        else:
            print(f'YOU HAVE {money} left')
    def bj_win():
        global playing, money
        print('YOU WIN')
        money = money + bj_bet * 2
        print(f'YOU NOW HAVE {money}')
        print('Returning to lobby....')
        time.sleep(2)
        playing = 0
    def bj_end_game():
        global playing, money
        if bj_card_total == 21:
            print('YOU WIN')
            time.sleep(1.5)
            money = money + bj_bet * 2
            print(f'YOU NOW HAVE {money}')
            print('PLAY AGAIN?')
        elif bj_card_total > 21:
            bj_check_aces()
            bj_check_aces()
            if bj_card_3 > 0:
                bj_check_aces()
                if bj_card_4 > 0:
                    bj_check_aces()
                    if bj_card_5 > 0:
                        bj_check_aces()
                    else:
                        bj_acecheck_done()
                else:
                    bj_acecheck_done()
            else:
                bj_acecheck_done()
        elif bj_card_total < 21:
            print('CHECKING WIN CHANCES.....')
            time.sleep(1.5)
            if bj_card_total == 20:
                if bj_winlose > 9:
                    bj_win()
                else:
                    bj_lose()
            elif 20 > bj_card_total >= 10:
                if bj_winlose > 16:
                    bj_win()
                else:
                    bj_lose()

            elif bj_card_total < 10:
                if bj_winlose > 18:
                    bj_win()
                else:
                    bj_lose()
    def bj_acecheck_done():
        global playing
        if bj_card_total > 21:
            print('YOU BUST')
            time.sleep(2)
            if money > 0:
                playing = 0
                print('Returning to lobby....')
                time.sleep(2)
            else:
                print('YOU RAN OUT OF MONEY')
                print('PLAY AGAIN?')
    def bj_check_ace_1():
        global bj_card_1, bj_card_2, bj_card_3, bj_card_4, bj_card_5
        if bj_card_1 == 11:
            bj_card_1 = 1
        elif bj_card_2 == 11:
            bj_card_2 = 1
        elif bj_card_3 == 11:
            bj_card_3 = 1
        elif bj_card_4 == 11:
            bj_card_4 = 1
        elif bj_card_5 == 11:
            bj_card_5 = 1
    def bj_check_aces():
        bj_check_ace_1()
        bj_check_ace_1()
        bj_check_ace_1()
        bj_check_ace_1()
        bj_check_ace_1()
        bj_acecheck_done()
    if which_game == 1:
        bj_winlose = random.randint(1, 20)
        bj_card_1 = random.randint(2, 11)
        bj_card_2 = random.randint(2, 11)
        bj_card_3 = 0
        bj_card_4 = 0
        bj_card_5 = 0
        bj_card_total = bj_card_1 + bj_card_2 + bj_card_3 + bj_card_4 + bj_card_5
        print(f'You have {money} dollars.')
        bj_bet = 0
        while bj_bet == 0:
            bj_bet = int(input('How much would you like to bet? '))
            if bj_bet >= money:
                print('GOING ALL IN')
                time.sleep(.5)
                time.sleep(.5)
                bj_bet = 100
                money = 0
            elif bj_bet < 1:
                print('You cannot bet less than one dollar.')
                bj_bet = input('How much would you like to bet? ')
        money = money - bj_bet
        print('11 = ACE (1 or 11)')
        print('Try to get 21 total, but not over 21.')
        time.sleep(3.3)
        print('Dealing Cards...')
        time.sleep(2)
        print(f'YOUR CARDS: {bj_card_1}, {bj_card_2}')
        bj_cards_total = bj_card_1 + bj_card_2
        time.sleep(3)
        bj_hit_stay = int(input('HIT (1) or STAY (2)? '))
        if bj_hit_stay == 1:
            print('Dealing Card...')
            time.sleep(1)
            bj_card_3 = random.randint(2, 11)
            print(f'YOUR CARDS: {bj_card_1}, {bj_card_2}, {bj_card_3}')
            time.sleep(.5)
            print('Check cards for wins/busts...')
            time.sleep(2)
            if bj_card_total > 21:
                bj_check_aces()
            elif bj_card_total < 21:
                bj_hit_stay = input('HIT (1) or STAY (2)? ')
                if bj_hit_stay == '1':
                    print('Dealing Card...')
                    time.sleep(.5)
                    time.sleep(.5)
                    bj_card_4 = random.randint(2, 11)
                    print(f'YOUR CARDS: {bj_card_1}, {bj_card_2}, {bj_card_3}, {bj_card_4}')
                    time.sleep(.5)
                    print('Checking for wins/busts...')
                    time.sleep(1.5)
                    if bj_card_total > 21:
                        bj_check_aces()
                    elif bj_card_total < 21:
                        bj_hit_stay = input('HIT (1) or STAY (2)? ')
                        if bj_hit_stay == '1':
                            print('Dealing Card...')
                            time.sleep(.5)
                            time.sleep(.5)
                            bj_card_5 = random.randint(2, 11)
                            print(f'YOUR CARDS: {bj_card_1}, {bj_card_2}, {bj_card_3}, {bj_card_4}, {bj_card_5}')
                            print('Checking for wins/busts...')
                            time.sleep(1.5)
                            if bj_card_total > 21:
                                bj_check_aces()
                            elif bj_card_total < 21 and not bj_card_5 == 0:
                                print('MAX CARDS REACHED')
                            print('CHECKING WIN CHANCES.....')
                            time.sleep(2)
                            bj_end_game()
        if bj_hit_stay == 2: bj_end_game()


    # SLOTS GAME CODE
    def slots_win():
        global money, slots_bet, slots_version, playing
        print('YOU WIN')
        money = money + (slots_bet * 7)
        print(f'You bet {slots_bet} dollars.')
        time.sleep(.5)
        print(f'You now have {money} dollars.')
        time.sleep(.5)
        print('.')
        time.sleep(.5)
        print('.')
        time.sleep(.5)
        slots_play_again = 0
        if money > 0:
            while slots_play_again == 0:
                print('1 to play SLOTS again')
                print('2 to return to lobby')
                slots_play_again = input('Would you like to play again or return to lobby? ')
                if slots_play_again == '2':
                    print('Returning to lobby....')
                    time.sleep(.5)
                    print('.')
                    time.sleep(.5)
                    print('.')
                    playing = 0
                elif slots_play_again == '1':
                    time.sleep(.5)
                    slots_version = 0
                else:
                    print('INVALID INPUT')
                    time.sleep(.5)
                    slots_play_again = 0
        else:
            print('You ran out of money')
    def slots_spin():
        print({random.randint(0, slots_chance)})
        time.sleep(.3)
        print({random.randint(0, slots_chance)})
        time.sleep(.3)
        print({random.randint(0, slots_chance)})
        time.sleep(.4)
        print({random.randint(0, slots_chance)})
        time.sleep(.4)
        print({random.randint(0, slots_chance)})
        time.sleep(.5)
        print({random.randint(0, slots_chance)})
        time.sleep(.5)
    def slots_lose():
        global money, slots_bet, slots_version, playing
        slots_play_again = 0
        print('You lose.')
        print(f'You bet {slots_bet} dollars.')
        while slots_play_again == 0:
            if money > 0:
                print(f'You now have {money} dollars.')
                print('1 to play SLOTS again')
                print('2 to return to lobby')
                slots_play_again = input('Would you like to play again or return to lobby? ')
                if slots_play_again == '2':
                    print('Returning to lobby....')
                    time.sleep(.5)
                    print('.')
                    time.sleep(.5)
                    print('.')
                    playing = 0
                elif slots_play_again == '1':
                    time.sleep(.5)
                    slots_version = 0
                else:
                    print('INVALID INPUT')
                    time.sleep(.5)
                    slots_play_again = 0
            else:
                print('You ran out of money.')
    if which_game == 2:
        slots_version = 0
        while slots_version == 0:
            slots_all = []
            print('3 = 3-slot game')
            print('5 = 5-slot game')
            print('7 = 7-slot game')
            slots_version = int(input('Which game would you like to play? '))
            slots_bet = 0
            while slots_bet == 0:
                print(f'You selected the {slots_version}-slot game.')
                print(f'You have {money} dollars.')
                slots_bet = int(input('How much would you like to bet? '))
                if slots_bet >= money:
                    print('GOING ALL IN')
                    money = 0
                elif slots_bet < 1:
                    print('You cannot bet less than one dollar.')
                    slots_bet = 0
                elif slots_bet >= 1:
                    print(f'You put in {slots_bet} dollars.')
                    time.sleep(.5)
                    print(f'You now have {money} dollars.')

            slots_start = 0

            if slots_version == 3:
                print('3-Slot game')
                print('.')
                time.sleep(.5)
                slots_chance = 16
                for slot_variable in range(3):
                    slots_all.append(random.randint(0, 16))
                global slots_start, slots_all, slots_version
                while slots_start == 0:
                    slots_start = input('Press SPACE and then ENTER to start Slots ')
                    if slots_start == " ":
                        print('SLOT 1 spinning.....')
                        slots_spin()
                        print(f'SLOT 1: {slots_all[0]}')
                        print('SLOT 2 spinning.....')
                        slots_spin()
                        print(f'SLOT 2: {slots_all[1]}')
                        print('SLOT 3 spinning.....')
                        slots_spin()
                        print(f'SLOT 3: {slots_all[2]}')
                        time.sleep(.5)
                        print('Results:')
                        for slot in slots_all:
                            print(slot)
                        if slots_all[0] == slots_all[1] == slots_all[2]:
                            slots_win()
                        else: slots_lose()
                    else:
                        slots_start = 0

            elif slots_version == 5:
                print('5-Slot game')
                print('.')
                time.sleep(.5)
                slots_chance = 11
                for slot_variable in range(5):
                    slots_all.append(random.randint(0, 11))
                while slots_start == 0:
                    slots_start = input('Press SPACE and then ENTER to start Slots ')
                    if slots_start == " ":
                        print('SLOT 1 spinning.....')
                        slots_spin()
                        print(f'SLOT 1: {slots_all[0]}')
                        print('SLOT 2 spinning.....')
                        slots_spin()
                        print(f'SLOT 2: {slots_all[1]}')
                        print('SLOT 3 spinning.....')
                        slots_spin()
                        print(f'SLOT 3: {slots_all[2]}')
                        print('SLOT 4 spinning.....')
                        slots_spin()
                        print(f'SLOT 4: {slots_all[3]}')
                        print('SLOT 5 spinning.....')
                        slots_spin()
                        print(f'SLOT 5: {slots_all[4]}')
                        time.sleep(.5)
                        print('Results:')
                        for slot in slots_all:
                            print(slot)
                        if slots_all[0] == slots_all[1] == slots_all[2] == slots_all[3] == slots_all[4]:
                            slots_win()
                        else: slots_lose()
                    else:
                        slots_start = 0

            elif slots_version == 7:
                print('7-Slot game')
                print('.')
                time.sleep(.5)
                slots_chance = 6
                for slot_variable in range(7):
                    slots_all.append(random.randint(0, 6))
                while slots_start == 0:
                    slots_start = input('Press SPACE and then ENTER to start Slots ')
                    if slots_start == " ":
                        print('SLOT 1 spinning.....')
                        slots_spin()
                        print(f'SLOT 1: {slots_all[0]}')
                        print('SLOT 2 spinning.....')
                        slots_spin()
                        print(f'SLOT 2: {slots_all[1]}')
                        print('SLOT 3 spinning.....')
                        slots_spin()
                        print(f'SLOT 3: {slots_all[2]}')
                        time.sleep(1)
                        print('SLOT 4 spinning.....')
                        slots_spin()
                        print(f'SLOT 4: {slots_all[3]}')
                        print('SLOT 5 spinning.....')
                        slots_spin()
                        print(f'SLOT 5: {slots_all[4]}')
                        print('Slot 6 spinning.....')
                        slots_spin()
                        print(f'SLOT 6: {slots_all[5]}')
                        print('SLOT 7 spinning.....')
                        slots_spin()
                        print(f'SLOT 7: {slots_all[6]}')
                        time.sleep(.5)
                        print('Results:')
                        for slot in slots_all:
                            print(slot)
                        if slots_all[0] == slots_all[1] == slots_all[2] == slots_all[3] == slots_all[4] == slots_all[5] == slots_all[6]:
                            slots_win()
                        else: slots_lose()
                    else:
                        slots_start = 0

            else:
                print('Please select valid game.')
                slots_version = 0


    # ROULETTE GAME CODE
    if which_game == 3:
        print('work in progress...')
        time.sleep(1)
        playing = 0


    # POKER GAME CODE
    if which_game == 4:
        print('work in progress...')
        time.sleep(1)
        playing = 0


    # LEAVE CODE
    if which_game == 5:
        print('Hope to see you again soon! ')

    else:
        print('INVALID')
        time.sleep(.5)
        playing = 0



