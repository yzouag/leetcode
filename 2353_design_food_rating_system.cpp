#include <vector>
#include <string>
#include <queue>
#include <unordered_map>

using namespace std;

struct FoodRate {
    string food_name;
    int rating;

    FoodRate(string food_name, int rating) : food_name(food_name), rating(rating) {}

    bool operator< (const FoodRate& other) const {
        if (this->rating == other.rating) {
            return this->food_name > other.food_name;
        } else {
            return this->rating < other.rating;
        }
    }
};

class FoodRatings {
    unordered_map<string, priority_queue<FoodRate>> cuisine_foodRate;
    unordered_map<string, int> foodName_rate;
    unordered_map<string, string> foodName_cuisine;

public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for (int i=0; i<foods.size(); i++) {
            foodName_rate[foods[i]] = ratings[i];
            foodName_cuisine[foods[i]] = cuisines[i];
            cuisine_foodRate[cuisines[i]].push(FoodRate(foods[i], ratings[i]));
        }
    }
    
    void changeRating(string food, int newRating) {
        if (newRating != foodName_rate[food]) {
            cuisine_foodRate[foodName_cuisine[food]].push(FoodRate(food, newRating));
            foodName_rate[food] = newRating;
        }
    }
    
    string highestRated(string cuisine) {
        auto foodrate = cuisine_foodRate[cuisine].top();
        while (foodName_rate[foodrate.food_name] != foodrate.rating) {
            cuisine_foodRate[cuisine].pop();
            foodrate = cuisine_foodRate[cuisine].top();
        }
        return foodrate.food_name;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */