import unittest
from tasks17_3 import Sum_elements


# 1 Сформувати вимоги
# Перевіряємо, чи правильно обчислюється сума цілих чисел.
# Перевіряємо, чи правильно обчислюється сума чисел з плаваючою комою.
# Перевіряємо, чи виникає виключення ValueError, якщо серед аргументів є нечислові значення.
# Перевіряємо, чи повертає функція 0, якщо аргументи не надані.

# 2 Написання тестів
class TestSumElements(unittest.TestCase):
    def test_sum_integers(self):
        sum_elements = Sum_elements()
        result = sum_elements
        result_success = isinstance(result,int)
        self.assertTrue(result_success)

    def test_sum_floats(self):
        sum_elements = Sum_elements()
        result = sum_elements
        result_success = isinstance(result, float)
        self.assertTrue(result_success)

    def test_sum_mixed_types(self):
        sum_elements = Sum_elements()
        with self.assertRaises(ValueError):
            sum_elements

    def test_empty_arguments(self):
        sum_elements = Sum_elements()
        result = sum_elements.sum()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
