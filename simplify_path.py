class Solution:
    def simplifyPath(self, path: str) -> str:
        my_stack = []
        path = path + "/"
        temp = ""
        for character in path:
            if character == "/":
                if temp != "":
                    if temp == ".":
                        pass
                    elif temp == "..":
                        if len(my_stack) > 0:
                            my_stack.pop()
                    else:
                        my_stack.append(temp)
                    
                    temp = ""
            else:
                temp += character

        return "/" + "/".join(my_stack)
