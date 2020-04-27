import json

class Config:

  def __init__(self):
    with open('config.json') as json_file:
      self.cfg = json.load(json_file)

    print(self.cfg)
