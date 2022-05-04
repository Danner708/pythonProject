class AddUpdateProduct:

    @staticmethod
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
                print("Az értéknek számnak kell lennie!\n" + "*" * 50)
                continue
            if type(product_value) != int:
                print("Az értéknek számnak kell lennie!\n" + "*" * 50)
                product_value = input("Kérlek adj meg egy értéket a terméknek: ")
            else:
                print(f"Sikeres hozzáadás!\n Az új termék: {product_name} és az értéke: {product_value}\n"
                      + "*" * 50)
                break
        warehouse[product_name] = product_value
