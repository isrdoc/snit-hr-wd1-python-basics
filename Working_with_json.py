import json

with open("people.json", "r") as people_file:
    people_dict = json.loads(people_file.read())
    people_dict["people"][0]["name"] = "Duško"
    print(people_dict)

with open("people.json", "w") as people_file:
    people_file.write(json.dumps(people_dict, indent=4))


