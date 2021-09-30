# lambda arg1, arg2: expression to return

lambda num: num ** 2

# or


def square(num): return num ** 2


# lambda in action
def a_function(callback):
    return callback(3)


print(
    a_function(lambda num: num ** 2)
)
