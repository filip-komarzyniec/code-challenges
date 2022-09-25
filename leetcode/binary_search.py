class Solution:
    def search(self, nums: List[int], target: int) -> int:
      middle_ind = len(nums) // 2
      middle_val = nums[middle_ind]

      if middle_val == target: # recursion stop case
        return middle_ind
      elif middle_ind != 0 and middle_val < target:
        ind = self.search(nums[middle_ind:], target)
        return middle_ind + ind if ind >= 0 else ind

      elif middle_ind != 0 and  middle_val > target:
        ind = self.search(nums[:middle_ind], target)
        return ind
      # no match
      return -1
