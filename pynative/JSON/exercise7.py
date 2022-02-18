#mijn versie
import json
from types import SimpleNamespace

data = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

#vehicleObj.name, vehicleObj.engine, vehicleObj.price

#data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
vehicleObj = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
#print(x.name, x.hometown.name, x.hometown.id)
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)

#site versie
# import json
#
# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
# def vehicleDecoder(obj):
#         return Vehicle(obj['name'], obj['engine'], obj['price'])
#
# vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
#            object_hook=vehicleDecoder)

print("Type of decoded object from JSON Data")
print(type(vehicleObj))
print("Vehicle Details")
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)