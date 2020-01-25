dict = {
    'list': 'A list is a collection of item in particular order.',
    'tuple': 'A tuple is just like a list but immutable and wrapped in parentheses.',
    'condition': 'An expression that can be evaluated true or false.',
    'string': 'A string is simply a series of characters.',
    'append': 'Add elements to the end of the list.'
    }

for key in dict.keys():
    print(key.title()+':')
    print("\t"+dict[key]+'\n')
