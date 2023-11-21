class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        next_states = {
            '0':['1','9'],
            '1':['2','0'],
            '2':['3','1'],
            '3':['4','2'],
            '4':['5','3'],
            '5':['6','4'],
            '6':['7','5'],
            '7':['8','6'],
            '8':['9','7'],
            '9':['0','8'],
        }
        deadends = set(deadends)
        wheels = range(4)

        record = deque()
        record.append(("0000", 0))
        visit = set()

        while record:
            while record and (record[0][0] in visit or record[0][0] in deadends):
                record.popleft()

            if record:
                state, step = record.popleft()

                if state == target:
                    return step

                visit.add(state)
                
                for i in wheels:
                    next_state = state[:i] + next_states[state[i]][0] + state[i+1:]
                    if next_state not in visit and next_state not in deadends:
                        record.append((next_state, step+1))
                    next_state = state[:i] + next_states[state[i]][1] + state[i+1:]
                    if next_state not in visit and next_state not in deadends:
                        record.append((next_state, step+1))

                    #record += [(state[:i] + next_states[state[i]][0] + state[i+1:], step+1), (state[:i] + next_states[state[i]][1] + state[i+1:], step+1)] 

        return -1
