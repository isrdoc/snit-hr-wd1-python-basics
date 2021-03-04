# __name__ = "greetings"

print(f"Greetings name: {__name__}")

def format_greeting(greeting, person):
    return f"{greeting}, {person}!"


def greet_nina():
    hello_nina = format_greeting("Yo", "Nina")
    print(hello_nina)

if "greetings" == "__main__":
    greet_nina()
