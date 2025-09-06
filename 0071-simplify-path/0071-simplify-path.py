class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = ""
        if path[-1] == "/":
            path = path[:-1]
        path = path.split("/")
        stack = []

        for c in path:
            if len(stack)>0 and c=="..":
                stack.pop()
            elif c!="." and c!="" and c!="..":
                stack.append(c)
        if len(stack) == 0:
            new_path="/"
        for c in stack:
            if c!="." and c!="":
                new_path+= "/"+c 
            
        return (new_path)
