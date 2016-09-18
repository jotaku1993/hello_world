class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int[2]> hash;
        int l = s.size();
        for (int i=0; i<l; i++) {
            if (hash.find(s[i]) == hash.end()) {
                hash[s[i]][0] = 1;
                hash[s[i]][1] = i;
            } else {
                hash[s[i]][0] = 2;
            }
        }
        
        map<char, int[2]>::iterator itr;
        int ret = -1;
        int poi = l;
        for (itr=hash.begin(); itr!=hash.end(); itr++) {
            if (itr->second[0] == 1) {
                if (itr->second[1] < poi) {
                    poi = itr->second[1];
                    ret = poi;
                }
            }
        }
        return ret;
    }
};
