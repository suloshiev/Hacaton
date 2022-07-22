import decimal
import json 


class Cars:
    FILE = 'jsonbd/haca.json'
    id = 0


    def __init__(self, brand, model, year, engine, color, body, mile, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.body = body
        self.mile = mile
        self.price = price
        self.send_cars_to_json()
    @classmethod
    def get_id(cls):
        cls.id += 1
        return cls.id

    @classmethod
    def listing(cls):
        with open(cls.FILE) as file:
            return json.load(file)

    @staticmethod
    def get_one_name(data, id):
        cars = list(filter(lambda x: x['id'] == id, data))
        if not cars:
            return 'не существует!'
        return cars[0]

    @classmethod
    def send_data_to_json(cls, data):
        with open(cls.FILE, 'w') as file:
            json.dump(data, file)

    def send_cars_to_json(self):
        data = Cars.listing()
        cars = {
            'id': Cars.get_id(),
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'color': self.color,
            'body': self.body,
            'mile': self.mile,
            'price': self.price
        }
        data.append(cars)

        with open(Cars.FILE, 'w') as file:
            json.dump(data, file)

        return {'status': '201', 'msg': cars}

    @classmethod
    def retrieve_cars(cls, id):
        data = cls.listing()
        cars = cls.get_one_name(data, id)
        return cars

    @classmethod
    def update_cars(cls, id, **kwargs):
        data = cls.listing()
        cars = cls.get_one_name(data, id)
        if type(cars) != dict:
            return cars
        index = data.index(cars)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return {'status': '201', 'msg': 'Updated'}

    @classmethod
    def delete_cars(cls, id):
        data = cls.listing()
        cars = cls.get_one_name(data, id)
        if type(cars) != dict:
            return cars

        index = data.index(cars)
        data.pop(index)
        cls.send_data_to_json(data)
        return {'status': '201', 'msg': 'Deleted'}

with open(Cars.FILE, 'w') as file:
    json.dump([], file)

car1 = Cars('BMW','M', 2022, round(4.43, 1), 'red', 'f90', 20000, round(78.5000, 2))
car2 = Cars('Mercedes', 'E', 2018, round(5.44, 1), 'white', 'w212', 10000, round(45.6000, 2))

print(Cars.listing())
print(Cars.update_cars(2, brand = 'Audi'))
print(Cars.retrieve_cars(2))
print(Cars.delete_cars(2))
print(Cars.listing())


