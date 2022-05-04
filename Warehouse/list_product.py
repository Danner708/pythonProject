class ListProduct:

    @staticmethod
    def list_product(warehouse):
        """
        List of products
        :return:
        """
        print("*" * 50 + "\nVálasztott menu: Terméklista")
        print("Ezek a termékek találhatóak az áruházban!")
        for i in warehouse:
            print(str(i) + ": " + str(warehouse[i]) + "Ft.")
        print("*" * 50)
