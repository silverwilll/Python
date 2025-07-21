people = {
    "Bob": 25,
    "Sue": 30,
    "Steve": 35,
}

keys = people.keys()
values = people.values()
items = people.items()

print(type(keys))
print(type(values))
print(type(items))

item_list = list(items)

print(items)
del people["Steve"]
print(items)
print(item_list)
