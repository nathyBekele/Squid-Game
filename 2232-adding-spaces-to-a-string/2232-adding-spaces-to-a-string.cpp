class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        int N = s.size(), S = spaces.size();
        string result(N + S, ' ');

        int i_str = 0, i_space = 0;
        for (int i = 0; i < N + S; i++){
            if (i_space < S && spaces[i_space] == i_str){
                i_space += 1;
                continue;
            }

            result[i] = s[i_str++];
            // cout << result << endl;
        }

        return result;
    }
};