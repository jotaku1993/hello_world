class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
            
        num = 0
        ans = 0
        nums = []
        symbols = []
        for i in range(l):
            if s[i] == ' ':
                continue
            elif ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                num = num*10 + int(s[i])
            else:
                if len(symbols) > 0 and (symbols[-1] == '*' or symbols[-1] == '/'):
                    symbol = symbols.pop()
                    num1 = nums.pop()
                    if symbol == '*':
                        num = num1 * num
                    elif symbol == '/':
                        num = num1 // num
                nums.append(num)
                symbols.append(s[i])
                num = 0
        if len(symbols) > 0 and (symbols[-1] == '*' or symbols[-1] == '/'):
            symbol = symbols.pop()
            num1 = nums.pop()
            if symbol == '*':
                num = num1 * num
            elif symbol == '/':
                num = num1 // num
        nums.append(num)
        #print symbols
        #print nums
        nums.reverse()
        symbols.reverse()
        while len(symbols) > 0:
            symbol = symbols.pop()
            tmp = nums.pop()
            if symbol == '+':
                tmp = nums.pop() + tmp
            elif symbol == '-':
                tmp = tmp - nums.pop()
            nums.append(tmp)
            #print symbols
            #print nums
        return nums[0]
