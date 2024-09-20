import pytest
from lib.solutions.CHK.checkout_solution import checkout


def test_empty_basket():
    assert checkout("") == 0

def test_single_item():
    assert checkout("A") == 50
    assert checkout("B") == 30
    assert checkout("C") == 20
    assert checkout("D") == 15
    assert checkout("E") == 40
    assert checkout("F") == 10

def test_special_offer_A():
    assert checkout("AAA") == 130
    assert checkout("AAAA") == 180
    assert checkout("AAAAA") == 200

def test_special_offer_B():
    assert checkout("BB") == 45
    assert checkout("BBB") == 75

def test_special_offer_F():
    assert checkout('FFF') == 20

def test_invalid_item():
    assert checkout("Z") == -1

def test_multiple_items():
    assert checkout("ABAC") == 150
    assert checkout("AABBCCDD") == 215

def test_offer_triggers_more_than_once():
    assert checkout("AAAAAAAAAA") == 400

def test_picks_best_offer():
    assert checkout("AAAAAA") == 250
    assert checkout("EEBB") == 110
