

def showState(state)
  puts "Sprint #{state[:sprint]}"
  state[:state].keys.each do |key|
    str = "  #{key}: #{state[:state][key][:current]}"
    if (state[:state][key][:blocked])
      str = str + " BLOCKED"
    end
    puts str
  end
end

def playCard(suit, card)
  puts "Playing #{card} of #{suit}"
end
