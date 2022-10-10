import random
import array

# max length of password needed.
# this can be altered to suit your needs.
MAX_LEN = 18

# declare ana array of characters that we need in our password.
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWERCASE_CHAR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPERCASE_CHAR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SYMBOLS = ['!', '<', '>', '<=', '>=', '>==', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']

# combine all the character array to form one array
COMBINED = DIGITS + UPPERCASE_CHAR + LOWERCASE_CHAR + SYMBOLS

# randomly selecting at least one character from each set
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPPERCASE_CHAR)
rand_lower = random.choice(LOWERCASE_CHAR)
rand_symbol = random.choice(SYMBOLS)

# combine the characters selected
# in this instance, we only have 4 characters
# the required characters are 16, thus
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

# now we are sure we have at least one character from each set we fill the rest by selecting randomly
# from the combined list
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED)
    
    # convert temporary password into an array and shuffle
    # to prevent a consistent pattern
    # making the first random and unpredictable
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

# transverse the temporary password array and append the characters to form the password
password = ""
for x in temp_pass_list:
    password = password + x

# print out the final password
print(password)