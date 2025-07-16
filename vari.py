def catalog(name, *args):
    print(f"Cataloging {name} with additional info: {args}")

    for value in args:
        print(f"Additional info: {value}")

catalog("Book", "Author: John Doe", "Genre: Fiction", "Year: 2023")