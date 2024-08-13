class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for directory in path.split("/"):
            if directory != ".." and directory != "" and directory != ".":
                stack.append(directory)
            elif stack and directory == "..":
                stack.pop()
        return "/" + "/".join(stack)
        


