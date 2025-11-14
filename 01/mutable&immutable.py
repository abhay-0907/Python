'''
mutable: list, dict, set
immutable: int, float, string, bool, tuple
Mutabel -> Mutable means their internal state (content) can be changed without changing their memory address.
Immutable -> Immutable means their internal state (content) cannot be changed without changing their memory address. Any "change" results in a new object being created, so memory reference changes.
'''

num_1 = 10
num_2 = num_1
num_1 = 15
print(num_1) # 15
print(num_2) # 10


string = "Hello"
print(string) # Hello
string = "World"
print(string) # World , here string change the memory referenc from hello to world