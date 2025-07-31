# and, not, or
# if, elif, else
# True, False, None
# is, in, not in
# ==, !=, <, >, <=, >=

raining = False
temperature = 18

if temperature > 19 and not raining:
    print("Weather fine!")
elif not raining:
    print("At least it is dry.")
else:
    print("Stay indoors")

mood = "good" if not raining else "bad"
print(mood)