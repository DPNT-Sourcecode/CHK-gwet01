import pytest
from lib.solutions.CHK.checkout_solution import checkout


def test_empty_basket():
    assert checkout("") == 0

def test_single_item():
    assert checkout("A") == 50
    # assert checkout("B") == 30
    # assert checkout("C") == 20
    # assert checkout("D") == 15

def test_special_offer_A():
    assert checkout("AAA") == 130
    assert checkout("AAAA") == 180

def test_special_offer_B():
    assert checkout("BB") == 45
    assert checkout("BBB") == 75

def test_invalid_item():
    assert checkout("Z") == -1

def test_multiple_items():
    assert checkout("ABAC") == 150
    assert checkout("AABBCCDD") == 215

def test_offer_triggers_more_than_once():
    assert checkout("AAAAAA") == 260
