class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n == 1) {
            return true;
        }
        if (n & 3 != 0) {
            return false;
        }
        return isPowerOfFour(n >> 2);
    }
};