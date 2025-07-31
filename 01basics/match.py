value = int(11)

match value:
    case 10 | 11:
        print("Ok, value is 10 or 11")
    case 15:
        print("Warning, value is 15")
    case _:
        print("Unknown value")

def process(val):
    match val:
        case int() if val > 0:
            return "Positive integer"
        case str() if len(val) > 5:
            return "Long string"
        case list() as l if len(l) == 0:
            return "Empty list"
        case _:
            return "Something else"
        
print(process("100000"))