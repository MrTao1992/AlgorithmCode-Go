#!/usr/bin/python3
from typing import List
def twoSum(nums: 'List[int]', target: 'int') -> 'List[int]':
    results = {}
    for i in range(len(nums)):
        c = target - nums[i]
        if c in results:
            return [results[c],i]
        results[nums[i]] = i
    return[]