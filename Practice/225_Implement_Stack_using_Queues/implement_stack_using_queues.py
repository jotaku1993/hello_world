import Queue
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = Queue.Queue()
        self.topele = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.topele = x
        self.q.put(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        qh = Queue.Queue()
        l = self.q.qsize()
        for i in range(l-1):
            tmp = self.q.get()
            qh.put(tmp)
            if i == l-2:
                self.topele = tmp
        self.q = qh
        

    def top(self):
        """
        :rtype: int
        """
        return self.topele

    def empty(self):
        """
        :rtype: bool
        """
        return self.q.empty()
