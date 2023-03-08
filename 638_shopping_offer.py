from typing import List
def shoppingOffers(price: List[int], special: List[List[int]], needs: List[int]) -> int:
    memo = {}
    def recursion(needs: List[int]) -> int:
        # check if already traversed
        if tuple(needs) in memo:
            return memo[tuple(needs)]
        
        # no combo
        cost = 0
        for i, need in enumerate(needs):
            cost += need * price[i]

        # select one combo
        for combo in special:
            for i, need in enumerate(needs):
                if combo[i] > need: # combo not valid
                    break
            else: # this else corresponds to `for loop`, if for loop does not break, this else will execute
                new_needs = [need - combo[i] for i, need in enumerate(needs)]
                cost = min(cost, combo[-1] + recursion(new_needs))
        memo[tuple(needs)] = cost
        return cost
    return recursion(needs)


price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print(shoppingOffers(price, special, needs))
# Output: 14

price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]
print(shoppingOffers(price, special, needs))
# Output: 11