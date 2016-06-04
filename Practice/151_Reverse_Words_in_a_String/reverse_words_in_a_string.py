class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l == 0:
            return ''
        
        words = []
        flag = 0
        start, end = 0, 0
        add_flag = 0
        for i in range(l):
            
            if i == l-1 and s[i] != ' ':
                add_flag = 1
                end = i+1
                print s[i], add_flag
            #space
            if s[i] == ' ':
                #previous is space
                if flag == 0:
                    pass
                ##previous is char
                else:
                    end = i
                    flag = 0
                    add_flag = 1
            #char
            else:
                if flag == 0:
                    start = i
                    flag = 1
                else:
                    pass
            if add_flag == 1:
                words.append(s[start:end])
                add_flag = 0
                
        if len(words) == 0:
            return ''
        else:
            return ' '.join(words[::-1])
