# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
      last_checked_minor = 1
      last_checked_major = n
      def findBadVersion(n):
        nonlocal last_checked_minor, last_checked_major
        middle_rev = n // 2 if n > 2 else 1
        isBad = isBadVersion(middle_rev)

        if isBad and middle_rev != 1 and not isBadVersion(middle_rev - 1):
          return middle_rev
        elif isBad and middle_rev == 1: # in case of only 2 revs and 2nd one Bad, necessary condition
          return middle_rev


        if isBad:  # we want to check lesser versions
          last_checked_major = middle_rev
          next_n = last_checked_minor + middle_rev# + 1
          ind = findBadVersion(next_n)
          return ind

        else: # we are checking major versions
          last_checked_minor = middle_rev
          next_n = last_checked_major + middle_rev + 1
          ind = findBadVersion(next_n)
          return ind
      return findBadVersion(n)
