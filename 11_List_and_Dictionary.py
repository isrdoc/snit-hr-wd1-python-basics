car_brands = [
    {
        "name": "tesla",
        "number_of_cars_made": 1000
    },
    {
        "name": "toyota",
        "number_of_cars_made": 2000
    },
    {
        "name": "nissan",
        "number_of_cars_made": 500
    }
]

for car_brand in car_brands:
    print(f'Brand {car_brand["name"]} has made {car_brand["number_of_cars_made"]} cars.')
