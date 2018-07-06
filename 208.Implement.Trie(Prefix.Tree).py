class Node:
    def __init__(self):
        self.next= [None] * 26
        self.val= [-1] * 26
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in range(len(word)):
            i = ord(word[c]) - 97
            if cur.val[i] < 0:
                cur.val[i] = 0
                cur.next[i] = Node()
            if c == len(word) - 1:
                cur.val[i] = 1
            else:
                cur = cur.next[i]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word[:-1]:
            i = ord(c) - 97
            if cur.next[i] is None: return False
            else:
                cur = cur.next[i]
        return True if cur.val[ord(word[-1]) - 97] == 1 else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            i = ord(c) - 97
            if cur.next[i] is None: return False
            else:
                cur = cur.next[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)