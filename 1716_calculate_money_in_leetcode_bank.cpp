class Solution {
public:
    int totalMoney(int n) {
        int weeks = n / 7;
        int days = n % 7;
        return 28 * weeks + (weeks-1)*weeks*7 + (1+days)*days/2 + weeks*7*days;
    }
};