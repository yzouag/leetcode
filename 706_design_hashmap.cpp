#include <vector>
#include <deque>

using namespace std;

class MyHashMap {
    vector<deque<pair<int, int>>> map;
    const int size = 19997;
    const int multiplication = 12582917;

public:
    MyHashMap() {
        map.resize(size);
    }
    
    void put(int key, int value) {
        remove(key);
        int pos = hash(key);
        map[pos].push_front({key, value});
    }
    
    int get(int key) {
        int pos = hash(key);
        deque<pair<int, int>>::iterator start = map[pos].begin();
        while (start != map[pos].end()) {
            if (start->first == key)
                return start->second;
            start++;
        }
        return -1;
    }
    
    void remove(int key) {
        int pos = hash(key);
        deque<pair<int, int>>::iterator start = map[pos].begin();
        while (start != map[pos].end()) {
            if (start->first == key)
                break;
            start++;
        }
        if (start!=map[pos].end())
            map[pos].erase(start);
    }

    int hash(int key) {
        return key * multiplication % size;
    }
};
