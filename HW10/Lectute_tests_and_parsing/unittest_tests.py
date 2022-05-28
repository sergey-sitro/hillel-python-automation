import unittest
import datetime


class Database:
    connect = False
    data = {
        "username": "Alex",
        "age": 30,
        "transactions": [
            100,
            -10,
            -50,
        ],
        "money": 40,
    }

    def connect(self):
        self.connect = True
        print("connected")
        return self

    def disconnect(self):
        self.connect = False
        print("disconnect")

    def transaction(self, money):
        if not isinstance(money, int):
            raise TypeError("money should be int")
        self.data["transactions"].append(money)
        self.data["money"] += money

    def flush(self):
        self.data = {
            "username": "Alex",
            "age": 30,
            "transactions": [
                100,
                -10,
                -50,
            ],
            "money": 40,
        }

    def get_data(self):
        if not self.connect:
            raise Exception("Can't connect to database")
        return self.data


class ExampleUnittestTestCase(unittest.TestCase):
    """python3 unittest_tests.py"""

    @classmethod
    def setUpClass(cls):
        cls._connector = Database().connect()

    @classmethod
    def tearDownClass(cls):
        cls._connector.disconnect()

    def setUp(self):
        data = self._connector.get_data()
        self.username = data["username"]
        self.age = data["age"]
        self.transactions = data["transactions"]
        self.money = data["money"]

    def tearDown(self):
        self._connector.flush()

    def test_sum(self):
        self.assertEqual(sum(self.transactions), self.money, f"Should be {self.money}")

    def test_instance(self):
        self.assertIsInstance(sum(self.transactions), int, "Should be int")

    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            0/0

    @unittest.skip("just skip")
    def test_nothing(self):
        # some complex code
        self.fail("description")


if __name__ == '__main__':
    unittest.main()
