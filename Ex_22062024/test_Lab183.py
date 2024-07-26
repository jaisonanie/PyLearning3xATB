import pytest
import allure

@allure.title("TC#1 - verify that 2-2 is equal to 0")
@allure.description("This is asmoke test case to verify 20-2")
@pytest.mark.regression
def test_sub0():
    assert 20-2 == 18

@allure.title("TC#2 - verify that 20-20 is equal to 0")
@allure.description("This is a sanity test case to verify 20-20")
@pytest.mark.sanity
def test_sub1():
    assert 20-20 == 0

@allure.title("TC#3 - verify that 21+21")
@allure.description("This is a smoke test case to verify 21+21")
@pytest.mark.smoke
def test_sub2():
    assert 21 + 21 == 42


@allure.title("TC#4 - verify that 1+9 is equal to 10")
@allure.description("This is a regression test case to verify 1+9")
@pytest.mark.regression
def test_sub3():
    assert 1+9 ==10

@pytest.mark.skip(reason="Not working")
def test_sub4():
    assert 1+9 ==10