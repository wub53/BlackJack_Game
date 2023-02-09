# Rules 
""""
Each card has its corresponding  according to the rank as mentioned below
Ace = 1
1 = 1
2 = 2
3 = 3
4 = 4
5 = 5
6 = 6
7 = 7
8 = 8
9 = 9
10 = 10
Jack = 10
King = 10
Queen = 10

* As the game starts 2 random cards will be dealt to player aswell as dealer.
* 1 card of the dealer will be hidden and 1 will be showed to the player.
* Player and Dealer will have their corresponding total value which is the sum of values of their respective cards
* After the cards are dealt Player will have 2 options : Hitme and Stand
* Hit me : It randomly pops the card out of deck and adds to the players card list
* Stand : Standing shifts the control of play from player to dealer.
* After the stand button is hit : If the total of dealer is greater less than 16 random cards are added to the dealer list until the dealer total gets more than 17 
* IF dealer total > 21 dealer busted
* IF player total > 21 player busted
* If player total = 21 >> Its BlackJack !! Player wins
* If player total > dealer total but less than 21 Player wins

"""
from tkinter import *
from tkinter import messagebox
import math
import random
from PIL import Image, ImageTk

root = Tk()
root.title('BlackJack_Game')
root.iconbitmap('codemy.ico')
root.geometry("1200x800")
root.configure(background="green")

global counter
counter = 0
global playerCard_spot, dealerCard_spot

playerCard_spot = 0
dealerCard_spot = 0

# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((100, 170))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

root.title(f'BlackJack_Game')

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(ipadx=20, pady=10)

# Put Dealer cards in frames
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

dealer_label_6 = Label(dealer_frame, text='')
dealer_label_6.grid(row=0, column=4, pady=20, padx=20)

dealer_label_7 = Label(dealer_frame, text='')
dealer_label_7.grid(row=0, column=4, pady=20, padx=20)

# Put Player cards in frames
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='')
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='')
player_label_5.grid(row=1, column=4, pady=20, padx=20)

player_label_6 = Label(player_frame, text='')
player_label_6.grid(row=1, column=5, pady=20, padx=20)

player_label_7 = Label(player_frame, text='')
player_label_7.grid(row=1, column=6, pady=20, padx=20)

player_label_8 = Label(player_frame, text='')
player_label_8.grid(row=1, column=7, pady=20, padx=20)


global isFlow
isFlow = True

