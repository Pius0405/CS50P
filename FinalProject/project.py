from cards_and_players import Card,Player,HumanPlayer,Dealer
import random
import sys
import time

def main():
    name = input("Enter your name: ")
    output_rules(name)
    stopper(5)
    #create player and dealer object
    player = HumanPlayer(name)
    dealer = Dealer()
    #begin the game
    game(player,dealer)


def game(p,d):
    #at the begining each party gets two cards
    print(f"{p.name}'s turn")
    for _ in range(2):
        p.add_card(Card.get_card())
    p.cal_score()
    p.display_hand()
    print(f"Your score: {p.get_score()}")
    stopper(2)
    print("Dealer's turn")
    for _ in range(2):
        d.add_card(Card.get_card())
    d.cal_score()
    d.display_hand(flag = False)
    stopper(2)


    #check if any party got blackjack at the begining
    if p.get_score() + d.get_score() == 42:
        sys.exit("Tie!")
    elif p.get_score() == 21:
        sys.exit("You win!")
    elif d.get_score() == 21:
        sys.exit("Dealer wins! You lose!")


    #if no winner at the begining, continue the game
    while True:
        print(f"{p.name}'s turn")
        move = get_move(p.score)
        if move == "H":
            p.add_card(Card.get_card())
            p.cal_score()
            p.display_hand()
            print(f"Your score: {p.get_score()}")
            stopper(1.5)
            if check_21(p.score):
                d.display_hand()
                print(f"Dealer's score: {d.get_score()}")
                sys.exit("You win!")
            elif check_busted(p.score):
                d.display_hand()
                print(f"Dealer's score: {d.get_score()}")
                sys.exit("Busted! You lose! Dealer wins!")
            stopper(1)
        else:
            #dealer's turn
            print("Dealer's turn")
            while True:
                if d.score< 12:
                    move = "H"
                else:
                    move = random.choice(("H","S","O"))
                if move == "H":
                    d.add_card(Card.get_card())
                    d.cal_score()
                    d.display_hand(flag = False)
                    stopper(1.5)
                    if check_21(d.score):
                        d.display_hand()
                        print(f"Dealer's score: {d.get_score()}")
                        sys.exit("Dealer wins! You lose!")
                    elif check_busted(d.score):
                        d.display_hand()
                        print(f"Dealer's score: {d.get_score()}")
                        sys.exit("Dealer busted! You win!")
                    stopper(1)
                elif move == "O":
                    #if move is "O", dealer no longer draw a card but reveals his card and compare, larger one wins
                    d.display_hand()
                    print(f"Dealer's score: {d.get_score()}")
                    if d.get_score() == p.get_score():
                        sys.exit("Tie")
                    elif d.get_score() > p.get_score():
                        sys.exit("Dealer wins! You lose!")
                    else:
                        sys.exit("You win!")
                else:
                    #dealer stands
                    d.display_hand(flag = False)
                    break


def output_rules(name):
    print("♢♠️♣️♥"*10)
    print(f"Welcome to BlackJack! {name}")
    print("Rules:")
    print("1. Do not exceed 21!")
    print("2. Minimum score to stand is 12")
    print("3. Moves:")
    print("(H) for hit and (S) for stand")
    print(f"Good luck! {name}")
    print("♢♠️♣️♥"*10)
    print(" ")

def get_move(score):
    while True:
        move = input("Enter your move: ")
        if move in ("H","S"):
            break
        else:
            print("Invalid move")
    #minimum score to stand is 12 so if score < 12 then player MUST draw a card hence move is "H"
    if score < 12 and move == "S":
        print("Insufficient score to stand")
        return "H"
    else:
        return move


def check_21(score):
    return score == 21

def check_busted(score):
    return score > 21

#slow down the whole game so that it's not that complicated and easier for user to see what's going on
def stopper(s):
    time.sleep(s)

if __name__ == "__main__":
    main()
