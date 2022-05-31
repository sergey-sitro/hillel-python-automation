from unittest import TestCase, main
from HW11 import *


class TestIsEven(TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(2))

    def test_not_even(self):
        self.assertFalse(is_even(3))

    def test_is_even_negative(self):
        self.assertTrue(is_even(-10))


class TestIsOdd(TestCase):

    def test_is_odd(self):
        self.assertTrue(is_odd(3))

    def test_not_odd(self):
        self.assertFalse(is_odd(2))

    def test_is_odd_negative(self):
        self.assertFalse(is_odd(-2))


class TestCustomMax(TestCase):

    def test_custom_max(self):
        self.assertEqual(custom_max(1, 2), 2)

    def test_custom_max_negative(self):
        self.assertEqual(custom_max(-2, -3), -2)

    def test_custom_max_str(self):
        self.assertEqual(custom_max("hello world", "hello"), "hello world")


class TestMultiply(TestCase):

    def test_multiply_with_base(self):
        self.assertEqual(multiply(*list(range(1, 10)), 2), 725760)

    def test_multiply_without_base(self):
        self.assertEqual(multiply(*list(range(1, 10))), 362880)

    def test_multiply_with_one_argument(self):
        self.assertEqual(multiply(5), 5)


class TestReverse(TestCase):

    def test_reverse(self):
        self.assertEqual(reverse("QWERqwer123!@#"), "#@!321rewqREWQ")

    def test_reverse_empty_str(self):
        self.assertEqual(reverse(""), "")

    def test_reverse_palindrome(self):
        self.assertEqual(reverse("madam"), "madam")


class TestUpperCount(TestCase):

    def test_upper_count(self):
        self.assertEqual(upper_count("QWER qwer 123 !@#"), 4)

    def test_upper_count_empty_str(self):
        self.assertEqual(upper_count(""), 0)

    def test_upper_count_all_lower(self):
        self.assertEqual(upper_count("hello"), 0)


class TestUnique(TestCase):

    def test_unique(self):
        self.assertEqual(unique([2, 2, 1, 5, 5, 2, 7]), [1, 2, 5, 7])

    def test_unique_empty_lst(self):
        self.assertEqual(unique([]), [])

    def test_unique_strings(self):
        self.assertEqual(unique(["a", "a", "b", "b", "b", "ba", "ba", "bbb"]), ["a", "b", "ba", "bbb"])


class TestIsPangram(TestCase):

    def test_is_pangram(self):
        self.assertTrue(is_pangram("The five boxing wizards jump quickly"))

    def test_is_not_pangram(self):
        self.assertFalse(is_pangram("hello"))

    def test_is_not_pangram_empty(self):
        self.assertFalse(is_pangram(""))


if __name__ == "__main__":
    main()
