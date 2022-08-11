from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        all_combinations = [''] if digits else []
        for digit in digits:
            current_combinations = list()
            for letter in mappings[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations

if __name__ == "__main__":
    digits = "23"
    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(Solution().letterCombinations(digits))

    digits = ""
    # []
    print(Solution().letterCombinations(digits))

    digits = "2"
    # ["a","b","c"]
    print(Solution().letterCombinations(digits))