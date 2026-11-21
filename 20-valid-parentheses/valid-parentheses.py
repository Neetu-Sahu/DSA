class Solution(object):
    def isValid(self, s):

        stack=[]
        for i in s:

            if i in "({[":
                stack.append(i)

            elif i == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()

            elif i == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()

            elif i == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()

        return len(stack) == 0
