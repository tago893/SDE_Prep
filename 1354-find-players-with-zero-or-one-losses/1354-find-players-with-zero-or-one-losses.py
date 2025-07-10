class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()

        for i in range(0,len(matches)):
            players.add(matches[i][0])
            players.add(matches[i][1])
        
        player_score = {}

        for i in players:
            player_score[i] = [0,0]
        
        for i in range(0,len(matches)):
            player_score[matches[i][0]][0] += 1
            player_score[matches[i][1]][1] += 1
        
        result = [[],[]]
        for player in player_score:
            if player_score[player][1] == 0:
                result[0].append(player)
                
            if player_score[player][1] == 1:
                result[1].append(player)
                
        result[0].sort()
        result[1].sort()
        return result
