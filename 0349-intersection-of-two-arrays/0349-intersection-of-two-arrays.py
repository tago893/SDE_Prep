class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        nums1.sort()
        nums2.sort()
        result = []
        seen = set()
        while i<len(nums1) and j<len(nums2):
            if nums1[i] ==  nums2[j]:
                if nums1[i] not in seen:
                    result.append(nums1[i])
                seen.add(nums1[i])
                i+=1
                j+=1
            else:
                if nums1[i]>nums2[j]:
                    j+=1
                else:
                    i+=1 

        return(result)                   