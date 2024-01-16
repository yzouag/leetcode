#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        priority_queue<int, vector<int>> queue;
        queue.push(prices[0]);
        queue.push(prices[1]);
        
        for (int i=2; i<prices.size(); i++) {
            queue.push(prices[i]);
            queue.pop();
        }
        int sums = queue.top();
        queue.pop();
        sums += queue.top();
        if (sums > money) {
            return money;
        } else {
            return money-sums;
        }
    }
};