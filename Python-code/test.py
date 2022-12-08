# Dictionary


alien_0 = {'color': 'green', 'speed': 'slow'}

# get function

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# items functions, key/value

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi"
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print()

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")


for name in favorite_languages.keys():
    print(name.title())

