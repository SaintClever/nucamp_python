my_string = "giraffe"


print(my_string[2:4])

# Reverts from right to left and showcases the other characters From -1: to -7:
print(my_string[-1:]) # e
print(my_string[-2:]) # fe
print(my_string[-3:]) # ffe
print(my_string[-4:]) # affe
print(my_string[-5:]) # raffe
print(my_string[-6:]) # iraffe
print(my_string[-7:]) # giraffe
print('')

# Reverts from right to left when a negative is applied from -1 to -7
print(my_string[-1]) # e
print(my_string[-2]) # f
print(my_string[-3]) # f
print(my_string[-4]) # a
print(my_string[-5]) # r
print(my_string[-6]) # i
print(my_string[-7]) # g
print('')

# Creates a tampered pattern :)
print(my_string[1:-1]) # iraff
print(my_string[2:-2]) # raf
print(my_string[3:-3]) # a
print('')

# Everything is the same: giraffe
print(
  my_string, my_string[:], my_string[-7:], my_string[-len(my_string):]
)