from .data_handling import DataHandling
from .logger import Logger


class DeleteProduct:
    logger = Logger()
    handler = DataHandling()
    inventory = handler.read_json()

    def delete_product(self):

        print("*" * 50 + "\nVálasztott menu: Termék törlése")
        """
        Delete product founction!
        """
        product_to_delete = input("Melyik terméket szeretnéd törölni?")

        try:

            self.logger.log_delete_record_successful(
                self.handler.get_product_name(
                    product_id_to_delete,
                    self.inventory)
            )
            self.inventory.pop(product_id_to_delete)
            print(f"Sikeres törlés!\n {product_to_delete} torölve. \n" + "*" * 50)
        except KeyError:
            print("Sikertelen törlés!\n Nincs ilyen termék!\n" + "*" + 50)
            self.logger.log_delete_record_successful()
        self.handler.write_json(self.inventory)

    def confirm_deletion(self, item_to_delete):
        while True:
            confirm_deletion = input(f"Biztos vagy benne"
                                     f", hogy törölni szeretnéd?: {self.handler.get_product_name(item_to_delete, self.inventory)}"
                                     f"\ny - delete; n - cancel exit: ")
            if confirm_deletion == "y":
                decision = True
            if confirm_deletion == "n":
                break
            else:
                print("y/n az elfogadható érték\n" + "*" * 50)

            return decision
