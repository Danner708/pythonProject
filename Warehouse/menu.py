from add_update_product import AddUpdateProduct
from delete_product import DeleteProduct
from list_product import ListProduct
from exit_program import ExitProgram


class Menu:

    @staticmethod
    def menu(warehouse):
        """
        Menu of the warehouse
        :param warehouse:
        :return:
        """
        while True:
            chose_option = input("Válassz egy menűpontot:\n1 - Termék hozzáadása/frissítése \n2 - Termék törlése "
                                 "\n3 - Terméklista \n4 - Kilépés\nVálassz egy menupontot: ")
            if chose_option == "1":
                AddUpdateProduct.add_update_product(warehouse)
            elif chose_option == "2":
                DeleteProduct.delete_product(warehouse)
            elif chose_option == "3":
                ListProduct.list_product(warehouse)
            elif chose_option == "4":
                ExitProgram.exit_program()
