from .add_update_product import AddOrUpdate
from .delete_product import DeleteProduct
from .list_product import ListProduct
from .exit_program import ExitProgram


class MainMenu:

    @staticmethod
    def selector():
        """
        Menu of the warehouse
        :param warehouse:
        :return:
        """
        while True:
            chose_option = input("Válassz egy menűpontot:\n1 - Termék hozzáadása/frissítése \n2 - Termék törlése "
                                 "\n3 - Terméklista \n4 - Kilépés\nVálassz egy menupontot: ")
            if chose_option == "1":
                add = AddOrUpdate()
                add.create_or_update_product()
            elif chose_option == "2":
                delete = DeleteProduct()
                delete.delete_product()
            elif chose_option == "3":
                ListProduct.list_products()
            elif chose_option == "4":
                ExitProgram.exit_program()
            else:
                print("Nem megfelelő érteék!\n" + "*" * 50)
