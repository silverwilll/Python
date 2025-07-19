days = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}

del days["Mon"] # remove the key "Mon"
print(days)

print(days.pop("Thu")) # remove the key "Thu" and return its value
print(days)

print(days.popitem()) # remove the last inserted item
print(days)

days["abc"] = "abc" # add a new key-value pair
print(days)
print(days.popitem())

days.clear()
days = {}
print(days) # now it's an empty dictionary