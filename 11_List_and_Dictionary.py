fruits = ["apple", "banana", "cherry", 100]

fruit_1_string = "apple, red, big, fresh"

fruit_1_dict = {
    "name": "apple",
    "color": "red",
    "size": 10,
    "freshness": True
}
box_2 = {
    "name": "books",
    "height": 30,
    "width": 50,
    "depth": 20,
    "items": []
}

box_1 = {
    "name": "toys",
    "height": 50,
    "width": 30,
    "depth": 20,
    "items": [
        {
            "name": "ball",
            "size": "big",
            "colors": "blue"
        },
        {
            "name": "truck",
            "color": "black",
            "size": "small"
        }
    ]
}

boxes = [box_1, box_2]

print(boxes[0]["items"][1]["name"])
