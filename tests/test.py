
from utils import assert_pos, goto


def test_check_variable():
    assert_pos('@var_a100', goto('a100', '@check_variable'))
    assert_pos('@var_b200', goto('b200', '@check_variable'))
    assert_pos('@var_c300', goto('c300', '@check_variable'))
    assert_pos('@def_inner_400', goto('d400', '@check_variable'))
    assert_pos('@OS.get_name', goto('OS.get_name', '@inner_get_name'))

    assert_pos('@def_inner_400', goto('inner', '@return_inner'))

    assert_pos('@lib.foo', goto('foo', '@main_version_body'))
    assert_pos('@lib.bar', goto('lib.bar', '@main_version_body'))
    assert_pos('@lib.test', goto('test_system', '@get_name.test_system'))
    assert_pos('@lib.System.read', goto('SS.read', '@get_name.ss_read'))
    assert_pos('@lib.bar', goto('L2.bar', '@get_name.L2.bar'))

    assert_pos('@OS.get_version', goto('self.get_version', '@get_name.get_version'))

    assert_pos('@OS.set_value0', goto('self', '@set_value.self'))
    assert_pos('@OS.set_value0', goto('timeout', '@set_value.timeout'))

    assert goto('wrong_var', '@set_value.wrong_var') is None
