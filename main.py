from graphs.path_exists import Solution

if __name__ == '__main__':
    s = Solution()
    edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
    print(s.validPath(n = 10, edges = edges, source = 5, destination = 9))