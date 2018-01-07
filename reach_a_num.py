class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        # make target as positive, the answer is the same
        if target < 0:
            target = -target
        
        # find the first n such that 1+2+...+n >= target
        position = 0
        steps = 0
        while position < target:
            steps += 1
            position += steps
        
        # 1+2+...+n = target + k, depending on k, the return results are different    
        if position == target:
            return steps
        else:
            exceed = position - target
            if exceed % 2 == 0:
                return steps
            elif (steps + 1) % 2 == 1:
                return steps+1
            else: 
                return steps+2
        
