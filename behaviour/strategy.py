
from behaviour.strategies import ownworkfirst as owf
from behaviour.strategies import ownworkunlessblocked as owub
from behaviour.strategies import othersworkfirst as othwf

class Strategy:

  def __init__(self, play_strategy):

    if (play_strategy == 'Own Work First'):
      self.strategy = owf.OwnWorkFirst()
    elif (strategy == "Own Work Unless Blocked"):
      self.strategy = owub.OwnWorkUnlessBlocked()
    elif (strategy == "Others Work First"):
      self.strategy = othwf.OtherWorkFirst()
    else:
      print("Unknown Strategy")

  def play_next_card(self, suit, cards):
    return self.strategy.play_next_card(suit, cards)
