from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i],nums[j])
            if nums[j] == target - nums[i]:
                return [i, j]

print(twoSum(nums=[1,2,3,4],target=7))