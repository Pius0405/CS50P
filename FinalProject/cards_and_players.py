import random
class Card:
    suites = ["♢","♠️","♣️","♥"]
    values = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
    deck = []
    #insert cards to deck
    for i in range(len(suites)):
        for j in range(len(values)):
            deck.append([suites[i],values[j]])

    @classmethod
    def get_card(cls):
        random.shuffle(cls.deck)
        card = random.choice(cls.deck)
        cls.deck.remove(card)
        return card

    @classmethod
    def display_cards(cls,cards,front):
        card_body = ["" for _ in range(4)]
        if front:
            #display the front side
            for card in cards:
                card_body[0] += f"{'_'*6} "
                card_body[1] += f"|{card[1]}{' '*4}|"
                card_body[2] += f"|{' '*2}{card[0]}{' '*2}|"
                card_body[3] += f"|{'_'*4}{card[1]}!"
        else:
            #display the set of cards as unknown (hide the cards first)
            l = len(cards)
            card_body[0] += f"{'_'*6} " * l
            card_body[1] += f"|?{' '*4}|" * l
            card_body[2] += f"|{' '*2}?{' '*2}|" * l
            card_body[3] += f"|{'_'*4}?!" * l
        for layer in card_body:
            print(layer)


class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.hand = []

    def get_score(self):
        return self.score

    def add_card(self,card):
        self.hand.append(card)

    def cal_score(self):
        """
        A function to make player's or dealer's score dynamic instead of static

        This function must be called each time a card is added to the hand in order to get a
        new score for current cards in hand.
        This fucntion decides the most suitable score (1 or 11) for Ace.
        """
        score = 0
        num_of_aces = 0
        for card in self.hand:
            if card[1] in ("J","Q","K"):
                score += 10
            elif card[1] == "A":
                num_of_aces += 1
            else:
                score += int(card[1])
        for _ in range(num_of_aces):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
        self.score = score

    def display_hand(self, flag = True):
        Card.display_cards(self.hand, flag)


class HumanPlayer(Player):
    def __init__(self,name):
        super().__init__(name)

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
