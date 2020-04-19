'''
https://leetcode.com/problems/guess-number-higher-or-lower/
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l, r = 1, n
        while(l<=r):
            mid = int(  (r - l)/2 + l )
            tmp = guess(mid)
            
            if(tmp == 0): 
                return mid
            if tmp == -1 :
                r = mid - 1
                
            else: 
                l = mid + 1
        return -1