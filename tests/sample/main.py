
import lib
from lib import bar, \
    foo


class OS:
    def get_name(self):  # @OS.get_name
        a100 = 0  # @var_a100
        tmp = a100

        def inner(d400):  # @def_inner_400
            c300 = 2  # @var_c300
            OS.get_name()  # @inner_get_name
            return a100 + b200 + c300 + d400  # @check_variable

        b200 = 1  # @var_b200
        tmp = a100 + b200

        return inner  # @return_inner

    def get_version(self):
        return foo() + lib.bar()  # @main_version_body
