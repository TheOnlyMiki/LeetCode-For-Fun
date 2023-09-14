class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        queue = senate
        temp = None
        visit = {'R', 'D'}
        R = D = 0
        
        while len(visit) == 2:
            temp = []
            visit = set()
            for p in queue:
                if p == 'R':
                    if D == 0:
                        R += 1
                        temp.append(p)
                        visit.add(p)
                    else:
                        D -= 1
                else:
                    if R == 0:
                        D += 1
                        temp.append(p)
                        visit.add(p)
                    else:
                        R -= 1
            
            queue = temp
        
        return "Radiant" if 'R' in visit else "Dire"
