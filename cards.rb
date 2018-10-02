

$suit = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Setup
#
def cardsToPlay()
  cards = []
  $suit.each do |card|
    cards << card
  end
  cards
end

def swapCards(state)
  state[:state].keys.each do |suit|
    cards = state[:state][suit][:cards]
    state[:state][suit][:for_others] = []
    for i in 0..2
      other = rand(cards.length - 1)
      state[:state][suit][:for_others] << cards[other]
      cards.delete_at(other)
    end
  end
  suits = state[:state].keys
  state[:state].keys.each do |suit|
    i = 0
    suits.each do |otherSuit|
      if (otherSuit != suit)
        state[:state][otherSuit][:other_cards] << [suit, state[:state][suit][:for_others][i]]
        i = i + 1
      end
    end
    state[:state][suit].delete([:for_others])
  end
  state
end

def initialState
  state = {
    :sprint => 0,
    :state => {
      'Diamonds' => { :current => '', :blocked => false, :cards => cardsToPlay(), :other_cards => [] },
      'Hearts' => { :current => '', :blocked => false, :cards => cardsToPlay(), :other_cards => [] },
      'Clubs' => { :current => '', :blocked => false, :cards => cardsToPlay(), :other_cards => [] },
      'Spades' => { :current => '', :blocked => false, :cards => cardsToPlay(), :other_cards => [] }
    }
  }
  state = swapCards(state)
  puts state
  state
end

# Game Play
#
def done(state)
  done = true
  state[:state].keys.each do |suit|
    if !state[:state][suit][:cards].nil?
      done = false
    end
  end
  done || state[:sprint] == 10
end

def playNextSprint(state)
  state[:state].keys.each do |suit|
    if state[:state][suit][:current].empty?
      next_card = $suit[0]
    else
      current_index = $suit.index(state[:state][suit][:current])
      next_card = $suit[current_index + 1]
    end
    if state[:state][suit][:cards][0] == next_card
      state[:state][suit][:current] = next_card
      state[:state][suit][:cards].shift
    else
      state[:state][suit][:blocked] = true
    end
  end
  state[:sprint] = state[:sprint] + 1
end
