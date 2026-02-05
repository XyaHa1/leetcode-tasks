import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int, b_int = int(a, 2), int(b, 2)
        return bin(a_int + b_int)[2:]

        

class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # Тест: сложение двух нулей
    def test_add_zeros(self):
        self.assertEqual(self.solution.addBinary("0", "0"), "0")

    # Тест: сложение нуля и единицы
    def test_add_zero_and_one(self):
        self.assertEqual(self.solution.addBinary("0", "1"), "1")
        self.assertEqual(self.solution.addBinary("1", "0"), "1")

    # Тест: сложение двух единиц
    def test_add_two_ones(self):
        self.assertEqual(self.solution.addBinary("1", "1"), "10")

    # Тест: разная длина строк
    def test_different_lengths(self):
        self.assertEqual(self.solution.addBinary("1010", "11"), "1101")  # 10 + 3 = 13
        self.assertEqual(self.solution.addBinary("1", "111"), "1000")    # 1 + 7 = 8

    # Тест: одна строка — длинное число
    def test_long_binary_string(self):
        a = "111111111111"
        b = "1"
        expected = bin(int(a, 2) + int(b, 2))[2:]
        self.assertEqual(self.solution.addBinary(a, b), expected)

    # Тест: максимальное сложение (перенос по всем битам)
    def test_carry_all_bits(self):
        self.assertEqual(self.solution.addBinary("1111", "1"), "10000")  # 15 + 1 = 16


    # Тест: очень большие двоичные числа
    def test_very_large_numbers(self):
        a = "1" * 100  # 2^100 - 1
        b = "1"
        expected = bin(int(a, 2) + int(b, 2))[2:]
        self.assertEqual(self.solution.addBinary(a, b), expected)

    # Тест: только единицы
    def test_all_ones(self):
        self.assertEqual(self.solution.addBinary("111", "111"), "1110")  # 7 + 7 = 14

    # Тест: симметричные значения
    def test_symmetric_inputs(self):
        result1 = self.solution.addBinary("101", "11")
        result2 = self.solution.addBinary("11", "101")
        self.assertEqual(result1, result2)
        self.assertEqual(result1, "1000")  # 5 + 3 = 8

if __name__ == "__main__":
    unittest.main()