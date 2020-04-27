
from behaviour import strategy as s

class Play:

  def __init__(self, cards, strategy):
    self.sprint = 0
    self.cards = cards
    self.play_strategy = strategy
    self.strategy = s.Strategy()

  def all_work_done(self):
    done = True
    for suit in self.cards.state:
      if (len(self.cards.state[suit]['cards']) > 0):
        done = False
    return done

  def show_state(self):
    print("---------------------------------------")
    print("Sprint {}".format(self.sprint))
    print("---------------------------------------")
    for suit in self.cards.state:
      str = "  {}: {}".format(suit, self.cards.state[suit]['current'])
      if (self.cards.state[suit]['blocked']):
        str = str + " BLOCKED"
      str = "{} {} {}".format(str, self.cards.state[suit]['cards'], self.cards.state[suit]['others cards'])
      print(str)

  def play_next_sprint(self):
    for suit in self.cards.state:
      if (self.cards.next_card_is_playable(suit)):
        self.cards.play_next_card(suit)
      else:
        self.cards.state[suit]['blocked'] = True
        self.strategy.play_next_card(self.play_strategy, suit, self.cards)
    self.sprint = self.sprint + 1
