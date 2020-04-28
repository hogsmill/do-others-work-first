
import unittest

from behaviour import cards as c, play as p, strategy as s

class TestStrategy(unittest.TestCase):

  pass

class TestPlay(unittest.TestCase):

  def test_all_work_done(self):
    cards = c.Cards()
    play = p.Play(cards, 'Own Work First')

    self.assertFalse(play.all_work_done())

    cards.state['Hearts']['current'] = 13
    self.assertFalse(play.all_work_done())

    cards.state['Diamonds']['current'] = 13
    cards.state['Spades']['current'] = 13
    cards.state['Clubs']['current'] = 13
    self.assertTrue(play.all_work_done())

class TestCards(unittest.TestCase):

  def test_next_lowest_others_card(self):
    cards = c.Cards()

    cards.state['Hearts']['others cards'] = [{'suit': 'Diamonds', 'card': 8}, {'suit': 'Spades', 'card': 6}, {'suit': 'Clubs', 'card': 9}]

    self.assertEqual(cards.next_lowest_others_card('Hearts'), {'suit': 'Spades', 'card': 6})

  def test_play_others_card(self):
    cards = c.Cards()

    cards.state['Hearts']['cards'] = cards.cards_to_play()
    cards.state['Spades']['cards'] = cards.cards_to_play()
    del cards.state['Spades']['cards'][3]
    other_card = {'suit': 'Spades', 'card': 4}
    cards.state['Hearts']['others cards'] = [other_card, {'suit': 'Diamonds', 'card': 8}]

    cards.play_others_card('Hearts')
    self.assertEqual(len(cards.state['Spades']['cards']), 13)
    self.assertEqual(cards.state['Spades']['cards'][3], other_card['card'])

  def test_all_blocked(self):
    cards = c.Cards()

    self.assertFalse(cards.all_blocked())

    cards.state['Spades']['blocked'] = True
    self.assertFalse(cards.all_blocked())

    cards.state['Hearts']['blocked'] = True
    cards.state['Clubs']['blocked'] = True
    cards.state['Diamonds']['blocked'] = True
    self.assertTrue(cards.all_blocked())

if __name__ == '__main__':
    unittest.main()
