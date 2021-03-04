# __name__ = "__main__"

print(f"Functions name: {__name__}")

import greetings

sad_greeting = "Heeeey..."
person_1 = "Igor"


igor_greeting = greetings.format_greeting(person="Igor", greeting="Heeeey...")

print(igor_greeting)
