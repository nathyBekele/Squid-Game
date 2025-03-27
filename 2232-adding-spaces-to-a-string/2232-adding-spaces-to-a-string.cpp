class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        int N = s.size(), S = spaces.size();
        string result;
        result.reserve(N + S);

        result = s.substr(0, spaces[0]);
        for (int i = 1; i < S; i++){
            result += ' ';
            result += s.substr(spaces[i - 1], spaces[i] - spaces[i - 1]);
        }

        return result + ' ' + s.substr(spaces[S - 1], N - spaces[S - 1]);
    }
};