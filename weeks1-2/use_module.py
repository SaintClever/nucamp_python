'''
import my_module

my_module.greet("Albert Einstein")
print("My favorite ice cream flavor is", my_module.flavor)
'''

# or

from my_module import greet, flavor

greet("Albert Einstein")
print("My favorite ice cream flavor is", flavor)
