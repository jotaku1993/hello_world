class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        
        stk = []
        signs = []
        
        ans = 0
        num, sign = 0, 1
        for i in range(l):
            if s[i] == ' ':
                continue
            elif ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                num = num*10 + int(s[i])
            else:
                ans += sign * num
                num = 0
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i] == '(':
                    signs.append(sign)
                    stk.append(ans)
                    ans = 0
                    sign = 1
                elif s[i] == ')':
                    ans = stk.pop() + signs.pop() * ans
                    
        ans += num * sign
        return ans
