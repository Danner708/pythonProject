from .data_handling import DataHandling


class ListProduct:

    @staticmethod
    def list_products():
        """
        List of products
        :return:
        """
        handler = DataHandling()
        inventory = handler.read_json()
        num_of_products = handler.product_counter()

        print("*" * 50 + "\nVálasztott menu: Terméklista")
        print(f"Ezek a termékek találhatóak az áruházban, termékek száma: {num_of_products}")
        for item in inventory:
            print(f"Product ID: {item}, value: {inventory[item]}")
        print("*" * 50)
