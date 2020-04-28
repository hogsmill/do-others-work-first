
class OwnWorkUnlessBlocked:

  def play_next_card(self, suit, cards):
    blocked = True
    suit_state = cards.state[suit]
    suit_cards = suit_state['cards']
    other_cards = suit_state['others cards']

    if (not suit_state['current'] and suit_cards[0] == 1):
      cards.play_next_suit_card(suit)
      blocked = False
    elif (len(suit_cards) > 0):
      if (suit_state['current'] + 1 == suit_cards[0]):
        cards.play_next_suit_card(suit)
        blocked = False
      elif (len(other_cards) > 0):
        cards.play_others_card(suit)
    elif (len(other_cards) > 0):
      cards.play_others_card(suit)
    return blocked
