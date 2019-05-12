class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # brute force way:
        # set flower type of first one = 1
        answer = [1] + [None] * (N-1)
        for garden in range(1, N+1):  # start at the first
            # print(garden)
            neighbours = self.getNeighbour(garden, paths)
            # print(neighbours)
            for neighbour in neighbours:
                for flower in range(1, 5): # try flowers 1-4
                    if self.checkNeighbours(flower, neighbour, paths, answer):
                        answer[neighbour-1] = flower
                        break  # need to cancel search once first answer is found or it will keep running
            # print("ans", answer)
                        
        return answer

    def getNeighbour(self, node: int, paths):
        """returns list of neighbours
        probably could be speed optimised to go through list in
        1 pass
        """
        neighbours = []
        for i in paths:
            if i[0] == node:
                neighbours.append(i[1]) 
                # this is neighbours, NOT python index
            if i[1] == node: # paths are both ways
                neighbours.append(i[0])
        return neighbours

    
    def checkNeighbours(self, flower: int, neighbour: int, paths, answer):
        # return True if no neighbour of neighbour has this
        # else false
        NofN = self.getNeighbour(neighbour, paths) # get list of neighbours
        for i in NofN:
            if answer[i-1] == flower:
                return False
        return True