class Card:

    def __init__(self,suit ,rank):
        self.suit_list = ["clubs","diamonds","hearts","spades"]
        self.rank_list = ["None","1","2","3","4","5","6","7","8","9","10","11","12","13"]
        self.suit = suit
        self.rank = rank
        self.cardName = self.rank_list[self.rank] + "_of_" + self.suit_list[self.suit]
        self.m_unique_number = pow(2,suit) + pow(3,rank)
        self.cardValue = 0
        if (self.rank_list[rank] == "1"): # remember ace mightt also take value 11
            self.cardValue = 1
        elif(self.rank_list[rank] == "2"):
            self.cardValue = 2
        elif(self.rank_list[rank] == "3"):
            self.cardValue = 3
        elif(self.rank_list[rank] == "4"):
            self.cardValue = 4
        elif(self.rank_list[rank] == "5"):
            self.cardValue = 5
        elif(self.rank_list[rank] == "6"):
            self.cardValue = 6
        elif(self.rank_list[rank] == "7"):
            self.cardValue = 7
        elif(self.rank_list[rank] == "8"):
            self.cardValue = 8
        elif(self.rank_list[rank] == "9"):
            self.cardValue = 9
        elif(self.rank_list[rank] == "10"):
            self.cardValue = 10
        elif(self.rank_list[rank] == "11"): #Jack
            self.cardValue = 10
        elif(self.rank_list[rank] == "12"): #Queen
            self.cardValue = 10
        elif(self.rank_list[rank] == "13"): #King
            self.cardValue = 10
            
    def __str__(self):
        return (self.rank_list[self.rank] + "_of_ " + self.suit_list[self.suit])
    
    def __eq__(self,other):
        return (self.rank == other.rank and self.suit == other.suit)
    
    def __gt__(self,other):
        if self.suit > other.suit:
            return True
        elif self.suit == other.suit:
            if self.rank > other.rank:
                return True
        else: 
            return False

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range (4):
            for rank in range (1,14):
                self.cards.append(Card(suit,rank))
        # Shuffle the deck
        n_cards = len(self.cards)
        for i in range(n_cards):
            j = random.randrange(0,n_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
                
    def __str__(self):
        for i in self.cards:
            s = str(i.rank) + "_of_" + str(i.suit)  
            return s
            
    def shuffle(self):
        n_cards = len(self.cards)
        for i in range(n_cards):
            j = random.randrange(0,n_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    
    def pop_card(self):
        return self.cards.pop()
    
    def is_empty(self):
        return len(self.cards) == 0
    
    def dealAHand(self, hands, n_cards = 52):
        n_players = len(hands)
        for i in range(n_cards):
            if self.is_empty():
                break
            card = self.pop_card()
            current_player = i % n_players
            hands[current_player].add_card(card)

class BlackJackGameController:
    pass

class Dealer(BlackJackGameController):
    def __init__(self,g):  
        global dealer_image1,dealer_image2,dealerCard_spot
        dealerCard_spot = 0
        self.cards = []
        self.total = 0

        card1 = g.deck.pop_card()
        card1name = card1.cardName
        self.total = self.total + card1.cardValue
        self.cards.append( card1 )
        self.show = True
        # Resize Card
        dealer_image1 = resize_cards(f'images/cards/{card1name}.png')
        # Output Card To Screen
        dealer_label_1.config(image=dealer_image1)

        card2 = g.deck.pop_card()
        card2name = card2.cardName
        dealerCard_spot += 1
        dealer_image2 = resize_cards(f'images/cards/{card2name}.png')
        self.total = self.total + card2.cardValue
        self.cards.append( card2 )
        self.show = False

    def __str__(self):
        string = ""
        if (self.show == True):
            for i in self.cards:
                string = string + i.rank_list[i.rank] + " of " + i.suit_list[i.suit] + "\n"   
            return string
        else:
            string = self.cards[0].rank_list[self.cards[0].rank] + " of " + self.cards[0].suit_list[self.cards[0].suit] + "\n"
            return string

    def hitMe(self):
        print("i am in dealer hit func")
        global dealerCard_spot
        card = g.deck.pop_card()
        self.cards.append(card)
        self.total = self.total + card.cardValue
        cardName = card.cardName
        global dealer_image3, dealer_image4, dealer_image5,dealer_image6,dealer_image7,dealer_image8

        # Display card
        if dealerCard_spot < 8:
           
            if dealerCard_spot == 1:
                # Resize Card
                global dealer_image2
                # Output Card To Screen
                dealer_label_2.config(image=dealer_image2)
                # Increment our player spot counter
                dealerCard_spot += 1
            if dealerCard_spot == 2:
                # Resize Card
                dealer_image3 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                dealer_label_3.config(image=dealer_image3)
                # Increment our player spot counter
                dealerCard_spot += 1
            elif dealerCard_spot == 3:
                # Resize Card
                dealer_image4 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                dealer_label_4.config(image=dealer_image4)
                # Increment our player spot counter
                dealerCard_spot += 1
            elif dealerCard_spot == 4:
                # Resize Card
                dealer_image5 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                dealer_label_5.config(image=dealer_image5)
                # Increment our player spot counter
                dealerCard_spot += 1

            elif dealerCard_spot == 5:
                # Resize Card
                dealer_image6 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                dealer_label_6.config(image=dealer_image6)
                # Increment our player spot counter
                dealerCard_spot += 1



class Player(BlackJackGameController):
    def __init__(self,g):  
        self.standStatus = False
        global player_image1, player_image2
        self.cards = []
        self.total = 0
        
        card = g.deck.pop_card()
        card1 = card.cardName
        self.total = self.total + card.cardValue
        self.cards.append( card )
        
        card = g.deck.pop_card()
        card2 = card.cardName
        self.total = self.total + card.cardValue
        self.cards.append( card )

        print("player card value after calling conostructor: ",self.total)

        player_image1 = resize_cards(f'images/cards/{card1}.png')
        # Output Card To Screen
        player_label_1.config(image=player_image1)

        player_image2 = resize_cards(f'images/cards/{card2}.png')
        # Output Card To Screen
        player_label_2.config(image=player_image2)

        global playerCard_spot 
        playerCard_spot = 2
                  
    def __str__(self):
        string = ""
        for i in self.cards:
            string = string + i.rank_list[i.rank] + " of " + i.suit_list[i.suit] + "\n"   
        return string
    
    def hitMe(self):
            
        global playerCard_spot
        card = g.deck.pop_card()
        self.cards.append(card)
        self.total = self.total + card.cardValue
        cardName = card.cardName
        global player_image3, player_image4, player_image5,player_image6,player_image7,player_image8

        # Display card
        if playerCard_spot < 8:
           
            if playerCard_spot == 2:
                # Resize Card
                player_image3 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                player_label_3.config(image=player_image3)
                # Increment our player spot counter
                playerCard_spot += 1
            elif playerCard_spot == 3:
                # Resize Card
                player_image4 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                player_label_4.config(image=player_image4)
                # Increment our player spot counter
                playerCard_spot += 1
            elif playerCard_spot == 4:
                # Resize Card
                player_image5 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                player_label_5.config(image=player_image5)
                # Increment our player spot counter
                playerCard_spot += 1

            elif playerCard_spot == 5:
                # Resize Card
                player_image6 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                player_label_6.config(image=player_image6)
                # Increment our player spot counter
                playerCard_spot += 1

            elif playerCard_spot == 6:
                # Resize Card
                player_image7 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                player_label_7.config(image=player_image7)
                # Increment our player spot counter
                playerCard_spot += 1

            elif playerCard_spot == 7:
                # Resize Card
                player_image8 = resize_cards(f'images/cards/{cardName}.png')
                # Output Card To Screen
                player_label_8.config(image=player_image8)
                # Increment our player spot counter
                playerCard_spot += 1

        print("player cardValue = ",self.total)
        root.title(f'BlackJack_Game')
        if (self.total > 21):
            messagebox.showinfo("Player BUSTED !!", "Player total > 21")
            return

        if (self.total == 21):
            messagebox.showinfo("Its a BLACK JACK !!", "Player WINS ")
            return


    def stand(self,dealer):
        print("i am in stand func")
        print(dealer.total)
        
        if dealer.total > 16:
            global dealerCard_spot
            dealerCard_spot += 1
            dealer_label_2.config(image=dealer_image2)

        while(dealer.total <= 16):
            dealer.hitMe()

        if (dealer.total == self.total ):
            messagebox.showinfo("------ !!", "NO ONE WINs !!")

        if (dealer.total == 21 and self.total < 21):
            messagebox.showinfo("Hard Luck !!", "DEALER WINs !!")

        if ( (dealer.total < 21 and self.total < 21) and (dealer.total > self.total)):
            messagebox.showinfo("Hard Luck !!", "DEALER WINs !!")
        
        if ( (self.total < 21 and dealer.total < 21) and (self.total > dealer.total)):
            messagebox.showinfo("Congratulations !!", "PLAYER WIN !!")

        if (dealer.total > 21):
            messagebox.showinfo("Player WINS !!", "Dealer total > 21")

class BlackJackGameController:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.isPGameOn = True
        self.isBjckGameOn = True       
    

class RestartGame:
    
    def __init__(self):
        global counter 
        counter += 1
    
    def  restartGame(self):
        root.title(f'BlackJack_Game')
        global player,dealer,g
        global dealer_image1,dealer_image2,dealerCard_spot
        global player_image1, player_image2
        
        dealer_label_1.config(image='')
        dealer_label_2.config(image='')
        dealer_label_3.config(image='')
        dealer_label_4.config(image='')
        dealer_label_5.config(image='')
        dealer_label_6.config(image='')

        player_label_1.config(image='')
        player_label_2.config(image='')
        player_label_3.config(image='')
        player_label_4.config(image='')
        player_label_5.config(image='')
        player_label_6.config(image='')
        player_label_7.config(image='')
        player_label_8.config(image='')
        
        while (player.cards):
            player.cards.pop()

        while (dealer.cards):
            dealer.cards.pop()

        player.total = 0
        card = g.deck.pop_card()
        pcard1 = card.cardName
        player.total = player.total + card.cardValue
        player.cards.append( card )
        
        card = g.deck.pop_card()
        pcard2 = card.cardName
        player.total = player.total + card.cardValue
        player.cards.append( card )

        player_image1 = resize_cards(f'images/cards/{pcard1}.png')
        # Output Card To Screen
        player_label_1.config(image=player_image1)

        player_image2 = resize_cards(f'images/cards/{pcard2}.png')
        # Output Card To Screen
        player_label_2.config(image=player_image2)

        global playerCard_spot 
        playerCard_spot = 2
        
        dealerCard_spot = 0
        dealer.total = 0
        card1 = g.deck.pop_card()
        dcard1name = card1.cardName
        dealer.total = dealer.total + card1.cardValue
        dealer.cards.append( card1 )
        dealer.show = True
        # Resize Card
        dealer_image1 = resize_cards(f'images/cards/{dcard1name}.png')
        # Output Card To Screen
        dealer_label_1.config(image=dealer_image1)

        card2 = g.deck.pop_card()
        dcard2name = card2.cardName
        dealerCard_spot += 1
        dealer_image2 = resize_cards(f'images/cards/{dcard2name}.png')
        dealer.total = dealer.total + card2.cardValue
        dealer.cards.append( card2 )
        dealer.show = False
  
if __name__ == "__main__":
    print ("i am in isFlow while loop")
    global g,dealer,player
    g = BlackJackGameController()
    dealer = Dealer(g)
    player = Player(g)
    restart = RestartGame()

    # Create Button Frame
    button_frame = Frame(root, bg="green")
    button_frame.pack(pady=20)

    # Create a couple buttons
    deal_button = Button(button_frame, text="Deal", font=("Helvetica", 14), command=restart.restartGame)
    deal_button.grid(row=0, column=0)

    card_button = Button(button_frame, text="Hit Me!", font=("Helvetica", 14), command=player.hitMe)
    card_button.grid(row=0, column=1, padx=10)

    stand_button = Button(button_frame, text="Stand!", font=("Helvetica", 14),command=lambda:player.stand(dealer))
    stand_button.grid(row=0, column=2)
    
    root.mainloop()



print("exited the isflow while()")



