from typing import List,Dict

# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# nums = [1,2,3,1,1,3]


def get_good_pairs(nums:List[int])->int:
    d:Dict={}
    count=0
    for i in range(len(nums)):
        if nums[i] in d:
            count += (d[nums[i]])
        else:
            d[nums[i]]=0
        d[nums[i]] += 1
    return count

print(get_good_pairs([1,2,3,1,1,3]))

# TC: O(N)
# SC: O(N)