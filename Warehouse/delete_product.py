class DeleteProduct:

    @staticmethod
    def delete_product(warehouse):
        print("*" * 50 + "\nVálasztott menu: Termék törlése")
        """
        Delete product founction!
        """
        product_to_delete = input("Melyik terméket szeretnéd törölni?")
        try:
            warehouse.pop(product_to_delete)
            print(f"Sikeres törlés!\n {product_to_delete} torölve. \n" + "*" * 50)
        except:
            print("Sikertelen törlés!\n Nincs ilyen termék!\n" + "*" + 50)
