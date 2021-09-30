state_capitals = {
  'Washington': 'Olympia',
  'Oregon': 'Salem',
  'California': 'Sacremento'
}

print(len(state_capitals))
print(state_capitals['Washington'])

state_capitals['Washington'] = 'Aberdeen'
print(state_capitals)

state_capitals['Texas'] = 'Austin'
print(state_capitals)

del state_capitals['California']
print(state_capitals)

# pop has a return value but del does not
removed_capital = state_capitals.pop('Oregon')
print(state_capitals)
print(removed_capital)