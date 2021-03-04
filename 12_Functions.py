# __name__ = "__main__"

print(f"Functions name: {__name__}")

from greetings import format_greeting

sad_greeting = "Heeeey..."
person_1 = "Igor"


igor_greeting = format_greeting(person="Igor", greeting="Heeeey...")

print(igor_greeting)
