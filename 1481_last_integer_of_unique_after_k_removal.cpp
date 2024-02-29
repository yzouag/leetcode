#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        unordered_map<int, int> counts;
        for (int num : arr) {
            counts[num]++;
        }
        
        // Vector to track all the frequencies
        vector<int> frequencies;
        for (auto it : counts) {
            frequencies.push_back(it.second);
        }

        // Sorting the frequencies
        sort(frequencies.begin(), frequencies.end());

        // Tracking the number of elements removed
        int elementsRemoved = 0;

        for (int i = 0; i < frequencies.size(); i++) {
            // Removing frequencies[i] elements which equates to
            // removing one unique element
            elementsRemoved += frequencies[i];

            // If the number of elements removed exceeds k, we'll return
            // the remaining number of unique elements.
            if (elementsRemoved > k) {
                return frequencies.size() - i;
            }
        }

        // We have removed all elements, so no unique integers remain
        // Return 0 in this case
        return 0;
    }
};