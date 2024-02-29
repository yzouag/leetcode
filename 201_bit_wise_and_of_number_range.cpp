class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        return (left == right) ? left : (rangeBitwiseAnd(left >> 1, right >> 1) << 1);
    }
};