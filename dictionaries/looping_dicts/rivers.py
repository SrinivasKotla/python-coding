rivers = {
    "ganga": "india",
    "nile": "egypt",
    "amazon": "brazil",
    }

for key, value in rivers.items():
    print("The " + key.title() + " flows through " + value.title())

print("\nList of rivers in the list.")
for river in rivers.keys():
    print(river.title())

print("\nList of countries in the list.")
for country in rivers.values():
    print(country.title())
