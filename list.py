list1 = list((1,2,3))
# print(list1)

list2 = ["1", 1, "Hello", 0, "Goodmorning", "Snow"]
# print(list2[1:4])
# for i in list2:
#     if i == 0:
#         pass
#     else:
#         print(i)

myList = ["news", 1, 2, "Network", "Sunrise", "Book"]
# print(myList[:3]) # Slice first three items
# ['news', 1, 2]
# print(myList[::2]) # Print every second element with a skip count 2
# ['news', 2, 'Sunrise']
# print(myList[::-1]) # Reversing the list
# print(myList[3:]) # Stating from 3nd item to last item without end value

myList.insert(2,[3, "welcome", "apple"])
# print(myList)
# ['news', 1, [3, 'welcome', 'apple'], 2, 'Network', 'Sunrise', 'Book']

myList.remove(1)
# print(myList)
# ['news', [3, 'welcome', 'apple'], 2, 'Network', 'Sunrise', 'Book']
x = myList.pop(2)
# print(x)
# 2

list3 = ["apples", "mangoes", "bananas"]
list4 = ["grapes", "oranges"]

list3.extend(list4)
# print(list3)
# ['apples', 'mangoes', 'bananas', 'grapes', 'oranges']
list5 = list3 + list4
# print(list5)
# ['apples', 'mangoes', 'bananas', 'grapes', 'oranges']


list6 = ["apples", "apples", "bananas", "mangoes", "mangoes",  "grapes", "bananas"]
list7 = []

list8 = [1,2,1,2,3,4,5,2,3,4,5,4,3,1]


for i in list8:
    if i not in list7:
        list7.append(i)
print(list7)



        




