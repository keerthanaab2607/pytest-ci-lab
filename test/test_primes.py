import pytest
from src.primes import is_prime


@pytest.mark.parametrize("num", (-5, 0, 1))
def test_non_primes_below_two(num):
    assert is_prime(num) is False


@pytest.mark.parametrize("num", (2, 3, 5, 7, 11, 13))
def test_prime_numbers(num):
    assert is_prime(num) is True


@pytest.mark.parametrize("num", (4, 6, 8, 9, 10, 12))
def test_composite_numbers(num):
    assert is_prime(num) is False


def test_large_prime():
    assert is_prime(97) is True


def test_large_composite():
    assert is_prime(100) is False
