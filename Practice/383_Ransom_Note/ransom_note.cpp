class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int l1 = ransomNote.size();
        int l2 = magazine.size();
        if (l1 == 0) return true;
        if (l2 == 0) return false;
        map<char, int> hash;
        
        for (int i=0; i<l2; i++) {
            if (hash.find(magazine[i]) == hash.end()) {
                hash[magazine[i]] = 1;
            } else {
                hash[magazine[i]] ++;
            }
        }
        
        for (int i=0; i<l1; i++) {
            if (hash.find(ransomNote[i]) != hash.end() && hash[ransomNote[i]] != 0) {
                hash[ransomNote[i]]--;
            } else {
                return false;
            }
        }
        return true;
    }
};
