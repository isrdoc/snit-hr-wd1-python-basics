message = "Hello"
user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))

is_user_logged_in = False

if message == "Hello":
    print(message + " " + user_name)
    print("Your age is: " + str(user_age - 10))
    print("User is logged in.")

print("After conditional")
