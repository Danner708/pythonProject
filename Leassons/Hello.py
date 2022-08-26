import datetime


def hello_xy():
    name = input("What is your name?")
    if name == "Dani":
        print(f"{datetime.datetime.now()} - Hello {name}")
    else:
        print(f"{datetime.datetime.now()} - I don't know you! {name}")


hello_xy()
