
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
