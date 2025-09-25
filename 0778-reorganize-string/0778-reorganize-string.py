from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_count = max(count.values())
        if max_count>(len(s)+1)//2:
            return ""
        
        heap = []
        heapq.heapify(heap)
        for char,val in count.items():
            heapq.heappush(heap,(-val,char))
        result = ""
        while len(heap)>=2:
            freq1,char1 = heapq.heappop(heap)
            freq2,char2 = heapq.heappop(heap)
            result+=char1+char2
            if freq1+1<0:
                heapq.heappush(heap,(freq1+1,char1))
            if freq2+1<0:
                heapq.heappush(heap,(freq2+1,char2))
        if heap:
            result+=heap[-1][1]    
        return result
        