from art import logo
import random

ma_cards = [1, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
flag = True

def user_card_picker():
    user_cards = random.choice(ma_cards)
    new_card = random.choice(ma_cards)
    return user_cards, new_card
def computer_card_picker():
    computer_cards = random.choice(ma_cards)
    new_computer_cards = random.choice(ma_cards)
    return computer_cards, new_computer_cards

answer = input("Do you want to play a game of Blackjack? Type 'y or 'n': ").lower()
if answer == 'y':
    # print(logo)
    may_cards = user_card_picker()
    maa_cards = list(may_cards)
    computa_cards = computer_card_picker()
    computer_cards = list(computa_cards)

    while flag:
        print(f'Your cards are: {maa_cards[0], maa_cards[1]}, current score is: {maa_cards[0] + maa_cards[1]}')
        print(f"The computer's first card is: {computer_cards[0]}")
        answer_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if answer_game == 'y':
            flag = True
            maa_cards.append(random.choice(ma_cards))
            user_total = sum(maa_cards)

            computer_cards.append(random.choice(ma_cards))
            computer_total = sum(computer_cards)

            print(f"Your cards are: {maa_cards}, this is your total: {user_total}")
            print(f"The computer's cards are {computer_cards}, and the computer's total is: {computer_total}")

            if user_total > 21:
                print(f"You lose, your number: {user_total}, computer's number: {computer_total} ")
                break
            elif user_total <= 21 and user_total > computer_total:
                print(f"You win, your number: {user_total}, computer's number: {computer_total} ")
                break
            elif computer_total > 21:
                print(f"You win, your number: {user_total}, computer's number: {computer_total} ")
                break
            elif computer_total <= 21 and computer_total > user_total:
                print(f"You lose, your number: {user_total}, computer's number: {computer_total} ")
                break
            elif user_total == computer_total:
                print(f"It's a tie, {user_total}")
                break
            computer_cards.append(random.choice(ma_cards))
            print(computer_cards)
        if answer_game == 'n':
            flag = False
            user_total = sum(maa_cards)
            computer_cards.append(random.choice(ma_cards))
            computer_total = sum(computer_cards)
            if user_total > 21:
                print(f"You lose, your number: {user_total}, computer's number: {computer_total} ")
                break
            elif user_total <= 21 and user_total > computer_total:
                print(f"You win, your number: {user_total}, computer's number: {computer_total} ")
                break
            elif computer_total > 21:
                print(f"You win, your number: {user_total}, computer's number: {computer_total} ")
                break
            elif computer_total <= 21 and computer_total > user_total:
                print(f"You lose, your number: {user_total}, computer's number: {computer_total} ")
                break
            elif user_total == computer_total:
                print(f"It's a tie, {user_total}")
                break

elif answer == 'n':
    exit('Exit')