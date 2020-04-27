
class Strategy:

  def __init__(self):
    pass

  def play_next_card(self, strategy, suit, cards):
    if (strategy == 'Own Work First'):
      self.own_work_first(suit, cards)
    elif (strategy == "Own Work Unless Blocked"):
      print(strategy)
    elif (strategy == "Other Work First"):
      print(strategy)
    else:
      print("Unknown Strategy")

  def own_work_first(self, suit, cards):
    # If everybody's blocked, play other etam's cards. Simulates a big pow-wow
    # escalation to work out priorities once everyone's blocked :-)
    #
    if (cards.all_blocked()):
      print("All Blocked")
      cards.play_others_card(suit)
