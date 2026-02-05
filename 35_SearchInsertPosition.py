from typing import List
import unittest


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] >= target:
                return 0
        elif nums[-1] < target:
            return len(nums)
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid
            else: 
                r = mid
            
            if r - l == 1:
                return l + 1
        return l



class TestSearchInsert(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # Тест: элемент найден в середине
    def test_target_found_in_middle(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)

    # Тест: элемент не найден, нужно вставить в середину
    def test_insert_in_middle(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 4), 2)  # 4 между 3 и 5 → индекс 2

    # Тест: вставка в начало (меньше первого)
    def test_insert_at_beginning(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)

    # Тест: вставка в конец (больше последнего)
    def test_insert_at_end(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)

    # Тест: список из одного элемента, и он совпадает
    def test_single_element_found(self):
        self.assertEqual(self.solution.searchInsert([1], 1), 0)

    # Тест: список из одного элемента, target меньше
    def test_single_element_less(self):
        self.assertEqual(self.solution.searchInsert([1], 0), 0)

    # Тест: список из одного элемента, target больше
    def test_single_element_greater(self):
        self.assertEqual(self.solution.searchInsert([1], 2), 1)

    # Тест: два элемента, ищем между ними
    def test_two_elements_insert_between(self):
        self.assertEqual(self.solution.searchInsert([1, 3], 2), 1)

    # Тест: два элемента, ищем первое
    def test_two_elements_first(self):
        self.assertEqual(self.solution.searchInsert([1, 3], 1), 0)

    # Тест: два элемента, ищем второе
    def test_two_elements_second(self):
        self.assertEqual(self.solution.searchInsert([1, 3], 3), 1)

    # Тест: два элемента, вставка после обоих
    def test_two_elements_insert_end(self):
        self.assertEqual(self.solution.searchInsert([1, 3], 4), 2)

    # Тест: два элемента, вставка перед обоими
    def test_two_elements_insert_start(self):
        self.assertEqual(self.solution.searchInsert([1, 3], 0), 0)

    # Тест: дубликаты (если разрешены)
    def test_with_duplicates(self):
        self.assertEqual(self.solution.searchInsert([1, 2, 2, 3], 2), 1)  # может вернуть любой из 2, но бинарный поиск должен быть стабильным?
        # Здесь важно: если target найден — возвращается его индекс, что корректно

    # Тест: три элемента, вставка в середину
    def test_three_elements_insert_middle(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5], 4), 2)

    # Тест: искомый элемент равен первому
    def test_target_equals_first(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 1), 0)

    # Тест: искомый элемент равен последнему
    def test_target_equals_last(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 6), 3)

    # Тест: большой массив, ищем в начале, середине, конце
    def test_large_array(self):
        nums = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
        self.assertEqual(self.solution.searchInsert(nums, 0), 0)
        self.assertEqual(self.solution.searchInsert(nums, 50), 25)
        self.assertEqual(self.solution.searchInsert(nums, 99), 50)
        self.assertEqual(self.solution.searchInsert(nums, 100), 50)

    # Тест: потенциальное зацикливание (критический!)
    def test_potential_infinite_loop_case(self):
        # Этот случай может вызвать проблему из-за l = mid, а не mid+1
        # Например: l=0, r=1, mid=0, nums[mid] < target → l = 0 → цикл повторяется
        # Проверим на конкретном примере
        result = self.solution.searchInsert([1, 3], 2)
        self.assertEqual(result, 1)  # Ожидаем 1
        # Но важно: в текущей реализации условие `if r - l == 1` должно спасти
        # Однако при [1, 2], target=3: сначала l=0, r=1; mid=0 → nums[0]=1<3 → l=0 → r-l=1 → return 1 → потом снова цикл?
        # Давайте проверим [1,3], target=2: mid=(1+0)//2=0 → nums[0]=1<2 → l=0 → r-l=1 → return 1 → OK

    # Дополнительный тест: когда разница между l и r == 1 с самого начала
    def test_initial_gap_of_one(self):
        self.assertEqual(self.solution.searchInsert([1, 3], 2), 1)



if __name__ == "__main__":
    unittest.main()