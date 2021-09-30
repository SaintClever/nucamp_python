state_capitals = {
  'Washington': 'Olympia',
  'Oregon': 'Salem',
  'California': 'Sacremento'
}

# keys
for state in state_capitals:
  print(state)


# values
for city in state_capitals.values():
  print(city)


# keys and values
for state in state_capitals:
  print(state_capitals[state], 'is the capital of', state)


# keys and values
for state, city in state_capitals.items():
  print(state, 'is the capital of', city)