from year_2019.challenge_4 import valid_password

valid_passwords = 0
for i in range(347312, 805915 + 1):
    if valid_password(i):
        valid_passwords += 1
print(valid_passwords)

valid_passwords = 0
for i in range(347312, 805915 + 1):
    if valid_password(i, additional_check=True):
        valid_passwords += 1
print(valid_passwords)
