from Moduls.menu import Menu
from Moduls.create_warehouse import WareHouse

if __name__ == "__main__":
    print("Üdvözöllek az oldalon!")
    warehouse = WareHouse.create_warehouse()
    Menu.menu(warehouse)
