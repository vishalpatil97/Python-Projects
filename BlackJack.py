import random

suits = {'Hearts', 'Spades', 'Diamond', 'Clubs'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queens', 'King', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queens': 10, 'King': 10, 'Ace': 11}

playing = True


class Cards:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + ' of ' + self.rank


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit, rank))

    def __str__(self):
        deck_of_card = ''
        for card in self.deck:
            deck_of_card += '\n ' + card.__str__()
        return 'The deck has :' + deck_of_card

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while (self.value > 21) and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def loss_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Enter the bet money : '))
        except:
            print('Please enter the integer')
            continue
        else:
            if chips.bet > chips.total:
                print('Please enter valid amount ')
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        choice = input("Choose Hit or stand:enter  'h' or 's'").lower()
        if choice == 'h':
            hit(deck, hand)
        elif choice == 's':
            print("Player stands, dealer is playing")
            playing = False
        else:
            print('Please enter valid input')
            continue
        break


def show_some(player, dealer):
    print('dealers cards:')
    print('One card hidden')
    print(dealer.cards[1])
    print('\nPlayers cards:')
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print('dealers cards:')
    for card in dealer.cards:
        print(card)
    print('Players cards:')
    for card in player.cards:
        print(card)


def player_busts(player, dealer, chips):
    print('Bust player!')
    chips.loss_bet()


def player_wins(player, dealer, chips):
    print('player wins')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Dealer bust! Player wins!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer wins!')
    chips.loss_bet()


def push():
    print("This hand Tied! push")


while True:

    # Print an opening statement
    print('Welcome to Black Jack')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_card = Hand()
    dealer_card = Hand()
    player_card.add_card(deck.deal())
    player_card.add_card(deck.deal())
    dealer_card.add_card(deck.deal())
    dealer_card.add_card(deck.deal())
    # Set up the Player's chips
    players_chips = Chips()
    # Prompt the Player for their bet
    take_bet(players_chips)
    # Show cards (but keep one dealer card hidden)
    show_some(player_card, dealer_card)

    while playing:
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_card)
        # Show cards (but keep one dealer card hidden)
        show_some(player_card, dealer_card)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_card.value > 21:
            player_busts(player_card, dealer_card, players_chips)
            break
    if player_card.value <= 21:
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer_card.value < 17:
            hit(deck, dealer_card)
        # Show all cards
        show_all(player_card, dealer_card)
        # Run different winning scenarios
        if dealer_card.value > 21:
            dealer_busts(player_card, dealer_card, players_chips)
        elif player_card.value > dealer_card.value:
            player_wins(player_card, dealer_card, players_chips)
        elif player_card.value < dealer_card.value:
            dealer_wins(player_card, dealer_card, players_chips)
        else:
            push()
        # Inform Player of their chips total
    print("Your chips are : {}".format(players_chips.total))

    play_again = input("Want to play another hand? :Enter yes or no ?")
    if play_again[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing")
        break
