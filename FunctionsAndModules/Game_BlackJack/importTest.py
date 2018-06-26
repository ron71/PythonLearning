import blackjack
# from blackjack import *


blackjack.play_blackjack()
print(blackjack.cards)
"""
# now we can use same cards in any other program or card
# NOTE : In Python protected members are named as _nameofthemember.
# However there is no concept of private or protected members in Python.
# Using import we should only access the members which are not private or protected
# We should also not use "from blackjack import * ". It can import each and every function of the module.
# So after that we will gain access to write the functions directly using their names, which is not good,
    because it will become difficult to differentiate between method calling of this program and the imported module.
"""
# Example:
g = sorted(globals())
for x in g:
    print(x)

"""O/P:
__annotations__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
blackjack
"""
# Now if we use from blackjack import *

"""O/P:
__annotations__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
button_frame
card_frame
cards
deal_cards
deal_dealer
deal_player
dealer_button
dealer_card_frame
dealer_hand
dealer_score_label
deck
load_cards
mainWindow
new_game
new_game_button
play_blackjack
player_button
player_card_frame
player_hand
player_score
player_score_label
random
result
result_text
score_hand
shuffle
shuffle_button
tkinter
"""