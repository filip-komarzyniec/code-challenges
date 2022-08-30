# return last index at the next tree level
def next_tree_level():
	last_index = 0
	lvl = 1
	while True:
		last_index += 2 ** lvl
		yield lvl, last_index
		lvl += 1


class Solution:
    # nums array is sorted in ascending order
    def search(self, nums: List[int], target: int) -> int:

        lvl, index = 0,0
        tree_lvl_gen = next_tree_level()
        try:
          while nums[index] < target:  # choose tree level where you should look for the number
            lvl, index = next(tree_lvl_gen)
        except IndexError:
          if index == len(nums) - 1:  # last tree level is fully populated and the number is not there
            return -1

        start = index - 2**lvl if (index - 2**lvl) > 0 else 0
        # end at a specific tree level or at the end of nums array (if we are searching through not fully populated last tree lvl)
        end = len(nums) if len(nums) < index+1 else index+1

        for i in range(start,end):  ## iterate through the specific tree level and look for the target number
          if nums[i] == target:
            return i
        return -1
