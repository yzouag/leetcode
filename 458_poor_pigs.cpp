// With 2 pigs, poison killing in 15 minutes, and having 60 minutes, 
// we can find the poison in up to 25 buckets in the following way. 
// Arrange the buckets in a 5×5 square:
//  1  2  3  4  5
//  6  7  8  9 10
// 11 12 13 14 15
// 16 17 18 19 20
// 21 22 23 24 25
// Now use one pig to find the row (make it drink from buckets 1, 2, 3, 4, 5, 
// wait 15 minutes, make it drink from buckets 6, 7, 8, 9, 10, wait 15 minutes, etc). 
// Use the second pig to find the column (make it drink 1, 6, 11, 16, 21, then 2, 7, 12, 17, 22, etc).

// With 3 pigs, we can similarly use a 5×5×5 cube instead of a 5×5 square 
// and again use one pig to determine the coordinate of one dimension 
// (one pig drinks layers from top to bottom, one drinks layers from left to right, 
// one drinks layers from front to back). So 3 pigs can solve up to 125 buckets.
#include <math.h>
class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int pigs = 0;
        while (pow((minutesToTest/minutesToDie + 1), pigs) < buckets)
            pigs += 1;
        return pigs;
    }
};