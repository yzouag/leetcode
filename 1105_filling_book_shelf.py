from typing import List

def minHeightShelves(books: List[List[int]], shelfWidth: int) -> int:
    # dp[i] = min_j (dp[j] + max(books[j+1].height, ..., books[i].height))
    # where sum(books[j+1].width, ..., books[i].width <= shelfWidth)

    dp = [0] * (len(books) + 1)
    
    for i in range(1, len(books)+1):
        min_total_height = float('inf')
        max_height = 0
        total_width = 0
        j = i-1

        while j >= 0:
            width, height = books[j]
            
            total_width += width
            if total_width > shelfWidth:
                break
            
            max_height = max(max_height, height)
            min_total_height = min(min_total_height, dp[j]+max_height)
            j -= 1
        
        dp[i] = min_total_height
    
    return dp[-1]

        

books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(minHeightShelves(books, shelf_width)) # 6

books = [[1,3],[2,4],[3,2]]
shelf_width = 6
print(minHeightShelves(books, shelf_width)) # 4
