class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjs = defaultdict(list)
        for email in accounts:
            for i in range(1,len(email)):
                adjs[email[1]].append(email[i])
                adjs[email[i]].append(email[1])
        
        def dfs(visited,same_email,curr_email):
            visited.add(curr_email)
            same_email.append(curr_email)
            for adj in adjs[curr_email]:
                if adj not in visited:
                    dfs(visited, same_email, adj)
                    

        result = []
        visited = set()
        for email in accounts:
            if email[1] not in visited:
                user = [email[0]]
                dfs(visited,user,email[1])
                user[1:] = sorted(user[1:])
                result.append(user)
        return result

