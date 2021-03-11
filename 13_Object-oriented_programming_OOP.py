class Dish:
    def __init__(self, color, pattern):
        self.color = color
        self.pattern = pattern

    def pretty_color(self):
        return f"pretty {self.color}"

class Cup(Dish):
    def __init__(self, color, liquid, pattern):
        super().__init__(color=color, pattern=pattern)
        self.liquid = liquid

    def description(self):
        return f"This is a {self.pretty_color()} {self.pattern} cup with {self.liquid}."

class Plate(Dish):
    def __init__(self, color, pattern, logo):
        super().__init__(color=color, pattern=pattern)
        self.logo = logo


dinner_plate = Plate(color="gray", pattern="empty", logo="Ikea")

tea_cup = Cup(color="blue", liquid="tea", pattern="oriental")
coffee_cup = Cup(color="white", liquid="coffee", pattern="british")
juice_cup = Cup("black", "juice", "plain")

print(dinner_plate.pretty_color())
print(tea_cup.description())
#print(coffee_cup.__dict__)
#print(juice_cup.__dict__)


def make_cup(color, liquid, pattern):
    def description():
        return f"This is a {color} {pattern} cup with {liquid}."

    return {
        "color": color,
        "liquid": liquid,
        "pattern": pattern,
        "description": description,
    }

beer_cup = make_cup(color="gray", liquid="beer", pattern="barbaric")

print(beer_cup["description"]())
