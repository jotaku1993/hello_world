class TrieNode(object):
    def __init__(self, c = None):
        """
        Initialize your data structure here.
        """
        self.char = c
        self.child = {}
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        head = self.root
        
        for c in word:
            if c in head.child:
                head = head.child[c]
                continue
            else:
                head.child[c] = TrieNode(c)
                head = head.child[c]
        if 'end' not in head.child:
            head.child['end'] = None
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        head = self.root
        
        for c in word:
            if c in head.child:
                head = head.child[c]
            else:
                return False
        if 'end' in head.child:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        head = self.root
        
        for c in prefix:
            if c in head.child:
                head = head.child[c]
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
