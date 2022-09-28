class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        right_queue = []
        left_queue = []
        for index, dominoe in enumerate(dominoes):
            if dominoe == 'R':
                right_queue.append(index)
            elif dominoe == 'L':
                left_queue.append(index)

        while len(right_queue) > 0 or len(left_queue) > 0:
            l, r = len(left_queue), len(right_queue)
            for _ in range(l):
                index = left_queue.pop(0)
                if index >= 1 and dominoes[index-1] == '.':
                    if index >= 2 and dominoes[index-2] == 'R':
                        dominoes[index-1] = 'x'
                        continue
                    else:
                        dominoes[index-1] = 'L'
                        left_queue.append(index-1)

            for _ in range(r):
                index = right_queue.pop(0)
                if index < len(dominoes)-1 and dominoes[index+1] == '.':
                    dominoes[index+1] = 'R'
                    right_queue.append(index+1)
        return "".join(dominoes).replace('x', '.')

if __name__ == "__main__":
    dominoes = "RR.L"
    print(Solution().pushDominoes(dominoes))
    # assert Solution().pushDominoes(dominoes) == "RR.L"

    dominoes = ".L.R...LR..L.."
    print(Solution().pushDominoes(dominoes))
    # assert Solution().pushDominoes(dominoes) == "LL.RR.LLRRLL.."