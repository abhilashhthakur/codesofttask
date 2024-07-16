import random
import string
char_values = string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase

pass_len = int(input("Enter Password Length:"))

password=""
for i in range(pass_len):
    password += random.choice(char_values)

print(f"Your Generated Password:{password}")

