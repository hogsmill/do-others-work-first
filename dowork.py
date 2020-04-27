

from utils import config as cfg
from behaviour import cards as c, play as p, strategy as s

config = cfg.Config()
cards = c.Cards()
play = p.Play(cards, config.cfg['strategy'])

while not play.all_work_done():
  play.play_next_sprint()
  play.show_state()
  input('Enter: ')
