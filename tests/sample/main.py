
import lib
import lib as L2
from lib import bar, \
    foo, test as test_system
from lib import System as SS


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
        self.get_version()  # @get_name.get_version
        test_system()  # @get_name.test_system
        SS.read()  # @get_name.ss_read
        L2.bar()  # @get_name.L2.bar

        return inner  # @return_inner

    def get_version(self):  # @OS.get_version
        return foo() + lib.bar()  # @main_version_body

    def set_value(self, name,  # @OS.set_value0
                  value, timeout=None, error=5):  # @OS.set_value1
        self  # @set_value.self
        timeout  # @set_value.timeout
