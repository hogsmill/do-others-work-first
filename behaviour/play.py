
from behaviour import strategy as s

class Play:

  def __init__(self, cards, play_strategy):
    self.sprint = 0
    self.cards = cards
    self.strategy = s.Strategy(play_strategy)

  def all_work_done(self):
    done = True
    for suit in self.cards.state:
      if (self.cards.state[suit]['current'] < 13):
        done = False
    return done

  def show_state(self):
    print("---------------------------------------")
    print("Sprint {}".format(self.sprint))
    print("---------------------------------------")
    for suit in self.cards.state:
      cards_done = len(self.cards.state[suit]['cards']) == 0
      other_cards_done = len(self.cards.state[suit]['others cards']) == 0
      str = "  {}: {}".format(suit, self.cards.state[suit]['current'])
      if (cards_done and other_cards_done):
        str = str + " DONE"
      elif (self.cards.state[suit]['blocked']):
        str = str + " BLOCKED"
      str = "{} {} {}".format(str, self.cards.state[suit]['cards'], self.cards.state[suit]['others cards'])
      print(str)

  def play_next_sprint(self):
    for suit in self.cards.state:
      self.cards.state[suit]['blocked'] = self.strategy.play_next_card(suit, self.cards)
    self.sprint = self.sprint + 1
