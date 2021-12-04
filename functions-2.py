# list1 = [1,4,5,7,0,8]
# print(all(list1))

# list2 = [True , True, True, True]
# print(all(list2))

# list3 = []
# print(all(list3))

# list4 = {1,2,3,4,5}
# print(all(list4))

# list5 = {
#     "name": "ankush",
#     "sex": "m",
#     "age": "20"
# }
# print(all(list5))

# for x in "mango":
#     print(x)
#     if (x=="n"):
#         break

# for x in "banana":
#     if x == "a":
#         continue
#     print(x)

# for x in range(2,25,3):
#     print(x)

# for x in range(10):
#     if x==6: 
#         break
#     print(x)
# else:
#     print("End of the line")

# fruits = ["banana", "cherry", "mango", "guava"]
# flowers = ["tulip", "jasmin", "sunflower", "acasia"]

# for x in fruits:
#     for y in flowers:
#         print(x, y)

import json
# data = {
#     'name': 'Sonam', 'roll_no': 2
#     }
# json_data = json.dumps(data)
# print(json_data)
json_data = {
   "('Hello')": "('Hi')",
   "('Bye')": 3
    
}
parsed_data = json.dumps(json_data)
print(parsed_data)
print(json.dumps(parsed_data))
print(json.dumps(json.dumps(parsed_data)))