x = "12"
if type(x) == int:
    print("string")
else:
    print("not string")


def summa(x: int) -> int:
    if type(x) == str:
        print("nope")
        return
    return x + 2

summa(2)

print(isinstance(123, str))