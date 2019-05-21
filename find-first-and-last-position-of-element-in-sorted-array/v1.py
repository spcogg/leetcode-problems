class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ start by finding location of 1 number that matches"""
        # handle edge cases
        size = len(nums)
        if size == 0:
            return [-1, -1]
        currentpos = int(size / 2)  # will return 0 if size ==1, which is great
        while(1):  # start searching 
            currentval = nums[int(currentpos)]
            if currentval == target:
                return self.findFirstLast(nums, target, currentpos)
            elif currentval > target: # larger > need to go left
                if currentpos == 0:  # check is it at the start.
                    return [-1, -1]  # not found
                else:  # move some steps left halfway to 0 TODO adjust for last known pos when jumping
                    currentpos = max(0, min(currentpos - 1, currentpos / 2))
                # if not, find the next halfway value
            elif currentval < target:
                if currentpos == size:  
                    return [-1, -1]
                else:  # halfway to end - TODO adjust for last known pos when jumping
                    stepsright = currentpos + (size - currentpos) / 2
                    currentpos = min(size, max(currentpos + 1, stepsright))

    def findFirstLast(self, nums, target, currentpos):
        # finds the size of 
        #lower, upper = target, target
        #while(1):
        #    if nums[target]
        #return [lower, upper]
        return currentpos