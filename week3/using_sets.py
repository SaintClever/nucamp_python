numbers_set = {1, 2, 3, 4, 4}  # set cannot have duplicates
print(numbers_set)


# numbers_set = {1, 2, 3, 4, [5, 6]}  # sets cannot have mutable data types
# print(numbers_set)


numbers_set = {1, 2, 3, 4, (5, 6)}
print(numbers_set)


words_set = {'Alpha', 'Bravo', 'Charlie'}

abcd = ''
for word in words_set:
    abcd += word
print(abcd)


if 'Alpha' in words_set:
    print('Alpha is in set')
else:
    print('Alpha not in set')


words_set.add('Delta')
print(words_set)

words_set.discard('Bravo')
print(words_set)


print(
    type(("tuple item",)),
    type(("string item"))
)

print(type({}))
print(type({'1', '2', '3'}))

test = {(1, 2), (3, 4), (5, 6)}
print(test)

my_string = "Nucamp"
print(my_string[3:5])
