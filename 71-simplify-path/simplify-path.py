class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        mypath = path.split("/")
        for i in mypath:
            if i != "" and i != ".." and i != ".":
                stack.append(i)
            elif i == ".." and stack :
                stack.pop()
        return '/' + '/'.join(stack)


