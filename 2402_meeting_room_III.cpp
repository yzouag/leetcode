#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        vector<int> meetingCount(n, 0);
        // [endtime, room_number]
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> usedRooms;
        priority_queue<int, vector<int>, greater<int>> unusedRooms;
        for (int i = 0; i < n; i++) {
            unusedRooms.push(i);
        }
        sort(meetings.begin(), meetings.end());

        for (auto meeting : meetings) {
            int start = meeting[0], end = meeting[1];

            // pop all the rooms in meeting that ends earlier than current meeting start time
            while (!usedRooms.empty() && usedRooms.top().first <= start) {
                int room = usedRooms.top().second;
                usedRooms.pop();
                unusedRooms.push(room);
            }

            if (!unusedRooms.empty()) { // if there are some empty rooms, get the smallest room number and put current meeting in
                int room = unusedRooms.top();
                unusedRooms.pop();
                usedRooms.push({end, room});
                meetingCount[room]++;
            } else { // if all rooms are used, get the earliest ended meeting room, update its end time to this meeting end time
                auto [roomAvailabilityTime, room] = usedRooms.top();
                usedRooms.pop();
                usedRooms.push({roomAvailabilityTime + end - start, room});
                meetingCount[room]++;
            }
        }

        int maxMeetingCount = 0, maxMeetingCountRoom = 0;
        for (int i = 0; i < n; i++) {
            if (meetingCount[i] > maxMeetingCount) {
                maxMeetingCount = meetingCount[i];
                maxMeetingCountRoom = i;
            }
        }
        return maxMeetingCountRoom;
    }
};