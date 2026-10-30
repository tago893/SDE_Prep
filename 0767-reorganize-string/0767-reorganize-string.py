from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # a a b -> a b a
        # first need to know if the count of characters  for len of string 4 we need atleast 2 for each character for length 5 also atleast 2 characters even length of 6 >2 

        # aab -> a:2,b:1 
        # a -> a:1,b:1
        
        freq_map = Counter(s)
        max_count = max(freq_map.values())
        if max_count > (len(s)+1)//2:
            return ""
        
        heap = []
        heapq.heapify(heap)
        for char,freq in freq_map.items():
            heapq.heappush(heap,(-freq,char))
        
        result = ''
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

        

