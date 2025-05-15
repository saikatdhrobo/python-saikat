name = input("Enter your fullname: ")
phone_no = input("Enter phone number: ")

# find() returns the index of the first occurrence of the character "a" in name
result = name.find("a")
print(result)

# rfind() returns the index of the last occurrence of the character "a" in name
# Example: For "jakaria saikat dhrobo"
# find("a") returns 1 (first 'a')
# rfind("a") returns 12 (last 'a')
# If character not found, both return -1
lastFindresult = name.rfind("a")
print(lastFindresult)

# Capitalize the first letter of the name and make the rest lowercase
name = name.capitalize()
print(name)

# Convert the entire name string to uppercase
name = name.upper()
print(name)

# Convert the entire name string to lowercase
name = name.lower()
print(name)

# Check if name contains only digits (will be False here because name contains letters)
result = name.isdigit()
print(result)

# Check if name contains only alphabetic letters (will be True if no spaces or digits)
result = name.isalpha()
print(result)

# Count how many times '-' appears in the phone number
result = phone_no.count("-")
print(result)

# Remove all '-' characters from the phone number
phone_no = phone_no.replace("-", "")
print(phone_no)

# Show the help documentation for string methods
print(help(str))
