'''

#-- Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        available = 0
        
        idx = 1
        flowerbed.insert(0,0)   # padding on the first end
        flowerbed.append(0)     # padding on the last end

        while idx < len(flowerbed)-1:
            if (flowerbed[idx]==0) and (sum(flowerbed[idx-1:idx+2]) == 0):
                available += 1
                idx = idx + 2
            else:
                idx = idx + 1
        
        if available >= n:
            return True
        else:
            return False
