from http.client import NETWORK_AUTHENTICATION_REQUIRED


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(car["brand"])
# print(car.get('model'))
# print(car.keys())
# print(car.values())
# print(car.items())
# for key in car:
#   print(key, '=>', car[key])

# for key_val in car.items():
#   print(key_val[0],'=>', key_val[1])
car['color'] = 'Olive Red'
# print(car)

# for key, val in car.items():
#   print(key, '=>', val)

car_features = {
  "steering": "Power",
  "navigation": "Inbuild GPS",
  "airbags": ["front seat", "side seat", "backseat"]
}


car.update(car_features) 
# print(car.items())
# print(car['steering'])
# print(car["airbags"][0])

car1 = {
  "model": "Ford",
  "Year": 1999
}
car2 = {
  "model": "Tesla",
  "Year": 2016
}
car3 = {
  "brand": "Gypsi",
  "engine": "v8"
}

cars = {**car1, **car2, **car3}
# print(cars.items())
# dict_items([('model', 'Tesla'), ('Year', 2016), ('brand', 'Gypsi'), ('engine', 'v8')])


hobbies = {
  "foo": "bar",
  "john": "dee",
  "lorem": "ipsum"
}

interests = hobbies.copy()
likes = dict(interests)
motivations = likes
# print(interests.items())
# print(likes.items())
# print(motivations.items())
# dict_items([('foo', 'bar'), ('john', 'dee'), ('lorem', 'ipsum')])
# dict_items([('foo', 'bar'), ('john', 'dee'), ('lorem', 'ipsum')])
# dict_items([('foo', 'bar'), ('john', 'dee'), ('lorem', 'ipsum')])

john = {
  "grade": 1,
  "teacher": "Lilly"
}
dee = {
  "grade": 2,
  "teacher": "Jasmin"
}
students = {
  "stud1": john, "stud2": dee
}
print("Student1 grade:", students["stud1"]["grade"])
print("Student2 teacher:", students["stud2"]["teacher"])
for key, val in students.items():
  print(key, val)

# Student1 grade: 1
# Student2 teacher: Jasmin
# stud1 {'grade': 1, 'teacher': 'Lilly'}
# stud2 {'grade': 2, 'teacher': 'Jasmin'}
