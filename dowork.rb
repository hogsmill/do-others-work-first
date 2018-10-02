#
# dowork.rb - simulation of do other team's work first...
#
require_relative './io'
require_relative './cards'

state = initialState()

done = false
showState(state)
while !done
  playNextSprint(state)
  showState(state)
  done = done(state)
end
