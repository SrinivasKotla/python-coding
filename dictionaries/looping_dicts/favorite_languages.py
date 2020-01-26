favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

for name in favorite_languages.keys():
    print(name.title())

print('\n')

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
