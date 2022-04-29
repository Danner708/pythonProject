"""
Module is not for import
"""


class MainClass:
    class_variable: str = "default value"

    def __int__(self, class_variable: str = "default argument"):
        self.class_variable = class_variable

    def just_a_method(self):
        print(self.class_variable)

    @staticmethod
    def static_thing():
        """
        this method type will try to reach a class variable without success.
        :return:
        """
        try:
            print(self.class_variable)
        except Exception as err:
            print(err)

        print("This is a static method, cannot use class variables")
