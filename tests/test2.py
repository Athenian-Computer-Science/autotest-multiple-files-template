import src.my_code2


def test_inc():
    assert 8 == src.my_code2.double_it(4)
    assert 0 == src.my_code2.double_it(0)
    assert -2 == src.my_code2.double_it(-1)
