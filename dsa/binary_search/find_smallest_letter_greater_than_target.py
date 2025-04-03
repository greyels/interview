# https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        seen = set()
        letters = [char for char in letters if not (char in seen or seen.add(char))]
        left, right = 0, len(letters) - 1
        while right >= left:
            mid = (right + left) // 2
            if target == letters[mid]:
                return letters[mid+1]
            elif target > letters[mid]:
                if target < letters[mid+1]:
                    return letters[mid+1]
                left = mid + 1
            elif target < letters[mid]:
                if target >= letters[mid-1]:
                    return letters[mid]
                right = mid - 1
        return letters[0]
