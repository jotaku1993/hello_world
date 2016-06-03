class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        l = len(tokens)
        if l == 1:
            return int(tokens[0])
            
        stk = []
        opa = ['+','-','*','/']
        for i in range(l):
            if tokens[i] in opa:
                a = stk.pop()
                b = stk.pop()
                if tokens[i] == '+':
                    c = b + a
                elif tokens[i] == '-':
                    c = b - a
                elif tokens[i] == '*':
                    c = b * a
                else:
                    #pay attention to this
                    c = int(1.0 * b / a)
                stk.append(c)
            else:
                stk.append(int(tokens[i]))
        return stk[0]
