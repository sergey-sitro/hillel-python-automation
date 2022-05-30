from unittest import TestCase, main
from HW11 import *


class TestIsEven(TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(2))

    def test_not_even(self):
        self.assertFalse(is_even(3))

    def test_not_a_number_even(self):
        with self.assertRaises(TypeError):
            is_even("asd")


class TestIsOdd(TestCase):

    def test_is_odd(self):
        self.assertTrue(is_odd(3))

    def test_not_odd(self):
        self.assertFalse(is_odd(2))

    def test_not_a_number_odd(self):
        with self.assertRaises(TypeError):
            is_odd("asd")


class TestCustomMax(TestCase):

    def test_custom_max(self):
        self.assertEqual(custom_max(1, 2), 2)
        self.assertEqual(custom_max(-2, -3), -2)

    def test_custom_max_diff_types(self):
        with self.assertRaises(TypeError):
            custom_max(1, "a")

        with self.assertRaises(TypeError):
            custom_max("a", 1)

    def test_custom_max_str(self):
        self.assertEqual(custom_max("asda", "asd"), "asda")


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

    def test_reverse_int(self):
        with self.assertRaises(TypeError):
            reverse(5)


class TestUpperCount(TestCase):

    def test_upper_count(self):
        self.assertEqual(upper_count("QWER qwer 123 !@#"), 4)

    def test_upper_count_empty_str(self):
        self.assertEqual(upper_count(""), 0)

    def test_upper_count_not_str(self):
        with self.assertRaises(TypeError):
            upper_count(2)
            upper_count(True)
            upper_count(None)


class TestUnique(TestCase):

    def test_unique(self):
        self.assertEqual(unique([2, 2, 1, 5, 5, 2, 7]), [1, 2, 5, 7])

    def test_unique_empty_lst(self):
        self.assertEqual(unique([]), [])

    def test_unique_not_iter(self):
        with self.assertRaises(TypeError):
            unique(2)
            unique(None)
            unique(True)


class TestIsPangram(TestCase):

    def test_is_pangram(self):
        self.assertTrue(is_pangram("The five boxing wizards jump quickly"))

    def test_is_not_pangram(self):
        self.assertFalse(is_pangram("hello"))

    def test_is_pangram_not_str(self):
        with self.assertRaises(AttributeError):
            is_pangram(2)
            is_pangram(True)
            is_pangram(None)


if __name__ == "__main__":
    main()
