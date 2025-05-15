#validate user input exercise
# 1. username isn't more than 12 characters
# 2. username mustn't contain spaces
# 3. username mustn't contain digits


username = input("enter username: ")

if len(username) >12:
    print("Username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username can't contain spaces")
elif not username.isalpha():
    print("Username can't contain digits")
else:
    print(f"Welcome {username}")