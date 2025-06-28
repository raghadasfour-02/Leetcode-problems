"""
Problem Statement
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: The triplet [-1, 0, 3] has the sum '2' which is closest to the target.

There are two triplets with distance '1' from the target: [-1, 0, 3] & [-1, 2, 3]. Between these two triplets, the correct answer will be [-1, 0, 3] as it has a sum '2' which is less than the sum of the other triplet which is '4'. This is because of the following requirement: 'If there are more than one such triplet, return the sum of the triplet with the smallest sum.'
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
Example 4:

Input: [0, 0, 1, 1, 2, 6], target=5
Output: 4
Explanation: There are two triplets with distance '1' from target: [1, 1, 2] & [0, 0, 6]. Between these two triplets, the correct answer will be [1, 1, 2] as it has a sum '4' which is less than the sum of the other triplet which is '6'. This is because of the following requirement: 'If there are more than one such triplet, return the sum of the triplet with the smallest sum.'
Constraints:

3 <= arr.length <= 500
-1000 <= arr[i] <= 1000
-104 <= target <= 104
"""
import math

class Solution:
  def searchTriplet(self, arr, target_sum):
    arr.sort()
    smallest_difference = math.inf

    for i in range(len(arr)-2):
      left = i + 1
      right = len(arr) - 1

      while left < right:
        target_diff = target_sum - arr[left] - arr[right] - arr[i]
        if target_diff == 0:
          return target_sum

        if abs(target_diff) < abs(smallest_difference)  \
              or (abs(target_diff) == abs(smallest_difference) 
              and target_diff > smallest_difference):
          smallest_difference = target_diff  # save the closest and the biggest difference
        
        if target_diff > 0:
          left += 1
        
        else: 
          right -=1
          
    return target_sum - smallest_difference
