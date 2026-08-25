import random
from Classes.Deck import Deck
from Classes.Player import Player

def start_game():

    print("Welcome to the game of War!")

    player_name1 = input("Please enter the first player's name: ")
    player_name2 = input("Please enter the second player's name: ")

    player1 = Player(player_name1)
    player2 = Player(player_name2)

    deck = Deck()
    deck.shuffle()

    for index, card in enumerate(deck.cards):

        if index % 2 == 0:
            player1.add_cards([card])

        else:
            player2.add_cards([card])

    print(f"{player1} has {player1.total_cards()} cards")
    print(f"{player2} has {player2.total_cards()} cards")

    play_game(player1, player2)

def play_game(player1, player2):

    while True:

        if len(player1.cards) == 0 and len(player1.won_cards) == 0:
            print(f"{player1} is out of cards. Game Over!")
            break

        if len(player2.cards) == 0 and len(player2.won_cards) == 0:
            print(f"{player2} is out of cards. Game Over!")
            break

        if len(player1.cards) == 0:
            player1.cards.extend(player1.won_cards)
            player1.won_cards.clear()
            random.shuffle(player1.cards)
            continue

        if len(player2.cards) == 0:
            player2.cards.extend(player2.won_cards)
            player2.won_cards.clear()
            random.shuffle(player2.cards)
            continue

        play_round(player1, player2)

def play_round(player1, player2):

    battle_cards = []

    while True:

        player1_card = player1.draw_card()
        player2_card = player2.draw_card()

        battle_cards.extend([player1_card, player2_card])

        print(f"{player1_card} vs {player2_card}")


        if player1_card.value > player2_card.value:

            player1.won_cards.extend(battle_cards)

            print(
                f"{player1} wins the round and now has "
                f"{player1.total_cards()} cards!\n"
            )
            break

        elif player2_card.value > player1_card.value:

            player2.won_cards.extend(battle_cards)

            print(
                f"{player2} wins the round and now has "
                f"{player2.total_cards()} cards!\n"
            )

            break

        else:

            print("War!")

            if len(player1.cards) < 4 or len(player2.cards) < 4:
                print("Not enough cards for war. Game Over!")
                break

            for _ in range(3):

                battle_cards.append(player1.draw_card())
                battle_cards.append(player2.draw_card())

            print("War cards played...\n")
            continue

if __name__ == "__main__":
    start_game()