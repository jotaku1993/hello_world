class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ret;
        map<int, int> nums;
        
        for (int i=0; i<nums1.size(); i++) {
            if (nums.find(nums1[i])==nums.end()) {
                nums[nums1[i]] = 1;
            } else {
                nums[nums1[i]] += 1;
            }
        }
        
        for (int i=0; i<nums2.size(); i++) {
            if (nums.find(nums2[i])!=nums.end() && nums[nums2[i]]!=0) {
                ret.push_back(nums2[i]);
                nums[nums2[i]] -= 1;
            }
        }
        
        return ret;
    }
};
