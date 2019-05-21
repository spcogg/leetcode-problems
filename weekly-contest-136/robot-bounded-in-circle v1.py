class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # False if: direction facing the same
        # also require at least 1 move in starting direction
        # create a dict with keys to track total moves:
        moves = {0: 0, 1: 0, 2: 0, 3: 0}
        dir_change = 0  
        for i in instructions:
            if i == 'L':
                dir_change += 1
            if i == 'R':
                dir_change -= 1
            if dir_change == -1:
                dir_change = 3 # reset direction tracker
            if dir_change == 4:
                dir_change = 0
            if i == 'G':  #
                moves[dir_change] += 1  # if moving, track it
                
        if dir_change == 0:
            if (moves[0] != moves[2] or moves[1] != moves[3]):           
                return False
        return True