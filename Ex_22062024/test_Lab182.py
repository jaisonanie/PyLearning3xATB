import pytest
@pytest.mark.regression
def test_sub0():
    assert 20-2 == 18

@pytest.mark.sanity
def test_sub1():
    assert 20-20 == 0

@pytest.mark.smoke
def test_sub2():
    assert 21 + 21 == 42

@pytest.mark.regression
def test_sub3():
    assert 1+9 ==10

@pytest.mark.skip(reason="Not working")
def test_sub4():
    assert 1+9 ==10