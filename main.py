from heaps.total_cost import Solution

if __name__ == '__main__':
    s = Solution()

    #print(s.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4))
    #print(s.totalCost(costs = [1,2,4,1], k = 3, candidates = 3))
    print(s.totalCost(costs = [47,48,46,63,91,56,3,55,40,93,97,37,31,31,37,58,41,10,74,40,17,58,58,33,78,53,88,1,15,44,82,74,56,41,48,96,71,35,89,57,71,34,43,4], k = 35, candidates = 15))