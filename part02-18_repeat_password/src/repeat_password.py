# Write your solution here
passw = input("Password: ")

while True:
    passw_repeat = input("Repeat password: ")

    if passw == passw_repeat:
        print("User account created!")
        break

    print("They do not match!")
