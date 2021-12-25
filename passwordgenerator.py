import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to PassWord Generator by Essien")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
# to make the password generator easy
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)    
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)    
# to make the password more randomized and harder for hackers to hack, 
password_li = []
for char in range(1, nr_letters + 1):
    password_li += random.choice(letters)
    # or password_li.append(random.random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_li += random.choice(symbols)    
for char in range(1, nr_numbers + 1):
    password_li += random.choice(numbers)    
random.shuffle(password_li)    
password = ""
for char in password_li:
    password +=  char
print(f"Here is your PassWord: {password}")
