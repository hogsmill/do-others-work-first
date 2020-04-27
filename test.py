
import unittest

from behaviour import cards as c, play as p

class TestPlay(unittest.TestCase):

  def test_all_work_done(self):
    cards = c.Cards()
    play = p.Play(cards, '')

    self.assertFalse(play.all_work_done())

    cards.state['Hearts']['cards'] = []
    self.assertFalse(play.all_work_done())

    cards.state['Diamonds']['cards'] = []
    cards.state['Spades']['cards'] = []
    cards.state['Clubs']['cards'] = []
    self.assertTrue(play.all_work_done())

class TestCards(unittest.TestCase):

  def test_next_card_in_suit(self):
    cards = c.Cards()

    self.assertEqual(cards.next_card_in_suit(False), 1)
    self.assertEqual(cards.next_card_in_suit(5), 6)
    self.assertEqual(cards.next_card_in_suit(12), 13)
    self.assertEqual(cards.next_card_in_suit(1), 2)
    self.assertFalse(cards.next_card_in_suit(13))

  def test_next_lowest_others_card(self):
    cards = c.Cards()

    cards.state['Hearts']['others cards'] = [{'suit': 'Diamonds', 'card': 8}, {'suit': 'Spades', 'card': 6}, {'suit': 'Clubs', 'card': 9}]

    self.assertEqual(cards.next_lowest_others_card('Hearts'), {'suit': 'Spades', 'card': 6})

  def test_next_card_is_playable(self):
    cards = c.Cards()
    cards.state['Hearts']['cards'] = cards.cards_to_play()

    self.assertTrue(cards.next_card_is_playable('Hearts'))

    del cards.state['Hearts']['cards'][0]
    self.assertFalse(cards.next_card_is_playable('Hearts'))

    cards.state['Hearts']['cards'] = cards.cards_to_play()[5:]
    cards.state['Hearts']['current'] = 5
    self.assertTrue(cards.next_card_is_playable('Hearts'))

    cards.state['Hearts']['cards'] = []
    cards.state['Hearts']['current'] = 13
    self.assertFalse(cards.next_card_is_playable('Hearts'))

  def test_play_next_card(self):
    cards = c.Cards()
    cards.state['Hearts']['cards'] = cards.cards_to_play()
    next_card_1 = cards.state['Hearts']['cards'][1]
    next_card_2 = cards.state['Hearts']['cards'][2]
    length = len(cards.state['Hearts']['cards'])

    cards.play_next_card('Hearts')
    self.assertEqual(cards.state['Hearts']['cards'][0], next_card_1)
    self.assertEqual(cards.state['Hearts']['current'], 1)
    self.assertEqual(len(cards.state['Hearts']['cards']), length - 1)

    cards.play_next_card('Hearts')
    self.assertEqual(cards.state['Hearts']['cards'][0], next_card_2)
    self.assertEqual(cards.state['Hearts']['current'], 2)
    self.assertEqual(len(cards.state['Hearts']['cards']), length - 2)

    cards.state['Hearts']['cards'] = []
    cards.state['Hearts']['current'] = 13
    cards.state['Spades']['cards'] = [3, 4, 6]
    cards.state['Hearts']['others cards'] = [{'suit': 'Clubs', 'card': 8}, {'suit': 'Spades', 'card': 5}]

    cards.play_next_card('Hearts')
    self.assertEqual(cards.state['Spades']['cards'], [3, 4, 5, 6])
    self.assertEqual(cards.state['Hearts']['others cards'], [{'suit': 'Clubs', 'card': 8}])

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
