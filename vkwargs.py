def details(name, **kwargs):
    print(f"Details for {name}:")

    print(type(kwargs))
    print(kwargs)

    if "height" in kwargs:
        print("Height", kwargs['height'])

    for key in kwargs:
        print(key, kwargs[key])

details("Sue", age=30, city="New York", occupation="Engineer")