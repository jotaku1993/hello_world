class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char, int> hash;
        int l = s.size();
        for (int i=0; i<l; i++) {
            if (hash.find(s[i]) == hash.end()) {
                hash[s[i]] = 1;
            } else {
                hash[s[i]]++;
            }
        }
        
        for (int i=0; i<l+1; i++) {
            if (hash.find(t[i]) != hash.end() && hash[t[i]] != 0) {
                hash[t[i]]--;
            } else {
                return t[i];
            }
        }
        return ' ';
    }
};
