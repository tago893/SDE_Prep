class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in tasks.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            if maxHeap:
                task = -heapq.heappop(maxHeap)
                if task>1:
                    q.append((task-1,time+n+1))
            time+=1

            if q and q[0][1] == time:
                task,_ = q.popleft()
                heapq.heappush(maxHeap,-task)
        return time