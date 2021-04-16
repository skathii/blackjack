import random
import time
import sys

card_values = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
options = ["Hit", "Stand"]
subtract_count = 0

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def view(self):
        print(self.suit + str(self.val))
        
class Deck:
    def __init__(self, deckcount):
        self.cards = []
        self.deckcount = deckcount
        self.create_deck()
        self.shuffle_deck()
        
    def create_deck(self):
        for x in range(1, self.deckcount + 1):
            for i in ["c", "d", "h", "s"]:
                for j in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                    self.cards.append(Card(i, j))      
                    
    def view(self):
        for x in self.cards:
            x.view()
   
    def shuffle_deck(self):
        for i in range(len(self.cards)-1, 0, -1):
            randint = random.randint(0, i)
            self.cards[i], self.cards[randint] = self.cards[randint], self.cards[i]
            
    def draw_card(self):
        card = self.cards[-1]
        del self.cards[-1]
    
        return card
            
class Player:    
    def __init__(self, Dealer):
        self.cards_dealt = []
        self.Dealer = Dealer
        self.score = 0
        self.subtract_count = 0
    
    def view_hand(self):
        for x in self.cards_dealt:
            x.view()
        
    def dealer_hand(self):
        self.cards_dealt[0].view()
        
    def dealer_facedown(self):
        self.cards_dealt[1].view()
        
        
    def val_hand(self):
        ace_count = 0
        self.score = 0
        for x in self.cards_dealt:
            self.score += card_values[x.val]

        if self.score > 21:
            for x in self.cards_dealt:
                if x.val == "A":
                    ace_count +=1
                
                if ace_count > self.subtract_count:
                    self.score -= 10
                    self.subtract_count += 1
                
    def val_dealerhand(self):
        self.score = 0
        self.score += card_values[self.cards_dealt[0].val]

    def clear_hands(self):
        self.cards_dealt = []
        

def first_hands(dealer, player, deck):
    draw1 = deck.draw_card()
    player.cards_dealt.append(draw1)
    draw2 = deck.draw_card()
    dealer.cards_dealt.append(draw2)
    draw3 = deck.draw_card()
    player.cards_dealt.append(draw3)
    draw4 = deck.draw_card()
    dealer.cards_dealt.append(draw4)


def view_hands(dealer, player):
    player.val_hand()    
    dealer.val_dealerhand()
    
    print("Your current hand: [" + str(player.score) + "]")
    player.view_hand()
    print('\n')
    print("The dealers hand: [" + str(dealer.score) + "]")
    dealer.dealer_hand()
    print('\n')

                
def blackjack(deckcount):

    keep_playing = True
    
    dealer = Player(True)
    player = Player(False)
    deck = Deck(1)


    while keep_playing == True:

        print('\n')
        print('########################')

        dealer.clear_hands()
        player.clear_hands()

        first_hands(dealer, player, deck)
        view_hands(dealer, player)

        while player.score < 22:
            if player.score == 21:
                print("BLACKJACK! YOU HIT 21!")
            move = input("What would you like to do? [h/s]: ")
            
            if move == "h":
                print('\n')
                print('########################')
                print("The dealer passes you a card.")
                draw = deck.draw_card()
                player.cards_dealt.append(draw)
                player.val_hand()
                
                if player.score > 21:
                    break
                
                print("Your current hand: [" + str(player.score) + "]")
                player.view_hand()
                print('\n')
                
            if move =="s":
                print('\n')
                break


        if move == "s":
            print('########################')
            print("You stood on " + str(player.score) + ". The Dealers face-down card was:")
            dealer.dealer_facedown()
            print('\n')
            dealer.val_hand()
            print("The Dealers hand is: [" + str(dealer.score) + "]")
                
            while dealer.score < player.score:
                print("The dealer gives himself a card.")
                draw = deck.draw_card()
                dealer.cards_dealt.append(draw)
                dealer.val_hand()
                print("His score is now " + str((dealer.score)))
                dealer.view_hand()

            if dealer.score == player.score:
                print('\n')
                print('########################')
                print("Wow! The dealer got the same score as you resulting in a PUSH!")
                print('\n')
                print("Your final hand: [" + str(player.score) + "]")
                player.view_hand()
                print('\n')
                print("The Dealers final hand: [" + str(dealer.score) + "]")
                dealer.view_hand()

            if dealer.score > player.score and dealer.score < 22:
                print('########################')
                print("Unlucky! The dealer got a higher score! [" + str(dealer.score) + "]." +  " Better luck next time!")
                print('\n')
                print("Your final hand: [" + str(player.score) + "]")
                player.view_hand()
                print('\n')
                print("The Dealers final hand: [" + str(dealer.score) + "]")
                dealer.view_hand()
                    
                
            if dealer.score > player.score and dealer.score > 21:
                print('\n')
                print('########################')
                print("Hurray! The dealer Busted with a score of " + str(dealer.score) + "! Congratulations!")
                print('\n')
                print("Your final hand: [" + str(player.score) + "]")
                player.view_hand()
                print('\n')
                print("The Dealers final hand: [" + str(dealer.score) + "]")
                dealer.view_hand()
                        
        else:
            print('\n')
            print('########################')
            print("Oops! You busted with a score of " + str(player.score) + ". Better luck next time!")
            print('\n')
            print("Your final hand:")
            player.view_hand()


        print('\n')
        print('########################')
        replay = input("Would you like to continue playing? [y/n] ")

        if replay == "n":
            print("Thanks for playing! Created by skathii; (http://www.github.com/skathii)")
            print("The program will terminate in three seconds.")
            time.sleep(3)
            sys.exit()