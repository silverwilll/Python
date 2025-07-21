try:
    d = {}
    d["hello"]
    print(1 / 0)
except ZeroDivisionError as zde:
    print("Failed.", zde)
except Exception as e:
    print("Caught an exception.", type(e), e)
finally:
    print("This will always execute")