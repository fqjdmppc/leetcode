class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = set()
        cow = dict()
        for _ in range(len(guess)):
            if secret[_] == guess[_]:
                bull.add(_)
            else:
                if secret[_] not in cow:
                    cow[secret[_]] = 1
                else:
                    cow[secret[_]] += 1
        cows = 0    
        for _ in range(len(guess)):
            if _ not in bull and guess[_] in cow and cow[guess[_]] > 0:
                cows += 1
                cow[guess[_]] -= 1
                
        return "%dA%dB" % (len(bull), cows)
                    
        