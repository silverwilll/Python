def catalog(name, *args):
    print(f"Cataloging {name} with additional info: {args}")
    print("Type: ", type(args))

    if len(args) > 0:
        print(args[0])

    for value in args:
        print(f"Additional info: {value}")
    print(f"Kindle: {kindlle}")

catalog("Tree", "oak", "ash", "linden")
catalog("Tree")