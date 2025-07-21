from collections import defaultdict

people = {
    "Bob": 25,
    "Sue": 30,
    "Steve": 35,
}

print(people.get("Ethel", 99))

days = defaultdict(str)
days.update({"Mon": "Monday", "Tue": "Tuesday"})
print(days)
print(days["Mon"])  # Will return "Monday"
print(days["Wed"])  # Will return an empty string since "Wed" is not set