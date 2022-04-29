def main():
    """
    Main függvény
    :return:
    """
    print("Üdvözöllek az oldalon!")
    warehouse = create_warehouse()
    menu(warehouse)


def menu(warehouse):
    """
    Menu of the warehouse
    :param warehouse:
    :return:
    """
    while True:
        chose_option = input("Válassz egy menűpontot:\n1 - Termék hozzáadása/frissítése \n2 - Termék törlése \n3"
                             " - Kilépés")
        if chose_option == "1":
            add_update_product(warehouse)
        elif chose_option == "2":
            delete_product(warehouse)
        elif chose_option == "3":
            exit_program()


def create_warehouse():
    """
    Create warehouse
    :return:
    """
    warehouse = {
        "Ablak": 30000,
        "Ajtó": 67000
    }
    return warehouse


def add_update_product(warehouse):
    """
    Create new line to warehouse.
    :param warehouse:
    :return:
    """
    print("*" * 50 + "\nVálasztott menu: Termék hozáadása/frissítése")
    product_name = input("Kérlek adj meg egy terméknevet: ")
    while True:
        try:
            product_value = int(input("Kérlek adj meg egy értéket a terméknek: "))
        except ValueError:
            print("Az értéknek számnak kell lennie:\n" + "*" * 50)
            continue
        if type(product_value) != int:
            print("Az értéknek számnak kell lennie:\n" + "*" * 50)
            product_value = input("Kérlek adj meg egy értéket a terméknek: ")
        else:
            print(f"Sikeres hozzáadás!\n Az új termék: {product_name} és az értéke: {product_value}\n"
                  + "*" * 50)
            break
    warehouse[product_name] = product_value


def delete_product(warehouse):
    print("*" * 50 + "\nVálasztott menu: Termék törlése")
    """
    Delete product function!
    """
    product_to_delete = input("Melyik terméket szeretnéd törölni?")
    try:
        warehouse.pop(product_to_delete)
        print(f"Sikeres törlés!\n {product_to_delete} törölve.\n" + "*" * 50)
    except:
        print("Sikertelen törlés!\n Nincs ilyen termék!\n" + "*" * 50)


def exit_program():
    """
    Exit of program
    :return:
    """
    while True:
        quit_or_not = input("Ki szeretne lépni? y - kilépés; n - visszalépés: ")
        if quit_or_not == "y":
            print("Viszont látásra!")
            quit()
        if quit_or_not == "n":
            break
        else:
            print("y/n nem megfelelő érték!\n" + "*" * 50)


main()
