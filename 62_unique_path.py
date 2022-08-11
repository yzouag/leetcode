class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        possible_paths = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                possible_paths[j] += possible_paths[j-1]
        return possible_paths[-1]

        # method 2: math
        # return factorial(m+n-2) // factorial(m-1) // factorial(n-1)


if __name__ == "__main__":
    m = 3
    n = 7
    assert 28 == Solution().uniquePaths(m, n)

    m = 3
    n = 2
    assert 3 == Solution().uniquePaths(m, n)