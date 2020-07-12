from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_index_mapping = {}
        for e, num in enumerate(nums):
            z = target - num
            if z in number_index_mapping:
                return number_index_mapping[z], e
            number_index_mapping[num] = e


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))
