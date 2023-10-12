#include <vector>
#include <stack>

using namespace std;

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 */

class NestedInteger {
  public:
    // Return true if this NestedInteger holds a single integer, rather than a nested list.
    bool isInteger() const;
    // Return the single integer that this NestedInteger holds, if it holds a single integer
    // The result is undefined if this NestedInteger holds a nested list
    int getInteger() const;
    // Return the nested list that this NestedInteger holds, if it holds a nested list
    // The result is undefined if this NestedInteger holds a single integer
    const vector<NestedInteger> &getList() const;
};

class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        starts.push(nestedList.begin());
        ends.push(nestedList.end());
    }
    
    int next() {
        // hasNext();
        return (starts.top()++)->getInteger();
    }
    
    bool hasNext() {
        while (starts.size()) {
            if (starts.top() == ends.top()) {
                starts.pop();
                ends.pop();
            } else {
                auto x = starts.top();
                if (x->isInteger())
                    return true;
                // whenever a new sublist is pushed, the parent list should go to the next position
                starts.top()++;
                starts.push(x->getList().begin());
                ends.push(x->getList().end());
            }
        }
        return false;
    }
private:
    stack<vector<NestedInteger>::iterator> starts, ends;
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */