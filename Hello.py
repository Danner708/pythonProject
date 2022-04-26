import datetime


def hello_xy(name: str = "asd"):
    name = input("What is your name?")
    if name == "Dani":
        print(f"Hello {name}")
    else:
        print("I don't know you!")


hello_xy()
