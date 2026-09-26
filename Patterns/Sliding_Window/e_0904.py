class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fruit_counts = {}
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit_counts[fruits[right]] = fruit_counts.get(fruits[right], 0) + 1

            while len(fruit_counts) > 2:
                left_fruit = fruits[left]
                fruit_counts[left_fruit] -= 1
                if fruit_counts[left_fruit] == 0:
                    del fruit_counts[left_fruit]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
