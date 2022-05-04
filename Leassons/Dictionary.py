import datetime
import time
from pprint import pprint


def dict_test():
    dict_a_thor = {
        "window": 78000,
        "door": 6000,
        "boolean_var": {
            "sub": "asd"
        }
    }
    dict_a_thor.pop("door")  # törlés pop érték alapján remove index
    print("#" * 50)
    print(dict_a_thor)
    pprint(dict_a_thor)
    dict_a_thor["window"] = 80000
    print(f"How much is the window: {dict_a_thor.get('window')}")


def list_and_for_cycle():
    test_list = [
        "e1",
        45,
        123.23,
        [
            "e2",
            "e3"
        ]
    ]

    print(range(5, 10))
    print(len(test_list))

    test_list.append("Appended")

    for index in range(len(test_list)):
        print(f"{index}: {test_list[index]}")

    print("\n")
    for index, element in enumerate(test_list):
        if type(element) == list:
            print(f"This is a list:")
            for i, e in enumerate(element):
                print(f"\t{i}: {e}")
            print(("-" * 50))
        print(f"{index} - {element}")


dict_test()
list_and_for_cycle()
print(("-"*50))


def while_true():
    while True:
        timestemp = datetime.datetime.now()
        print(timestemp)

        time.sleep(1)
        if "9" in str(timestemp):
            break
    return 
# return funkcióból break ciklusból lép ki

while_true()
