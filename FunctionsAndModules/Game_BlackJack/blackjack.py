import random

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def shuffle():
    global deck
    random.shuffle(deck)


def play_blackjack():
    global mainWindow
    print("PLAY")
    mainWindow.mainloop()



def new_game():
    global deck
    global player_hand
    global dealer_hand
    global dealer_card_frame
    global player_card_frame
    global result_text
    result_text.set("BLACK JACK")
    # deck.clear()
    # Instead of clearing the deck we can er insert the card in the deck at last and then add a shuffle button to allow
    # shuffle anytime (See in deal_cards function)
    player_hand = list()
    print(player_hand)
    dealer_hand = list()
    # deck = list(cards)
    shuffle()

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2, pady=10)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2, pady=10)

    # Now we will automatically give two cards to player and one to dealer in beginning,

    deal_player()
    dealer_hand.append(deal_cards(dealer_card_frame)[0])
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def deal_cards(frame):
    """This function will pop one card at a time and the corresponding image will be embedded in frame.
     NOTE : Pop method gives exception if list is empty.
     """
    next_card = deck.pop(0)
    deck.append(next_card)
    # now we will add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised', borderwidth=3).pack(side='left', padx=3)
    # image attribute sets the image in that label
    # Well we can observe we have pack geometry layout because it would be good over here
    # NOTE: We cant add grid layout in that frame now
    # Now we have to link the action to the buttons

    return next_card


def deal_dealer():
    score = score_hand(dealer_hand)
# We want that dealer's deal should be done by the computer its self and the player should click dealer button to stick.
    while 0 < score < 17:
        dealer_hand.append(deal_cards(dealer_card_frame)[0])
        score = score_hand(dealer_hand)
        dealer_score_label.set(score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("DEALER WINS!!")
    elif score > 21 or score < player_score:
        result_text.set("PLAYER WINS!!")
    elif score > player_score:
        result_text.set("DEALER WINS!!")
    else:
        result_text.set("DRAW")


def score_hand(hand):
    """Here hand refers to the list of cards drawn out of the deck"""
    print(hand)
    score = 0
    ace = False
    for card in hand:
        if card == 1 and not ace:
            ace = True
            score += 11
            if score > 21 and ace:
                score -= 10
        else:
            score += card
    return score


def deal_player():
    # """We will check the drawn ace card whether it is value of 1 or 10.
    #     If we assign the other values to a global variable (like player_score and player_ace),
    #     They become local to that function and they are unreferenced from the global variable which
    #     will not be accessed after that.(THIS IS KNOWN AS SHADOWING)
    #     Here in player_score we are assigning a new value so it became local, whereas player_ace is still global
    #     We can check it by using locals() method
    #     So Avoid prevent shadowing we will use global keyword"""
    # global player_score
    # global player_ace
    #
    # # player_score = 0
    # card_drawn = deal_cards(player_card_frame)[0]
    #
    # if card_drawn == 1 and not player_ace:
    #     card_drawn = 11
    #     player_ace = True
    #     # Now here might be the case of busting by choosing 11 so, we will minus 10 if getting busted
    #     if player_score > 21:
    #         card_drawn -= 10
    #         player_ace = False
    #
    # player_score += card_drawn
    # player_score_label.set(player_score)

    # All the commented part is converted into one method score_hand

    global player_score
    player_hand.append(deal_cards(player_card_frame)[0])
    score = score_hand(player_hand)
    player_score_label.set(score)
    player_score = score

    if score > 21:
        result_text.set('DEALER WINS!!')


def load_cards(card_images):
    # for loading card images
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    suits = ['club', 'diamond', 'spade', 'heart']
    face_cards = ['jack', 'queen', 'king']

    # for each suit retrieve the card name
    for suit in suits:
        for cardno in range(1, 11):
            name = 'cards/{}_{}.{}'.format(cardno, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((cardno, image))

        # for face cards
        for face_card in face_cards:
            name = 'cards/{}_{}.{}'.format(face_card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


if __name__ == '__main__':
    """This if part is added so that we can open this game from any other program by importing this module over there.
    Suppose we make a game having collection of games. So to play this specific game it is preferred to take this 
    approach. We can make a play function which will open the game from ant other program."""
    play_blackjack()

mainWindow = tkinter.Tk()

# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow['background'] = 'green'
mainWindow.minsize(440, 400)
mainWindow.maxsize(440, 400)

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, background='green', foreground='white', font='arial', textvariable=result_text)
result.grid(row=0, column=0, columnspan=3, pady=10)

card_frame = tkinter.Frame(mainWindow, borderwidth='1', background="green")
card_frame.grid(row=1, column=0, sticky='news', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", font="consolas", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, font="consolas", background="green", fg="white")\
    .grid(row=1, column=0)
# embedded dealer frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", font="consolas", fg="white")\
    .grid(row=2, column=0, padx=3)
tkinter.Label(card_frame, textvariable=player_score_label, font="consolas", background="green", fg="white")\
    .grid(row=3, column=0, padx=3)

# embedded player frame to hold the card images

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow, background='green')
button_frame.grid(column=0, row=3, columnspan=3, sticky='w', padx=8, pady='8')

# here player_ace check whether the ace drawn has a value of 11 or 1

# dealer_button = tkinter.Button(button_frame, text='DEALER', command=deal_cards(dealer_card_frame))
#                   .grid(column=0, row=0)
# Above we can observe the command attribute, here whats happening is that we assigning the method to the
# command attribute by passing the arguments which is not as we wanted
# so to overcome this situation we gonna put this method in another method with no parameters
dealer_button = tkinter.Button(button_frame, text='DEAL', command=deal_dealer, background="blue")\
    .grid(column=0, row=0, padx='5')
player_button = tkinter.Button(button_frame, text='PLAYER', command=deal_player)\
    .grid(row=0, column=1, padx='5')
new_game_button = tkinter.Button(button_frame, text='NEW GAME', command=new_game, background='Yellow')
new_game_button.grid(row=0, column=2, padx='5')
shuffle_button = tkinter.Button(button_frame, text='SHUFFLE', command=shuffle, background='magenta')
shuffle_button.grid(row=0, column=3, padx='5')

cards = list()
load_cards(cards)
# we will  have a deck of cards containing shuffled cards using shuffle method from random
# note: its return type is None
deck = list(cards)
random.shuffle(deck)
player_score = 0
# Creating the list for storing the dealer's and player's hands

player_hand = list()
dealer_hand = list()

new_game()
# mainWindow.mainloop()