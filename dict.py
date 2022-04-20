# birthdays = {"John":"August 1","Marcus":"April 8"}
# birthdays["mary"] = "September 14"
# print(list(birthdays.keys())) 
print("Enter a string")

input_string = input()

characters = {}

for character in input_string:
    characters.setdefault(character,0)
    characters[character] = characters[character] + 1
print(characters)