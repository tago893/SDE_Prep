class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        def merge(left,right)->list:
            merged_list = [0]*(m+n)
            l=0
            r=0
            k = 0
            while l<m and r<n:
                if left[l]<right[r]:
                    merged_list[k] = left[l]
                    l+=1
                else:
                    merged_list[k] = right[r]
                    r+=1
                k+=1
            while l<m:
                merged_list[k] = left[l]
                l+=1
                k+=1
            while r<n:
                merged_list[k] = right[r]
                k+=1
                r+=1
            return merged_list

        res = merge(nums1,nums2)
        print(res)
        low = 0
        high = len(res)-1
        mid = low + (high-low)//2
        if len(res)%2==0:
            median =(float)(res[mid] + res[mid+1])/2
        else:
            median = res[mid]
        return median
