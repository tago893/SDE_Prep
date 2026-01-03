# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        peak = self.find_peak_index(0, n - 1, mountainArr)

        # search increasing part
        idx = self.binary_search(0, peak, target, mountainArr, False)
        if idx != -1:
            return idx

        # search decreasing part
        return self.binary_search(peak + 1, n - 1, target, mountainArr, True)

    
    def find_peak_index(self,l,r,mountainArr):
        while l<r:
            mid = l + (r-l)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                l = mid+1
            else:
                r = mid
        return l
    
    def binary_search(self, l, r, target, mountainArr, reversed):
        while l <= r:
            mid = l + (r - l) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid

            if not reversed:
                if val < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if val < target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1



