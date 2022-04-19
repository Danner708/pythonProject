import datetime

truefalse: bool = True


def hello_xy(name: str = "asdfasgas"):
    print("#"*50)

    if truefalse:
        print(True)

    if name == "asdfasgas":
        name = input("What is your name?")
        if name == "asd":
            print("asd")
    else:
        print("I know you!")
    return f"{datetime.datetime.now()} - Hello {name}!"


print(hello_xy())
print(hello_xy("Pisti"))
