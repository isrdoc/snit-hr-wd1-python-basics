class BasketballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

print(self.first_name)
print(kev_dur.__dict__)
