import random

values = {'two': 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
          "jack": 11, "queen": 12, "king": 13, "ace": 14}
suits = ('Hearts', "Diamonds", "Spades", "Clubs")

ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + "of" + self.suit


class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_method(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()


class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove(self):
        return self.all_cards.pop(0)

    def add(self, new_card):
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards'


if __name__ == '__main__':
    player1 = Player("Mark")
    player2 = Player("Anna")
    deck = Deck()
    deck.shuffle_method()
    for x in range(26):
        player1.add(deck.deal_card())
        player2.add(deck.deal_card())
    game_on = True
    while game_on == True:
        if len(player1.all_cards) == 0:
            print(f"Player one has lost")
            break
        if len(player2.all_cards) == 0:
            print("Player 2 has lost ")
            break
        player_one_cards = []
        player_one_cards.append(player1.remove())
        player_two_cards = []
        player_two_cards.append(player2.remove())
        at_war = True
        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player1.add(player_one_cards)
                player1.add(player_two_cards)
                at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player2.add(player_one_cards)
                player2.add(player_two_cards)
                at_war = False
            else:
                print("WAR!")
                if len(player1.all_cards) < 3:
                    print("Player 1 unable to play war")
                    game_on = False
                    break
                elif len(player2.all_cards) < 3:
                    print("Player 2 unable to play war")
                    game_on = False
                    break
                else:
                    for num in range(3):
                        player_one_cards.append(player1.remove())
                        player_two_cards.append(player2.remove())
