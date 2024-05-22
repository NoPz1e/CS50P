# Ask user for their name, remove and capitalize
name = input("What's yout name? ").strip().title()

# Split user's name into frist name and last name
frist, last = name.split(' ')

# Say hello to user
print(f"hello, {frist}")
