favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

friends = ['phil', 'sarah']
for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print("\tHi " + name.title() +
              ", I see you favorite language is " +
              favorite_languages[name].title())
