piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# slicing list from c to e
print(piano_keys[2:5])

# slicing list from c to e with increment of 2
print(piano_keys[2:5:2])

# reverse slice the list
print(piano_keys[::-1])

# SLICING ALSO WORKS WITH TUPLES
piano_keys_tuple = ('do', 're', 'mi', 'fa', 'so', 'la', 'ti')
print(piano_keys_tuple[2:5])