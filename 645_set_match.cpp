#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int A = -reduce(nums.begin(), nums.end()) + n*(n+1)/2;
        int B = -transform_reduce(nums.begin(), nums.end(), 0, plus<int>(), [](int i) {return i*i;}) + n*(n+1)*(2*n+1)/6;
        return {(B-A*A)/2/A, (B+A*A)/2/A};
    }
};