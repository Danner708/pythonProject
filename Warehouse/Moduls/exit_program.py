class ExitProgram:

    @staticmethod
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
