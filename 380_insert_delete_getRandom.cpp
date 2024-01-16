#include <unordered_map>
#include <vector>
#include <random>

using namespace std;

class RandomizedSet {
private:
    vector<int> arr;
    unordered_map<int, int> pos;
    int index;
public:
    RandomizedSet() {
        index = -1;
    }
    
    bool insert(int val) {
        if (pos.find(val) != pos.end())
            return false;
        index += 1;
        pos[val] = index;
        arr.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (pos.find(val) == pos.end())
            return false;
        
        arr[pos[val]] = arr[index];
        pos[arr[index]] = pos[val];
        pos.erase(val);
        arr.pop_back();
        index -= 1;
        return true;
    }
    
    int getRandom() {
        return arr[rand() % (index+1)];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */