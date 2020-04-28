
from random import seed
from random import randint

class Cards:

  def __init__(self):

    self.suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    self.suit_names = {
      1:'Ace', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13:'King'
    }
    self.state = {
          'Diamonds': { 'current': False, 'blocked': False, 'cards': self.cards_to_play(), 'for others': [], 'others cards': []},
          'Hearts': { 'current': False, 'blocked': False, 'cards': self.cards_to_play(), 'for others': [], 'others cards': []},
          'Clubs': { 'current': False, 'blocked': False, 'cards': self.cards_to_play(), 'for others': [], 'others cards': []},
          'Spades': { 'current': False, 'blocked': False, 'cards': self.cards_to_play(), 'for others': [], 'others cards': []}
    }
    self.sprint = 0,

    self.get_cards_for_others()
    self.get_others_cards()

  def print_state(self):
    for suit in self.state:
      print("{}: {}".format(suit, self.state[suit]))

  def cards_to_play(self):
    cards = []
    for card in self.suit:
      cards.append(card)
    return cards

  def get_cards_for_others(self):
    for suit in self.state:
      suit_state = self.state[suit]
      for i in range(3):
        index = randint(0, len(suit_state['cards']) - 1)
        other = suit_state['cards'][index]
        suit_state['for others'].append(other)
        del suit_state['cards'][index]

  def get_others_cards(self):
    for suit in self.state:
      self.get_others_cards_for_suit(suit)
    for suit in self.state:
      self.state[suit].pop('for others', None)

  def get_others_cards_for_suit(self, suit):
    for other_suit in self.state:
      if (suit != other_suit):
        this_suit = self.state[suit]
        that_suit = self.state[other_suit]
        index = randint(0, len(that_suit['for others']) - 1)
        this_suit['others cards'].append({'suit': other_suit, 'card': that_suit['for others'][index]})
        del that_suit['for others'][index]

  def play_next_suit_card(self, suit):
    self.state[suit]['current'] = self.state[suit]['cards'][0]
    del self.state[suit]['cards'][0]

  def next_lowest_others_card(self, suit):
    next_card = False
    l = len(self.state[suit]['others cards'])
    for i in range(l):
      if (not next_card or self.state[suit]['others cards'][i]['card'] < next_card['card']):
        next_card = self.state[suit]['others cards'][i]
    return next_card

  def insert_others_card_into_cards(self, suit, card):
    cards = self.state[card['suit']]['cards']
    cards.append(card['card'])
    cards.sort()
    self.state[suit]['others cards'].remove(card)
    return cards

  def remove_added_card(self, suit, card):
    self.state[suit]['others cards'].remove(card)

  def play_others_card(self, suit):
    other_card = self.next_lowest_others_card(suit)
    if (other_card):
      other_suit = other_card['suit']
      print("Playing {}:{}".format(other_suit, other_card['card']))
      self.state[other_suit]['cards'] = self.insert_others_card_into_cards(suit, other_card)
      if (self.state[other_suit]['current'] + 1 == self.state[other_suit]['cards'][0]):
        self.state[other_suit]['blocked'] = False

  def all_blocked(self):
    all_blocked = True
    for suit in self.state:
      if not self.state[suit]['blocked']:
        all_blocked = False
    if (all_blocked):
      print("Everybody's blocked!")
    return all_blocked
