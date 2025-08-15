class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        max_index = events[0][0]
        max_time = events[0][1]

        for i in range(1,len(events)):
            time_taken = events[i][1] - events[i-1][1]
            if time_taken > max_time:
                max_time = time_taken
                max_index = events[i][0]

            elif time_taken == max_time:
                max_index = min(events[i][0],max_index)
            print([time_taken,max_time])
        return max_index