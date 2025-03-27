class Solution {
public:
    struct cmp {
        bool operator()(const pair<int, int>& a,const pair<int, int>& b) const {
            if (a.first != b.first) {
                return a.first > b.first;
            }

            return a.second < b.second;
        }
    };

    int minimumIndex(vector<int>& nums) {
        unordered_map<int, int> first_half;
        unordered_map<int, int> second_half;
        set<pair<int, int>, cmp> first_half_sorted;
        set<pair<int, int>, cmp> second_half_sorted;
        int N = nums.size();

        for (auto& num: nums) {
            first_half[num] += 1;
        }

        for (auto& [num, count]: first_half){
            first_half_sorted.insert({count, num});
            // cout << num << ' ' << count << endl;
        }

        for (int i = 0; i < N - 1; i++){
           if(second_half_sorted.count({second_half[nums[i]], nums[i]}) != 0){
                second_half_sorted.erase({second_half[nums[i]], nums[i]});
           }

           second_half[nums[i]] += 1;
           second_half_sorted.insert({second_half[nums[i]], nums[i]});

            first_half_sorted.erase({first_half[nums[i]], nums[i]});
            first_half[nums[i]] -= 1;
            first_half_sorted.insert({first_half[nums[i]], nums[i]});

            auto dom_from_first_half = first_half_sorted.begin();
            auto dom_from_second_half = second_half_sorted.begin();

            cout << dom_from_first_half->first << " " << dom_from_first_half->second << endl;
            cout << dom_from_second_half->first << " " << dom_from_second_half->second << endl << endl;

            if (dom_from_first_half->first > (N - i - 1)/2 && //dominant ele in first half exists
                dom_from_second_half->first > (i+1)/2 && //dominant ele in second exists?
                dom_from_first_half->second == dom_from_second_half->second // are they both the same
            ) {
                return i; //then return the dividing index
            }
        }

        return -1;
    }
};